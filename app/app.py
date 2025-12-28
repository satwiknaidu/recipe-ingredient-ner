from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("model/ingredient_ner")

@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()
    text = data.get("text", "")

    doc = nlp(text)
    ingredients = []

    temp = {}

    for ent in doc.ents:
        if ent.label_ == "INGREDIENT":
            temp["name"] = ent.text
        elif ent.label_ == "QUANTITY":
            temp["quantity"] = ent.text
        elif ent.label_ == "UNIT":
            temp["unit"] = ent.text

        if len(temp) == 3:
            ingredients.append(temp)
            temp = {}

    return jsonify({"ingredients": ingredients})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
