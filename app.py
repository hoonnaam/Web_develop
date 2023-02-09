from flask import Flask , render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://team:sparta@cluster0.yqkj8bv.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('landing.html')

@app.route('/mainpage.html')
def mainpage():
   return render_template('mainpage.html')  #(기존)index.html -> templates 폴더 내 mainpage.html로 파일 이름 변경

@app.route('/foods', methods=['GET'])
def foods_get():
    foods_list = list(db.foods.find({}, {'_id': False}))
    return jsonify({'foods':foods_list})


@app.route('/foods', methods=['POST'])
def foods_post():
    username_receive = request.form['username_give']
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    image_receive = request.form['image_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # headers.content.decode('utf-8','replace')
    html = requests.get(url_receive, headers=headers)  # 네이버지도가 잘 안되서 모바일 네이버지도로 변경

    html.encoding = 'UTF-8'  # 한글깨짐 때문에 인코딩 변경 -> utf-8

    soup = BeautifulSoup(html.text, 'html.parser')

    title = soup.select_one('#_title > span.Fc1rA').text
    print(title)

    location = soup.select_one(
        "#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.tQY7D > div > a > span.LDgIH").text
    print(location)

    doc = {
         'username': username_receive,
         'title': title,
         'location': location,
         'url': url_receive,
         'star': star_receive,
         'comment': comment_receive,
         'image': image_receive
   }
    db.foods.insert_one(doc)
    return jsonify({'msg': '기록완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)