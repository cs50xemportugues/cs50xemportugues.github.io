Lab 8: Trivia
=============

<div class="alert" data-alert="warning" role="alert"><p>Vous pouvez collaborer avec un ou deux camarades sur ce lab, mais il est attendu que chaque élève de ce groupe contribue également au travail.</p></div>


Écrivez une page Web qui permet aux utilisateurs de répondre à des questions de trivia.

![capture d'écran des questions de trivia](https://cs50.harvard.edu/x/2023/labs/8/questions.png)

Pour commencer
---------------

<div class="alert" data-alert="primary" role="alert"><p>Vous avez commencé CS50x en 2021 ou avant et vous devez migrer votre travail de CS50 IDE vers le nouveau codespace de VS Code? N'oubliez pas de consulter nos instructions sur la façon de <a href="../../new/">migrer</a> vos fichiers !</p></div>

Ouvrez [VS Code] (https://code.cs50.io/).

Commencez par cliquer à l'intérieur de votre fenêtre de terminal, puis exécutez `cd` tout seul. Vous devriez constater que son "invite" ressemble à celle ci-dessous.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2022/fall/labs/8/trivia.zip
    

suivi de Enter pour télécharger un fichier ZIP appelé `trivia.zip` dans votre codespace. Veillez à ne pas manquer l'espace entre `wget` et l'URL suivante, ou tout autre caractère pour cette question!

Maintenant, exécutez

    unzip trivia.zip
    

pour créer un dossier appelé "trivia". Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm trivia.zip
    

et répondez par "y" suivi de Enter à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd trivia
    

suivi de Enter pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle ci-dessous.

    trivia/ $
    

Si tout s'est bien passé, vous devriez exécuter

    ls
    

et vous devriez voir un fichier `index.html` et un fichier `styles.css`.

Si vous rencontrez des problèmes, suivez ces mêmes étapes à nouveau et voyez si vous pouvez déterminer où vous avez mal tourné!

Détails de mise en œuvre
----------------------

Concevez une page Web en utilisant HTML, CSS et JavaScript pour permettre aux utilisateurs de répondre à des questions de trivia.

* Dans `index.html`, ajoutez sous « Partie 1 » une question de trivia à choix multiples de votre choix avec HTML.
    * Vous devriez utiliser un titre `h3` pour le texte de votre question.
    * Vous devriez avoir un `bouton` pour chacun des choix de réponse possibles. Il devrait y avoir au moins trois choix de réponse, dont exactement un devrait être correct.
* À l'aide de JavaScript, ajoutez une logique pour que les boutons changent de couleur lorsqu'un utilisateur clique dessus.
    * Si un utilisateur clique sur un bouton avec une réponse incorrecte, le bouton doit devenir rouge et du texte doit apparaître sous la question qui dit "Incorrect".
    * Si un utilisateur clique sur un bouton avec la bonne réponse, le bouton doit devenir vert et du texte doit apparaître sous la question qui dit "Correct !".
* Dans `index.html`, ajoutez sous « Partie 2 » une question gratuite de réponse de votre choix avec HTML.
    * Vous devriez utiliser un titre `h3` pour le texte de votre question.
    * Vous devriez utiliser un champ `input` pour permettre à l'utilisateur de saisir une réponse.
    * Vous devriez utiliser un `bouton` pour permettre à l'utilisateur de confirmer sa réponse.
* À l'aide de JavaScript, ajoutez une logique pour que le champ de texte change de couleur lorsqu'un utilisateur confirme sa réponse.
    * Si l'utilisateur tape une réponse incorrecte et appuie sur le bouton de confirmation, le champ de texte doit devenir rouge et du texte doit apparaître sous la question qui dit "Incorrect".
    * Si l'utilisateur tape la bonne réponse et appuie sur le bouton de confirmation, le champ de saisie doit devenir vert et du texte doit apparaître sous la question qui dit "Correct!".

Facultativement, vous pouvez également :

* Éditez `styles.css` pour modifier le CSS de votre page Web !
* Ajouter d'autres questions de trivia à votre quiz de trivia si vous le souhaitez !

### Procédure
<div class="alert" data-alert="primary" rôle="alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse être différente de celle de votre codespace, le comportement des deux environnements devrait être largement similaire !</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/WGd0Jx7rxUo"></iframe>


### Conseils

* Utilisez [`document.querySelector`] (https://developer.mozilla.org/fr/docs/Web/API/Document/querySelector) pour interroger un élément HTML unique.
* Utilisez [`document.querySelectorAll`] (https://developer.mozilla.org/fr/docs/Web/API/Document/querySelectorAll) pour interroger plusieurs éléments HTML qui correspondent à une requête. La fonction renvoie un tableau de tous les éléments correspondants.

<details><summary>Pas sûr de savoir comment résoudre ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/FLlI7rSSV_M"></iframe></details>


### Test

Il n'y a pas de `check50` pour ce lab, car les implémentations varieront en fonction de vos questions! Mais assurez-vous de tester les réponses incorrectes et correctes pour chacune de vos questions afin de vous assurer que votre page Web répond de manière appropriée.

Exécutez `http-server` dans votre terminal tout en étant dans votre répertoire `lab8` pour démarrer un serveur Web qui sert votre page Web.

Comment soumettre
-------------

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

    submit50 cs50/labs/2023/x/trivia