import threading
import socket 


host = "localhost" 
port = 5550
server.bind((host, port))

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.listen()
print("host")
print("Waiting for ant incomming connections...")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str("please enter the filename of the file: "))
file = open(filename , "rb")
file_data = file.read(1024)
conn.send(file_data)
print("Data has been sendt successfully!")
