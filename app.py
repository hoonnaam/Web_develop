from flask import Flask , render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://team:sparta@cluster0.yqkj8bv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('landing.html')

@app.route('/mainpage')
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

    doc = {
         'username': username_receive,
         'url': url_receive,
         'star': star_receive,
         'comment': comment_receive,
         'image': image_receive
   }
    db.foods.insert_one(doc)
    return jsonify({'msg': '기록되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)