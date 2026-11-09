import json, soundfile as sf, numpy as np
from kokoro import KPipeline
lines = json.load(open('voz/lineas.json'))
pipe = KPipeline(lang_code='e')
for voice in ['em_alex', 'ef_dora']:
    for i, text in enumerate(lines):
        audio = [a for _, _, a in pipe(text, voice=voice, speed=1.08)]
        sf.write(f'voz/{voice}_{i:02d}.wav', np.concatenate(audio), 24000)
        print(voice, i, text)
