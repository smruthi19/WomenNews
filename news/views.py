from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
import datetime
import urllib.request as url
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import requests
import json
import pytz
from bson import json_util
from pattern.en import sentiment
from textblob import TextBlob


# def batchUpdate():
#     cluster = "mongodb+srv://smruthi19:denver737@cluster0.7nlg0ut.mongodb.net/test?retryWrites=true&w=majority"
#     client=MongoClient(cluster)
#
#
#     # print(client.list_database_names()) #database name - test, collection name - news
#
#     db=client.test #choosing the database test
#     # print(db.list_collection_names()) #printing the collection in test database
#
#     news = db.news
#     print("hi")
#
#     currentTime= datetime.datetime.now(tz=pytz.timezone('America/New_York'))
#     print(currentTime)
#     if(currentTime.hour==15 and currentTime.minute==35):
#         print("y")
#         newsItem1 = {"title": "first", "text": "this is the first news", "datePublished":datetime.datetime.utcnow()}
#         result = news.insert_one(newsItem1)
#
#     updateTime = datetime.datetime(2022,11, 7, 3,14).strftime("%Y-%m-%d %H:%M")
#     if (currentTime == updateTime):
#         print("hello")
#         newsItem1 = {"title": "first", "text": "this is the first news", "datePublished":datetime.datetime.utcnow()}
#         result = news.insert_one(newsItem1)

def getData(request):
    # batchUpdate()
    # testing the api
    # analyze = SentimentIntensityAnalyzer()
    # website = "https://gnews.io/api/v4/search?q=women%20sports&token=c3d778f78051de561ad0e0d91793aee8&lang=en"
    # open = url.urlopen(website)
    # data = open.read()
    # dataUpdated = json.loads(data)
    # print(dataUpdated["articles"][0])
    #
    # element = dataUpdated["articles"][0]


    #accessing db
    cluster = "mongodb+srv://smruthi19:denver737@cluster0.7nlg0ut.mongodb.net/test?retryWrites=true&w=majority"
    client=MongoClient(cluster)


    # print(client.list_database_names()) #database name - test, collection name - news

    db=client.test #choosing the database test
    # print(db.list_collection_names()) #printing the collection in test database

    #choosing the collection news
    news = db.news


    # accessing the API data
    # url = "https://api.newscatcherapi.com/v2/search"
    #
    # querystring = {"q":"\"Women in STEM\"","lang":"en","sort_by":"relevancy","page":"1"}
    #
    # headers = {
    #     "x-api-key":"0rev02lubXPbHWkJafN4U8kk4Q1N7rmDie753ZuFDbk"
    #     }
    #
    # # # retrieving the API data
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print("news")
    # print(response.text)
    # # convert response from API to json object
    # dataUpdated = json.loads(response.text)
    # index=0
    # # list that stores positive news, all elements have polarity > 0.5
    # positiveNews = []
    # print(len(dataUpdated["articles"]))
    # # iterate through the API data
    # while (index <len(dataUpdated["articles"])):
    #     #print(dataUpdated["articles"][0]["summary"])
    #     # initialize the sentiment analyzer
    #     analyze = SentimentIntensityAnalyzer()
    #     # get the dictionary of polarities
    #     polarity = analyze.polarity_scores(dataUpdated["articles"][index]["summary"])
    #     # print(dataUpdated["articles"][index]["summary"])
    #     # store compound polarity value for each article
    #     compound_polarity = polarity["compound"]
    #     print(compound_polarity)
    #     # if compound polarity greater than 0.5, check that list does not already have this article, then append
    #     if (compound_polarity>0.5):
    #         # print(dataUpdated["articles"][index])
    #         # if (dataUpdated["articles"][index]["title"] in positiveNews):
    #         #     print("here")
    #         positionInPostiveNews = 0
    #         containsValue = False
    #         # iterate through current positiveNews list to check that it does not have the current element, before adding it (checking for duplicates)
    #         while(positionInPostiveNews<len(positiveNews)):
    #             print("value")
    #             print(positiveNews[positionInPostiveNews]["title"])
    #             print(dataUpdated["articles"][index]["title"])
    #             if ((positiveNews[positionInPostiveNews]["title"]).__eq__(dataUpdated["articles"][index]["title"])):
    #                 containsValue = True
    #                 print("found")
    #             positionInPostiveNews=positionInPostiveNews+1;
    #
    #         # add to list if doesn't contain value
    #         if(containsValue ==False):
    #             positiveNews.append(dataUpdated["articles"][index])
                  # positiveNews[positionInPositiveNews+1].update(category="sports")

    #
    #         print(dataUpdated["articles"][index]["title"])
    #
    #         # print(compound_polarity)
    #     index=index+1
    #     print(index)
    #
    #
    # print((positiveNews))
    # print("positive")
    # print(len(positiveNews))
    #
    # positiveNewsIndex=0
    # # iterate through positiveNews list before batch insert to ensure no duplicate keys
    # while positiveNewsIndex < len(positiveNews):
    #     title = positiveNews[positiveNewsIndex]["title"]
    #     print(title)
    #     # if database already contains the title, remove this from list so that it doesn't get added again
    #     if (news.find_one({"title":title})):
    #         print("already there")
    #         print(title)
    #         positiveNews.remove(positiveNews[positiveNewsIndex])
    #
    #
    # print(len(positiveNews))
    # if(len(positiveNews)!=0):
    #     result=news.insert_many(positiveNews)

    # print(dataUpdated2["articles"])
    # get the most recent 10 values (last 10 values in database)
    recentValues = news.find("category:sports").sort('$natural',-1).limit(1)
    # db.foo.find().sort({$natural:1});
    recentValues2 = news.find().sort('$natural',-1).limit(2)
    print("start printing")


    # for position in range(2):
    #     print(recentValues2[position])
    #
    # print("recent")



    recentValues2_updated = json.loads(json_util.dumps(recentValues2))

    recentValues_updated = json.loads(json_util.dumps(recentValues))

    # x2 = json.loads(json_util.dumps(x))
    # recentValues_updated.append(x2)
    # print("x added")
    #
    # recentValues_updated.append(recentValues2_updated)


    # print(result2["title"])

    # print(sentiment(result2["excerpt"]))
    # print((TextBlob(result2["excerpt"])).sentiment.polarity)
    # result=json.dumps(result)
    # print("result")
    # print(result)

    # return render(request, "index.html",  {'result' : result})
    # output the last 10 added values in database
    return JsonResponse(recentValues_updated, safe=False)
    # return render(request,"index.html", {'output':output})

