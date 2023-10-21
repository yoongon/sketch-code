import os

def create_voices(idx=None):
    filename = 'sample.txt'
    f = open(filename, 'r')
    full_text = f.read()
    base_cmd = 'aws polly synthesize-speech --text-type ssml --output-format mp3 --voice-id Matthew --text \'<speak><break time="1s"/><prosody rate="medium">{0}</prosody></speak>\' {1}.mp3'

    texts = full_text.split("\n")
    lines = []
    for test in texts:
        s = test.strip()
        if s.startswith("Slide"):
            continue
        if s == "":
            continue
        lines.append(s)

    for i in range(len(lines)):
        if i + 1 == idx:
            line = lines[i]
            cmd = base_cmd.format(line, str(i + 1))
            os.system(cmd)
            break

create_voices(idx=None)