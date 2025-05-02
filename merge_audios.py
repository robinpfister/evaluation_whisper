from pydub import AudioSegment

audio = AudioSegment.from_file('Audio/k1.m4a')

for size in ['k', 'm', 'l']:
    for number in range(1, 11, 1):
        if size == 'k' and number == 1:
            continue
        audio_to_merge = AudioSegment.from_file(f'Audio/{size}{number}.m4a', format ='m4a')
        audio = audio.append(audio_to_merge)
        audio.export('merged', format ='m4a')
        break
    break