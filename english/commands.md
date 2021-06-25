---
description: These are all of the commands that RoboTito supports.
---

# Commands

## Aclarations 📌 

{% hint style="success" %}
The vast majority of commands have "aliases", i.e. different ways of calling them. Use `r.help <command>`  for specific information.
{% endhint %}

{% hint style="danger" %}
To do certain things, such as changing someone's nickname or kicking a user off a server, you will **need global permissions** within the server.
{% endhint %}

### Interaction 🗣 

| Command | Description | Sintaxis |
| :---: | :--- | :--- |
| hug | Hugs an user. | `r.hug <user>` |
| kiss | Kiss an user. | `r.kiss <user>` |
| pat | Pats an user. | `r.pat <user>` |
| punch | Punchs an user. | `r.punch <user>` |
| sleep | Sleep with/without an user. | `r.sleep <user> (optional)` |
| kill | Kills an user. | `r.kill <user>` |
| greet | Greets everyone or a specific user. | `r.greet <user> (optional)` |

### Information 📑 

| Command | Description | Sintaxis |
| :---: | :--- | :--- |
| botinfo | Bot's information. | `r.botinfo` |
| svinfo | Actual server's information. | `r.svinfo` |
| svicon | Actual server's icon. | `r.svicon` |
| userinfo | Information about you or another user. | `r.userinfo <user> (optional)` |
| avatar | Your avatar or someone else's. | `r.avatar <user> (optional)` |

### League of Legends 👾

| Command | Description | Sintaxis |
| :---: | :--- | :--- |
| chname | Searchs a champion by its name. | `r.chname <name>` |
| chrole | Get a champion by role. | `r.chrole <role>` |
| chrandom | Get a random champion. | `r.chrandom` |

### Moderation🔨 

| Command | Description | Sintaxis |
| :---: | :--- | :--- |
| ban | Bans an user. | `r.ban <user> <reason>` |
| kick | Kicks an user. | `r.kick <user> <reason>` |
| unban | Unbans an user. | `r.unban <tag> (for example: RoboTito#1684)` |
| clean | Deletes messages in the actual channel. | `r.clean <quantity> (less than 100)` |
| nick | Changes your nick or someone else's. | `r.nick <nick> <user> (optional)` |

### Russian roulette 🔫

| Command | Description | Sintaxis |
| :--- | :--- | :--- |
| rr | Plays russian roulette with a friend. | `r.rr <user>` |

{% hint style="info" %}
To play you have to write "try" every time the bot tells you. There are six bullets in the gun.
{% endhint %}

### Time ⌚

| Command | Description | Sintaxis |
| :--- | :--- | :--- |
| utc | Get the UTC time. | `r.utc` |
| bottime | Get the time of the bot. | `r.bottime` |
| localtime | Get the time of a timezone. | `r.localtime <hours>` |

{% hint style="info" %}
To know the time of a timezone, you have to pass as an argument the hours of difference between the timezone and UTC, for example Argentinian time is: `r.localtime -3`
{% endhint %}

### Translate 🔄

| Command | Description | Sintaxis |
| :--- | :--- | :--- |
| translate | Translates a sentence between two languages. | `r.translate <from> <to> <sentence>` |

{% hint style="info" %}
RoboTito currently makes use of a library that allows it to support more than 180 languages, but not all of them may be supported for translation. To see the supported languages click [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and to see the ways of naming the languages you can go [here](https://github.com/Ti7oyan/RoboTito/blob/master/databases/db_languages.json).
{% endhint %}

### Wikipedia 📰

| Command | Description | Sintaxis |
| :--- | :--- | :--- |
| summary | Get a Wikipedia article's summary. | `r.summary <article>` |

### Extra 🗃 

| Command | Description | Sintaxis |
| :--- | :--- | :--- |
| ping | Get the bot's latency. | `r.ping` |
| 8ball | Ask to the eight ball. | `r.8ball <question>` |
| prob | Discover the probabilities of something to happen. | `r.prob <question>` |
| penis | Discover your penis size or someone else's \(not real results\) | `r.penis <user> (optional)` |
| love | Discover the status of your relationship with someone. | `r.love <user>` |

