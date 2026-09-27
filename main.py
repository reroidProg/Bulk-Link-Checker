import asyncio
from checker import UrlChecker
from database import Database

async def main():
    db = Database()
    await db.init()

    # Замените на свой url list
    urls = [ 
        "https://www.google.com",
        "https://www.github.com",
        "https://httpbin.org/status/404",
        "https://invalid-domain-test-12345.com"
    ]

    checker = UrlChecker()

    print("=== Запуск проверки ссылок ===")
    for url in urls:
        result = await checker.checker(url)
        if result:
            status_code, checked_url = result
            print(f"Ссылка: {checked_url} | Статус: {status_code}")
            await db.save(status_code, checked_url)

    await checker.close()

    print("\n=== Данные из базы данных ===")
    rows = await db.fetch()
    for row in rows:
        print(row)

if __name__ == "__main__":
    asyncio.run(main())
