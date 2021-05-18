import time

# start_position [118.094373, 24.614504]
import pyautogui as pag
position = []
if __name__ == '__main__':
    f = open('foo.txt', 'r+')
    data = [x.replace('\n', '').split(' ') for x in f.readlines()]
    f.close()
    position = []
    for line in data:
        position.append([eval(line[0]), eval(line[1])])
    index = 0
    cnt = 0
    time.sleep(5)
    while True:
        if index >= len(position):
            index = 0
        cnt += 1
        x = position[index][0]
        y = position[index][1]

        pag.moveTo(x, y)
        pag.click()

        if cnt == 1:
            time.sleep(1)
        if cnt == 2:
            time.sleep(4)
        if cnt == 3:
            time.sleep(1)
            cnt = 0
        index += 1
