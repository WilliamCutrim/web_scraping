import pyautogui
import automagica
import time

pasta_image='C:\\Users\\William\\Documents\\GitHub\\web_scraping\\Tibia\\'

locationJanela = None
locationBarra = None
locationBattle = None
imagelocationJanela = pasta_image+'icone_janela.PNG'
imagelocationJanelaS = pasta_image+'icone_janela_s.PNG'
imagelocationBarra = pasta_image+'icone_barra.PNG'
imagelocationBattle = pasta_image+'battle.PNG'

print('Start')
while (locationBarra == None):
    try:
        locationPesq = pyautogui.locateCenterOnScreen(imagelocationJanelaS)
        if locationPesq != None:
            print('Imagem encontrada!')
            x,y = locationPesq
            print(x,y)
            pyautogui.click(x,y)
            locationBattle = pyautogui.locateCenterOnScreen(imagelocationBattle)
            if locationBattle != imagelocationBattle:
                pyautogui.press('space')
            # pyautogui.press('up')
            # time.sleep(0.5)
            # pyautogui.press('left')
            # time.sleep(0.5)
            # pyautogui.press('down')
            # time.sleep(0.5)
            # pyautogui.press('up')
            # time.sleep(0.5)
            # pyautogui.press('right')
            # time.sleep(0.5)
            # pyautogui.press('up')
            # time.sleep(0.5)
            # pyautogui.press('up')
            # time.sleep(0.5)
            # pyautogui.press('up')
            # time.sleep(0.5)       
    except:
        print('Imagem não encontrada')