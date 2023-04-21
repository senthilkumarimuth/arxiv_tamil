"""
Go to website https://arxiv.org/ and find the papers in the field of computer science for yesterday. I need both summary
and pdf of the papers
"""

import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import datetime
import PyPDF2
from textblob import TextBlob

# to get the date of yesterday
yesterday = datetime.date.today() - datetime.timedelta(days=1)
# print(yesterday)

# to get the date of yesterday in the format of the website
yesterday_date = yesterday.strftime("%Y%m%d")
# print(yesterday_date)

# to get the url of the page of the papers of yesterday
url = "https://arxiv.org/list/cs/pastweek?skip=0&show=" + yesterday_date
# print(url)

# to get the content of the page
page = requests.get(url)
# print(page)

# to get the soup of the page
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

# to get the list of all the papers of yesterday
papers = soup.find_all("div", class_="meta")
# print(papers)

# to get the links to the abstracts of the papers of yesterday
paper_links = []
for paper in papers:
    link = paper.find("a", href=True)
    paper_links.append("https://arxiv.org" + link["href"])
# print(paper_links)

# to get the title of the papers of yesterday
paper_titles = []
for paper in papers:
    title = paper.find("div", class_="list-title mathjax")
    paper_titles.append(title.text.replace("\n", ""))
# print(paper_titles)

# to get the authors of the papers of yesterday
paper_authors = []
for paper in papers:
    authors = paper.find("div", class_="list-authors")
    paper_authors.append(authors.text.replace("\n", ""))
# print(paper_authors)

# to get the summary of the papers of yesterday
paper_summaries = []
for link in paper_links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    summary = soup.find("span", class_="abstract-full has-text-grey-dark mathjax")
    if summary is not None:
        paper_summaries.append(summary.text.replace("\n", ""))
    else:
        paper_summaries.append("No summary available")
# print(paper_summaries)

# # to get the pdf of the papers of yesterday
# for link in paper_links:
#     pdf_link = link.replace("abs", "pdf") + ".pdf"
#     title = link.split("/")[-1]
#     urllib.request.urlretrieve(pdf_link, title + ".pdf")