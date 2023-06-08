### Guide

<div class="alert" data-alert="primary" role="alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire du code. Bien que l'interface puisse paraître différente de celle de votre espace de travail, le comportement des deux environnements devrait être globalement similaire !</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/o5Bkc7gtRjo"></iframe>


### Astuces

*   Lors de la lecture du fichier, vous pouvez trouver cette syntaxe utile, en utilisant `filename` comme nom de votre fichier et `file` comme variable. <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">with</span> <span class="nf">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="k">as</span> <span class="nb">file</span><span class="p">:</span>
      <span class="n">    reader</span> <span class="o">=</span> <span class="n">csv</span><span class="p">.</span><span class="nc">DictReader</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span>
</code></pre></div>    </div>
        
    
*   En Python, pour ajouter à la fin d'une liste, utilisez la fonction `.append()`.

    
<details><summary>Vous n'êtes pas sûr de la solution ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/Fo7Roe8hw3A"></iframe></details>


### Tests

Votre programme doit fonctionner comme les exemples ci-dessous. Étant donné que les simulations comportent une part de hasard pour chacune d'entre elles, votre sortie ne correspondra probablement pas parfaitement aux exemples ci-dessous.

    $ python tournament.py 2018m.csv
    Belgique: 20,9 % de chances de gagner
    Brésil: 20,3 % de chances de gagner
    Portugal: 14,5 % de chances de gagner
    Espagne: 13,6 % de chances de gagner
    Suisse: 10,5 % de chances de gagner
    Argentine: 6,5 % de chances de gagner
    Angleterre: 3,7 % de chances de gagner
    France: 3,3 % de chances de gagner
    Danemark: 2,2 % de chances de gagner
    Croatie: 2,0 % de chances de gagner
    Colombie: 1,8 % de chances de gagner
    Suède: 0,5 % de chances de gagner
    Uruguay: 0,1 % de chances de gagner
    Mexique: 0,1 % de chances de gagner
    

    $ python tournament.py 2019w.csv
    Allemagne: 17,1 % de chances de gagner
    États-Unis: 14,8 % de chances de gagner
    Angleterre: 14,0 % de chances de gagner
    France: 9,2 % de chances de gagner
    Canada: 8,5 % de chances de gagner
    Japon: 7,1 % de chances de gagner
    Australie: 6,8 % de chances de gagner
    Pays-Bas: 5,4 % de chances de gagner
    Suède: 3,9 % de chances de gagner
    Italie: 3,0 % de chances de gagner
    Norvège: 2,9 % de chances de gagner
    Brésil: 2,9 % de chances de gagner
    Espagne: 2,2 % de chances de gagner
    Chine PR: 2,1 % de chances de gagner
    Nigeria: 0,1 % de chances de gagner
    

*   Vous vous demandez peut-être ce qui s'est réellement passé lors des Coupes du monde 2018 et 2019 ! Pour les hommes, la France a remporté la victoire en battant la Croatie en finale. La Belgique a vaincu l'Angleterre pour la troisième place. Pour les femmes, les États-Unis ont remporté la victoire en battant les Pays-Bas en finale. L'Angleterre a vaincu la Suède pour la troisième place.