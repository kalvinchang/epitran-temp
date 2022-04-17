import argparse
import epitran
import re

parser = argparse.ArgumentParser()
parser.add_argument('--tailo_file', help='file in Tailo')
args = parser.parse_args()

tailo_file = args.tailo_file
epi = epitran.Epitran('temp-nan', tones=True)

with open(tailo_file, "r") as in_f, open('tailo-num-' + tailo_file, "w") as out_f:
    lines = in_f.readlines()

    for line in lines:
        # replace spaces with a token
        # line = re.sub(r' ', r" SP ", line)

        # punctuation
        # pad punctuation (including a dash) with a space around
        line = re.sub(r'([,.?!:-])', r" \1 ", line)

        punc = {'SP', ',', '.', '?', '!', ':', '-'}
        words = line.split()
        for i in range(len(words)):
            if words[i] not in punc:
                words[i] = epi.transliterate(words[i])

        line = ' '.join(words)

        # then recover by replacing punctuation with the space removed
        # line = re.sub(r'SP', r" SP ", line)
        # only replace dash
        line = re.sub(r' (-) ', r"\1", line)
        # the double dash does not have a dash preceding it
        line = re.sub(r'(\-\-) ', r"\1", line)

        print(line)