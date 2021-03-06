import re
from collections import Counter
import numpy as np
with open('chat.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)

for i in range(30):
	del word_counts[str(i)]

remove = []
for k in word_counts:
	if len(k)<4:
		remove.append(k)
for i in remove:		
	del word_counts[i]

print(word_counts.most_common(30))
print('amount of times the word happy was said:',word_counts['HAPPY'])

