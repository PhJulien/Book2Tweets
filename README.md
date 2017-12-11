Books2Tweet is a simple Python script turning a set of ebooks in txt formats into tweets, or, more generally, sentences of a desired length.

# Requirements

* Python 2.7 (anterior version might work too)

# Launching

> python Book2Tweets.py

You might want to redirect the output to a file

> python Book2Tweets.py > DarwinTweets.txt

# Arguments

All arguments are optional and have default values. To display them type:

> python Book2Tweets.py -h

For example:

> python Book2Tweets.py -m 140 -n 40 -v > DarwinTweets140.txt

extracts sentences between 40 and 140 characters in a verbose mode.

Main arguments are:

* -v: verbose
* -m value: max length of the sentence, default is 280 (a tweet)
* -n value: min length of the sentence, default is 100
* -f file: path to annotation file
* -d directory: path to eBooks directory

# About input files

The script takes two files as argument:
* Annotation file: provide information regarding books, in particular:
    * A short code corresponding to the name of the file without its .txt extension,
    * its title and
    * its year of publication.
Values are tab-separated. If you want to provide a different input, you have to modify accordingly, respecting the orginal format.

* eBooks directory: directory where the eBook in a .txt can format can be found. The name of the file without the .txt extension has to match the shortcode in the annotation file
