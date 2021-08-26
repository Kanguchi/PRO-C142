import csv

all_articles = []

with open("articles.csv",encoding="UTF8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

for articles in all_articles:
    if articles[14] == 'pt':
        all_articles.remove(articles)

liked_articles = []
not_liked_articles = []