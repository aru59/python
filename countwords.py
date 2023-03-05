from collections import Counter
import re

# READING A TEXTFILE

file_path = 'eext.txt'

with open(file_path) as file:
    text = file.read()

#Count Number of Words In Python Using split()

#text.split()
#print(len(text.split()))   #easy word count
print(len(re.findall(r'\w+', text)))

#Using defaultdict To Calculate Word Frequencies in Python
counts = Counter(re.findall('\w+',text))
print(counts)

#finding most common word
print(counts.most_common()[2])
