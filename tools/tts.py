"""Nagrywa data/listening.json do audio/<id>.mp3 głosami neuronowymi Microsoft (edge-tts).
A = pl-PL-ZofiaNeural (kobieta), B = pl-PL-MarekNeural (mężczyzna). Dialog = sklejone kwestie (ramki MP3)."""
import asyncio, json, os, sys
import edge_tts

VOICES = {"A": "pl-PL-ZofiaNeural", "B": "pl-PL-MarekNeural"}
RATE = "-6%"


async def synth(text, voice):
    for attempt in range(5):
        try:
            buf = bytearray()
            async for chunk in edge_tts.Communicate(text, voice, rate=RATE).stream():
                if chunk["type"] == "audio":
                    buf += chunk["data"]
            if len(buf) > 2000:
                return bytes(buf)
        except Exception as e:  # sieć / limit — spróbuj ponownie
            err = e
        await asyncio.sleep(2 + attempt * 3)
    raise RuntimeError(f"TTS nie powiodło się: {text[:40]}…")


async def record(item, outdir, sem, done):
    path = os.path.join(outdir, item["id"] + ".mp3")
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        done.append(item["id"]); return
    async with sem:
        parts = [await synth(t, VOICES[v]) for v, t in item["lines"]]
    with open(path, "wb") as f:
        for p in parts:
            f.write(p)
    done.append(item["id"])
    if len(done) % 20 == 0:
        print(f"  {len(done)} nagrań gotowe", flush=True)


async def main(src, outdir):
    items = json.load(open(src, encoding="utf-8"))["items"]
    os.makedirs(outdir, exist_ok=True)
    sem, done = asyncio.Semaphore(6), []
    await asyncio.gather(*(record(it, outdir, sem, done) for it in items))
    total = sum(os.path.getsize(os.path.join(outdir, f)) for f in os.listdir(outdir))
    print(f"gotowe: {len(done)} plików, {total / 1e6:.1f} MB")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
