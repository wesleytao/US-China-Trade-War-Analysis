def sentiment_analysis(sentence):
    import matplotlib.pyplot as plt
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentence)
    d=dict();
    d['neg']=vs['neg']
    d['neu']=vs['neu']
    d['pos']=vs['pos']
    d['compound']=vs['compound']
    return d
