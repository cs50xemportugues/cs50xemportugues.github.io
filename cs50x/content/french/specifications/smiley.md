Laboratoire 4: Smiley
=============

Objectifs de l'apprentissage
--------------

*   Apprendre à travailler avec des images.
*   Pratiquer la manipulation de pixels.

Contexte
----------

![Smiley](https://cs50.harvard.edu/x/2023/labs/4/smiley/smiley_spec_image.png)

Dans le cours, vous avez appris comment les images sont stockées sur un ordinateur. Dans ce laboratoire, vous travaillerez sur un fichier BMP, en fait l'image d'un smiley ci-dessus, et vous changerez tous les pixels noirs par une couleur de votre choix.

Cependant, le smiley sur lequel vous travaillerez n'est pas seulement composé de 0 et 1, ou de pixels noirs et blancs, mais est constitué de 24 bits par pixel. Il utilise huit bits pour représenter les valeurs de rouge, huit bits pour le vert et huit bits pour le bleu. Étant donné que chaque couleur utilise huit bits ou un octet, nous pouvons utiliser un nombre dans la plage de 0 à 255 pour représenter sa valeur de couleur. En hexadécimal, cela est représenté par `0x00` à `0xff`. En mélangeant ces valeurs de rouge, vert et bleu, nous pouvons créer des millions de couleurs possibles.

Si vous regardez `bmp.h`, l'un des fichiers d'aide du code de distribution, vous verrez comment chaque `RGB triple` est représenté par une `struct` comme:

    typedef struct
    {
        BYTE rgbtBlue;
        BYTE rgbtGreen;
        BYTE rgbtRed;
    }
    RGBTRIPLE;
    

où `BYTE` est défini comme un entier de 8 bits.

Vous remarquerez plusieurs fichiers fournis dans le code de distribution pour traiter la lecture et l'écriture d'un fichier image, ainsi que pour traiter les métadonnées ou les "en-têtes" de l'image. Vous compléterez la fonction `colorize` dans `helpers.c`, qui a déjà comme paramètres d'entrée la hauteur de l'image, la largeur et un tableau bidimensionnel de `RGBTRIPLE` qui créent l'image elle-même.

*   Conseils
    *   Si nous devions sauvegarder le premier pixel en tant que `RGBTRIPLE pixel = image[0][0]`, nous pourrions ensuite accéder à chacune des couleurs individuelles de `pixel` sous forme de `pixel.rgbtBlue`, `pixel.rgbtGreen` et `pixel.rgbtRed`.

Démo
----

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-vSNSSp3y9K4fvpMUghBaX2sl4" src="https://asciinema.org/a/vSNSSp3y9K4fvpMUghBaX2sl4.js"></script>

Pour commencer
---------------

Ouvrez  [VS Code](https://code.cs50.io/).

Commencez par cliquer dans votre fenêtre de terminal, puis tapez `cd`. Vous devriez voir apparaître quelque chose qui ressemble à cela.

    $
    

Cliquez à l'intérieur de cette fenêtre de terminal, puis tapez

    wget https://cdn.cs50.net/2022/fall/labs/4/smiley.zip
    

suivi de la touche Entrée pour télécharger un fichier ZIP appelé `smiley.zip` dans votre espace de code. Prenez soin de ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Maintenant, tapez

    unzip smiley.zip
    

pour créer un dossier appelé `smiley`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter :

    rm smiley.zip
    

et répondez "y" suivi de Entrée à la demande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd smiley
    

suivi de Entrée pour vous déplacer (c'est-à-dire ouvrir) dans ce répertoire. Votre invite devrait ressembler à ceci.

    smiley/ $
    

Si tout s'est bien passé, vous devez exécuter

    ls
    

et vous devriez voir `bmp.h`, `colorize.c`, `helpers.c`, `helpers.h`, `Makefile` et `smiley.bmp`.

Si vous rencontrez un problème, suivez à nouveau ces étapes et voyez si vous pouvez déterminer où vous avez commis une erreur.

Détails de mise en œuvre
----------------------

Ouvrez `helpers.c` et notez que la fonction `colorize` est incomplète. Notez que la hauteur de l'image, sa largeur et un tableau bidimensionnel de pixels sont configurés comme paramètres d'entrée pour cette fonction. Vous devez implémenter cette fonction pour changer tous les pixels noirs de l'image par la couleur de votre choix.

Vous pouvez compiler votre code en tapant simplement `make` à l'invite `$`.

Vous pouvez ensuite exécuter le programme en tapant :

    ./colorize smiley.bmp outfile.bmp
    

où `outfile.bmp` est le nom du nouveau BMP que vous créez.

Question réflexion
----------------

*   Comment représentez-vous un pixel noir lors de l'utilisation d'un fichier BMP en couleur 24 bits ?
*   Est-ce le même ou différent lors de la combinaison de peintures pour représenter différentes couleurs ?

Comment tester votre code
---------------------

Votre programme doit fonctionner comme les exemples ci-dessous.

    smiley/ $ ./colorize smiley.bmp smiley_out.bmp
    

Lorsque votre programme fonctionne correctement, vous devez voir un nouveau fichier, `smiley_out.bmp` dans votre répertoire `smiley`. Ouvrez-le et vérifiez si les pixels noirs sont maintenant de la couleur que vous avez spécifiée.

Vous pouvez vérifier votre code en utilisant `check50`, un programme que CS50 utilisera pour tester votre code lorsque vous le soumettrez, en tapant ce qui suit à l'invite `$`. Mais assurez-vous de le tester vous-même aussi !

    check50 cs50/labs/2023/x/smiley
    

Pour évaluer que le style de votre code (indentations et espacement) est correct, tapez ce qui suit à l'invite `$`.

    style50 helpers.c
    
"

Comment soumettre
-------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/labs/2023/x/smiley
    

<details><summary>Voulez-vous voir la solution du personnel ?</summary><div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">#include</span> <span class="cpf">"helpers.h"</span><span class="cp">
</span>
<span class="kt">void</span> <span class="nf">colorize</span><span class="p">(</span><span class="kt">int</span> <span class="n">height</span><span class="p">,</span> <span class="kt">int</span> <span class="n">width</span><span class="p">,</span> <span class="n">RGBTRIPLE</span> <span class="n">image</span><span class="p">[</span><span class="n">height</span><span class="p">][</span><span class="n">width</span><span class="p">])</span>
<span class="p">{</span>
    <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">height</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="k">for</span> <span class="p">(</span><span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">j</span> <span class="o">&lt;</span> <span class="n">width</span><span class="p">;</span> <span class="n">j</span><span class="o">++</span><span class="p">)</span>
        <span class="p">{</span>
            <span class="c1">// Rendre les pixels noirs en rouges</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtRed</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="o">&amp;&amp;</span> <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtGreen</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="o">&amp;&amp;</span> <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtBlue</span> <span class="o">==</span> <span class="mh">0x00</span><span class="p">)</span>
            <span class="p">{</span>
                <span class="n">image</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="n">j</span><span class="p">].</span><span class="n">rgbtRed</span> <span class="o">=</span> <span class="mh">0xff</span><span class="p">;</span>
            <span class="p">}</span>
        <span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>
</code></pre></div></div></details>

