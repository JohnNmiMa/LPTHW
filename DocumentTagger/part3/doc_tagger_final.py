#! /usr/local/bin/python
import re
import sys
import os
from optparse import OptionParser


def parse_options():
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="dir", help="Directory of text files")
    (options,args) = parser.parse_args()
    if (not options.dir):
        parser.error("You need to supply a directory of .txt files: -d")
    return dict(directory=options.dir, keywords=args)


class DocumentReporter:
    """ Useful for producing document reports """
    def __init__(self, keywords, doc_text):
        """ Constructor - stuff gets done in the right order """
        self.keywords = keywords
        self.patterns = self.__compile_regex_patterns()
        self.metadata = self.__get_metadata(doc_text)
        self.keyword_counts = self.__count_keywords()

    def __compile_regex_patterns(self):
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
        searches = {kw: re.compile(r'\b' + kw + r'\b', re.IGNORECASE) for kw in self.keywords}

        return dict(title=title_search, author=author_search, translator=translator_search,
                    illustrator = illustrator_search, body = body_search, searches = searches)

    def __search_metadata(self, pattern_name, text):
        """ Use regex to seach for patterns in the text """
        result = re.search(self.patterns[pattern_name], text)
        if result:
            return result.group(pattern_name)
        else:
            return None

    def __get_metadata(self, doc_text):
        """ Extract metadata from the text file. """
        title = self.__search_metadata('title', doc_text)
        author = self.__search_metadata('author', doc_text)
        translator = self.__search_metadata('translator', doc_text)
        illustrator = self.__search_metadata('illustrator', doc_text)
        body_text = self.__search_metadata('body', doc_text)
        return dict(title=title, author=author, translator=translator,
                    illustrator=illustrator, body_text=body_text)

    def __count_keywords(self):
        """ Returns keyword stats """
        counts = {}
        searches = self.patterns['searches']
        for search in searches:
            counts[search] = len(re.findall(searches[search], self.metadata['body_text']))
        return counts

    def report(self):
        print "***"*25
        print "The title of the text is {}".format(self.metadata['title'])
        print "The author(s) is {}".format(self.metadata['author'])
        print "The translator(s) is {}".format(self.metadata['translator'])
        print "The illustrator(s) is {}\n".format(self.metadata['illustrator'])
        print "Here's the counts for the keywords you searched for:"
        for count in self.keyword_counts:
            print "  {} : {}".format(count, self.keyword_counts[count])
        print '  {} characters long\n'.format(len(self.metadata['body_text']))


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
                             # and close file immediately after after return


def main(argv=sys.argv):
    options = parse_options()
    for full_text in TextFiles(options['directory']):
        dr = DocumentReporter(options['keywords'], full_text)
        dr.report()


if __name__ == '__main__':
    main()
