## Guide


<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>


## Test

Veillez à tester votre application web manuellement en :

- enregistrant un nouvel utilisateur et en vérifiant que sa page de portefeuille se charge avec les informations correctes,
- demandant un devis en utilisant un symbole d’action valide,
- achetant une action plusieurs fois, en vérifiant que le portefeuille affiche les totaux corrects,
- vendant toutes ou certaines actions, en vérifiant à nouveau le portefeuille, et
- vérifiant que votre page d'historique affiche toutes les transactions pour l'utilisateur connecté.

Testez également certains cas d'utilisation imprévus, tels que :

- saisir des chaînes alphabétiques dans des formulaires lorsqu'il faut uniquement des chiffres,
- saisir des nombres nuls ou négatifs dans des formulaires lorsque seuls des nombres positifs sont attendus,
- saisir des valeurs à virgule flottante dans des formulaires lorsque seuls des entiers sont attendus,
- essayer de dépenser plus d'argent qu'un utilisateur n'en a,
- essayer de vendre plus d'actions qu'un utilisateur n'en a,
- saisir un symbole d'action invalide, et
- inclure des caractères potentiellement dangereux comme `'` et `;` dans les requêtes SQL.

Une fois satisfait, pour tester votre code avec `check50`, exécutez la commande suivante.

    check50 cs50/problems/2023/x/finance

<div class="alert" data-alert="warning" role="alert"><p>Soyez conscients que <code class="language-plaintext highlighter-rouge">check50</code> testera l'ensemble de votre programme.  Si vous l'exécutez <strong>avant</strong> d'avoir terminé toutes les fonctions requises, il est possible qu'il signale des erreurs dans des fonctions qui sont en réalité correctes mais qui dépendent d'autres fonctions.</p></div>


Exécutez la commande suivante pour évaluer le style de vos fichiers Python avec `style50`.

    style50 *.py

## Solution de l'équipe enseignante

Vous pouvez styliser votre propre application de manière différente, mais voici à quoi ressemble la solution de l'équipe d'enseignants !

[https://finance.cs50.net/](https://finance.cs50.net/)

N'hésitez pas à vous inscrire pour un compte et à jouer. Ne **utilisez pas** un mot de passe que vous utilisez sur d'autres sites.

Il est **raisonnable** de regarder le HTML et le CSS de l'équipe enseignante.