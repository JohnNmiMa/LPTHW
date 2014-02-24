#! /usr/local/bin/python
import re
import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--dir", dest="dir", help="Directory of text files")
(options,args) = parser.parse_args()
if (not options.dir):
    parser.error("You need to supply a directory of .txt files: -d")

dir = options.dir

# PREPARE OUR REGEXES FOR METADATA SEARCHES #
# we'll use re.compile() here, which allows you to assign a regex pattern
# to a variable. We'll do this for each our metadata fields.
pattern = r'(title:\s*)(?P<title>.*?)(Author:|Illustrator:|Translator:|Release Date:)'
title_search = re.compile(pattern, re.IGNORECASE|re.DOTALL)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# Now we need to do something with the user supplied keywords
# which we're getting with sys.argv. Remember, the script name itself
# is at index 0 in sys.argv, and the directory is , so we'll slice everything from index 1 forward.
pattern = r'(?:.*\*{3}\s*start.*?\*{2})(?P<subdoc>.*)(?:\*{3}end\s*\*{2})'
body_search = re.compile(pattern, re.IGNORECASE|re.DOTALL)

# Use a Dictionary comprehensions to store the various keyword searches
#   d = {key: value for (key, value) in sequence}
searches = {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in sys.argv[3:]}

for fl in (os.listdir(dir)):  #for each item that appears in the directory
    if fl.endswith('.txt'):   #if it's a text file
        fl_path = os.path.join(dir, fl) #the full path to the file is the directory plus
                                              #the file name

        with open(fl_path, 'r') as f:         #open the file as f
            full_text = f.read()              #assign its contents to the var full_text


            # Extract and print output about metadata from the file.
            title = re.search(title_search, full_text).group('title')
            author = re.search(author_search, full_text)
            translator = re.search(translator_search, full_text)
            illustrator = re.search(illustrator_search, full_text)
            if author: 
                author = author.group('author')
            if translator:
                translator = translator.group('translator')
            if illustrator:
                illustrator = illustrator.group('illustrator')
            print "***" * 25
            print "Here's the info for file {}:".format(fl)
            print "The title of the text is {}".format(title)
            print "The author(s) is {}".format(author)
            print "The translator(s) is {}".format(translator)
            print "The illustrator(s) is {}".format(illustrator)
            print ""
            print "Here's the counts for the keywords you searched for"
            subdoc = re.search(body_search, full_text).group('subdoc')
            for search in searches:
                print "\"{0}\": {1}".format(search, len(re.findall(searches[search], subdoc)))

        print '{0} is {1} characters long\n\n'.format(fl, len(full_text))

