import requests
from bs4 import BeautifulSoup

from flask import Flask , render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://team:sparta@cluster0.yqkj8bv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# headers 콜을 날리기 위함
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# headers.content.decode('utf-8','replace')
html = requests.get('https://m.place.naver.com/restaurant/1043397620/home', headers=headers)  # 네이버지도가 잘 안되서 모바일 네이버지도로 변경
# print(html.encoding) #인코딩 확인

html.encoding = 'UTF-8'  # 한글깨짐 때문에 인코딩 변경 -> utf-8
# print(html.encoding)

soup = BeautifulSoup(html.text, 'html.parser')
# print(soup)

# 음식점 이름
title = soup.select_one('#_title > span.Fc1rA')

# 음식점 위치
location = soup.select_one("#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.tQY7D > div > a > span.LDgIH")

# 음식점 사진 - 이게 너무 어렵네요 ㅜㅜ

place = location.text.split()

result_location = " ".join(place[0:3])

print(result_location)

doc = {
    'title': title.text,
    'place': result_location
}
db.webscrap.insert_one(doc) # 음식점 이름과 위치 db의 'webscrap' collection에 저장

# print(title)
# print(title.text)
# print(location)
# print(location.text)
