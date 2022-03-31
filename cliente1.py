import json
import socket
from datetime import datetime
from traceback import print_tb

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

#criando o udp socket do client

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#mandando para o servidor usando udp socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
 
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#transformar message para string
msgFromServer_tostring = msgFromServer[0].decode()

#transformar message para json
json_server = json.loads(msgFromServer_tostring)

# print("\nMensagem recebida pelo servidor as: " + json_server.get("received").get("timestamp_msg_original"))

# print("\nMensagem enviada ao servidor as: " + json_server.get("received").get("timestamp_msg_resposta"))

# print("\nMensagem: " + json_server.get("received").get("mensagem_servidor"))

# printando o json inteiro recebido

print((json.dumps(json_server.get("received"), indent= len(json_server.get("received")))))

print("\n")

