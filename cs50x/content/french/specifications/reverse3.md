Spécification
-------------

Écrivons un programme appelé `reverse` qui nous permet de retourner un fichier WAV fourni par l'utilisateur et de créer un nouveau fichier WAV contenant l'audio inversé résultant. Pour simplifier, nous limiterons les fichiers que nous traitons au format WAV. Au moment où l'utilisateur exécute le programme, il doit fournir, à l'aide de deux arguments de ligne de commande, le nom du fichier d'entrée qui doit être lu et inversé et le nom du fichier de sortie dans lequel l'audio résultant doit être enregistré. Un programme exécuté avec succès ne devrait pas produire de texte et devrait créer un fichier WAV avec le nom spécifié par l'utilisateur qui lit l'audio du fichier WAV d'entrée en sens inverse. Par exemple :

    $ ./reverse input.wav output.wav
    

Dans le fichier `reverse.c`, vous remarquerez que quelques bibliothèques utiles ont été incluses, ainsi qu'un fichier d'en-tête, `wav.h`. Vous trouverez probablement cela utile lors de la mise en œuvre de votre programme. Nous avons laissé huit `TODO` et deux fonctions d'aide pour que vous les remplissiez, et nous vous recommandons de les aborder dans l'ordre de 1 à 8.

*   Dans le premier `TODO`, vous devez vous assurer que le programme accepte deux arguments de ligne de commande : le nom du fichier WAV d'entrée et le nom du fichier WAV de sortie. Si le programme ne répond pas à ces conditions, vous devez afficher un message d'erreur approprié et renvoyer `1`, mettant fin au programme.
    <ul>
      <li data-marker="+">Indice
        <ul>
          <li data-marker="*">N'oubliez pas que le nombre d'arguments de ligne de commande peut être trouvé dans les variables `argc` passées à la fonction `main` lorsque le programme est exécuté.</li>
          <li data-marker="*">N'oubliez pas que `argv[0]` contient le nom du programme en tant que premier argument de ligne de commande.</li>
        </ul>
      </li>
    </ul>
*   Dans le deuxième `TODO`, vous devez ouvrir votre fichier d'entrée. Nous devrons ouvrir le fichier d'entrée en mode "lecture seule", car nous ne lirons que des données à partir du fichier d'entrée. Il peut être judicieux de vérifier que le fichier a été ouvert avec succès. Sinon, vous devez afficher un message d'erreur approprié et renvoyer `1`, en quittant le programme. Nous devons toutefois attendre pour ouvrir le fichier de sortie, afin de ne pas créer un nouveau fichier WAV avant de savoir si le fichier d'entrée est valide !
    <ul>
      <li data-marker="+">Indice
        <ul>
          <li data-marker="*">Si le premier `TODO` a été implémenté correctement, nous pouvons supposer en toute sécurité que nous pouvons faire référence au nom du fichier d'entrée en utilisant `argv [1]`.</li>
          <li data-marker="*">N'oubliez pas que tout fichier que nous ouvrons, nous devons également le fermer lorsque nous avons fini de l'utiliser. Cela peut impliquer d'ajouter du code ailleurs dans le programme.</li>
        </ul>
      </li>
    </ul>
*   Dans le troisième `TODO`, vous devez lire l'en-tête du fichier d'entrée. Rappelez-vous que, dans `wav.h`, nous avons déjà implémenté une structure qui peut stocker l'en-tête d'un fichier WAV. Étant donné que nous avons écrit `#include "wav.h"` en haut de `reverse.c`, vous pouvez également utiliser la structure `WAVHEADER`.
    
*   Dans le quatrième `TODO`, vous devez compléter la fonction `check_format`. `check_format` prend un seul argument appelé `header`, qui est un `WAVHEADER` représentant une structure contenant l'en-tête du fichier d'entrée. Si `header` indique que le fichier est effectivement un fichier WAV, la fonction `check_format` doit renvoyer `true`. Si ce n'est pas le cas, `check_format` doit renvoyer `false`. Pour vérifier si un fichier est au format WAV, nous pouvons comparer les éléments de l'en-tête du fichier d'entrée à ceux que nous attendons d'un fichier WAV. Il suffit de montrer que les caractères de l'indicateur "WAVE" se trouvent dans le membre `format` de la structure `WAVHEADER` (voir [Background](#background) pour plus de détails sur les en-têtes de fichier WAV).
    
*   Dans le cinquième `TODO`, vous pouvez maintenant ouvrir en toute sécurité le fichier de sortie pour l'écriture. Il serait sage de vérifier que le fichier a été ouvert avec succès.
    <ul>
      <li data-marker="+">Indice
        <ul>
          <li data-marker="*">Si le premier `TODO` a été implémenté correctement, nous pouvons supposer en toute sécurité que nous pouvons faire référence au nom du fichier de sortie en utilisant `argv [2]`.</li>
          <li data-marker="*">N'oubliez pas que tout fichier que nous ouvrons, nous devons également le fermer lorsque nous avons fini de l'utiliser. Cela peut impliquer d'ajouter du code ailleurs dans le programme.</li>
        </ul>
      </li>
    </ul>

C'est peut-être un bon endroit pour arrêter et tester que votre programme fonctionne comme prévu. Si elle est correctement mise en œuvre, votre programme doit ouvrir un nouveau fichier lorsqu'il est exécuté avec les bons arguments de ligne de commande.

Si vous trouvez à un moment donné nécessaire de supprimer un fichier, exécutez la commande suivante dans votre répertoire de travail actuel.

    $ rm file_name.wav
    

Si vous préférez ne pas être invité à confirmer chaque suppression, exécutez plutôt la commande ci-dessous.

    $ rm -f file_name.wav
    

Soyez simplement prudent avec ce commutateur `-f`, car il "force" la suppression sans vous demander votre avis.

*   Ensuite, maintenant que le type de fichier a été vérifié, le sixième `TODO` nous dit d'écrire l'en-tête dans le fichier de sortie. Le fichier WAV inversé aura toujours la même structure de fichier sous-jacente que le fichier d'entrée (même taille, nombre de canaux, bits par échantillon, etc.), il suffit donc de copier l'en-tête que nous avons lu à partir du fichier d'entrée dans le troisième `TODO` dans le fichier de sortie.