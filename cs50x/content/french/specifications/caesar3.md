## Spécification

Concevez et implémentez un programme, `caesar`, qui chiffre des messages en utilisant le chiffre de César.

- Implémentez votre programme dans un fichier appelé `caesar.c` dans un répertoire appelé `caesar`.
- Votre programme doit accepter un seul argument en ligne de commande, un entier positif. Appelons-le `k` pour la discussion.
- Si votre programme est exécuté sans aucun argument en ligne de commande ou avec plus d'un argument en ligne de commande, votre programme doit afficher un message d'erreur de votre choix (avec `printf`) et retourner de `main` une valeur de `1` (ce qui tend à indiquer une erreur) immédiatement.
- Si l'un des caractères de l'argument en ligne de commande n'est pas un chiffre décimal, votre programme doit afficher le message `Usage: ./caesar key` et retourner de `main` une valeur de `1`.
- Ne supposez pas que `k` sera inférieur ou égal à 26. Votre programme doit fonctionner pour toutes les valeurs intégrales non négatives de `k` inférieures à <code>2<sup>31</sup> - 26</code>. En d'autres termes, vous n'avez pas besoin de vous inquiéter si votre programme finit par se briser si l'utilisateur choisit une valeur pour `k` qui est trop grande ou presque trop grande pour tenir dans un `int`. (Rappelez-vous qu'un `int` peut déborder.) Mais même si `k` est supérieur à `26`, les caractères alphabétiques dans l'entrée de votre programme doivent rester des caractères alphabétiques dans la sortie de votre programme. Par exemple, si `k` est `27`, `A` ne doit pas devenir `\` même si `\` est à `27` positions de `A` dans ASCII, selon [asciitable.com](https://www.asciitable.com/); `A` doit devenir `B`, car `B` est à `27` positions de `A`, à condition de revenir à `Z` à `A`.
- Votre programme doit produire une sortie `plaintext:` (avec deux espaces mais sans saut de ligne) puis demander à l'utilisateur une `chaîne` de texte brut (en utilisant `get_string`).
- Votre programme doit produire une sortie `ciphertext:` (avec un espace mais sans saut de ligne), suivie du texte brut correspondant au texte chiffré, avec chaque caractère alphabétique dans le texte brut "tourné" de _k_ positions; les caractères non alphabétiques doivent être affichés sans changement.
- Votre programme doit conserver la casse: les lettres majuscules, bien que tournées, doivent rester des lettres majuscules; les lettres minuscules, bien que tournées, doivent rester des lettres minuscules.
- Après avoir affiché le texte chiffré, vous devez imprimer un saut de ligne. Votre programme doit ensuite se terminer en retournant la valeur `0` de `main`.

## Conseils

Par où commencer ? Abordons ce problème une étape à la fois.

### Pseudo-code

Tout d'abord, essayez d'écrire une fonction `main` dans `caesar.c` qui implémente le programme en utilisant simplement le pseudo-code, même si vous n'êtes pas (encore!) sûr de savoir comment l'écrire en code réel.

<details><summary>Indice</summary><p>Il y a plus d'une façon de faire cela, voici donc juste l'une d'entre elles !</p>

    int main(void)
    {
        // Vérifiez que le programme a été exécuté avec un seul argument en ligne de commande

        // Vérifiez que chaque caractère de argv[1] est un chiffre

        // Convertit argv[1] d'une `chaîne` à un `entier`.

        // Demande à l'utilisateur un texte brut

        // Pour chaque caractère du texte brut :

            // Tourne le caractère s'il s'agit d'une lettre
    }

<p>Il est possible d'éditer votre propre pseudo-code après avoir vu le nôtre ici, mais ne vous contentez pas simplement de copier/coller le nôtre dans le vôtre !</p></details>