from flask import Flask,jsonify,request

app = Flask(__name__)

#Sample data
genus_species_map = {"Homo": ["Homo sapiens","Homo neanderthalensis"], "Pan": ["Pan troglodytes","Pan paniscus"], "Canis": ["canis lupus","Canis aureus"]}

@app.route('/species/<genus>',methods=['GET'])
def get_species(genus):
    print(f"Request got")
    if genus in genus_species_map:
        return jsonify({"species":genus_species_map[genus]})
    else:
        return jsonify({"error":f"Genus {genus} not found"})
if __name__ == "__main__":
    app.run(debug=True)

