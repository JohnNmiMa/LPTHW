#! /usr/local/bin/python
import re

regex = r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    '''
pattern = re.compile(regex, re.VERBOSE)



print "The phone number regular expression pattern is\n", regex
phnum = '970-227-1956'
matchstr = pattern.search(phnum)
if matchstr != None:
	print 'The phone number %s matches: %s' % (phnum, matchstr.groups())
else:
	print '{} did not match'

# phnum = '1-(970) 22-1956 ext. 3' # doesn't work
phnum = '(970)227-1957 ext. 21'
matchstr = pattern.search(phnum)
if matchstr != None:
	print 'The phone number {} matches: {}'.format(phnum, matchstr.groups())
else:
	print '{} did not match'

phnum = '(970)227-1957'
matchstr = pattern.search(phnum)
if matchstr != None:
	print 'The phone number {} matches: {}'.format(phnum, matchstr.groups())
else:
	print '{} did not match'

phnum = '9702271957'
matchstr = pattern.search(phnum)
if matchstr != None:
	print 'The phone number {} matches: {}'.format(phnum, matchstr.groups())
else:
	print '{} did not match'

phnum = '970.227-1956'
matchstr = pattern.search(phnum)
if matchstr != None:
	print 'The phone number {} matches: {}'.format(phnum, matchstr.groups())
else:
	print 'The phone number {} did not match'.format(phnum)

phnum = 'cell 1-(970) 227-1956'
matchstr = pattern.search(phnum)
if matchstr != None:
	print 'The phone number {} matches: {}'.format(phnum, matchstr.groups())
else:
	print 'The phone number {} did not match'.format(phnum)

