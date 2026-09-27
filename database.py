import aiosqlite

class Database:
    def __init__(self, db_name="database.db") -> None:
        self.db_name = db_name

    async def init(self):
        async with aiosqlite.connect(self.db_name) as conn:
            await conn.execute("""CREATE TABLE IF NOT EXISTS checker_database (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status_code TEXT NOT NULL,
                url TEXT NOT NULL
            )""")
            await conn.commit()
            
    async def save(self, status_code, url):
        async with aiosqlite.connect(self.db_name) as conn:
            await conn.execute(
                "INSERT INTO checker_database (status_code, url) VALUES (?, ?)", 
                (status_code, url)
            )
            await conn.commit()

    async def fetch(self):
        async with aiosqlite.connect(self.db_name) as conn:
            return await conn.execute_fetchall("SELECT * FROM checker_database")
