// Инициализация БД при первом запуске
db = db.getSiblingDB('hello_db');

db.greetings.insertOne({
  _id: 'counter',
  visits: 0,
  createdAt: new Date()
});

print('MongoDB инициализирована: hello_db.greetings');
