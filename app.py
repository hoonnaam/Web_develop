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
   return render_template('index.html')

@app.route('/foods', methods=['GET'])
def foods_get():
    foods_list = list(db.foods.find({}, {'_id': False}))
    return jsonify({'foods':foods_list})

## 닉네임 저장
@app.route("/api/nickname", methods=["POST"])
def name_init():
    # user 의 닉네임을 받아옵니다.
    name_receive = request.form['name_give']

    # user의 닉네임이 중복인지 확인합니다.
    users_list = list(db.users.find({}, {'_id': False}))
    for user in users_list:
        if name_receive == user.get('name'):
            return jsonify({'msg': '중복입니다!'})

    ## Result 값 0으로 init
    result_receive = 0

    ## url 값 임의의 url 값으로 init
    url_receive = ''

    ## result_list 값 0으로 init
    result_list_receive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    doc = {
        'name': name_receive,
        'result': result_receive,
        'image': url_receive,
        'result_list': result_list_receive
    }

    db.users.insert_one(doc)

    return jsonify({'msg': '동네이름과 닉네임 등록 완료! \n구경하러 가기!'})

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