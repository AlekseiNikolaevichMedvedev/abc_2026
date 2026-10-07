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

print(f"Inserted Ids:")
for item in result.inserted_ids:
    print(f"{item}")


word = collection.find_one({"category": "Музыка"})
print("Найдено:", word)

for w in collection.find({"difficulty": "лёгкая"}):
    print(w["word"], "-", w["hint"])


for w in collection.find({}, {"_id": 0, "word": 1, "category":
1}):
    print(w)

collection.update_one(
{"word": "ГИТАРА"},
{"$set": {"difficulty": "средняя"}}
)
# Инкремент счётчика
collection.update_one(
{"word": "КОСМОНАВТ"},
{"$inc": {"guessed_count": 1}}
)
# Массовое обновление
collection.update_many(
{"used": False},
{"$set": {"used": True}}
)
# ---------- DELETE ----------
# Удалить один документ
collection.delete_one({"word": "АЛГОРИТМ"})
# Удалить по условию
collection.delete_many({"difficulty": "сложная"})
