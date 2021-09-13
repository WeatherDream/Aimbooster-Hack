from screen_search import *
import pyautogui
import keyboard


while True:
    if keyboard.is_pressed("o"):
        while True:
            if keyboard.is_pressed("i"):
                print("Stopped")
                break

            search = Search("pic.png")

            pos = search.imagesearch()

            if pos[0] != -1:
                print("position : ", pos[0], pos[1])
                pyautogui.click(x=pos[0], y=pos[1])
            else:
                print("image not found")

