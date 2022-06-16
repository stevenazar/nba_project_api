from flask import Flask, request, jsonify, make_response
import pandas as pd
import json

app = Flask(__name__)

#exemple de data
data_exemple = {}
data_exemple['1']={
    "name":"steven",
    "age":21
}
data_exemple['2']={
    "name":"tony",
    "age":23
}

#créer les routes
@app.route('/allplayers', methods=['GET'])
def get_all():
    df = pd.read_csv('nabadata.csv')
    data = {}
    for index, row in df.iterrows():
        data[index] = dict(row)
    return jsonify(data)

#route pour obtenir un joueur en particulier
@app.route('/allplayers/<index>', methods=['GET'])
def get_by_name(index):
    data_json_dict = {}
    with open('data.json', 'r', encoding="utf-8") as json_data:
        data_json_dict = json.loads(json_data.read())
        if index in data_json_dict:
            response = make_response(jsonify(data_json_dict[index]), 200)
            return response
        else:
            response = make_response(jsonify("error : Object not found"), 404)
            return response
#méthode qui permet de tester notre api
if __name__ == "__main__":
    app.run(debug=True)