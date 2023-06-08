# Lab 9 : Anniversaires

<div class="alert" data-alert="warning" role="alert"><p>Vous pouvez collaborer avec un ou deux camarades de classe sur ce laboratoire, mais il est attendu que chaque élève de ce groupe contribue de manière équitable au laboratoire.</p></div>

Créez une application web pour suivre les anniversaires de vos amis.

![screenshot du site web des anniversaires](https://cs50.harvard.edu/x/2023/labs/9/birthdays.png)

## Pour commencer

<div class="alert" data-alert="primary" role="alert"><p>Vous avez commencé CS50x en 2021 ou avant et vous avez besoin de migrer votre travail depuis l'IDE CS50 vers le nouveau codespace VS Code ? N'oubliez pas de consulter nos instructions sur la façon de <a href="../../new/">migrer</a> vos fichiers !</p></div>

Ouvrez [VS Code] (https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` seul. Vous devriez constater que son "invite" ressemble à ce qui suit.

     $

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/labs/9/birthdays.zip

suivi de Enter pour télécharger un fichier ZIP appelé `birthdays.zip` dans votre espace de code. Veillez à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère, le cas échéant!

Maintenant, exécutez

    unzip birthdays.zip

pour créer un dossier appelé «birthdays». Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm birthdays.zip

et répondez par "y" suivi de Enter à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

     cd birthdays

suivi de Enter pour vous déplacer dans ce répertoire (c'est-à-dire l'ouvrir). Votre invite devrait ressembler à ceci.

     birthdays/ $

Si tout s'est bien passé, vous devriez exécuter

     ls

et vous devriez voir les fichiers et dossiers suivants :

     app.py  birthdays.db  static/  templates/

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Compréhension

Dans `app.py`, vous trouverez le début d'une application Web Flask. L'application a une route (`/`) qui accepte à la fois les demandes `POST` (après le `if`) et les demandes `GET` (après le `else`). Actuellement, lorsque la route `/` est demandée via `GET`, le modèle `index.html` est rendu. Lorsque la route `/` est demandée via `POST`, l'utilisateur est redirigé vers `/` via` GET`.

`birthdays.db` est une base de données SQLite avec une table, `birthdays`, qui a quatre colonnes: `id`, `nom`, `mois` et `jour`. Il y a déjà quelques lignes dans cette table, bien que votre application Web finira par prendre en charge la possibilité d'insérer des lignes dans cette table !

Dans le répertoire `static`, se trouve un fichier `styles.css` contenant le code CSS pour cette application Web. Pas besoin de modifier ce fichier, même si vous pouvez le faire si vous le souhaitez !

Dans le répertoire `templates`, se trouve un fichier `index.html` qui sera rendu lorsque l'utilisateur affichera votre application Web.

## Détails d'implémentation

Complétez l'implémentation d'une application Web permettant aux utilisateurs de stocker et de suivre les anniversaires.

- Lorsque la route `/` est demandée via `GET`, votre application Web doit afficher, dans un tableau, toutes les personnes de votre base de données avec leurs anniversaires.
  - Tout d'abord, dans `app.py`, ajoutez une logique à votre traitement de demande `GET` pour interroger la base de données `birthdays.db` pour tous les anniversaires. Transmettez toutes ces données au modèle `index.html`.
  - Ensuite, dans `index.html`, ajoutez de la logique pour afficher chaque anniversaire en tant que ligne dans le tableau. Chaque ligne doit avoir deux colonnes : une colonne pour le nom de la personne et une autre colonne pour la date de naissance de la personne.
- Lorsque la route `/` est demandée via `POST`, votre application Web doit ajouter un nouvel anniversaire à votre base de données, puis réafficher la page d'index.
  - Tout d'abord, dans `index.html`, ajoutez un formulaire HTML. Le formulaire doit permettre aux utilisateurs de saisir un nom, un mois d'anniversaire et un jour d'anniversaire. Assurez-vous que le formulaire est soumis à `/` (son "action") avec une méthode de `post`.
  - Ensuite, dans `app.py`, ajoutez de la logique à votre demande `POST` pour `INSERT` une nouvelle ligne dans la table `birthdays` en fonction des données fournies par l'utilisateur.

En option, vous pouvez également :

- Ajoutez la possibilité de supprimer et/ou modifier les entrées d'anniversaire.
- Ajoutez toutes les fonctionnalités supplémentaires de votre choix!

### Guide pratique

<div class = "alert" data-alert = "primary" role = "alert"> <p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse paraître différente de votre code espace, le comportement des deux environnements devrait être largement similaire!</p> </div>

<iframe allow = "accéléromètre; lecture automatique; encrypted-media; gyroscope; picture-in-picture" allowfullscreen = "" class = "border" data-video = "" src = "https://video.cs50.io/HXwvj8x1Fcs"> </ iframe>


### Astuces

- N'oubliez pas que vous pouvez appeler `db.execute` pour exécuter des requêtes SQL dans `app.py`.
  - Si vous appelez `db.execute` pour exécuter une requête `SELECT`, rappelez-vous que la fonction vous renverra une liste de dictionnaires, où chaque dictionnaire représente une ligne renvoyée par votre requête.
- Vous trouverez probablement utile de passer des données supplémentaires à `render_template ()` dans votre fonction `index` afin d'accéder aux données d'anniversaire dans votre modèle `index.html`.
- Rappelez-vous que la balise `tr` peut être utilisée pour créer une ligne de table et la balise `td` peut être utilisée pour créer une cellule de données de table.
- Rappelez-vous qu'avec Jinja, vous pouvez créer une [`boucle for`] (https://jinja.palletsprojects.com/fr/2.11. x / templates / # for) à l'intérieur de votre fichier `index.html`.
- Dans `app.py`, vous pouvez obtenir les données `POST`ées par la soumission de formulaire de l'utilisateur via `request.form.get(field)` où `field` est une chaîne représentant l'attribut `name` d'une entrée de votre formulaire.
  - Par exemple, si dans `index.html`, vous aviez une `<input name="foo" type="text">`, vous pourriez utiliser `request.form.get("foo")` dans `app.py` pour extraire la saisie de l'utilisateur.

<details> <summary> Pas sûr de savoir comment résoudre? </summary> <iframe allow =" accéléromètre; lecture automatique; encrypted-media; gyroscope; picture-in-picture "allowfullscreen =" " class =" border "data-video =" "src =" https://video.cs50.io/lVwv4o8vmvI "> </ iframe> </details>


### Test

Aucun `check50` pour ce laboratoire! Mais assurez-vous de tester votre application Web en ajoutant quelques anniversaires et en vous assurant que les données apparaissent dans votre tableau comme prévu.

Exécutez `flask run` dans votre terminal tout en étant dans votre répertoire `birthdays` pour démarrer un serveur Web qui sert votre application Flask.

## Comment soumettre

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/labs/2023/x/birthdays