# Projet 4 formation développeur d'applications python OC

## Démarrage
Ces instructions vous permettront d'obtenir une copie du projet sur votre ordinateur local pour le développement et les tests.

## Prérequis
Vous devez avoir python et pip installés sur votre ordinateur.

## Lancer un environnement virtuel
Pour lancer un environnement virtuel, ouvrez votre terminal et exécutez la commande suivante :

```
    python -m venv nom_de_votre_environnement_virtuel
```

Activez ensuite l'environnement virtuel en utilisant la commande suivante (notez que la commande peut varier selon votre système d'exploitation) :

bash
### Pour macOS et Linux

```
    source nom_de_votre_environnement_virtuel/bin/activate
```

### Pour Windows
```
    .\nom_de_votre_environnement_virtuel\Scripts\activate
```

Vous devriez maintenant voir le nom de votre environnement virtuel entouré de parenthèses à gauche de votre invite de commande, indiquant que vous travaillez dans un environnement virtuel.

Installer les packages
Pour installer les paquets nécessaires, utilisez la commande suivante :

```
    pip install -r requirements.txt
```

Cela installera tous les paquets listés dans le fichier requirements.txt dans votre environnement virtuel.

Vous devriez maintenant être en mesure de lancer un environnement virtuel Python et d'installer les paquets nécessaires à partir d'un fichier requirements.txt.

## Utilitaires
Vous pouvez utilisez le fichier lintall.sh pour lancer tout les outils de nettoyage du code en simultanés.

Pour nettoyer le code en cas de modifications
```
    lintall.sh
```

Pour génerer un rapport flake 8 vous pouvez utiliser la commande 

```
    generate_flake_report.py
    ./flake-report/index.html
```