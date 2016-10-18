import sys
import re
import collections

#open file from the command line. save it to variable 'my_file'
my_file = sys.argv[1]

#open text file and set it to variable text_file so we can iterate over it in the for loop
text_file = re.findall(r'\w+', open(my_file).read().lower())

#counter function that iterates over text_file list and counts how many words are repeated. saves it in a dictionary
sorted_items = collections.Counter(text_file)

#iterates over dictionary and sorts them into descending value. words repeated more often are last
for key, value in sorted(sorted_items.iteritems(), key=lambda (k,v): (v,k)):
    print '%s:%s' % (key, value)

