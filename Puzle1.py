#importacio de les llibreries necessaries per fer funcionar el perifric
import MFRC522
import signal
import time
#variable per indicar al perifric si ha de continuar llegint, inicialitzem a cert
continue_reading = True


#Funcio per llegir i converir el que li arriba en un string en format hexadecimial
def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = format(i, '02X') + mystring
    return mystring


#Funcio que posa a fals la variable global que diu si el periferic pot continuar llegint o no 
#si li arriba un Sigint (ctrl C)
def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False

# Si captura un SIGINT fa el end_read
signal.signal(signal.SIGINT, end_read)

# Crea un objecte de la classse MFRC522
MIFAREReader = MFRC522.MFRC522()

# Printga un missatge per començar a llegir
print("lector preparat, clica Ctrl-C per aturar l'execucio")

#Bucle per llegir tarjetes mentre la variable per llegir sigui certa
while continue_reading:
    # Busca tarjetes a prop
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    #Si l'estat es igual al mi_ok es que ha torbat una tarjeta
    if status == MIFAREReader.MI_OK: 
        #Aconsegeuix el UID de la tarjeta i l'estat
        (status, uid) = MIFAREReader.MFRC522_SelectTagSN()
        #Si encara esta la tarjeta i te el UID, el mostra per pantalla
        if status == MIFAREReader.MI_OK:
            print("Card read UID: %s" % uidToString(uid))
            
    time.sleep(0.5) #atura mig segon per donar temps a treure tarjeta

