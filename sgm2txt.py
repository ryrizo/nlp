import re
import sys

from bs4 import BeautifulSoup

def getString(element):
    output = ""
    if (element != None):
        output = re.sub("[\t\r\n]", " ", element.string)
    return output

input = open(sys.argv[1], "r")
text = " ".join(input.readlines())
input.close()

xml = BeautifulSoup(text, features = "xml")

for article in xml.findAll("REUTERS"):
    id = article["NEWID"]
    topics = ""
    topicsElement = article.find("TOPICS")
    if (topicsElement != None):
        topics = ",".join([ element.string for element in topicsElement.findAll("D") ])
    title = getString(article.find("TITLE"))
    body = getString(article.find("BODY"))
    print(id + "\t" + topics + "\t" + title + "\t" + body)
