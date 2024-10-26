import socket
import secrets
from Crypto.Cipher import Salsa20

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}...")

# Aceptar conexión de cliente
conn, addr = server_socket.accept()
print(f"Conexión establecida con {addr}")

# Generar una llave simétrica de 256 bits
symmetric_key = secrets.token_bytes(32)
print(f"Llave simétrica generada: {symmetric_key.hex()}")

# Enviar la llave al cliente
conn.sendall(symmetric_key)

# Recibir el nonce y el mensaje cifrado del cliente
nonce = conn.recv(8)  # Salsa20 usa un nonce de 8 bytes
ciphertext = conn.recv(1024)

# Crear el cifrador Salsa20 con la llave y el nonce recibido
cipher = Salsa20.new(key=symmetric_key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print(f"Mensaje recibido descifrado: {plaintext.decode('utf-8')}")

# Cerrar conexión
conn.close()
