#IFT606-DEV1
Devoir 1

Version de Python utilisé est: Python 2.7

Librairies utilisés:  pycrypto  (voir https://pypi.python.org/pypi/pycrypto)

#Installation

1- Installer Python 2.7

2- Installer Python-pip   (sudo apt-get install python-pip)

3- pip install pycrypto

4- Enjoy

#Installation sur Windows
1- Installer Python 2.7

2- Suivre le workaround que vous trouverez ici: http://stackoverflow.com/questions/13787258/pycrypto-install-error-on-windows

3- Utiliser le binaire précompilé de The Voidspace Python Modules: http://www.voidspace.org.uk/python/modules.shtml#pycrypto

4- Enjoy

#Utilisation du logiciel
1- Démarrer server.py

2- Démarrer une seule instance de client.py

3- Saisir un nombre infini de messages dans client.py

4- Saisir «QUIT» pour fermer la connexion entre le client et le serveur

5- Recommencer à partir de l'étape 2 sur un autre client

#Fonctionnement
1- Le Serveur démarre, ouvre un port au public

2- Le Serveur génère sa pair de clé privée/public

3- Un Client démarre et fait une demande de connexion au Serveur

4- Une fois la connexion établie, le Serveur envoie sa clé publique au Client

5- Le Client récupère la clé publique du serveur et s'en sert pour crypter ses messages

6- Le Client envoie le nombre de messages cryptés souhaité

7- Le Serveur utilise sa clé privée pour déchiffrer les messages envoyés par le Client

8- Serveur et Client vécurent heureux jusqu'à la fin des temps! Fin.

