import json
import socket
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

msgFromClient = input("Mensagem para o servidor: ")

ip = "127.0.0.1"

port = 20001

serverAddressPort = (ip, port)

ip_dest = "127.0.0.1"

port_dest = 20001

json_envio = {}

json_envio ['info_to_sent'] = {'ip_origem': ip, 
                            'ip_destino': ip_dest, 
                            'porta_origem': port, 
                            'porta_destino': port_dest, 
                            'timestamp': current_time, 
                            'msg': msgFromClient}

bytesToSend = str.encode(json.dumps(json_envio))

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 
msg = "Mensagem do servidor: {}".format(msgFromServer[0].decode())

print(msg)
