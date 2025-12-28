# 🍳 Recipe Ingredient Extraction Using Named Entity Recognition (NER)

This project implements an end-to-end **Natural Language Processing (NLP)** system that extracts **ingredients, quantities, and measurement units** from unstructured cooking recipe text using a **custom Named Entity Recognition (NER)** model built with **spaCy**.  
The trained model is deployed as a **Flask REST API** and containerized using **Docker**.

---

## 📌 Problem Statement

Cooking recipes are usually written in free-form text, which makes it difficult for applications to automatically understand ingredients and measurements.  
This project solves that problem by converting unstructured recipe text into **structured JSON data**.

---

## 🚀 Features

- Custom spaCy **NER model** trained for recipe domain
- Extracts:
  - **INGREDIENT**
  - **QUANTITY**
  - **UNIT**
- Flask-based REST API for real-time inference
- Dockerized for portability and reproducibility
- Clean and structured JSON output

## 🛠️ Technologies Used

- **Python**
- **spaCy**
- **Flask**
- **Docker**

## 📂 Project Structure

recipe-ingredient-ner/
├── app/
│ └── app.py # Flask API
├── training/
│ └── train_ner.py # spaCy NER training script
├── model/
│ └── ingredient_ner/ # Trained NER model (generated)
├── data/ # (Optional) Dataset folder
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## 🧠 How It Works

1. Input recipe text is sent to the API
2. spaCy NER model processes the text
3. Entities are extracted and grouped
4. Structured JSON is returned

## 📥 Sample Input
{
  "text": "Add 2 cups of rice and 1 tablespoon olive oil"
}
## Sample Output
```
json
{
  "ingredients": [
    {
      "name": "rice",
      "quantity": "2",
      "unit": "cups"
    },
    {
      "name": "olive oil",
      "quantity": "1",
      "unit": "tablespoon"
    }
  ]
}
```


## 🧪 Model Training
**Train the model**
```
python training/train_ner.py
```

# 🌐 Running the Flask API (Without Docker)
**Install dependencies:**
```
pip install -r requirements.txt
```
**Run the API OR Start the server:**
```
python app/app.py
```
**API will be available at:**
```
POST http://localhost:5000/extract
```
**🧪 Testing the API (PowerShell)**
```
Invoke-RestMethod http://localhost:5000/extract `
-Method POST `
-ContentType "application/json" `
-Body '{"text":"Add 2 cups of rice and 1 tablespoon olive oil"}'
```
## 🐳 Running with Docker
**Build and run:**
```
docker-compose up --build
```
**API will be available at:**
```
POST http://localhost:5000/extract
```
