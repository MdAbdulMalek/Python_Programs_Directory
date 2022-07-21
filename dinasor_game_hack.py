import pyautogui 
from PIL import Image, ImageGrab
import time


def press_key(key):
    pyautogui.keyDown(key)
    return

def find_location(data):
    for i in range(640, 655):
        for j in range(530, 560):
            if data[i, j] < 100:
                press_key("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        find_location(data)
            
        # print(asarray(image))
        
        # Draw the rectangle for cactus
        # for i in range(620, 635):
        #     for j in range(530, 560):
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(250, 300):
        #     for j in range(410, 563):
        #         data[i, j] = 171

        # image.show()
        # break
      
