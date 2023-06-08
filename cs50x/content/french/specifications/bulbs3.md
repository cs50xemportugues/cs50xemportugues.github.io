Spécification
-------------

Concevoir et implémenter un programme, `bulbs`, qui convertit du texte en instructions pour la bande de lumières sur la scène de CS50 de la manière suivante :

* Implémentez votre programme dans un fichier appelé `bulbs.c`.
* Votre programme doit d'abord demander à l'utilisateur un message en utilisant la fonction `get_string`.
* Votre programme doit ensuite convertir la `string` donnée en une série de nombres binaires de 8 bits, un pour chaque caractère de la chaîne.
* Vous pouvez utiliser la fonction `print_bulb` fournie pour imprimer une série de `0` et de `1` sous forme de série d'emoji jaunes et noirs, qui représentent des ampoules allumées et éteintes.
* Chaque "octet" de 8 symboles doit être imprimé sur sa propre ligne lorsqu'il est sorti ; il doit y avoir un `\n` après le dernier "octet" de 8 symboles également.

<details><summary>Conseils pour la conversion décimale en binaire</summary><p> Prenons un exemple avec le nombre 4. Comment convertir 4 en binaire ? Commencez par considérer le bit le plus à droite, celui qui, s'il est activé, ajoute 1 au nombre que nous représentons. Avez-vous besoin que ce bit soit activé ? Divisez 4 par 2 pour le savoir :</p>

`4 / 2 = 2`

<p>2 divise uniformément 4, ce qui nous indique qu'il n'y a pas de reste de 1 à s'inquiéter. Nous pouvons donc laisser ce bit le plus à droite inactif :</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>0
</code></pre></div></div>

<p>Et quelle est la situation pour le bit précédent, à gauche de ce bit que nous avons découvert ? Pour vérifier, suivons un processus similaire, mais reprenons où nous nous sommes arrêtés. Dans l'étape précédente, nous avons divisé 4 par 2 et obtenu 2. Maintenant, est-ce que 2 se divise uniformément dans 2 ? C'est le cas, il n'y a donc pas de reste de 2 à s'inquiéter :</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>00
</code></pre></div></div>

<p>Poursuivons encore plus loin. Après avoir divisé 2 par 2, il ne nous reste plus que 1. Division de 1 par 2 laisse un reste de 1. Cela signifie que nous devrons activer ce bit :</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>100
</code></pre></div></div>

<p>Et maintenant que nous avons divisé notre nombre jusqu'à 0, nous n'avons plus besoin de bits supplémentaires pour le représenter. Notez que nous avons découvert les bits pour représenter 4 dans l'ordre inverse dans lequel nous devons les imprimer : il est probable que nous aurons besoin d'une structure qui nous permet de stocker ces bits, afin que nous puissions les imprimer en avant plus tard. Et bien sûr, dans votre code réel, vous travaillerez avec des `chars` de 8 bits, vous voudrez donc préfixer les 0 nécessaires.</p>

<p>Lors de la vérification des restes, l'opérateur modulo (`%`) peut être utile ! <code class="language-plaintext highlighter-rouge">4 % 2</code>, par exemple, renvoie 0, ce qui signifie que 2 divise 4 avec un reste de 0.</p></details>