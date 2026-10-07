from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb://admin:admin123@localhost:27017/"
)

db = client['pole_chudes_db']
collection = db['words']

collection.delete_many({})

word1 = {
"word": "КОСМОНАВТ",
"category": "Профессии",
"hint": "Человек, работающий в космосе",
"difficulty": "средняя",
"used": False,
"guessed_count": 0
}

result = collection.insert_one(word1)
print(f"Inserted ID: {result.inserted_id}")

words = [
{"word": "ПИРАМИДА", "category": "Архитектура", "hint":
"Древнее сооружение в Египте",
"difficulty": "лёгкая", "used": False, "guessed_count": 0},
{"word": "ГИТАРА", "category": "Музыка", 
 "hint": "Струнный инструмент",
"difficulty": "лёгкая", "used": False, "guessed_count": 0},
{"word": "АЛГОРИТМ", "category": "IT", "hint":
"Последовательность действий",
"difficulty": "сложная", "used": False, "guessed_count": 0},
]

result = collection.insert_many(words)