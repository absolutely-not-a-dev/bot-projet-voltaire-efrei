@echo off 
setlocal
color 02
cls
:: warning message
echo Avant de commencer l'installation, merci de verifier
echo que vous avez bien 8GB de RAM minimum et une carte graphique 
echo pour faire tourner l'IA correctement. 
echo                    APPUYEZ SUR ENTREE
pause >nul 2>nul 
cls 

echo Ce script va :
echo    - verifier si PYTHON et OLLAMA sont installee (si ce n'est pas le cas, la page web d'installation s'ouvrira)
echo    - installer une IA specialisee dans la langue francaise nommee OpenEuroLLM-French.
echo    - effectuer un test pour verifier si l'IA arrive a generer une reponse dans le temps imparti.
echo    - installer la librairie python SELENIUM et KEYBOARD
echo --------------------------------------------------------------------------
echo Si vous acceptez toute ces conditions,
echo                     APPUYEZ SUR ENTREE
timeout 3 >nul 2>nul 
pause >nul 2>nul 

ollama -v >nul 2>nul 
if %errorlevel% neq 0 (
    echo Merci d'installer ollama
    echo Vous allez etre redirige vers le site web de ollama pour installer l'application.
    timeout /t 5 >nul 
    start "https://ollama.com/download/""
    exit /b 1
)

python --version >nul 2>nul 
if %errorlevel% neq 0 (
    echo Merci d'installer python
    echo Vous allez etre redirige vers le site web de python pour installer l'interpreteur.
    timeout /t 5 >nul 
    start "https://www.python.org/downloads/"
    exit /b 1
)

cls 
echo Téléchargement de l'ia (pas le test)
ollama pull jobautomation/OpenEuroLLM-French:latest 
if %errorlevel% neq 0 (
    echo Une erreur est apparu lors de l'installation de l'ia.
    timeout /t 5 >nul 
    start "https://www.youtube.com/watch?v=2bTHQx5qW8s"
    exit /b 1
)
echo IA installee !

ollama create Voltaire-bot -f Modelfile >nul 
ollama rm jobautomation/OpenEuroLLM-French:latest >nul  
cls 


echo DEMARRAGE DU TEST AI a %time% 
ollama run Voltaire-bot "Indique le mot ou le groupe de mots dont le sens est le plus proche dans un contexte professionnel. Le mot est 'Protocole'. Voici les differents elements: Ensemble de principes. Formation professionnelle. Reunion s'etendant en general sur plusieurs jours. Decision que l'on prend au dernier moment. Decoration militaire. Ensemble de regles a respecter."
echo FIN DU TEST AI a %time%
echo Si vous voyez que l'ia a mis plus de 2 minutes a repondre lors du test, 
echo cela signifie que votre pc n'est pas assez puissant. 
timeout 5

pip install selenium keyboard -q 
color 02


cls 
echo Il vous suffit de double cliquer sur le fichier Voltaire-Bot.cmd pour lancer le bot
echo Si vous voulez eviter d'entrer a chaque fois vos identifiants
echo projet voltaire, remplissez le fichier identifiants.txt
echo 1ere ligne = email 
echo 2nd ligne = mot de passe 
echo 3eme ligne = temps d'attente ajoutee entre chaque question (pour éviter d'être trop suspect)
echo 4ème ligne = raccourci clavier pour fermeture d'urgence lors de l'execution
echo     APPUYEZ SUR ENTREE POUR OUVRIR LE README GITHUB

echo adresse mail ici > identifiants.txt 
echo mot de passe ici >> identifiants.txt 
echo 0 >> identifiants.txt 
echo @echo off > Voltaire-Bot.cmd
echo cd "%cd%" && py main.py && cls >> Voltaire-Bot.cmd

pause >nul 2>nul
start "https://github.com/absolutely-not-a-dev/bot-projet-voltaire-efrei/blob/main/README.md"



endlocal