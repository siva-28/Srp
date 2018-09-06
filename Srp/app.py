from flask_pymongo import PyMongo
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'depstaff'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dep&staff'
mongo = PyMongo(app)


@app.route('/dep', methods=['GET'])
def get_dep():
    dep = mongo.db.department
    output = []
    for s in dep.find():
      output.append({'name': s['name']})
    return jsonify({'result': output})


@app.route('/CSE', methods=['GET'])
def get_cse():
    CSE = mongo.db.CSE
    output = []
    for s in CSE.find():
      output.append({'name': s['name']})
    return jsonify({'result': output})


@app.route('/CSE/<name>', methods=['GET'])
def get_cse_staff(name):
    CSE = mongo.db.CSE
    s = CSE.find_one({"name": name})
    if s: output = {"name": s['name'], "r1": s['r1'], "r2": s['r2'], "r3": s['r3'], "r4": s['r4'], "r5": s['r5']}
    else:
        output = "NO SUCH NAME"
    return jsonify({'result': output})


@app.route('/IT', methods=['GET'])
def get_it():
    IT = mongo.db.IT
    output = []
    for s in IT.find():
      output.append({'name' : s['name']})
    return jsonify({'result' : output})


@app.route('/IT/<name>', methods=['GET'])
def get_it_staff(name):
    IT = mongo.db.IT
    s = IT.find_one({"name": name})
    if s:output = {"name": s['name'], "r1": s['r1'], "r2": s['r2'], "r3": s['r3'], "r4": s['r4'], "r5": s['r5']}
    else:
        output = "NO SUCH NAME"
    return jsonify({'result': output})


@app.route('/IT/<name>/<r1>/<r2>/<r3>/<r4>/<r5>', methods=['GET'])
def insert_staff1(name, r1, r2, r3, r4, r5):
    IT = mongo.db.IT
    id = IT.insert({'name': name, 'r1': int(r1), 'r2': int(r2), 'r3': int(r3), 'r4': int(r4), 'r5': int(r5)})
    nam2 = IT.find_one({'name': name})
    output = {'name': nam2['name'], 'r1': nam2['r1'], 'r2': nam2['r2'], 'r3': nam2['r3'], 'r4': nam2['r4'], 'r5': nam2['r5']}
    return jsonify({'result': output})


@app.route('/CSE/<name>/<r1>/<r2>/<r3>/<r4>/<r5>', methods=['GET'])
def insert_staff2(name, r1, r2, r3, r4, r5):
    cse = mongo.db.CSE
    id = cse.insert({'name': name, 'r1': int(r1), 'r2': int(r2), 'r3': int(r3), 'r4': int(r4), 'r5': int(r5)})
    nam2 = cse.find_one({'name': name})
    output = {'name': nam2['name'], 'r1': nam2['r1'], 'r2': nam2['r2'], 'r3': nam2['r3'], 'r4': nam2['r4'], 'r5': nam2['r5']}
    return jsonify({'result': output})


@app.route('/CSE', methods=['POST'])
def update_staff1():
    cse = mongo.db.CSE
    name = request.json['name']
    r1 = request.json['r1']
    r2 = request.json['r2']
    r3 = request.json['r3']
    r4 = request.json['r4']
    r5 = request.json['r5']
    nam = cse.find_one({'name': name})
    rr1 = nam['r1']
    rr2 = nam['r2']
    rr3 = nam['r3']
    rr4 = nam['r4']
    rr5 = nam['r5']
    s1 = (rr1 + r1) / 2
    s2 = (rr2 + r2) / 2
    s3 = (rr3 + r3) / 2
    s4 = (rr4 + r4) / 2
    s5 = (rr5 + r5) / 2
    cse.update_one({'name': name}, {"$set": {"r1": s1}})
    cse.update_one({'name': name}, {"$set": {"r2": s2}})
    cse.update_one({'name': name}, {"$set": {"r3": s3}})
    cse.update_one({'name': name}, {"$set": {"r4": s4}})
    cse.update_one({'name': name}, {"$set": {"r5": s5}})
    nam2 = cse.find_one({'name': name})
    output = {'name': nam2['name'], 'r1': nam2[s1], 'r2': nam2[s2], 'r3': nam2[s3], 'r4': nam2[s4], 'r5': nam2[s5]}
    return jsonify({'result': output})


@app.route('/IT', methods=['POST'])
def update_staff2():
    it = mongo.db.IT
    name = request.json['name']
    r1 = request.json['r1']
    r2 = request.json['r2']
    r3 = request.json['r3']
    r4 = request.json['r4']
    r5 = request.json['r5']
    nam = it.find_one({'name': name})
    rr1 = nam['r1']
    rr2 = nam['r2']
    rr3 = nam['r3']
    rr4 = nam['r4']
    rr5 = nam['r5']
    s1 = (rr1 + r1) / 2
    s2 = (rr2 + r2) / 2
    s3 = (rr3 + r3) / 2
    s4 = (rr4 + r4) / 2
    s5 = (rr5 + r5) / 2
    it.update_one({'name': name}, {"$set": {"r1": s1}})
    it.update_one({'name': name}, {"$set": {"r2": s2}})
    it.update_one({'name': name}, {"$set": {"r3": s3}})
    it.update_one({'name': name}, {"$set": {"r4": s4}})
    it.update_one({'name': name}, {"$set": {"r5": s5}})
    nam2 = it.find_one({'name': name})
    output = {'name': nam2['name'], 'r1': nam2[s1], 'r2': nam2[s2], 'r3': nam2[s3], 'r4': nam2[s4], 'r5': nam2[s5]}
    return jsonify({'result': output})


if __name__ == '__main__':
    app.debug = True
    app.run(host='10.11.159.56')
