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