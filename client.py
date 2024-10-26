import socket
from Crypto.Cipher import Salsa20

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 65432

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((HOST, PORT))
print("Conectado al servidor")

# Recibir la llave simétrica del servidor
symmetric_key = client_socket.recv(32)
print(f"Llave simétrica recibida: {symmetric_key.hex()}")

# Mensaje a enviar
message = "Hola, servidor. Este es un mensaje cifrado con Salsa20."

# Crear el cifrador Salsa20 con la llave y un nonce aleatorio
cipher = Salsa20.new(key=symmetric_key)
ciphertext = cipher.encrypt(message.encode('utf-8'))

# Enviar el nonce y el mensaje cifrado al servidor
client_socket.sendall(cipher.nonce)
client_socket.sendall(ciphertext)

# Cerrar conexión
client_socket.close()
