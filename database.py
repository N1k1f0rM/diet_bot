import sqlite3 as sq

db = sq.connect("bot.db")
cr = db.cursor()

async def db_start():
    cr.execute("CREATE TABLE IF NOT EXISTS accounts("
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "name TEXT, "
               "age INTEGER, "
               "weight INTEGER, "
               "height INTEGER, "
               "activity INTEGER, "
               "city TEXT, "
               "aim INTEGER, "
               "weather FLOAT, "
               "norm_water INTEGER, "
               "norm_calories INTEGER)")
    db.commit()


async def add_user():
    cr.execute("INSERT INTO accounts "
               "(name, age, weight, height, activity, city, aim, weather, norm_water, norm_calories)"
               "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (name, age, weight, height, activity, city, aim, weather, norm_water, norm_calories))
    db.commit()