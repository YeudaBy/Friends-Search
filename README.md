
<div align="center">
  
  <img src="/web/public/icon.ico" width="100px"></img>

  <h1>Friends Search 🔎</h1>
  
  <p><a href="#">API</a> • <a href="#">WebSite</a> • <a href="#">TelegramBot</a></p>

</div>

### You can search and find sentence from the popular TV show - Friends.

> You can check our Website [here](https://t.me/userbot) and our Telegram bot [here](https://t.me/userbot).

## Usage

#### API
_Full Documention can be found at [here.](https://example.com/api)_

The api include one and simple methode, call `search`. 

the methode taken only one argument: `query`, and return list of results mathes. 

you can provide more arguments, such as language and limit. the argument can be: 
- `query` or `q`: text, sentence or word to search.
- `language` or `lang`: one of the [Supported languages](Supported languages), like `he`/`en`.
- `limit` or `l`: limit of results to show. default to 50.

#### WebSite
Go to [our website](https://example.com) and search there for free.

#### Telegram Bot
We build a telegram bot for searching inline from our api. the bot runs at https://t.me/_bot.

## Examples
#### Api Example
```bash
$ curl "http://127.0.0.1:5000/api/search?query=unagi"
```
=
```python
import requests

url = "http://127.0.0.1:5000/api/search?query=unagi"
r = requests.get(url)
print(r.json())
```
the results will be looks like:

```json
{
  "count": 10,
  "results": [
    {
      "content": "It's what the Japanese call unagi.",
      "end": "0:03:16.236000",
      "episode": "17",
      "season": "6",
      "start": "0:03:11.858000"
    },
    {
      "content": "Unagi is a state of total awareness.",
      "end": "0:03:46.391000",
      "episode": "17",
      "season": "6",
      "start": "0:03:41.387000"
    },
    {
      "content": "Okay? Only by achieving true unagi...",
      "end": "0:03:49.186000",
      "episode": "17",
      "season": "6",
      "start": "0:03:46.559000"
    },
    {
      "content": "All right, you knew that was coming, but that doesn't mean you have unagi.",
      "end": "0:04:26.265000",
      "episode": "17",
      "season": "6",
      "start": "0:04:20.635000"
    },
    {
      "content": "Ooh, if we made reservations, we could have unagi in about a half-hour.",
      "end": "0:04:32.771000",
      "episode": "17",
      "season": "6",
      "start": "0:04:29.185000"
    },
    {
      "content": "A lesson in the importance of unagi.",
      "end": "0:08:10.697000",
      "episode": "17",
      "season": "6",
      "start": "0:08:06.611000"
    },
    {
      "content": "Ah, huh? Unagi.",
      "end": "0:08:48.985000",
      "episode": "17",
      "season": "6",
      "start": "0:08:45.274000"
    },
    {
      "content": "Unagi.",
      "end": "0:09:39.160000",
      "episode": "17",
      "season": "6",
      "start": "0:09:37.660000"
    },
    {
      "content": "Okay, are you aware that unagi is an eel?",
      "end": "0:09:44.833000",
      "episode": "17",
      "season": "6",
      "start": "0:09:41.872000"
    },
    {
      "content": "- Say it. - Say we are unagi.",
      "end": "0:16:05.046000",
      "episode": "17",
      "season": "6",
      "start": "0:16:02.628000"
    }
  ]
}
```

# WebSite
![image](https://user-images.githubusercontent.com/68661509/144731448-4a15ea1f-db3b-4929-a9cf-9c5e24e8bc6c.png)


## Languages and translation Contributions
If you want to add your language subtitles, you need to send us the files (or open PR) in the folowing format:
```
├──This repo / your zip file
  └── DB
    └── RawFiles
      └── LANG_CODE
        ├── s1 // seasions
        ├── s2
        ├── s3
        └── s4
          ├── 04-01 // episodes without .srt extention
          ├── 04-02
```
You can add your language to the Telegram bot by editing the [strings.py](/Bot/strings.py) file and adding a translation in the appropriate format:
```python
strings = {
    "example1": {
        "en": "This string represents message exmple1",
        "he": "המחרוזת הזו מייצגת הודעת דוגמה 1",
        "ru": "Эта строка представляет сообщение exmple1"
    },
     "example2": {
        "en": "This string represents message exmple2",
        "he": "המחרוזת הזו מייצגת הודעת דוגמה 2",
        "ru": "Эта строка представляет сообщение exmple2"
    }
}
```
- Add your language code as key, the lang-code should be in `IETF language tag` format.
- Try to stick to the format and translate from the English language available in the file.
- Maintain the position of the special characters (emojis, `.*,-/\{}`).
- When you done, open a __pull request__ or send us the file to [our](https://t.me/RobotTrickSupport) Telegram.

## Supported languages
- [x] English
- [x] Hebrew
- [x] French

## TODO's
- [x] Search words or sentences.
- [x] Get random sentence.

---
Created with ❤️ by [David Lev](https://davidlev.me) & [Yehuda By](https://t.me/M100achuzBots)
