Pas à pas
----------

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

Utilisation
-----------

Votre programme doit se comporter comme indiqué ci-dessous.

    $ ./recover
    Usage: ./recover IMAGE
    

où `IMAGE` est le nom de l'image forensique. Par exemple :

    $ ./recover card.raw
    

Conseils
-------

Notez que vous pouvez ouvrir `card.raw` de manière programmable avec `fopen`, comme ci-dessous, à condition que `argv[1]` existe.

<div class="language-c highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kt">FILE</span> <span class="o">*</span><span class="n">file</span> <span class="o">=</span> <span class="n">fopen</span><span class="p">(</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="s">"r"</span><span class="p">);</span>
</code></pre></div></div>
    

Lors de son exécution, votre programme doit récupérer chaque fichier JPEG de `card.raw`, en le stockant en tant que fichier distinct dans votre répertoire de travail actuel. Votre programme doit numéroter les fichiers de sortie en nommant chaque fichier `###.jpg`, où `###` est un nombre décimal à trois chiffres à partir de `000`. Devenez ami avec [`sprintf`](https://man.cs50.io/3/sprintf) et notez que `sprintf` stocke une chaîne formatée dans une zone mémoire. Compte tenu du format prescrit `###.jpg` pour le nom de fichier JPEG, combien d'octets devez-vous allouer pour cette chaîne ? (N'oubliez pas le caractère NUL !)

Vous n'avez pas besoin d'essayer de récupérer les noms d'origine des fichiers JPEG. Pour vérifier si les fichiers JPEG générés par votre programme sont corrects, double-cliquez simplement et regardez ! Si chaque photo apparaît intacte, votre opération a probablement été un succès !

Il est peu probable, cependant, que les fichiers JPEG que la première rédaction de votre code génère soient corrects. (Si vous les ouvrez et ne voyez rien, ils ne sont probablement pas corrects !) Exécutez la commande ci-dessous pour supprimer tous les fichiers JPEG de votre répertoire de travail actuel.

    $ rm *.jpg
    

Si vous ne voulez pas être invité à confirmer chaque suppression, exécutez plutôt la commande ci-dessous.

    $ rm -f *.jpg
    

Soyez juste prudent avec cette commutation `-f`, car elle "force" la suppression sans vous demander confirmation.

Si vous voulez créer un nouveau type pour stocker un octet de données, vous pouvez le faire via le code ci-dessous, qui définit un nouveau type appelé `BYTE` comme étant un `uint8_t` (un type défini dans `stdint.h`, représentant un entier non signé de 8 bits).

    typedef uint8_t BYTE;
    

Il convient également de rappeler que vous pouvez lire des données depuis un fichier en utilisant la fonction [`fread`](https://man.cs50.io/3/fread), qui lira des données depuis un fichier dans une zone mémoire. Conformément à sa [page de manuel](https://man.cs50.io/3/fread), `fread` renvoie le nombre d'octets qu'il a lus, auquel cas il doit soit renvoyer `512`, soit renvoyer `0`, étant donné que `card.raw` contient un certain nombre de blocs de 512 octets. Afin de lire chaque bloc de `card.raw`, après l'avoir ouvert avec `fopen`, il suffit d'utiliser une boucle comme celle-ci :

   
<pre class="highlight">
<span class="k">while</span> (fread(buffer, <span class="mi">1</span>, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
{


}
</pre>
De cette façon, dès que `fread` renvoie `0` (ce qui est effectivement `false`), votre boucle se terminera.

Test
----

Exécutez la commande ci-dessous pour évaluer la correction de votre code en utilisant `check50`. Mais assurez-vous de le compiler et de le tester vous-même également !

    check50 cs50/problems/2023/x/recover
    

Exécutez la commande ci-dessous pour évaluer le style de votre code en utilisant `style50`.

    style50 recover.c
    

Comment soumettre
-----------------

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail.

    submit50 cs50/problems/2023/x/recover"