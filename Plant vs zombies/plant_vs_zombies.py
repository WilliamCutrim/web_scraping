import pyautogui
import automagica
import time

pasta_image='C:\\Users\\William\\Documents\\GitHub\\web_scraping\\Plant vs zombies\\'


locationZombie01 = None
locationPaint = None
imagelocationZombie01 = pasta_image+'zombie01.PNG'
imagelocationPincel = pasta_image+'paint.PNG'

print(imagelocationZombie01)
print(pyautogui.locateCenterOnScreen(imagelocationZombie01))

try:
    locationZombie = pyautogui.locateCenterOnScreen(imagelocationZombie01)
    if locationZombie != None:
        print('Imagem encontrada!')
        x,y = locationZombie
        print(x,y)
except:
    locationP = pyautogui.locateCenterOnScreen(imagelocationPincel)
    if locationP != None:
        print('Imagem encontrada!')
        x,y = locationP
        print(x,y)
else:
    print('Nenhuma imagem encontrada!')