from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os, random

app = Flask(__name__)

# Render gives database URL as an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Create a simple model
class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(100))
    calories = db.Column(db.Integer)

@app.route('/')
def home():
    return "🍎 Calorie AI Backend Connected to Database!"

@app.route('/add', methods=['POST'])
def add_food():
    data = request.get_json()
    food = data.get("food")
    calories = random.randint(50, 400)  # later use AI or real logic
    entry = FoodEntry(food=food, calories=calories)
    db.session.add(entry)
    db.session.commit()
    return jsonify({"message": "Food added!", "food": food, "calories": calories})

@app.route('/list')
def list_foods():
    foods = FoodEntry.query.all()
    result = [{"food": f.food, "calories": f.calories} for f in foods]
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
