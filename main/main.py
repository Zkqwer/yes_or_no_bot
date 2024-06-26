import aiohttp

url = 'https://yesno.wtf/api'


async def yes_or_no():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as request:
            response = await request.json()
            if response.get('answer') == 'yes':
                answer = 'Да'
            elif response.get('answer') == 'no':
                answer = 'Нет'
            elif response.get('answer') == 'maybe':
                answer = 'Возможно'
            else:
                answer = 'пиздец'
            gif = response.get('image')
            return gif, answer
