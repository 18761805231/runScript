import PyHook3
import win32gui
import pythoncom
import time

# start_position [118.094373, 24.614504]
import pyautogui as pag

position = []
fo = open("foo.txt", "w")

if __name__ == "__main__":
    while True:
        time.sleep(5)
        x, y = pag.position()
        # if x > 1800:
        #     fo.close()
        #     break
        print(x, ' ', y)
        fo.write(str(x)+' '+str(y)+'\n')
