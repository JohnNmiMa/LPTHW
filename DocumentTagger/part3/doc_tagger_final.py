#! /usr/local/bin/python
import re
import sys
import os
from optparse import OptionParser


def parseOptions(argv):
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="dir", help="Directory of text files")
    (options,args) = parser.parse_args()
    if (not options.dir):
        parser.error("You need to supply a directory of .txt files: -d")
    return dict(directory=options.dir, keywords=args)

def compile_regex_patterns(options):
    """ Compile the document meta data patterns """
    pattern = r'(title:\s*)(?P<title>.*?)(Author:|Illustrator:|Translator:|Release Date:)'
    title_search = re.compile(pattern, re.IGNORECASE|re.DOTALL)
    author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
    translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
    illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

    # compile the pattern that retrieves the main body text
    pattern = r'(?:.*\*{3}\s*start.*?\*{2})(?P<body>.*)(?:\*{3}end\s*\*{2})'
    body_search = re.compile(pattern, re.IGNORECASE|re.DOTALL)

    # Use a Dictionary comprehensions to store the various keyword searches
    #   d = {key: value for (key, value) in sequence}
    searches = {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in options['keywords']}

    return dict(title=title_search,
                author=author_search,
                translator=translator_search,
                illustrator = illustrator_search,
                body = body_search,
                searches = searches)

def search_meta(patterns, pattern_name, text):
    """ Use regex to seach for patterns in the text """
    result = re.search(patterns[pattern_name], text)
    if result:
        return result.group(pattern_name)
    else:
        return None

def get_metadata(patterns, full_text):
    """ Extract metadata from the text file. """
    title = search_meta(patterns, 'title', full_text)
    author = search_meta(patterns,'author', full_text)
    translator = search_meta(patterns, 'translator', full_text)
    illustrator = search_meta(patterns, 'illustrator', full_text)
    body_text = search_meta(patterns, 'body', full_text)
    return dict(title=title, author=author, translator=translator, illustrator=illustrator, body_text=body_text)

def count_keywords(searches, body_text):
    """ Returns keyword stats """
    counts = {}
    for search in searches:
        counts[search] = len(re.findall(searches[search], body_text))
    return counts

class TextFiles:
    """ Useful for returning a list of text documents in a directory """
    """ Can be iterated """
    def __init__(self, directory):
        self.directory = directory
        self.dirs = os.listdir(self.directory)
        self.index = 0
    def __iter__(self):
        return self;
    def next(self):
        while self.index < len(self.dirs):
            if self.dirs[self.index].endswith('.txt'):
                break;
            index += 1
        else:
            raise StopIteration

        path = os.path.join(self.directory, self.dirs[self.index]) 
        self.index += 1
        with open(path, 'r') as f:
            return f.read()  # get the text contents of the file

def report(meta_data, keyword_counts):
    print "***"*25
    print "The title of the text is {}".format(meta_data['title'])
    print "The author(s) is {}".format(meta_data['author'])
    print "The translator(s) is {}".format(meta_data['translator'])
    print "The illustrator(s) is {}\n".format(meta_data['illustrator'])
    print "Here's the counts for the keywords you searched for:"
    for count in keyword_counts:
        print "  {} : {}".format(count, keyword_counts[count])
    print '  {} characters long\n'.format(len(meta_data['body_text']))

def main(argv=sys.argv):
    options = parseOptions(argv)
    patterns = compile_regex_patterns(options)

    for full_text in TextFiles(options['directory']):
        meta_data = get_metadata(patterns, full_text)
        keyword_counts = count_keywords(patterns['searches'], meta_data['body_text'])
        report(meta_data, keyword_counts)


if __name__ == '__main__':
    main()
