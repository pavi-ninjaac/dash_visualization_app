from textblob import TextBlob


analysis=TextBlob('textblob looks like having a very interesting features')
print(dir(analysis))
print(analysis.translate(to='es'))

#analysed values
print(analysis.sentiment)

#Sentiment(polarity=0.65, subjectivity=0.65)
"""
polarity is between -1 to 1 and >0.5 is pasitive and <-0.5 is negative and <0.5 and >-0.5 is nuetral values

"""
#then check the vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analuser=SentimentIntensityAnalyzer()
v_polarity_score=analuser.polarity_scores('vader have too some interesting feature and i really like it')
print(v_polarity_score)

#{'neg': 0.0, 'neu': 0.621, 'pos': 0.379, 'compound': 0.6697}
"""
some rules:
positive statement : compound >= 0.5
negative statement : compound <= -0.5
nuetral statement  : compound < 0.5 and compound > -0.5
so clearly above statement is pasitive statement done.
"""
