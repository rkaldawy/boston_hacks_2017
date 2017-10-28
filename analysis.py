'''
Created on Oct 28, 2017

@author: Remy Kaldawy
'''

import json
import tokenizer as tk
from collections import Counter

data = []

with open('python.json') as f:
    for line in f:
        data.append(line)

count_all = Counter()

for line in data:
    jsdata = json.loads(line)
    print(jsdata['text'])
    hashtags = (jsdata['entities'])['hashtags']  
    
    hashtag_terms = []
    for hashtag in hashtags:
        hashtag_terms.append(hashtag['text'])
    count_all.update(hashtag_terms)
print(count_all)        
    
        
     