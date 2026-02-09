# Imports
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, subprocess, sys, keyboard

# Fonctions
def ask_ai(prompt: str) -> str:
    return subprocess.run(["ollama", "run", "Voltaire-bot", prompt], capture_output=True, text=True, encoding="utf-8").stdout
     
def driver_wait(locator=(By.XPATH, "//*"), click=False) -> None:
    wait = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
    if click: wait.click()
    else: return wait.text

def shortcut_detection():
    driver.quit()
    os._exit(0)

# Constants
LOGIN_PAGE = "https://compte.groupe-voltaire.fr/login" 
TRAINING_PAGE = "https://apprentissage.appli3.projet-voltaire.fr/entrainement"
MAIN_BOX_XPATH = "//div[contains(@class, 'r-hwh8t1 r-1wzrnnt r-nsbfu8')]"

# Check if user put his credential in identifiants.txt 
if os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "identifiants.txt")):
    with open("identifiants.txt", "r") as f:
        USERNAME, PASSWORD, ATTENTE_ENTRE_QUESTIONS, SHORTCUT = f.readline().strip(), f.readline().strip(), int(f.readline().strip()), f.readline().strip()
        credential_status = True
else:
    USERNAME, PASSWORD, ATTENTE_ENTRE_QUESTIONS, SHORTCUT = "Stv, tu peux inscrire tes identifiants dans identifiants.txt", "", 0, "ctrl+alt+q"
    credential_status = False

# Start keyboard detection
keyboard.add_hotkey(SHORTCUT, shortcut_detection)

# Init Chrome driver + fullscreen + no cookies + mute
options = Options()
options.add_argument("--mute-audio") 
options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"), options=options)
driver.delete_all_cookies()
driver.get(LOGIN_PAGE)
ai_already_anwsered = False 

# Fill email + password
input_elem = driver.find_elements(By.TAG_NAME, "input")
email_form, password_form = input_elem[1], input_elem[2] 
email_form.send_keys(USERNAME)
password_form.send_keys(PASSWORD)

# Press enter if email and password are valid
if credential_status: 
    password_form.send_keys(Keys.ENTER) 
else :
    while driver.current_url == LOGIN_PAGE:
        time.sleep(1) 
    
# Click on "Entrainement" button 
driver_wait((By.TAG_NAME, "span"), click=True)

# Main loop
while True:
    while driver.current_url == TRAINING_PAGE: 
        driver_wait()
        try: driver.find_element(By.XPATH, "//div[contains(@class, 'css-g5y9jx r-1phboty r-1q8sk3r r-8dgmk1')]/button").click()
        except NoSuchElementException: pass
        try: driver.find_element(By.XPATH, "//div[contains(@class, 'css-g5y9jx r-1phboty r-1q8sk3r r-1qfr5kh r-1yadl64')]/button").click()
        except NoSuchElementException: pass   

        full_text = driver_wait((By.XPATH, "//*")).split("\n")
        for text in full_text:
            if "CONTINUER" in text or "Question cruciale" in text:
                LISTE_ELEMENTS = driver.find_elements(By.XPATH, f"//button//div//*[text()='Continuer']")
                FIRST = LISTE_ELEMENTS[0]
                continue
            if "SUIVANT" in text or "Règle acquise" in text:
                driver.find_elements(By.XPATH, f"//button//div//*[text()='SUIVANT']")[0].click()
                continue
        
        
        all_text = driver.find_element(By.XPATH, MAIN_BOX_XPATH).text.split("\n")
        for text in all_text: # remove useless content
            for to_del in ("JE NE PEUX PAS ÉCOUTER", "RÉVÉLER UN INDICE", "Utiliser un indice n'affecte pas", "☰", "0 / "):
                if to_del in text:
                    all_text.remove(text)

        theme = all_text[0] 
        instruction = all_text[1].replace("Cliquer sur", "Trouver")


        if "Vocabulaire" in theme: # expression tab
            prompt = f"{instruction}. Il n'y a qu'une seule réponse possible. Le mot est {all_text[2]}. La réponse se trouve dans les propositions suivantes: '{" ".join(all_text[3::])}'"


        elif "Cliquez sur la faute" in theme: # courriel tab
            prompt = f"Tu dois trouver la faute dans la phrase. Il n'y a qu'une seule réponse possible. Si tu ne repère pas de faute, écrit 'Il n’y a pas de faute'. Voici la phrase: '{" ".join(all_text)}'"


        elif "Cliquez sur le mot" in theme : 
            div_text = driver.find_elements(By.XPATH, MAIN_BOX_XPATH + "//div[contains(@class, 'css-g5y9jx r-18u37iz r-1w6e6rj r-1h0z5md r-1peese0 r-1wzrnnt r-3pj75a r-13qz1uu')]")
            prompt = f"{instruction}. Il n'y a qu'une seule réponse possible. La réponse se trouve dans les propositions suivantes :'{"".join([text.text for text in div_text])}'"


        elif "Cliquer / Déposer" in theme : # orthographe tab
            box1, box2 = driver.find_elements(By.XPATH, MAIN_BOX_XPATH + "//div[contains(@class, 'css-g5y9jx r-13awgt0 r-vacyoi')]")
            choices = [choice.text for choice in driver.find_elements(By.XPATH, MAIN_BOX_XPATH + "//div[not (contains(@style, 'center')) and @class='css-146c3p1 r-lrvibr']")]
            categorie1, categorie2 = driver.find_elements(By.XPATH, MAIN_BOX_XPATH + "//div[contains(@class, 'css-g5y9jx r-13awgt0 r-1fdo3w0')]")
            prompt = f"{instruction}. Tu dois indiquer seulement les mots respéctant cette règle : '{categorie2.text}'. Voici la liste des éléments: '{choices}'"


        elif theme == "RÈGLE" : # help tab (useless so directly click on CONTINUER)
            driver_wait((By.XPATH, f"//*[contains(text(), 'Continuer')]"), True)
            continue

        if not ai_already_anwsered:
            ai_anwser = ask_ai(prompt).replace("\\n", "\n").replace("\n", " ").replace("-", "‑").strip()
        ai_already_anwsered = False  
      
        driver.implicitly_wait(ATTENTE_ENTRE_QUESTIONS)

        if "Cliquer / Déposer" in theme:
            for choice in choices:
                right_box = box2 if choice in ai_anwser else box1
                driver.find_elements(By.XPATH, MAIN_BOX_XPATH + f"//*[contains(text(), \"{choice}\")]")[0].click()
                ActionChains(driver).move_to_element_with_offset(right_box, 0, 100).click().perform()
            driver.find_element(By.XPATH, f"//div[contains(@class, 'r-q4m81j r-tsynxw r-180ddmb r-lrvibr') and contains(text(), 'Valider')]").click()
        
        else :
            try : 
                driver.find_elements(By.XPATH, MAIN_BOX_XPATH + f"//*[contains(text(), \"{ai_anwser}\")]")[0].click()
                driver_wait((By.XPATH, f"//div[contains(text(), 'SUIVANT')]"), click=True)
            except (ElementClickInterceptedException, IndexError) as e:
                print("Error as occured : \n", e)
                ia_already_anwsered = True 
                continue  

        

driver.quit()