def getBusinessData(request):
    # batchUpdate()
    # testing the api
    # analyze = SentimentIntensityAnalyzer()
    # website = "https://gnews.io/api/v4/search?q=women%20sports&token=c3d778f78051de561ad0e0d91793aee8&lang=en"
    # open = url.urlopen(website)
    # data = open.read()
    # dataUpdated = json.loads(data)
    # print(dataUpdated["articles"][0])
    #
    # element = dataUpdated["articles"][0]


    #accessing db
    cluster = "mongodb+srv://smruthi19:denver737@cluster0.7nlg0ut.mongodb.net/test?retryWrites=true&w=majority"
    client=MongoClient(cluster)


    # print(client.list_database_names()) #database name - test, collection name - news

    db=client.test #choosing the database test
    # print(db.list_collection_names()) #printing the collection in test database

    #choosing the collection news
    news = db.news


    # accessing the API data
    # url = "https://api.newscatcherapi.com/v2/search"
    #
    # querystring = {"q":"\"Women in STEM\"","lang":"en","sort_by":"relevancy","page":"1"}
    #
    # headers = {
    #     "x-api-key":"pFmuhXwbEj6M28ka1fGxfOR_6y3PiinaoCOkh-5qfjA"
    #     }
    #
    # # # retrieving the API data
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print("news")
    # print(response.text)
    # # convert response from API to json object
    # dataUpdated = json.loads(response.text)
    # index=0
    # # list that stores positive news, all elements have polarity > 0.5
    # positiveNews = []
    # print(len(dataUpdated["articles"]))
    # # iterate through the API data
    # while (index <len(dataUpdated["articles"])):
    #     #print(dataUpdated["articles"][0]["summary"])
    #     # initialize the sentiment analyzer
    #     analyze = SentimentIntensityAnalyzer()
    #     # get the dictionary of polarities
    #     polarity = analyze.polarity_scores(dataUpdated["articles"][index]["summary"])
    #     # print(dataUpdated["articles"][index]["summary"])
    #     # store compound polarity value for each article
    #     compound_polarity = polarity["compound"]
    #     print(compound_polarity)
    #     # if compound polarity greater than 0.5, check that list does not already have this article, then append
    #     if (compound_polarity>0.5):
    #         # print(dataUpdated["articles"][index])
    #         # if (dataUpdated["articles"][index]["title"] in positiveNews):
    #         #     print("here")
    #         positionInPostiveNews = 0
    #         containsValue = False
    #         # iterate through current positiveNews list to check that it does not have the current element, before adding it (checking for duplicates)
    #         while(positionInPostiveNews<len(positiveNews)):
    #             print("value")
    #             print(positiveNews[positionInPostiveNews]["title"])
    #             print(dataUpdated["articles"][index]["title"])
    #             if ((positiveNews[positionInPostiveNews]["title"]).__eq__(dataUpdated["articles"][index]["title"])):
    #                 containsValue = True
    #                 print("found")
    #             positionInPostiveNews=positionInPostiveNews+1;
    #
    #         # add to list if doesn't contain value
    #         if(containsValue ==False):
    #             positiveNews.append(dataUpdated["articles"][index])
    #
    #         print(dataUpdated["articles"][index]["title"])
    #
    #         # print(compound_polarity)
    #     index=index+1
    #     print(index)
    #
    #
    # print((positiveNews))
    # print("positive")
    # print(len(positiveNews))
    #
    # positiveNewsIndex=0
    # # iterate through positiveNews list before batch insert to ensure no duplicate keys
    # while positiveNewsIndex < len(positiveNews):
    #     title = positiveNews[positiveNewsIndex]["title"]
    #     print(title)
    #     # if database already contains the title, remove this from list so that it doesn't get added again
    #     if (news.find_one({"title":title})):
    #         print("already there")
    #         print(title)
    #         positiveNews.remove(positiveNews[positiveNewsIndex])
    #
    #
    # print(len(positiveNews))
    # if(len(positiveNews)!=0):
    #     result=news.insert_many(positiveNews)

    # print(dataUpdated2["articles"])
    # get the most recent 10 values (last 10 values in database)
    recentValues = news.find().sort('$natural',-1).limit(10)
    # db.foo.find().sort({$natural:1});

    print(recentValues)
    for position in range(10):
        print(recentValues[position])

    print("recent")

    # print(result2["title"])

    # print(sentiment(result2["excerpt"]))
    # print((TextBlob(result2["excerpt"])).sentiment.polarity)
    # result=json.dumps(result)
    # print("result")
    # print(result)

    # return render(request, "index.html",  {'result' : result})
    # output the last 10 added values in database
    return JsonResponse(json.loads(json_util.dumps(recentValues)), safe=False)
    # return render(request,"index.html", {'output':output})

