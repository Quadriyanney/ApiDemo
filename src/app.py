from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'api_test'
app.config['MONGO_URI'] = 'mongodb://Quadriyanney:quadriy@ds133104.mlab.com:33104/api_test'

mongo = PyMongo(app)


@app.route("/utensils", methods=['GET'])
def get_all_utensils():
	collection_utensils = mongo.db.utensils
	sort = str(request.args['sort'])
	
	if sort == "desc":
		utensils = collection_utensils.find().sort('name', pymongo.DESCENDING)
	elif sort == "asc":
		utensils = collection_utensils.find().sort('name', pymongo.ASCENDING)
	else:
		utensils = collection_utensils.find()
	
	results = []
	
	for item in utensils:
		results.append({"name": item["name"],
			"use": item["use"]})
	
	return jsonify({"results": results})


@app.route("/utensils/<name>", methods=['GET'])
def get_one_utensil_by_name(name):
	collection_utensils = mongo.db.utensils
	utensil = collection_utensils.find_one({"name": name})

	if utensil:
		result = [{"name": name,
		"use": utensil["use"]}
		]
		return jsonify({"result": result})

	return "No item with name {}".format(name)


@app.route("/utensils/<name>", methods=['DELETE'])
def delete_one_utensil_by_name(name):
	collection_utensils = mongo.db.utensils
	utensil = collection_utensils.find_one({"name": name})

	if utensil:
		collection_utensils.delete_one({"name": name})
		return "Item with name {} deleted".format(name)

	return "No Item with name {}".format(name)


@app.route("/utensils", methods=['POST'])
def add_one_utensil():
	collection_utensils = mongo.db.utensils

	name = request.json['name']
	use = request.json['use']

	collection_utensils.insert({"name": name, "use": use})
	utensil = collection_utensils.find_one({"name": name})

	if utensil:
		return "Item add succeddfully"
	return "Item not added"


@app.route("/utensils/<name>", methods=['PUT'])

def update_one_utensil(name):
	collection_utensils = mongo.db.utensils
	utensil = collection_utensils.find_one({"name": name})

	if utensil:
		new_name = request.json["name"]
		use = request.json["use"]

		collection_utensils.update({"name": name}, {"name": new_name, "use": use})

		return "Update successful"
	return "No Item with name {}".format(name)


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)