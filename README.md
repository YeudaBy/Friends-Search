# Friends Search 🔎

### You can search and find sentence from the popular TV show - Friends.

> You can check our Website [here](https://t.me/userbot) and our Telegram bot [here](https://t.me/userbot).

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

## TODO's
- [x] Search words or sentences.
- [ ] Get random sentence.

---
Created with ❤️ by [David Lev](https://davidlev.me) & [Yehuda By](https://t.me/M100achuzBots)
