# -*- coding: utf-8 -*-

textfilename = 'text.txt'
wubi = True
wubi = False

print 'Wubi stats:' if wubi else 'Pinyin stats:'

dictfilename = 'wubi86.dict.txt' if wubi else 'pinyin_simp.dict.txt'
import csv
with open(dictfilename) as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    lookupdict = {}
    for row in spamreader:
        if row[0] in lookupdict:
            #in rare cases, such as '绿'
            #will have two or more records in dict file
            #the later code 'lu' will replace 'lv'
            #ignore later one
            continue 
        lookupdict[row[0]] = row[1]

import string
result = {}
for letter in string.lowercase:
    result[letter] = 0

textfile = open(textfilename)
text = textfile.read()
text = unicode(text, 'utf-8')
textwordcount = 0
for char in text:
    char = char.encode('utf-8')
    if char not in lookupdict:
        continue;
    textwordcount += 1
    code = lookupdict[char]
    for codeletter in code:
        result[codeletter] += 1

print 'words: ' + str(textwordcount)

total = 0
for letter in result:
    total += result[letter]
total = float(total)

stat = {}
for letter, count in result.items():
    stat[letter.upper()] = count / total * 100;

letterDescList = sorted(stat, key = stat.get, reverse = True)
for letter in letterDescList:
    print letter + '\t' + '%.3f%%' % (stat[letter])
