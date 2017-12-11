
import sys, re, glob, os
from random import shuffle
import argparse

#### Arguments management

#### Defining and parsing arguments

parser = argparse.ArgumentParser(description="Turns Darwin's books into tweetable sentences")
parser.add_argument("--max", "-m", default = 280, help="Max length of extracted sentences", type=int)
parser.add_argument("--min", "-n", default = 100, help="Min length of extracted sentences", type=int)

parser.add_argument("--file", "-f", default = "./Darwin_book_info.txt", help="Path to annotation file", type=str)
parser.add_argument("--dir", "-d", default = "./Darwin/", help="Directory containing ebooks")

parser.add_argument("-v", "--verbose", help="increase output verbosity",  action="store_true")


#### Processing
args = parser.parse_args()
print args

#### Checking arguments validity

if args.max < args.min:
    print >> sys.stderr, "Error. Min value is greater than max"
    sys.exit()
if not os.path.exists(args.dir):
    print >> sys.stderr, "Error. Books dir not found."
    sys.exit()
if not os.path.exists(args.file):
    print >> sys.stderr, "Error. Annotation file not found."
    sys.exit()




##### First we need to match the file name to the title


info = {}
dates = {}
try:
    a = open(args.file)
    for lines in a.readlines():
        tab = lines.strip().split("\t")
        info[tab[0]] = tab[1]
        dates[tab[0]] = tab[2]
    a.close()
except IOError:
     print >> sys.stderr, "Error. Could not open file " + str(args.file)


min_len = 100
max_len = 280
i = 0

files = glob.glob(args.dir + "/*.txt")
#file = "/Users/pjulien/Dropbox/Code/text_phylo/Darwin/OriginofSpecies.txt"
tot = 0
for file in files:
    title = os.path.basename(file).replace(".txt", "")
    titleFull = info[title]
    d = dates[title]
    if args.verbose:
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
        if args.verbose:
            print >> sys.stderr, str(len(tws)) + " extractions"

        tot += len(tws)
        for t in tws:
            i += 1
            print str(i) + "\t" + str(t) + "\t" + str(title) + "\t" + str(titleFull) + "\t" + str(d )
    except IOError:
        print >> sys.stderr, "Error. Could not open file " + str(file)

if args.verbose:
    print >> sys.stderr, "Extracted " + str(tot) + " sentences in total"