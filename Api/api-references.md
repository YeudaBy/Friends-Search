# Friends-Search Api

### With this api you can search for sentences that says in friends series.


## Entities
### sentence
> ``https://api.friends-search.com/sentence/{}``
#### get sentence by id
You can simply find sentence by specific `sentence id`, like in the example below: 
<details>
<summary>
Example for: <code> get sentence by id </code>
</summary>
<div>

- http end-point:

``https://api.friends-search.com/sentence/24``
- results:
```json
{
  "content": "She's living my life, and she's doing it better than me.", 
  "end": "0:02:10.838000", 
  "episode": "21", 
  "id": 24, 
  "lang_code": "en", 
  "lang_name": "English", 
  "season": "1", 
  "start": "0:02:07.168000"
}
```
</div>
</details>

As you can see, each one include the following attributes:
- `content`: the original sentence, as it used on the series.
>NOTE: the source of the content is based on the [resource](#credits) we used. you can find some mistakes, or non-original content, as much it contains. we would love#TODOto get
- `lang_code`: the language code of the content. e.g. `en`, `fr`, `he`.
- `lang_name`: the language name as called, e.g. `English`, `Français`, `עברית`.
- `id`: a unique id of the result itself. by this is you can get the next or previous sentence.
- `season`: the number of the season in the series.
- `episode`: the number of the episode in each series.
- `start`: time of the start of the content, as `timedelta`. 
- `end`: time of the end of the sentence.
> You can simply find the actual time by getting the 
#### random
Also, a nice way to exposer sentences is to get them randomly. 

Each result will include _10_ sentences, with no filters like [language](#language).

<details>
<summary>
Example for: <code>random</code>
</summary>
<div>

- http end-point:

``https://api.friends-search.com/sentence/random``
- results:
```json
[
  {
    "content": "- She's with me. Dr. Drake Ramoray. - Dr. Drake who?", 
    "end": "0:14:37.906000", 
    "episode": "23", 
    "id": 64291, 
    "lang_code": "en", 
    "lang_name": "English", 
    "season": "8", 
    "start": "0:14:32.234000"
  }, 
  {
    "content": "That's right. I love you.", 
    "end": "0:01:50.526000", 
    "episode": "10", 
    "id": 65351, 
    "lang_code": "en", 
    "lang_name": "English", 
    "season": "8", 
    "start": "0:01:47.565000"
  }, 
  {
    "content": "Look, Monica's been working hard all day.", 
    "end": "0:06:24.466000", 
    "episode": "8", 
    "id": 80664, 
    "lang_code": "en", 
    "lang_name": "English", 
    "season": "10", 
    "start": "0:06:22.298000"
  }, 
  {
    "content": ",אולי זה בסדר מבחינתך", 
    "end": "0:19:06.261000", 
    "episode": "21", 
    "id": 104341, 
    "lang_code": "he", 
    "lang_name": "עברית", 
    "season": "3", 
    "start": "0:19:04.676000"
  }, 
  {
    "content": ".הם מרגישים לא רצויים", 
    "end": "0:11:23.194000", 
    "episode": "20", 
    "id": 133812, 
    "lang_code": "he", 
    "lang_name": "עברית", 
    "season": "7", 
    "start": "0:11:21.525000"
  }, 
  {
    "content": "Très bien. Je prendrai rendez-vous.", 
    "end": "0:16:00.287000", 
    "episode": "22", 
    "id": 176863, 
    "lang_code": "fr", 
    "lang_name": "Français", 
    "season": "2", 
    "start": "0:15:58.092000"
  }, 
  {
    "content": "Merci ! Je vous adore !", 
    "end": "0:19:27.723000", 
    "episode": "10", 
    "id": 183665, 
    "lang_code": "fr", 
    "lang_name": "Français", 
    "season": "3", 
    "start": "0:19:25.892000"
  }, 
  {
    "content": "Tu le sais si vite ?", 
    "end": "0:15:59.523000", 
    "episode": "12", 
    "id": 189361, 
    "lang_code": "fr", 
    "lang_name": "Français", 
    "season": "4", 
    "start": "0:15:57.692000"
  }, 
  {
    "content": "Ça tuerait pas plus d'animaux, tu mangerais les miens !", 
    "end": "0:12:40.682000", 
    "episode": "16", 
    "id": 192718, 
    "lang_code": "fr", 
    "lang_name": "Français", 
    "season": "4", 
    "start": "0:12:37.372000"
  }, 
  {
    "content": "Ça explique beaucoup de choses !", 
    "end": "0:00:53.048000", 
    "episode": "11", 
    "id": 220018, 
    "lang_code": "fr", 
    "lang_name": "Français", 
    "season": "8", 
    "start": "0:00:50.773000"
  }
]
```

</div>
</details>