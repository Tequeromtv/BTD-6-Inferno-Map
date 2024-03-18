from pyautogui import *
import pyautogui
import time
import keyboard
import pyscreeze

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

pyautogui.alert("""             Pressione OK para começar a automação!
       pressione 'q' a qualquer momento para parar!""", title="M0NK3Y by: TK V0.2", button="OK")

# Regiões da tela
regiao_inc = (522, 611, 656,724)
region_dif = (908,657, 1005,735)
region_map = (0,0, 1365,767)
region_mapdif = (381,223, 511,353)
region_modedif = (846,255, 985,399)
region_ok = (612,114, 753,245)
region_casa = (1081,399, 1156,500)
region_sniper = (1041,368, 1107,442)
region_alch = (1102,351, 1167,427)
region_comece = (1278,700, 1336,749)
region_cliq = (649,85, 709,154)
region_reload = (470,563, 550,643)

# Values
inc_pos = None
dificulty_select = None
map_selector = None
map_dif = None
mode_dif = None
okvar = None
house = None
sniper = None
alquimista = None
iniciar = None
cliq = None
reload = None
keyboardpresser = None




while not keyboard.is_pressed('q'):
    # Apertar play
    while inc_pos is None:
        inc_pos = pyautogui.locateOnScreen('imagens/inc.png', region=(regiao_inc), confidence=0.7,)     
        if inc_pos is not None:
            pyautogui.moveTo(600,665)  
            pyautogui.click() 
            time.sleep(0.2)
            break 
        else:
            continue
                
    # Selecionar a dificuldade dos mapas
    while dificulty_select is None:
        dificulty_select = pyautogui.locateOnScreen('imagens/mapinf.png', region=(region_map), confidence=0.7)
        if dificulty_select is not None:
            pyautogui.moveTo(989,406)
            time.sleep(0.2)
            break
        else:
            pyautogui.moveTo(950,703)
            pyautogui.click()
            time.sleep(0.2)
            continue

    # Map selector
    while map_selector is None:
        map_selector = pyautogui.locateOnScreen('imagens/mapinf.png', region=(region_map), confidence=0.7)
        if map_selector is not None:
            pyautogui.moveTo(989,406)
            pyautogui.click()
            time.sleep(0.2)
            break
        else:
            continue

    # Selecionar dificuldade do Mapa
    while map_dif is None:
        map_dif = pyautogui.locateOnScreen('imagens/mapdif.png', region=(region_mapdif), confidence=0.7)
        if map_dif is not None:
            pyautogui.moveTo(450,295)
            pyautogui.click()
            time.sleep(0.2)
            break
        else:
            continue

    # Select dificult mode of the map
    while mode_dif is None:
        mode_dif = pyautogui.locateOnScreen('imagens/modedif.png', region=(region_modedif), confidence=0.7)
        if map_dif is not None:
            pyautogui.moveTo(914,327)
            pyautogui.click()
            time.sleep(0.2)
            break
        else:
            continue
            
    # Click OK button
    while okvar is None:
        time.sleep(1.0)
        okvar = pyautogui.locateOnScreen('imagens/okball.png', region=(region_ok), confidence=0.9)
        if okvar is not None:
            pyautogui.moveTo(685,541)
            pyautogui.click()
            time.sleep(0.4)
            break
        else:
            continue

    # Colocar a casa e dar upgrade
    while house is None:
        keyboard.press_and_release('k')
        pyautogui.moveTo(1125,475)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        house = pyautogui.locateOnScreen('imagens/house.png', region=(region_casa), confidence=0.7) 
        if house is not None:
            pyautogui.moveTo(1125,475)  
            time.sleep(0.5)
            keyboard.press_and_release(';')
            time.sleep(0.2)
            keyboard.press_and_release(';')
            time.sleep(0.2)
            keyboard.press_and_release(',')
            time.sleep(0.2)
            keyboard.press_and_release(',')
            time.sleep(0.2)
            keyboard.press_and_release('esc')
            time.sleep(0.2)
            break
        else:
            continue

     # Colocar Sniper
    while sniper is None:
        keyboard.press_and_release('z')
        pyautogui.moveTo(1082,430)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1.0)
        sniper = pyautogui.locateOnScreen('imagens/sniper.png', region=(region_sniper), confidence=0.7) 
        if sniper is not None:
            pyautogui.moveTo(1082,430)  
            time.sleep(0.5)
            keyboard.press_and_release(';')
            time.sleep(0.2)
            keyboard.press_and_release(';')
            time.sleep(0.2)
            keyboard.press_and_release(';')
            time.sleep(0.2)
            keyboard.press_and_release(';')
            time.sleep(0.2)
            keyboard.press_and_release('.')
            time.sleep(0.2)
            keyboard.press_and_release('.')
            time.sleep(0.2)
            keyboard.press_and_release('esc')
            time.sleep(0.2)
            break
        else:
            continue     

    # Colocar Alquimista
    while alquimista is None:
        keyboard.press_and_release('f')
        pyautogui.moveTo(1134,419)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1.0)
        alquimista = pyautogui.locateOnScreen('imagens/alch.png', region=(region_alch), confidence=0.7) 
        if alquimista is not None:
            pyautogui.moveTo(1134,419)  
            time.sleep(0.5)
            keyboard.press_and_release(',')
            time.sleep(0.2)
            keyboard.press_and_release(',')
            time.sleep(0.2)
            keyboard.press_and_release(',')
            time.sleep(0.2)
            keyboard.press_and_release(',')
            time.sleep(0.2)
            keyboard.press_and_release('.')
            time.sleep(0.2)
            keyboard.press_and_release('.')
            time.sleep(0.2)
            keyboard.press_and_release('esc')
            time.sleep(0.2)
            break
        else:
            continue       

    # Iniciar e colocar herói
    while iniciar is None:
        keyboard.press_and_release('u')
        pyautogui.moveTo(592,239)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(0.5)
        keyboard.press_and_release('space')
        time.sleep(0.5)
        keyboard.press_and_release('space')
        iniciar = pyautogui.locateOnScreen('imagens/comece.png', region=(region_comece), confidence=0.7) 
        if iniciar is not None:
            time.sleep(0.5)
            break
        else: 
            continue

    # Clicar na tela e Usar Hab
    while cliq is None:
        pyautogui.moveTo(603,21)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.0)
        pyautogui.click()
        keyboard.press_and_release('1')
        time.sleep(0.5)
        keyboard.press_and_release('2')
        time.sleep(1.0)
        cliq = pyautogui.locateOnScreen('imagens/cliq.png', region=(region_cliq), confidence=0.9) 
        if cliq is not None:
            pyautogui.moveTo(684,643)  
            time.sleep(0.5)
            pyautogui.click()           
            time.sleep(0.5)
            break
        else:
            continue
                                                    
    # voltar pro menu principal
    while reload is None:
        reload = pyautogui.locateOnScreen('imagens/reload.png', region=(region_reload), confidence=0.9) 
        if reload is not None:
            pyautogui.moveTo(510,605)  
            time.sleep(0.5)
            pyautogui.click()           
            time.sleep(3.5)
            break
        else:
            continue 

                                        
   

    

