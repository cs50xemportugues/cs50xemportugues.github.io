Page d'accueil
==============

Créez une page d'accueil simple en utilisant HTML, CSS et JavaScript.

Contexte
--------

Internet a rendu possible des choses incroyables : nous pouvons utiliser un moteur de recherche pour explorer tout ce qui est imaginable, communiquer avec des amis et des membres de la famille partout dans le monde, jouer, suivre des cours, et bien plus encore. Mais il s'avère que presque toutes les pages que nous visitons sont construites en utilisant trois langages de base, chacun répondant à un objectif légèrement différent :

1. HTML, ou _HyperText Markup Language_, qui est utilisé pour décrire le contenu des sites web;
2. CSS, ou _Cascading Style Sheets_, qui est utilisé pour décrire l'esthétique des sites web; et
3. JavaScript, qui est utilisé pour rendre les sites web interactifs et dynamiques.

Créez une page d'accueil simple qui vous présente, présente votre passe-temps préféré ou vos activités extrascolaires, ou tout ce qui vous intéresse.

Mise en route
-------------

Connectez-vous sur [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal, et exécutez `cd` seul. Vous devriez voir que l'invite de votre fenêtre de terminal ressemble à celle ci-dessous :

    $
    

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/8/homepage.zip
    

afin de télécharger un fichier ZIP appelé `homepage.zip` dans votre espace de code.

Ensuite, exécutez

    unzip homepage.zip
    

pour créer un dossier appelé `homepage`. Vous n'avez plus besoin du fichier ZIP, donc vous pouvez exécuter

    rm homepage.zip
    

et répondre par "y", suivi d'Entrée, à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd homepage
    

suivi d'Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    homepage/ $
    

Exécutez `ls` seul, et vous devriez voir quelques fichiers :

    index.html  styles.css
    

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur ! Vous pouvez immédiatement démarrer un serveur pour voir votre site en exécutant

    http-server
    

dans la fenêtre de terminal. Ensuite, faites un clic-clic (si vous êtes sur Mac) ou un clic droit (si vous êtes sur PC) sur le premier lien qui apparaît :

    http-server running on LINK
    

Où LINK est l'adresse de votre serveur.