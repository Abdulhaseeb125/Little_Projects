import random
import requests
import html
from twilio.rest import Client

with open("words.txt") as file:
    words = file.read().split()
    word = random.choice(words)

# MY Memory headers
memory_header = {
    "X-RapidAPI-Key": "2272278372msh49118a7bebf2f86p1dca40jsn79c66904a336",
    "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
}
memory_url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"
querystring = {"langpair": "en|ur", "q": word, "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

# Oxford Headers
headers = {
    'app_id': 'f67a12cf',
    'app_key': '93b8f18febeec78094559a0c3e12f39a'
}
language = 'en-gb'
url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word.lower()

# memory
try:
    response = requests.request("GET", memory_url, headers=memory_header, params=querystring)
    memory_content = response.json()
    # oxford
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()

    # -------------memory----------
    translation_list = [html.unescape(key['translation']) for key in memory_content['matches']]

    quality_list = [html.unescape(key['quality']) for key in memory_content['matches']]

    segment_list = [html.unescape(key['segment']) for key in memory_content['matches']]

    # ---------------oxford----------
    definition_list = [item for item in
                       content['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']]
    ex_list = [item for item in content['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples']]
    example_list = [f"{item['text']}," for item in ex_list]

    # usable data
    data = {
        'Word': content['word'],
        'Definition': definition_list,
        'Examples': example_list,
        'translation': memory_content['responseData']['translatedText'],
        'segment_list': segment_list,
        'translation_list': translation_list,
        'quality_list': quality_list
    }

    # twilio

    account_sid = "ACfd5bbcb573babf4806e355959e3d856a"
    auth_token = "ace520253270b002e23d341c3a499398"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=data.__str__(),
        from_='+16088892416',
        to='+923056007293'
    )
    print(message.status)


except:
    print("Error")
