import feedparser

#Grab Azure RSS Feed
NewsFeed = feedparser.parse("https://azurecomcdn.azureedge.net/en-us/updates/feed/")

entry = NewsFeed.entries[0]
count=len(NewsFeed.entries)
print(count)

print (entry.title)
print ("------News Link--------")
print (entry.link)