import os
import asyncio

from dotenv import load_dotenv, find_dotenv
import aiohttp

load_dotenv(find_dotenv())
API_KEY_MAIL = os.getenv('API_MAIL_KEY')
TEST_USERNAME_MAIL = os.getenv('TEST_USERNAME_MAIL')
TEST_PASSWORD_MAIL = os.getenv('TEST_PASSWORD_MAIL')

async def main():
    guard_code = await get_auth_code_steam(TEST_USERNAME_MAIL, TEST_PASSWORD_MAIL)
    print(guard_code)

async def get_auth_code_steam(login_mail: str, password_mail: str):
    url = ("https://api.firstmail.ltd/v1/market/get/message?"
           f"username={login_mail}&password={password_mail}")
    headers = {
        "accept": "application/json",
        "X-API-KEY": API_KEY_MAIL
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, headers=headers)
    response_json = await response.json()
    print(response_json)
    if not response_json['has_message']:
        return False
    find_text = ('color:#3a9aed; font-weight:bold; text-align:center;">'
                 '\/n\/t\/t\/t\/t\/t\/t\/t\/t\/t\/t\/t\/t')
    print(find_text)
    guard_in_text = str(response_json['message'])
    index_in_text = guard_in_text.find(find_text)
    print(index_in_text)
    guard_code = guard_in_text[index_in_text+20:index_in_text+25]
    return guard_code

if __name__ == '__main__':
    asyncio.run(main())