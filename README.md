# **Projet 11 python openclassrooms**
Site de réservation de compétition pour les entreprises de vêtements de fitness de marque par l'entreprise _**GÜDLFT**_


La version de **Python** à utiliser : _**3.10.5**_



# **ENVIRONNEMENT VIRTUEL**
Création de l'environnement virtuel :


Pour créer l'environnement virtuel il faut exécuter la commande suivante à la racine du projet :

    python -m venv env


Puis la commande suivante pour démarrer l'environnement :

-   sous Linux

    
    source env/bin/activate

-   sous Windows


    env/Scripts/activate.bat


Pour installer les packages spécifiés dans le fichier requirements.txt il faut exécuter la commande suivante :

    pip install -r requirements.txt


# **SCRIPT**

Il faut dans un premier temps démarrer le serveur FLASK à l'aide des commandes suivantes :

      set FLASK_APP=server.py
      flask run

Le site se trouvera ensuite sur l'URL suivante : ___http://127.0.0.1:5000/___

Les différentes adresses mails de connexion sont :

| *Email*              |
|----------------------|
| john@simplylift.co   |
| admin@irontemple.com |
| kate@shelifts.co.uk  |

# **TESTS**

Les tests sont situés dans le dossier tests, le module pytest permet de lancer ces tests via la commande :

      pytest

Il y a également la possibilité de tester la couverture des tests sur le projet et d'avoir un rapport, 
avec le module coverage via la commande :

      coverage report

Les performances de l'application peuvent être testées grace au module locust via la commande en se 
plaçant dans le repertoire /tests/performance_tests :

      locust

Une fois locust démarré, il faut aller sur l'URL suivante : ___http://localhost:8089/___
puis renseigner les différents champs du formulaire, nombre d'utilisateurs simultanés, vitesse 
d'apparition des utilisateurs, ainsi que l'Host (ici ___http://127.0.0.1:5000/___)

Les rapports de ces 3 tests sont disponibles dans le repertoire rapports.
