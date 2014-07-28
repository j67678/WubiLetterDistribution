#!/usr/bin/env python3

import collections
import string
import sys

textfilename = 'text.txt'


def main(dictfilename):

    lookupdict = {}
    with open(dictfilename, 'r', encoding='utf-8') as dictfile:
        for line in dictfile:
            line = line.split()
            if line[0] not in lookupdict:
                # in rare cases, such as '绿'
                # will have two or more records in dict file
                # the later code 'lu' will replace 'lv'
                # ignore the later one
                lookupdict[line[0]] = line[1]

    with open(textfilename, 'r', encoding='utf-8') as textfile:
        imecode = ''.join(
            (lookupdict.get(word, '') for word in textfile.read())
        )

    counts = collections.Counter(imecode)
    print('Statistics:')
    print('Dictinary: %s' % dictfilename)
    for i in string.ascii_lowercase:
        counts[i] = counts[i]  # If a key is not used, give it zero
    total = sum(counts.values())
    for key, freq in counts.most_common():
        print('%s\t%.3f%%' % (key.upper(), 100*freq/total))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        main('wubi86.dict.txt')
