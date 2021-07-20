import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def define(word):
    word.lower()
    if word in data: 
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead Enter Y or N " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "error word doesn't exist"

    else:
        return "error word doesn't exist"


word = input("word ")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
