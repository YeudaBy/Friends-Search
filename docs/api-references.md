# Api references
___
<div>
<details>
<summary>Browse content</summary>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#api-references">Api-references</a></li>
<li><a href="#examples">Examples</a></li>
<li><a href="#contribute">Contribute</a></li>
</ul>
</details>
</div>

___
## introduction
Our service is simple and easy to use.

We don't have any authentication (mostly), and we have only a few entities.

Just follow the [example](#examples) section below, and see how easy it.

# Api-references

## Sentence
__any sentence from the series. are present as "Sentence" entity.__

Each one have the following attributes (the attribute type are present as [python type](https://docs.python.org/3/library/stdtypes.html)):

- `content`, [str]: the text that are spoken in the time.
- `id`, [int]: a unique id, mostly by chronology order.
- `position`, [dict]: an object that include the following data about the position of the sentence in the series:
    + `season`, [int]: tne number of the season, that the sentence appears.
    + `episode`, [int]: the number of the episode from the `season`.
    + `start`, [datetime]: time the sentence are start to be spoken.
    + `end`, [datetime]: the end-time of the sentence. 
- `language`, [dict]: an object that include the following data about the sentence language: 
    + `language_code`, [str]: one of the [Supported languages](#language), based on [the languages-code's list](https://www.science.co.il/language/Codes.php). e.g.: `en`, `he`, etc.
    + `language_name`: the most known name of the language, such as `English`, `Hebrew`, etc. 
- `details`, [dict]: an object that include the following data about the 'community' details of the sentence:
    + `likes`, [int]: count of times people react the sentence, by the api, bot or the site.
    + `verified`, [bool]: true, if the content of the sentence was verified by us. see more at [report-problems](Report problems).
    + [ ] `views`, [int]: count of times people saw this sentence. #TODO

All this information is return by sample request:
```shell
$ wget -O data.json https://api.friends-search.com/sentence/<id>
```
this command will create a file name `data.json` with all the information presented above. for example:

for more examples of usage, see the [Examples](#examples) section below.

### Methods
The `Sentence` object are support the following methods:

- `search`: of course, see [Search sentences](#search).
- `like`: mark the sentence as "liked". it does not require any login or other oath methode.
- [ ] `view`: mark the sentence as "views".
- `report`: report a sentence content. 
- [ ] `edit`: edit and correct the sentence content. this method require an admin permissions. 
- [ ] `verify`: verify the sentence content. this method also require an admin permissions.
> Read more about the three last methods at [Report problems](report-problems) section below.

## Language
__You can get a list of all the supported languages.__
All these languages are fully supported, in the Database, the Website and the Telegram bot.

Get the list, simply by request to:
```shell
$ wget https://api.friends-search.com/language
```
The response will look like:
```json
{
  "ok": true, 
  "results": {
    "ag": "All languages", 
    "en": "English", 
    "fr": "Français", 
    "he": "עברית"
  }
}
```

if you want to check if any language is supported, you can GET the query in the url, such as:
```shell
$ wget https://api.friends-search.com/language/en
```
The request above will return the following response:
```json
{
  "ok": true
}
```
When a language is not supported yet, you will get #TODO

> NOTE: the `ag` language are present `All languages` and intended for internal use.

## Search
Of course, you can search sentence... that why we came here.
