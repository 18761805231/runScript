import pythoncom, PyHook3

position = []


def onMouseEvent(event):
    print("Position:", event.Position)
    position.append([event.Position[0], event.Position[1]])
    return True

def save(event):
    f = open('foo.txt', 'w')
    for i in position:
        f.write(str(i[0])+' '+str(i[1])+'\n')
    f.close()
    return True

def main():
    hm = PyHook3.HookManager()
    hm.HookKeyboard()
    hm.MouseAllButtonsDown = onMouseEvent
    hm.MouseRightDown = save
    hm.HookMouse()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
