#Importo las librerias necesarias
import MFRC522
import signal
import time

class RFIDReader:
    #constructor de la clase
    def __init__(self):
        # Inicializamos el lector RFID y la variable para continuar la lectura
        self.reader = MFRC522.MFRC522()
        self.continue_reading = True
        print("Lector preparado, presiona Ctrl-C para detener la ejecucion.")

        # Configuramos la seÃ±al de interrupcion para terminar la lectura
        signal.signal(signal.SIGINT, self.end_read)

    # Metodo para convertir el UID en un string hexadecimal en el orden correcto
    def uid_to_string(self, uid):
        mystring = ""
        for i in uid:
            mystring += format(i, '02X') 
        return mystring

    # Metodo que se ejecuta al recibir una seÃ±al de interrupcion (Ctrl+C)
    def end_read(self, signal, frame):
        self.continue_reading = False
        print("Ctrl+C capturado, terminando lectura.")

    # Metodo principal para realizara la lectura de las tarjetas
    def lectura(self):
        uid_hex=None #variable que devuelve el uid en hexadecimal
        if self.continue_reading:
            # Busca tarjetas cercanas
            (status, TagType) = self.reader.MFRC522_Request(self.reader.PICC_REQIDL)

            # Si se encuentra una tarjeta, intenta leer el UID
            if status == self.reader.MI_OK:
                (status, uid) = self.reader.MFRC522_SelectTagSN()
                
                # Si el UID se obtiene correctamente, lo guardo en variable
                if status == self.reader.MI_OK:
                    uid_hex=self.uid_to_string(uid)
            
            time.sleep(0.2)  # Pausa para dar tiempo a retirar la tarjeta
        return uid_hex #retorno el uid 

# Bloque principal de ejecucion
if __name__ == "__main__":
    rfid_reader = RFIDReader() #Creo objeto de la clase
    rfid_reader.lectura() #Ejecuta el metodo lectura
