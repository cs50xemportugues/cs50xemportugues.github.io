## Pour commencer

Connectez-vous à [code.cs50.io](https://code.cs50.io/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez voir une invite de terminal comme ci-dessous:

    $

Ensuite, exécutez

    wget https://cdn.cs50.net/2022/fall/psets/9/finance.zip

pour télécharger un fichier ZIP appelé `finance.zip` dans votre espace de code.

Ensuite, exécutez

    unzip finance.zip

pour créer un dossier appelé `finance`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm finance.zip

et répondre "y" suivi de Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd finance

suivi de Entrée pour vous déplacer (c.-à-d. ouvrir) ce dossier. Votre invite devrait maintenant ressembler à celle ci-dessous.

    finance/ $

Exécutez `ls` tout seul et vous devriez voir quelques fichiers et dossiers:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous avez commis une erreur !

### Configuration

Avant de commencer cette affectation, nous devrons nous inscrire pour une clé d'API afin de pouvoir interroger les données d'IEX. Pour ce faire, suivez ces étapes:

- Visitez [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
- Sélectionnez le type de compte "Individual", puis saisissez votre nom, votre adresse e-mail et un mot de passe, et cliquez sur "Créer un compte".
- Une fois inscrit, faites défiler jusqu'à "Commencer gratuitement" et cliquez sur "Sélectionner le plan de démarrage" pour choisir le plan gratuit. _Notez que ce plan ne fonctionne que pendant 30 jours à partir du jour où vous créez votre compte._ Gardez cela à l'esprit si vous envisagez d'utiliser la même API pour votre projet final !
- Une fois que vous avez confirmé votre compte par email de confirmation, visitez [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
- Copiez la clé qui apparaît sous la colonne _Token_ (elle doit commencer par `pk_`).
- Dans votre fenêtre de terminal, exécutez:

<pre>
$ export API_KEY=value
</pre>

où `value` est la valeur collée, sans aucun espace immédiatement avant ou après le signe `=`. Vous pouvez également coller cette valeur dans un document texte quelque part, au cas où vous en auriez besoin ultérieurement.