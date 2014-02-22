#! /usr/local/bin/python

text = """Mary had a little lamb,
whose fleece was white as snow.
And everywhere that Mary went,
the lamb was sure to go.
It followed her to school one day
which was against the rule.
It made the children laugh and play,
to see a lamb at school.
And so the teacher turned it out,
but still it lingered near,
And waited patiently about,
till Mary did appear.
"Why does the lamb love Mary so?"
the eager children cry.
"Why, Mary loves the lamb, you know."
 the teacher did reply."""

# Use the .find() function
text.find("Mary") 
text[0:len("Mary")]
index = text.find('Fred')
print index

# Use the .count() function
index = text.count("Mary") 
print index
index = text.count('Fred')
print index

# Use the .index() function
index = text.index("Mary") 
print index
# index = text.index('Fred') # must comment this out as we get an error

index = text.find('as')
print index
print text[30:49]
