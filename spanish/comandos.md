---
description: Aquí está la lista de comandos soportados por RoboTito.
---

# Comandos

## Aclaraciones 📌 

{% hint style="success" %}
La gran mayoría de los comandos tienen "aliases", es decir, diferentes formas de llamarlos. Utiliza `r.help <comando>` para obtener información específica.
{% endhint %}

{% hint style="danger" %}
Para realizar ciertas cosas, como cambiarle el apodo a alguien o expulsar a un usuario de un servidor, necesitarás **permisos globales** dentro del servidor.
{% endhint %}

### Interacción 🗣 

| Comando | Descripción | Sintaxis |
| :---: | :--- | :--- |
| hug | Abraza a un usuario. | `r.hug <usuario>` |
| kiss | Besa a un usuario. | `r.kiss <usuario>` |
| pat | Acaricia a un usuario. | `r.pat <usuario>` |
| punch | Golpea a un usuario. | `r.punch <usuario>` |
| sleep | Duerme con/sin un usuario. | `r.sleep <miembro> (opcional)` |
| kill | Mata a un usuario. | `r.kill <miembro>` |
| greet | Saluda a todo el mundo o a un usuario. | `r.greet <miembro> (opcional)` |

### Información 📑 

| Comando | Descripción | Sintaxis |
| :---: | :--- | :--- |
| botinfo | Información sobre el bot. | `r.botinfo` |
| svinfo | Información sobre el servidor actual. | `r.svinfo` |
| svicon | Ícono del servidor. | `r.svicon` |
| userinfo | Información sobre ti o alguien más. | `r.userinfo <miembro> (opcional)` |
| avatar | Tu ícono o el de alguien más. | `r.avatar <miembro> (opcional)` |

### League of Legends 👾

| Comando | Descripción | Sintaxis |
| :---: | :--- | :--- |
| chname | Busca un campeón por su nombre. | `r.chname <nombre>` |
| chrole | Busca un campeón aleatorio por su rol. | `r.chrole <rol>` |
| chrandom | Obtén un campeón aleatorio. | `r.chrandom` |

### Moderación 🔨 

| Comando | Descripción | Sintaxis |
| :---: | :--- | :--- |
| ban | Expulsa a un usuario y revoca su acceso. | `r.ban <miembro> <motivo>` |
| kick | Expulsa a un usuario pero permite su reingreso. | `r.kick <miembro> <motivo>` |
| unban | Permite el reingreso de un usuario vetado. | `r.unban <tag> (por ejemplo: RoboTito#1684)` |
| clean | Borra mensajes en el canal actual. | `r.clean <cantidad> (menor a 100)` |
| nick | Cambia tu apodo o el de alguien más. | `r.nick <apodo> <miembro> (opcional)` |

### Ruleta Rusa 🔫

| Comando | Descripción | Sintaxis |
| :--- | :--- | :--- |
| rr | Juega a la ruleta rusa con un amigo/a. | `r.rr <miembro>` |

{% hint style="info" %}
Para jugar, deberás escribir "intentar" o "probar" cada vez que el bot te lo indique. Hay un total de 6 balas.
{% endhint %}

### Tiempo ⌚

| Comando | Descripción | Sintaxis |
| :--- | :--- | :--- |
| utc | Conoce la hora del meridiano de Greenwich \(UTC\) | `r.utc` |
| bottime | Conoce la hora del lugar donde el bot se está ejecutando. | `r.bottime` |
| localtime | Conoce la hora de una zona horaria. | `r.localtime <horas>` |

{% hint style="info" %}
Para conocer la hora de una zona horaria, deberás ingresar las horas de diferencia con el horario de Greenwich, por ejemplo para Argentina: `r.localtime -3`
{% endhint %}

### Traducir 🔄

| Comando | Descripción | Sintaxis |
| :--- | :--- | :--- |
| translate | Traduce una oración entre dos idiomas. | `r.translate <origen> <destino> <frase>` |

{% hint style="info" %}
Actualmente, RoboTito hace uso de una librería que le permite aceptar más de 180 idiomas, pero quizá no todos sean compatibles con la traducción. Para ver los idiomas soportados haz clic [aquí](https://es.wikipedia.org/wiki/ISO_639-1) y para ver las formas de nombrar los idiomas puedes ir [aquí](https://github.com/Ti7oyan/RoboTito/blob/master/databases/db_languages.json).
{% endhint %}

### Wikipedia 📰

| Comando | Descripción | Sintaxis |
| :--- | :--- | :--- |
| summary | Obtén un resumen sobre un artículo de Wikipedia. | `r.summary <articulo>` |

### Varios 🗃 

| Comando | Descripción | Sintaxis |
| :--- | :--- | :--- |
| ping | Obtén la latencia del bot. | `r.ping` |
| 8ball | Pregúntale a la bola ocho. | `r.8ball <pregunta>` |
| prob | Descubre la probabilidad de que algo pase. | `r.prob <pregunta>` |
| penis | Descubre el tamaño de tu aparato o el de alguien más \(resultados incomprobables\) | `r.penis <miembro> (opcional)` |
| love | Conoce el estado de tu relación con cierto usuario. | `r.love <miembro>` |

