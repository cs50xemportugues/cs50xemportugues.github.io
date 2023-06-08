### Conseils

- Si vous voulez demander à l'utilisateur la valeur d'une variable plusieurs fois jusqu'à ce qu'une condition soit remplie, vous pourriez utiliser une boucle `do ... while`. Par exemple, rappelez-vous le code suivant du cours, qui demande à l'utilisateur plusieurs fois jusqu'à ce qu'il entre un entier positif. <div class= "language-c highlighter-rouge"> <div class= "highlight"> <pre class= "highlight"> <code> <span class="kt">int</span> <span class="n"> n </span> <span class="p">;</span>
  <span class = "k">do</span>
    <span class="p"> {</span>
      <span class="n">n</span> <span class="o"> =</span> <span class="n">get_int</span><span class = "p"> (</span> <span class = "s"> "Entier positif: "</span> <span class = "p">);</span>
    <span class="p">} </span>
  <span class = "k">while</span> <span class = "p"> (</span> <span class = "n">n </span> <span class = "o"> &lt; </span> <span class = "mi">1 </span> <span class = "p">);</span>
  </code> </pre> </div> </div>
  Comment pourriez-vous adapter ce code pour garantir une taille de départ d'au moins 9 et une taille finale d'au moins la taille de départ?

* Pour déclarer une nouvelle variable, assurez-vous de spécifier son type de données, un nom pour la variable et (éventuellement) quelle devrait être sa valeur initiale.
  - Par exemple, vous voudrez peut-être créer une variable pour suivre le nombre d'années écoulées.
* Pour calculer combien d'années il faudra pour que la population atteigne la taille finale, une autre boucle pourrait être utile! À l'intérieur de la boucle, vous voudrez probablement mettre à jour la taille de la population selon la formule de l'arrière-plan et mettre à jour le nombre d'années écoulées.
* Pour imprimer un entier `n` sur le terminal, rappelez-vous que vous pouvez utiliser une ligne de code comme <div class = "language-c highlighter-rouge"> <div class = "highlight"> <pre class = "highlight"> <code> <span class = "n"> printf </span> <span class = "p"> (</span> <span class = "s"> "Le nombre est% i "</span> <span class = "se"> \ n </span> <span class ="s"> "</span> <span class ="p">,</span> <span class ="n"> n </span> <span class ="p">);</span>
  </code> </pre> </div> </div>
  pour spécifier que la variable `n` doit remplacer le paramètre de substitution `%i`.

### Comment tester votre code

Votre programme doit se comporter comme indiqué ci-dessous.

     $ ./population
     Taille de départ: 1200
     Taille finale: 1300
     Années : 1


     $ ./population
     Taille de départ: -5
     Taille de départ: 3
     Taille de départ: 9
     Taille finale: 5
     Taille finale: 18
     Années : 8


     $ ./population
     Taille de départ: 20
     Taille finale: 1
     Taille finale: 10
     Taille finale: 100
     Années : 20


     $ ./population
     Taille de départ: 100
     Taille finale: 1000000
     Années : 115

<details><summary> Vous n'êtes pas sûr de savoir comment résoudre?</summary><iframe allow = " accéléromètre; lecture automatique; media crypté; gyroscope; picture-in-picture " allowfullscreen =" " class =" border " data-video ="" src = "https://video.cs50.io/2CcqQnLbGOE"></iframe></details>

Exécutez le code ci-dessous pour évaluer la justesse de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même aussi!

     check50 cs50 / labs / 2023 / x / population

Exécutez le code ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 population.c

## Comment soumettre

Dans votre terminal, exécutez le code ci-dessous pour soumettre votre travail.

     submit50 cs50 / labs / 2023 / x / population