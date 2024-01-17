from fastapi import FastAPI
from telethon import TelegramClient

app = FastAPI()

@app.post("/")
async def your_route():
    return {"status": "ok"}

async def get_code():
    code = input('введите код:')
    return code

# https://my.telegram.org/
# get id and hash 
@app.get('/sign-in')
async def sign_in():
    phone_number = "+7999999999"
    session_name = "session_name"
    tg_id: int = 1
    tg_hash: str = "2"
    client = TelegramClient(session_name, tg_id, tg_hash)
    await client.start(phone=phone_number, code_callback=get_code)
    return {"data": "output"}

