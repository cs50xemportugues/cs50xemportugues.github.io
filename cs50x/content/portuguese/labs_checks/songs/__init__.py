# Porting the Python code to Portuguese:

```python
from cs50 import SQL

import check50
import sqlparse


@check50.check()
def sql_existe():
    """Arquivos SQL existem"""
    for i in range(1, 8):
        check50.exists(f"{i}.sql")
    check50.include("songs.db")


@check50.check()
def respostas_existe():
    """answers.txt existe"""
    check50.exists("answers.txt")


@check50.check(sql_existe)
def teste1():
    """1.sql produz resultado correto"""
    solucao = {
        "God's Plan",
        "SAD!",
        "rockstar (feat. 21 Savage)",
        "Psycho (feat. Ty Dolla $ign)",
        "In My Feelings",
        "Better Now",
        "I Like It",
        "One Kiss (with Dua Lipa)",
        "IDGAF",
        "FRIENDS",
        "Havana",
        "Lucid Dreams",
        "Nice For What",
        "Girls Like You (feat. Cardi B)",
        "The Middle",
        "All The Stars (with SZA)",
        "no tears left to cry",
        "X",
        "Moonlight",
        "Look Alive (feat. Drake)",
        "These Days (feat. Jess Glynne, Macklemore & Dan Caplen)",
        "Te Bote - Remix",
        "Mine",
        "Youngblood",
        "New Rules",
        "Shape of You",
        "Love Lies (with Normani)",
        "Meant to Be (feat. Florida Georgia Line)",
        "Jocelyn Flores",
        "Perfect",
        "Taste (feat. Offset)",
        "Solo (feat. Demi Lovato)",
        "I Fall Apart",
        "Nevermind",
        "Echame La Culpa",
        "Eastside (with Halsey & Khalid)",
        "Never Be the Same",
        "Wolves",
        "changes",
        "In My Mind",
        "River (feat. Ed Sheeran)",
        "Dura",
        "SICKO MODE",
        "Thunder",
        "Me Niego",
        "Jackie Chan",
        "Finesse (Remix) [feat. Cardi B]",
        "Back To You - From 13 Reasons Why",
        "Let You Down",
        "Call Out My Name",
        "Ric Flair Drip (& Metro Boomin)",
        "Happier",
        "Too Good At Goodbyes",
        "Freaky Friday (feat. Chris Brown)",
        "Believer",
        "FEFE (feat. Nicki Minaj & Murda Beatz)",
        "Rise",
        "Body (feat. brando)",
        "XO TOUR Llif3",
        "Sin Pijama",
        "2002",
        "Nonstop",
        "Fuck Love (feat. Trippie Redd)",
        "In My Blood",
        "Silence",
        "God is a woman",
        "Dejala que vuelva (feat. Manuel Turizo)",
        "Flames",
        "What Lovers Do",
        "Taki Taki (with Selena Gomez, Ozuna & Cardi B)",
        "Let Me Go (with Alesso, Florida Georgia Line & watt)",
        "Feel It Still",
        "Pray For Me (with Kendrick Lamar)",
        "Walk It Talk It",
        "Him & I (with Halsey)",
        "Candy Paint",
        "Congratulations",
        "1, 2, 3 (feat. Jason Derulo & De La Ghetto)",
        "Criminal",
        "Plug Walk",
        "lovely (with Khalid)",
        "Stir Fry",
        "HUMBLE.",
        "Vaina Loca",
        "Perfect Duet (Ed Sheeran & Beyonc?)",
        "Corazon (feat. Nego do Borel)",
        "Young Dumb & Broke",
        "Siguelo Bailando",
        "Downtown",
        "Bella",
        "Promises (with Sam Smith)",
        "Yes Indeed",
        "I Like Me Better",
        "This Is Me",
        "Everybody Dies In Their Nightmares",
        "Rewrite The Stars",
        "I Miss You (feat. Julia Michaels)",
        "No Brainer",
        "Dusk Till Dawn - Radio Edit",
        "Be Alright",
    }
    verifica_coluna_unico(rodar_query("1.sql"), solucao, ordenado=False)


@check50