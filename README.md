# Devoir 2 - Ingénierie des Systèmes à base de Services

## TP API - Interface de recherche d'adresse 

### Sommaire 

1. Information générale
2. Technologie utilisée
3. Ouvrir le terminal 
4. Questionnement de l'interface
5. Remerciements 
6. Créateurs 

----
### Information générale

L'installation de cette interface implique que vous ayez des notions en environnement Python et que vous l'ayez déjà installé.
Si ce n'est pas le cas, vous pouvez le télécharger à partir du site officiel : <strong>https://www.python.org/downloads/</strong>.

----
### Technologie utilisé

Pour la réalisation de ce projet, nous avons utilisé le langage de programmation <strong>Python</strong>. 

Avant de commencer, veuillez télécharger le module Python en saisisant la commande <strong>pip install requests</strong> dans un terminal.

----
### Ouvrir le terminal 

Pour utiliser l'interface de recherche d'adresse, veuillez suivre les étapes suivantes. 

Tout d'abord, téléchargez le fichier zip <strong>recherche-adresse-api</strong>. 

Ensuite, dézipez le dossier dans le répertoire de votre choix. 

Ouvrez le terminal, puis rendez vous sur le chemin allant dans le répertoire où est stocké votre fichier <strong>recherche-adresse-api</strong>.

Maintenant que vous êtes sur le chemin permettant d'accéder au dossier, pour accéder à l'interface utilisateur, entrez la commande <strong>python .\rechercheadresseapi.py</strong>. 

----
### Questionnement de l'interface

Le but de cette interface Python est de permettre à l'utilisateur de chercher et de trouver une adresse. 

L'utilisateur doit passer par plusieurs étapes afin d'aboutir au résultat escompté. 

<strong>Veuillez saisir le numéro et le nom de la rue recherchée ?</strong> : Saisir de façon controlée l'adresse en composant le numéro et le nom de la rue recherché.

<strong>Saisir le nombre de villes maximum recherchées</strong> : Saisir le nombre de villes maximum recherchées.

<strong>Recherche terminé, il y a (nombre de réultats) résultats</strong> : Affichage d'une liste représentant le nombre de villes maximum recherchées intitulé.

<i>Exemple, si le nombre de ville maximum recherchées est de 15, la liste sera composée de 15 villes comportant le numéro et le nom de la rue recherchée saisi par l'utilisateur.</i> 

<strong>Voulez-vous plus de résultat (y/n)</strong> : L'utilisateur va pouvoir afficher plus de résultats en sélectionnant <i>y</i>, <i>oui</i> pour afficher le reste des résultats ou n, <i>non</i> pour ne pas afficher le reste des résulats.

<strong>Voulez-vous afficher une adresse sur Google Maps ? </strong> : L'utilisateur pourra sélectionner <i>y</i>, <i>oui</i>, pour afficher une adresse sur Google Maps ou <i>n</i>, <i>non</i>, pour ne pas afficher une adresse sur Google Maps.  

<strong>Adresse(s) visualisable(s) sur Google Maps</strong> : Si l'utilisateur sélectionne <i>y</i>, <i>oui</i>, la liste des adresses visualisables sur Google Maps seront affichées sinon non. 

<strong>Sélectionnez l'index de l'adresse que vous désirez visualiser via Google Maps</strong> : L'utilisateur peut choisir l'adresse qu'il désire dans la liste des adresses visualisables sur Google Maps en sélectionnant son index. En sélectionnant l'index de l'adresse désiré, une fenêtre navigateur internet s'ouvrira sur Google Maps à l'adresse recherché par l'utilisateur.   
Enfin l'utilisateur pourra alors sélectionner <i>y</i>, <i>oui</i>, pour rechercher une autre adresse ou <i>n</i>, <i>non</i>, pour terminer le programme Python.  

----
### Remerciements 

Merci d'avoir prit le temps de lire ce README. En espèrant qu'il vous aura été utile. 

----
### Créateurs

Projet réalisé par les winner Dimitri TRAN DUC HUY & Mathilde NYIKEINE. #yeswecan!

Etudiants en première année de Master MIAGE à l'Université de la Nouvelle-Calédonie.

Promotion 2021.

---