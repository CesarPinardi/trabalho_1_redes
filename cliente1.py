import json
import socket
from datetime import datetime
from traceback import print_tb
import time

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

ip_dest = input("IP do servidor: ")

msgFromClient = input("Mensagem para o servidor: ")

port = 20001

ip = "192.168.0.11"

serverAddressPort = (ip_dest, port)

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


print((json.dumps(json_server.get("received"), indent= len(json_server.get("received")))))
ack = json_server.get("received").get("ACK")
print(ack)

# como pegar outro JSON no mesmo request
while time.sleep(10):
    if ack == "true":

        print("Mensagem esperando servidor: ")


        print((json.dumps(json_server.get("send"), indent= len(json_server.get("send")))))




print("\n")

