* Dans le septième `TODO`, vous devriez implémenter la fonction `get_block_size`. `get_block_size`, comme `check_format`, prend un seul argument : c'est un `WAVHEADER` appelé `header`, représentant la structure contenant l'en-tête du fichier d'entrée. `get_block_size` devrait retourner un entier représentant la taille de **blocs** du fichier WAV donné, en octets. Nous pouvons considérer un _bloc_ comme une unité de données auditives. Pour l'audio, nous calculons la taille de chaque bloc avec le calcul suivant : **nombre de canaux** multiplié par **nombre d'octets par échantillon**. Heureusement, l'en-tête contient toutes les informations dont nous avons besoin pour calculer ces valeurs. Assurez-vous de référencer la section [Background](#background) pour une explication plus approfondie de ce que signifient ces valeurs et comment elles sont stockées. Consultez également `wav.h`, pour déterminer quels membres de `WAVHEADER` pourraient être utiles.
<ul>
<li data-marker="+">Conseils
  <ul>
    <li data-marker="*">Remarquez qu'un des membres de la structure `WAVHEADER` est `bitsPerSample`. Mais pour calculer la taille de bloc, vous aurez besoin d'octets par échantillon!</li>
  </ul>
</li>
</ul>

* Le huitième et dernier `TODO` est où le renversement de l'audio a lieu. Pour cela, nous devons lire chaque bloc de données auditives à partir de la fin du fichier d'entrée et avancer de manière rétrograde, en écrivant simultanément chaque bloc vers le fichier de sortie afin qu'ils soient écrits dans l'ordre inverse. Tout d'abord, nous devons déclarer un tableau pour stocker chaque bloc que nous lisons. Ensuite, c'est à vous d'itérer à travers les données audio du fichier d'entrée. Vous voudrez être sûr que vous lisez tout l'audio, mais ne copiez pas par erreur aucune des données de l'en-tête ! De plus, à des fins de test, nous aimerions maintenir l'ordre des canaux pour chaque bloc audio. Par exemple, dans un fichier WAV avec deux canaux (son stéréophonique), nous voulons nous assurer que le premier canal du dernier bloc audio en entrée devient le premier canal du premier bloc audio en sortie.

<ul>
<li data-marker="+">Conseils
    <ul>
      <li data-marker="*">Quelques fonctions (et une compréhension approfondie de leur utilisation) peuvent être particulièrement utiles pour cette section - les pages du manuel CS50 peuvent s'avérer particulièrement utiles ici :
        <ul>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fread"><code class="language-plaintext highlighter-rouge">fread</code></a> : lit à partir d'un fichier et écrit vers un buffer. La sortie de la fonction auxiliaire <code class="language-plaintext highlighter-rouge">get_block_size</code> peut être utile ici pour décider des valeurs à utiliser pour la taille et le nombre de données à lire à chaque fois.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fwrite"><code class="language-plaintext highlighter-rouge">fwrite</code></a> : écrit à partir d'un buffer vers un fichier.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/fseek"><code class="language-plaintext highlighter-rouge">fseek</code></a> : définit un pointeur de fichier sur un décalage donné. Il peut être utile d'expérimenter avec des valeurs de décalage négatives pour déplacer un pointeur de fichier vers l'arrière.</li>
          <li data-marker="*"><a href="https://manual.cs50.io/3/ftell"><code class="language-plaintext highlighter-rouge">ftell</code></a> : retourne la position courante d'un pointeur de fichier. Il peut être utile d'inspecter quelle valeur <code class="language-plaintext highlighter-rouge">ftell</code> renvoie après que l'en-tête d'entrée est lu dans le troisième `TODO`, en plus de ce qu'elle renvoie pendant que les données audio sont lues.</li>
        </ul>
      </li>
      <li data-marker="*">Gardez à l'esprit qu'après avoir utilisé `fread` pour charger un bloc de données, le pointeur d'entrée pointerait à l'emplacement où la lecture s'est terminée. En d'autres termes, le pointeur d'entrée doit être déplacé de retour de deux tailles de bloc après chaque `fread`, une pour revenir à l'endroit où `fread` a commencé, et la seconde pour passer au bloc non lu précédent. </li>
    </ul>
</li>
</ul>

* Enfin, assurez-vous de fermer tous les fichiers que vous avez ouverts !