def getStemData(request):
    # batchUpdate()
    # testing the api
    # analyze = SentimentIntensityAnalyzer()
    # website = "https://gnews.io/api/v4/search?q=women%20sports&token=c3d778f78051de561ad0e0d91793aee8&lang=en"
    # open = url.urlopen(website)
    # data = open.read()
    # dataUpdated = json.loads(data)
    # print(dataUpdated["articles"][0])
    #
    # element = dataUpdated["articles"][0]


    #accessing db
    cluster = "mongodb+srv://smruthi19:denver737@cluster0.7nlg0ut.mongodb.net/test?retryWrites=true&w=majority"
    client=MongoClient(cluster)


    # print(client.list_database_names()) #database name - test, collection name - news

    db=client.test #choosing the database test
    # print(db.list_collection_names()) #printing the collection in test database

    #choosing the collection news
    news = db.news


    # accessing the API data
    # url = "https://api.newscatcherapi.com/v2/search"
    #
    # querystring = {"q":"\"Women in STEM\"","lang":"en","sort_by":"relevancy","page":"1"}
    #
    # headers = {
    #     "x-api-key":"pFmuhXwbEj6M28ka1fGxfOR_6y3PiinaoCOkh-5qfjA"
    #     }
    #
    # # # retrieving the API data
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print("news")
    # print(response.text)
    # # convert response from API to json object
    # dataUpdated = json.loads(response.text)
    # index=0
    # # list that stores positive news, all elements have polarity > 0.5
    # positiveNews = []
    # print(len(dataUpdated["articles"]))
    # # iterate through the API data
    # while (index <len(dataUpdated["articles"])):
    #     #print(dataUpdated["articles"][0]["summary"])
    #     # initialize the sentiment analyzer
    #     analyze = SentimentIntensityAnalyzer()
    #     # get the dictionary of polarities
    #     polarity = analyze.polarity_scores(dataUpdated["articles"][index]["summary"])
    #     # print(dataUpdated["articles"][index]["summary"])
    #     # store compound polarity value for each article
    #     compound_polarity = polarity["compound"]
    #     print(compound_polarity)
    #     # if compound polarity greater than 0.5, check that list does not already have this article, then append
    #     if (compound_polarity>0.5):
    #         # print(dataUpdated["articles"][index])
    #         # if (dataUpdated["articles"][index]["title"] in positiveNews):
    #         #     print("here")
    #         positionInPostiveNews = 0
    #         containsValue = False
    #         # iterate through current positiveNews list to check that it does not have the current element, before adding it (checking for duplicates)
    #         while(positionInPostiveNews<len(positiveNews)):
    #             print("value")
    #             print(positiveNews[positionInPostiveNews]["title"])
    #             print(dataUpdated["articles"][index]["title"])
    #             if ((positiveNews[positionInPostiveNews]["title"]).__eq__(dataUpdated["articles"][index]["title"])):
    #                 containsValue = True
    #                 print("found")
    #             positionInPostiveNews=positionInPostiveNews+1;
    #
    #         # add to list if doesn't contain value
    #         if(containsValue ==False):
    #             positiveNews.append(dataUpdated["articles"][index])
    #
    #         print(dataUpdated["articles"][index]["title"])
    #
    #         # print(compound_polarity)
    #     index=index+1
    #     print(index)
    #
    #
    # print((positiveNews))
    # print("positive")
    # print(len(positiveNews))
    #
    # positiveNewsIndex=0
    # # iterate through positiveNews list before batch insert to ensure no duplicate keys
    # while positiveNewsIndex < len(positiveNews):
    #     title = positiveNews[positiveNewsIndex]["title"]
    #     print(title)
    #     # if database already contains the title, remove this from list so that it doesn't get added again
    #     if (news.find_one({"title":title})):
    #         print("already there")
    #         print(title)
    #         positiveNews.remove(positiveNews[positiveNewsIndex])
    #
    #
    # print(len(positiveNews))
    # if(len(positiveNews)!=0):
    #     result=news.insert_many(positiveNews)

    # print(dataUpdated2["articles"])
    # get the most recent 10 values (last 10 values in database)
    recentValues = news.find().sort('$natural',-1).limit(10)
    # db.foo.find().sort({$natural:1});

    print(recentValues)
    for position in range(10):
        print(recentValues[position])

    print("recent")

    # print(result2["title"])

    # print(sentiment(result2["excerpt"]))
    # print((TextBlob(result2["excerpt"])).sentiment.polarity)
    # result=json.dumps(result)
    # print("result")
    # print(result)

    # return render(request, "index.html",  {'result' : result})
    # output the last 10 added values in database
    return JsonResponse(json.loads(json_util.dumps(recentValues)), safe=False)
