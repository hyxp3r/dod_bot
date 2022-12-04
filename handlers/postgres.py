from dotenv import load_dotenv
import os
import asyncpg


load_dotenv(r"C:\dod_Bot\dodBot\.env")
dbname = os.environ.get("dbname")
user = os.environ.get("user")
password = os.environ.get("pass")
host = os.environ.get("host")


async def write(data):

                         

    #conn = await asyncpg.connect(user = user, password = password, database = dbname, host = host)
    conn = await asyncpg.connect(f'postgresql://{user}:{password}@{host}/{dbname}')
    #print(conn)

    #cursor = conn.cursor()

    await conn.execute('''INSERT INTO members  (id, fio) VALUES ($1, $2);''', str(data["id"]), data["name"])
    await conn.close()


async def count():

    conn = await asyncpg.connect(f'postgresql://{user}:{password}@{host}/{dbname}')
    count = await conn.fetchval('select count(*) as "Количество" from members')
    
    return count



