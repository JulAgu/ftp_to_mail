import pyautogui
import pyperclip
import time
from datetime import date

from globals import SRC_PATH, OUTPUT_PATH


def especial_string(string):
    pyperclip.copy(string)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy("")

def create_mail():
    pyautogui.click(x=1173, y=18)
    pyautogui.sleep(0.2)
    pyautogui.click(x=93, y=105)
    pyautogui.sleep(0.2)

def change_mail():
    pyautogui.click(x=138, y=227)
    pyautogui.sleep(0.2)
    pyautogui.click(x=160, y=297)
    pyautogui.sleep(0.2)
    pass

def create_contents(tuple_info):
    objet = "AGRILITY : Rapport de culture"
    message1 = "Bonjour " +  tuple_info[1] + ", \n\nVeuillez trouver ci-joint le rapport Agrility au " + date.today().strftime("%d/%m/%Y") +  " \n\nCordialement,\nLe service Agronomique"
    message2 = "Ceci est un message automatique, merci de ne pas y répondre. Au cas où vous auriez des questions, veuillez contacter t.patrier@agrial.com"
    return objet, message1, message2

# def redact_mail(src_path, tuple, objet, message1, message2):
def redact_mail(tuple_info, objet, message1, message2):
    # Write the mail
    pyautogui.click(x=242, y=265)
    pyautogui.sleep(0.5)
    especial_string(tuple_info[2])
    pyautogui.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.sleep(0.5)
    pyautogui.press("tab")
    pyautogui.sleep(0.5)
    especial_string("t.patrier@agrial.com")
    pyautogui.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.moveTo(x=207, y=354)
    pyautogui.sleep(0.5)
    pyautogui.click(x=207, y=354)
    pyautogui.sleep(0.5)
    especial_string(objet)
    pyautogui.sleep(0.5)
    pyautogui.click(x=52, y=383)
    pyautogui.sleep(0.5)
    especial_string(message1)
    pyautogui.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.hotkey('ctrl', 'g')
    pyautogui.write("------------\n")
    pyautogui.sleep(0.8)
    especial_string(message2)
    pyautogui.sleep(0.5)

def attach_file(tuple_info):
    pyautogui.click(x=739, y=102)
    pyautogui.sleep(0.5)
    parcourir = pyautogui.locateCenterOnScreen('src\parcourir_bouton.png', region=(640, 715, 1206, 910))
    pyautogui.moveTo(parcourir)
    pyautogui.sleep(0.2)
    pyautogui.click(parcourir)
    pyautogui.sleep(0.8)
    pyautogui.click(x=900, y=53, clicks=2)
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    especial_string(r"D:\HOMEdev\ftp_to_mail\compressed")
    pyautogui.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.click(x=292, y=969)
    pyautogui.sleep(0.2)
    especial_string(tuple_info[0])
    pyautogui.sleep(0.2)
    pyautogui.click(x=1746, y=992)
    pyautogui.sleep(1.5)

def send_mail():
    pyautogui.click(x=53, y=241)
    pyautogui.sleep(1)

print(pyautogui.position())

if __name__ == "__main__":
    # start = time.time()
    # create_mail()
    # change_mail()
    # objet, m1, m2 = create_contents((r"GAECdesPortesHellins_PDF_2024_09_03.pdf", "Jéan Dupont", "t.patrier@agrial.com"))
    # redact_mail((r"GAECdesPortesHellins_PDF_2024_09_03.pdf", "Jéan Dupont", "t.patrier@agrial.com"), objet, m1, m2)
    # attach_file((r"GAECdesPortesHellins_PDF_2024_09_03.pdf", "Jéan Dupont", "t.patrier@agrial.com"))
    # send_mail()
    # end = time.time()
    # print(end - start)
    pass