def getSportsData(request):
    # batchUpdate()
    # testing the api
    # analyze = SentimentIntensityAnalyzer()
    # website = "https://gnews.io/api/v4/search?q=women%20sports&token=c3d778f78051de561ad0e0d91793aee8&lang=en"
    # open = url.urlopen(website)
    # data = open.read()
    # dataUpdated = json.loads(data)
    # print(dataUpdated["articles"][0])
    #
    # element = dataUpdated["articles"][0]


    #accessing db
    cluster = "mongodb+srv://smruthi19:denver737@cluster0.7nlg0ut.mongodb.net/test?retryWrites=true&w=majority"
    client=MongoClient(cluster)


    # print(client.list_database_names()) #database name - test, collection name - news

    db=client.test #choosing the database test
    # print(db.list_collection_names()) #printing the collection in test database

    #choosing the collection news
    news = db.news


    # accessing the API data
    # url = "https://api.newscatcherapi.com/v2/search"
    #
    # querystring = {"q":"\"Women in STEM\"","lang":"en","sort_by":"relevancy","page":"1"}
    #
    # headers = {
    #     "x-api-key":"pFmuhXwbEj6M28ka1fGxfOR_6y3PiinaoCOkh-5qfjA"
    #     }
    #
    # # # retrieving the API data
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print("news")
    # print(response.text)
    # # convert response from API to json object
    # dataUpdated = json.loads(response.text)
    # index=0
    # # list that stores positive news, all elements have polarity > 0.5
    # positiveNews = []
    # print(len(dataUpdated["articles"]))
    # # iterate through the API data
    # while (index <len(dataUpdated["articles"])):
    #     #print(dataUpdated["articles"][0]["summary"])
    #     # initialize the sentiment analyzer
    #     analyze = SentimentIntensityAnalyzer()
    #     # get the dictionary of polarities
    #     polarity = analyze.polarity_scores(dataUpdated["articles"][index]["summary"])
    #     # print(dataUpdated["articles"][index]["summary"])
    #     # store compound polarity value for each article
    #     compound_polarity = polarity["compound"]
    #     print(compound_polarity)
    #     # if compound polarity greater than 0.5, check that list does not already have this article, then append
    #     if (compound_polarity>0.5):
    #         # print(dataUpdated["articles"][index])
    #         # if (dataUpdated["articles"][index]["title"] in positiveNews):
    #         #     print("here")
    #         positionInPostiveNews = 0
    #         containsValue = False
    #         # iterate through current positiveNews list to check that it does not have the current element, before adding it (checking for duplicates)
    #         while(positionInPostiveNews<len(positiveNews)):
    #             print("value")
    #             print(positiveNews[positionInPostiveNews]["title"])
    #             print(dataUpdated["articles"][index]["title"])
    #             if ((positiveNews[positionInPostiveNews]["title"]).__eq__(dataUpdated["articles"][index]["title"])):
    #                 containsValue = True
    #                 print("found")
    #             positionInPostiveNews=positionInPostiveNews+1;
    #
    #         # add to list if doesn't contain value
    #         if(containsValue ==False):
    #             positiveNews.append(dataUpdated["articles"][index])
    #
    #         print(dataUpdated["articles"][index]["title"])
    #
    #         # print(compound_polarity)
    #     index=index+1
    #     print(index)
    #
    #
    # print((positiveNews))
    # print("positive")
    # print(len(positiveNews))
    #
    # positiveNewsIndex=0
    # # iterate through positiveNews list before batch insert to ensure no duplicate keys
    # while positiveNewsIndex < len(positiveNews):
    #     title = positiveNews[positiveNewsIndex]["title"]
    #     print(title)
    #     # if database already contains the title, remove this from list so that it doesn't get added again
    #     if (news.find_one({"title":title})):
    #         print("already there")
    #         print(title)
    #         positiveNews.remove(positiveNews[positiveNewsIndex])
    #
    #
    # print(len(positiveNews))
    # if(len(positiveNews)!=0):
    #     result=news.insert_many(positiveNews)

    # print(dataUpdated2["articles"])
    # get the most recent 10 values (last 10 values in database)
    recentValues = news.find().sort('$natural',-1).limit(10)

    # get the most recent 10 values
    # db.foo.find().sort({$natural:1});

    print(recentValues2)
    for position in range(10):
        print(recentValues[position])

    print("recent2")




    # print(result2["title"])

    # print(sentiment(result2["excerpt"]))
    # print((TextBlob(result2["excerpt"])).sentiment.polarity)
    # result=json.dumps(result)
    # print("result")
    # print(result)

    # return render(request, "index.html",  {'result' : result})
    # output the last 10 added values in database
    return JsonResponse(json.loads(json_util.dumps(recentValues)), safe=False), JsonResponse(json.loads(json_util.dumps(recentValues2)), safe=False)
    # return render(request,"index.html", {'output':output})




    ## To Do:
    ## 1. Move sentiment analysis code/inserting into database to separate python file in this djangoproject (insert.py)
    ## 2. Cron job should run on insert.py for batch inserting/updating the list_database (once a day)
    ## 3. Have a separate python file in this project for cleaning the database (removes the oldest 5 entries)
    ## 4. Cron job to run on clean.py (once in 2 weeks?)

    # Is it better to create >1 collections (tables) within the one database for each category of news
