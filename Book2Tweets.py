#!/usr/bin/python

import sys, re, glob, os
from random import shuffle


##### First we need to match the file name to the title
ann_file = "./Darwin_book_info.txt"
info = {}
dates = {}
try:
    a = open(ann_file)
    for lines in a.readlines():
        tab = lines.strip().split("\t")
        info[tab[0]] = tab[1]
        dates[tab[0]] = tab[2]
    a.close()
except IOError:
     print >> sys.stderr, "Error. Could not open file " + str(ann_file)       


min_len = 100
max_len = 280
i = 0

files = glob.glob("./Darwin/*.txt")
#file = "/Users/pjulien/Dropbox/Code/text_phylo/Darwin/OriginofSpecies.txt"
tot = 0
for file in files:
    title = os.path.basename(file).replace(".txt", "")
    titleFull = info[title]
    d = dates[title]
    print >> sys.stderr, "Reading " + str(file)
    try:
        f = open(file)
        content = f.readlines()
        content = [c.strip() for c in content]
        content = [c.replace("--", "-") for c in content]
        tab = []
        for c in content:
            if c:
                tab.append(c)
        text = " ".join(tab)
        sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)

        # Selecting sentences of desired length only
        tw = [s for s in sentences if (len(s) >= min_len and len(s) <= max_len)]

        # If the sentence is 1 characther longer than the max value, we remove the last character (generally a dot)
        tw2 = [s for s in sentences if len(s)==max_len + 1]
        tws = tw + tw2

        # We shuffle the list for randomised printing later
        shuffle(tws)

        print >> sys.stderr, str(len(tws)) + " extractions"
        tot += len(tws)
        for t in tws:
            i += 1
            print str(i) + "\t" + str(t) + "\t" + str(title) + "\t" + str(titleFull) + "\t" + str(d )
    except IOError:
        print >> sys.stderr, "Error. Could not open file " + str(file)
    
print >> sys.stderr, "Extracted " + str(tot) + " sentences in total"