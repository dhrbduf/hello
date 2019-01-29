import requests, json
from bs4 import BeautifulSoup

headers = {
    "X-Naver-Client-Id": "dRgjJjP4QdJyV3qR8oqS",
    "X-Naver-Client-Secret": "uB4v_zPuG0"
}

# title = "Python"
title = "파이썬"

params = {
    "display": 20,
    "start": 1,
    "sort": "date",
    "query": title
}

# url = "https://openapi.naver.com/v1/search/book.json"
url = "https://openapi.naver.com/v1/search/blog"
# url = "https://openapi.naver.com/v1/search/image"
html = requests.get(url, params=params, headers=headers).text
jsonData = json.loads(html)
print(json.dumps(jsonData, ensure_ascii=False, indent=2))

for i in jsonData['items']:
    print(i['title'], i['link'], i['bloggername'], i['postdate'])
