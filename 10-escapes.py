# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print '.'*10
note = """
    This string is bounded by triple double quotes (3 times ").
Unescaped newlines in the string are retained, though \
it is still possible\nto use all normal escape sequences.

    Whitespace at the beginning of a line is
significant.  If you need to include three opening quotes
you have to escape at least one of them, e.g. \""".

    This string ends in a newline.
"""
print note
note2 = """
NOTE: the tripple quote is sometimes called a 'doc string'. It can
be used as a comment block in python code.
"""
print note2
