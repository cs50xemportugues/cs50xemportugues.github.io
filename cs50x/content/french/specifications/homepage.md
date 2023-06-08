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

Spécifications
-------------

Mettez en œuvre dans votre répertoire `homepage` un site Web qui doit :

*   Contenir au moins quatre pages HTML différentes, dont au moins une est `index.html` (la page principale de votre site), et il doit être possible de passer d'une page à l'autre en suivant un ou plusieurs hyperliens.
*   Utiliser au moins dix (10) balises HTML distinctes en plus de `<html>`, `<head>`, `<body>` et `<title>`. Utiliser une balise plusieurs fois (par exemple `<p>`) compte toujours comme une seule (1) des dix !
*   Intégrer une ou plusieurs fonctionnalités de Bootstrap dans votre site. Bootstrap est une bibliothèque populaire (qui inclut de nombreuses classes CSS et autres) avec laquelle vous pouvez embellir votre site. Consultez [la documentation de Bootstrap](https://getbootstrap.com/docs/5.2/) pour commencer. En particulier, certains des [composants de Bootstrap](https://getbootstrap.com/docs/5.2/components/) peuvent vous intéresser. Pour ajouter Bootstrap à votre site, il suffit d'inclure <div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"</span> <span class="na">integrity=</span><span class="s">"sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;</span>
<span class="nt">&lt;script </span><span class="na">src=</span><span class="s">"https://code.jquery.com/jquery-3.5.1.slim.min.js"</span> <span class="na">integrity=</span><span class="s">"sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;&lt;/script&gt;</span>
<span class="nt">&lt;script </span><span class="na">src=</span><span class="s">"https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"</span> <span class="na">integrity=</span><span class="s">"sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"</span> <span class="na">crossorigin=</span><span class="s">"anonymous"</span><span class="nt">&gt;&lt;/script&gt;</span>
</code></pre></div></div> dans la balise `<head>` de vos pages, en dessous duquel vous pouvez également inclure <div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;link</span> <span class="na">href=</span><span class="s">"styles.css"</span> <span class="na">rel=</span><span class="s">"stylesheet"</span><span class="nt">&gt;</span>
</code></pre></div>    </div>

    pour lier votre propre CSS.
    
*   Avoir au moins un fichier de style personnalisé, `styles.css`, qui utilise au moins cinq (5) sélecteurs CSS différents (par exemple, de balise (`example`), de classe (`.exemple`) ou d'ID (`#exemple`)), et dans lequel vous utilisez un total d'au moins cinq (5) propriétés CSS différentes, telles que `font-size` ou `margin`. 
*   Intégrez une ou plusieurs fonctionnalités JavaScript dans votre site pour le rendre plus interactif. Par exemple, vous pouvez utiliser JavaScript pour ajouter des alertes, pour avoir un effet à intervalles réguliers, ou pour ajouter de l'interactivité à des boutons, des menus déroulants ou des formulaires. N'hésitez pas à être créatif !
*   Assurez-vous que votre site a un design agréable sur les navigateurs des appareils mobiles ainsi que sur les ordinateurs portables et de bureau.

Test
----

Si vous voulez voir à quoi ressemble votre site pendant que vous travaillez dessus, vous pouvez exécuter `http-server`. Cliquez sur le premier lien présenté par http-server en utilisant la commande ou en appuyant sur `control+click`.  Cela devrait ouvrir votre page web dans un nouvel onglet. Vous devriez ensuite pouvoir rafraîchir l'onglet contenant votre page web pour voir vos derniers changements.

Rappelez-vous également qu'en ouvrant les Outils de développement dans Google Chrome, vous pouvez _simuler_ la visite de votre page sur un appareil mobile en cliquant sur l'icône en forme de téléphone à gauche de **Elements** dans la fenêtre des outils de développement, ou, une fois que l'onglet Outils de développement a déjà été ouvert, en tapant `Ctrl` +`Shift`+`M` sur un PC ou `Cmd`+`Shift` +`M`sur un Mac, sans avoir besoin de visiter votre site sur un appareil mobile séparément !

Évaluation
----------

Pas de `check50` pour cette mission ! Au lieu de cela, la précision de votre site sera évaluée en fonction de la manière dont vous répondez aux exigences de la spécification telles qu'elles sont décrites ci-dessus et si votre HTML est bien formé et valide. Pour vous assurer que vos pages le sont, vous pouvez utiliser ce [Markup Validation Service](https://validator.w3.org/#validate_by_input), en copiant-collant directement votre HTML dans la zone de texte fournie. Veillez à éliminer toutes les alertes ou erreurs suggérées par le valideur avant de soumettre !

Considérez également :

*   si l'esthétique de votre site est telle qu'il est intuitif et facile pour un utilisateur de naviguer ;
*   si votre CSS a été séparé en fichier(s) CSS distinct(s) ;
*   si vous avez évité la répétition et la redondance en "cascade" des propriétés de style à partir des balises parentes.

Malheureusement, `style50` ne prend pas en charge les fichiers HTML. Il vous incombe donc de bien indenter et aligner vos balises HTML. Sachez également que vous pouvez créer un commentaire HTML avec :

    <!-- Le commentaire est ici -->

Mais commenter votre code HTML n'est pas aussi impératif que le commentaire du code dans, disons, C ou Python. Vous pouvez également commenter votre CSS dans des fichiers CSS, avec :

    /* Le commentaire est ici */

Indices
------

Pour des guides assez complets sur les langages présentés dans ce problème, consultez ces tutoriels :

*  [HTML](https://www.w3schools.com/html/)
*  [CSS](https://www.w3schools.com/css/)
*  [JavaScript](https://www.w3schools.com/js/)

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande suivante pour soumettre votre travail.

    submit50 cs50/problems/2023/x/homepage"

