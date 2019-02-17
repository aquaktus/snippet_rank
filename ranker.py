import json
import random
import pprint

files = ["human_1.tgt",
         "human_2.tgt",
         "django_retrieval.tgt",
         "docstring_retrieval.tgt",
         "conala_retrieval.tgt",
         "synthetic_retrieval.tgt",
         "django_nmt.tgt",
         "docstring_nmt.tgt",
         "conala_nmt.tgt",
         "synthetic_nmt.tgt",
         "django_seekNMT.tgt",
         "docstring_seekNMT.tgt",
         "conala_seekNMT.tgt",
         "synthetic_seekNMT.tgt"
         ]
results_dir = "./results/"

try:
    with open("survay_result.json", "r") as survay_file:
        survay = json.load(survay_file)
        print("loaded survay from file: survay_result.json")
except:
    survay = {
        "id": random.randint(100,1000),
        "total":770,
        "progress":0,
        "left":[],
        "done":[]
    }

    for f in files:
        dataset = f.split("_")[0]
        model = f.split("_")[1].split(".")[0]
        index = 0
        with open(results_dir+f, "r") as results_file, open(results_dir+"descriptions.src") as descriptions_file:
            lines = results_file.read().split('\n')
            descriptions = descriptions_file.read().split('\n')
            for line, description in zip(lines, descriptions):
                index += 1
                question = {
                    "dataset":dataset,
                    "model":model,
                    "description": description,
                    "snippet": line,
                    "index": index
                }
                survay["left"].append(question)
    print("Saving blank survay to file")
    survay["left"] = sorted(survay["left"], key=lambda k: k['description']) 
    with open("survay_result.json", 'w') as fp:
        json.dump(survay,fp)

print("Total snippets:", survay["total"])
print("Snippets Ranked:", survay["progress"])
print("")

intro_text = """The aim of this experiment is to investigate the suitability of these generated code snippets given an initial description.
We cannot tell how good the generated code is unless we ask those people who are likely to be using them, which is why we need to run experiments like these. You will have time to read each description and rank the following code snippets on a 5 point scale. Please ask questions if you need to and please let me know when you are finished.
Please remember that it is the system, not you, that is being evaluated.
You are welcome to withdraw from the experiment at any time.


Example:
Description: get first element from list of tuples my_list.

Code: 
[x for x.append() in x]))(<unk>)

Rank: 1, 2, 3, 4, 5
         ^

Explanation: There are constructs relevant to list creation but the variables used don't match and the syntax is off. This is not a useful code snippet.


Do you agree to taking part in this evaluation?           (press Any key to accept ctrl+C to exit)
"""
print(intro_text)
input()

while(survay["left"]):
    q = survay["left"].pop()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Description:", q["description"])
    print("")
    print("Code:")
    print(q["snippet"].replace("DCNL","\n").replace("DCSP",""))
    print("")
    print("")
    print("Rank: 1, 2, 3, 4, 5       (enter number from 1-5")
    while(True):
        user_input = input()
        try:
            rank = int(user_input)
            if(rank >= 1 and rank <= 5):
                q["rank"] = rank
                break
        except ValueError:
            print("not an int!")
    survay["done"].append(q)
    survay["progress"] += 1
    print("Completed questions:", survay["progress"])
    with open("survay_result.json", 'w') as fp:
        json.dump(survay,fp)
        print("saving progress")
