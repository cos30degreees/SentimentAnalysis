from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

analysis = TextBlob("TextBlob sure looks like it has some interesting features!")
print(analysis.translate(to='es'))
print(analysis.tags)
print(analysis.sentiment)

pos_count = 0
pos_correct = 0
threshold = 0.5

neg_count = 0
neg_correct = 0

with open("positive.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        if analysis.sentiment.polarity >= 0.1:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1



with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= -0.0000001:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count +=1
# with open("positive.txt","r") as f:
#     for line in f.read().split('\n'):
#         vs = analyzer.polarity_scores(line)
#         if not vs['neg'] > 0.1:
#             if vs['pos']-vs['neg'] > 0:
#                 pos_correct += 1
#             pos_count +=1
#
#
# neg_count = 0
# neg_correct = 0
#
# with open("negative.txt","r") as f:
#     for line in f.read().split('\n'):
#         vs = analyzer.polarity_scores(line)
#         if not vs['pos'] > 0.1:
#             if vs['pos']-vs['neg'] <= 0:
#                 neg_correct += 1
# with open('positive.txt',"r") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#         if analysis.sentiment.polarity <= 0:
#             neg_correct += 1
#         neg_count += 1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores("VADER Sentiment looks interesting, I have high hopes!")
print(vs)