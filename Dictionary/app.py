import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))



def returnDef(word,data):
    word = word.lower()
    if word in data: 
        return data[word]
    elif word.title() in data:     #for proper noun
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("did you mean %s ans Y/N? " % get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "word not exist"

    else:
        return "word not exist"


word = input("enter word:")
print(returnDef(word,data))   
#len(get_close_matches(word,data.keys()))>0
