import os

filename = 'sample.txt'
f = open(filename, 'r')
full_text = f.read()

texts = full_text.split("\n")
lines = []
for test in texts:
    s = test.strip()
    if s.startswith("Slide"):
        continue
    if s == "":
        continue
    lines.append(s)

base_cmd = 'aws polly synthesize-speech --text-type ssml --output-format mp3 --voice-id Matthew --text \'<speak><break time="1s"/><prosody rate="medium">{0}</prosody></speak>\' {1}.mp3'

for i in range(len(lines)):
    line = lines[i]
    cmd = base_cmd.format(line, str(i+1))
    os.system(cmd)
