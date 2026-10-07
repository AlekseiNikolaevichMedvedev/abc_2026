import  random

from pymongo import MongoClient
MONGO_URI = "mongodb://admin:admin123@localhost:27017/"
DB_NAME = "pole_chudes_db"
def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db["words"]

class Game:
    def __init__(self):
        self._dict = {'False': 'Логическое значение', 'None': 'Пустой'}
        self.keys = list(self._dict.keys())
        self.ind = random.randint(0, len(self.keys) - 1)
        self.secret = self.keys[self.ind]
        self.mask = [' * '] * len(self.secret)
        db_words = self.dictionary  
        if db_words:
            self.dictionary = db_words
            print(f"Словарь из БД загружен (Слов: {len(db_words)})")
        else:
            print("Игра запущена с дефолтным словарем.")

    @property
    def dictionary(self):
        collection = get_collection()
        db_words = collection.find({}, {"_id": 0, "word": 1, "hint": 1, "category": 1})
        result = {}
        for doc in db_words:
            if "word" in doc:
                word = str(doc["word"])
                category = doc.get("category", "Общая")
                hint = doc.get("hint", "Описание отсутствует")
                result[word] = f"[{category}] {hint}"              
        return result
    
    @dictionary.setter
    def dictionary(self, new_dict):
        if isinstance(new_dict, dict) and len(new_dict) > 0:
            collection = get_collection()
            
            collection.delete_many({})
            mongo_docs = [{"word": str(k), "describe": str(v)} for k, v in new_dict.items()]
            collection.insert_many(mongo_docs)
            
            self._dict = new_dict
            self.keys = list(self._dict.keys())
            self.ind = random.randint(0, len(self.keys) - 1)
            self.secret = self.keys[self.ind]
            self.mask = [' * '] * len(self.secret)

    def show_describe(self):
        print(self._dict[self.secret])


    def show_secret(self):
        for val in self.mask:
           print(val, end="")


    def get_letter(self):
        letter = input("\n Введите букву:")
        return letter


    def check_letter(self, letter):
        for ind, val in enumerate(self.secret):
            if val.upper() == letter.upper():
                self.mask[ind] = f" {letter} "


    def start(self):
        while ( " * " in self.mask):
            self.show_describe()
            self.show_secret()
            letter = self.get_letter()
            self.check_letter(letter)

if __name__ == '__main__':
    game = Game()
    game.start()
