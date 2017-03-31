import re


def clean(text):
    text = re.sub("\d:\d+:\d+\.\d [a-zA-Z0-9 ]+: ", "", text)
    text = re.sub("\[.+?\]", "", text)
    text = re.sub("\-|_", " ", text)
    text = re.sub("\s{2,}", " ", text)
    return text.strip()

with open(transcript) as fh:
    lines = fh.readlines()

lines = [clean(line) for line in lines]
lines = [line for line in lines if len(line.strip()) > 0]

raw_text = ' '.join(lines)
