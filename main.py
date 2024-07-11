from pynput import keyboard as kb
import interaz
import pyautogui
from ocr import ocr
# bxs = pytesseract.image_to_boxes("demo.png")

# for _,x in enumerate(bxs.split("\n")):
#     print((x + str(_))  )


def run():
    # time.sleep(2)
    image = pyautogui.screenshot()
    image.save("scr.png")
    interaz.show("scr.png")



def pulsa(tecla):
	if (str(tecla) == "'c'"): run()
		

with kb.Listener(pulsa) as escuchador:
	escuchador.join()