# bot-projet-voltaire-efrei

## Description
Ceci est un bot pour le projet voltaire de l'EFREI (testé sur les tests des années P1) afin de compléter sa progression aux entraînements (pas aux test !!!) automatiquement.      
Ce projet a été écrit en python et se base sur la librairie Selenium.    
Pour résoudre tout types de questions, une IA local est utilisée grâce au service Ollama.   
Un bon pc est donc requis:   
- **MINIMUM** 10Go de RAM (8Go = très limite) + RTX3050 / RX6600 + 17Go disponible sur disque dur. 
- **RECOMMENDÉ** 16Go de RAM + RTX3070 / RTX4060 / RX7600 + 20Go disponible sur disque dur.
- **MA CONFIG (réponse de l'IA en 4sec)** 32Go de RAM + RTX4070 + 100Go disponible sur disque dur. 
    


## Téléchargement

> [!WARNING]
> Vous devez installer [Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") et [Ollama](https://ollama.com/download "https://ollama.com/download") au préalable.

Maintenir le raccourci clavier <kbd>Win + R</kbd>, écrire "cmd" puis appuyer sur <kbd>Entrée</kbd>.   
Un terminal devrait s'ouvrir, copier/coller la commande suivante dans le terminal:

```bash
cd "%userprofile%\Documents" && git clone https://github.com/absolutely-not-a-dev/bot-projet-voltaire-efrei.git
```



## Installation et Lancement
- Maintenir le raccourci clavier <kbd>Win + R</kbd>, écrire "documents" puis appuyer sur <kbd>Entrée</kbd>.   
- Allez dans le dossier 'bot-projet-voltaire-efrei' 
- Double cliquez sur 'installation.cmd' puis suivez les consignes.   
- Pour lancer le bot, double cliquez sur le fichier 'Voltaire-bot.cmd'


## A savoir
L'ia risque de prendre du temps à démarrer lors de la 1ère question (10sec environ) donc soyez patient au début de chaque session.    

D'après mes tests, l'ia excelle dans l'orthographe (repérer les adverbes, COD, COI ...) mais aussi le vocabulaire (cliquer sur la faute dans la phrase).
Lorsqu'il faut trier les mots dans 2 catégories, l'ia galère un peu donc à éviter
pour l'instant et la catégorie mail est optionnelle donc non supportée.


J'ai fine-tuner l'ia grace au Modelfile mais ce n'est pas encore parfait.    
J'ai testé avec d'autres IA plus légères mais elles ne répondaient pas sous forme standardisée donc inutilisable dans un script python.   
Il est donc fortement déconseillé de changer d'IA dans le Modelfile.


## Ressources
Voici les ressources qui m'ont aidé à réaliser ce projet:
- [Tuto Selenium Python](https://www.youtube.com/watch?v=NB8OceGZGjA "https://www.youtube.com/watch?v=NB8OceGZGjA") de "Tech With Tim"
- [Documentation officiel](https://www.selenium.dev/documentation/ "https://www.selenium.dev/documentation/") de Selenium
- [Hugging face](https://huggingface.co/ "https://huggingface.co/"), site sur l'IA, le machine learning, le fine-tuning ...



## Confidentialité
- Vous avez le choix de remplir vos identifiants projet voltaire dans identifiants.txt mais ce n'est pas obligatoire.   

- Si vous inscrivez vos indentifiants dans le fichier, ils ne seront ni partagés à un tiers, ni à moi, ni enregistrés autre part que dans ce fichier sous forme **NON-ENCRYPTEE** donc à remplir à vos risques et périls. 

- Ollama est un service local (fonctionne sans internet) donc toutes les conversations sont enregistrées en local et aucune n'est divulgée à un tiers.