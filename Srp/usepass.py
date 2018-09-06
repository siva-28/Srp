from flask_pymongo import PyMongo
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'depstaff'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dep&staff'
mongo = PyMongo(app)


@app.route('/usepass', methods=['GET'])
def get_dep():
    up = mongo.db.usepass
    output = []
    for s in up.find():
      output.append({'uname': s['uname'], 'pass': s['pass']})
    return jsonify({'result': output})


@app.route('/usepass/user/Pass', methods=['GET'])
def insert_user(user,Pass):
    use = mongo.db.usepass
    id = use.insert({'uname': user, 'pass': Pass})
    nam2 = use.find_one({'uname': user})
    output = {'uname': user, 'pass': Pass}
    return jsonify({'result': output})
