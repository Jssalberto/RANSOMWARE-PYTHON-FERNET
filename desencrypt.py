from cryptography.fernet import Fernet
import os

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(items, Key):
    f = Fernet(Key)
    for item in items:
        with open(item,'rb') as file: # With, Es la forma de abrir el fichero
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item,'wb') as file:
            file.write(decrypted_data)
        
if __name__ == '__main__':
    # Ruta de archivos objetivos a Decifrar
    Key = cargar_key()
    path_to_encrypt = '*:\\*****\\*************\\*******'
    os.remove(path_to_encrypt+'\\'+ 'Rescate.txt')
    if not 'Rescate.txt' in path_to_encrypt:
        with open(path_to_encrypt+'\\'+ 'Clave_Decifrado.txt', 'w') as file:
            file.write('Utiliza la clave de Decifrado\n')
            file.write(f"Tu clave es: {Key}")
    else:
        os.remove(path_to_encrypt+'\\'+ 'Rescate.txt')
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]
    decrypt(full_path, Key)