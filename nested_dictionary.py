import glob
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
filepaths = glob.glob("diary/*txt")
dates_keys = [date.replace("diary/","").replace(".txt","") for date in filepaths ] 

positive_scores =[]
negative_scores =[]

for file in filepaths:
    with open(file,"r") as file:
        day = file.read()
    scores = analyzer.polarity_scores(day)
    positive_scores.append(scores["pos"])
    negative_scores.append(scores["neg"])

#print(dates_keys)
#print(positive_scores)
#print(negative_scores)

'''
Construct dict:
my_dict = {
'2023-10-25':{
        "pos":0.159,
        "neg":0.203
    },
...
}
'''

my_dict = {}

for date in dates_keys:
    my_dict[date] = {}
    for score_neg in positive_scores:
        my_dict[date]["pos"] = score_neg
    for score_pos in negative_scores:
        my_dict[date]["neg"] = score_pos

print(my_dict)    


