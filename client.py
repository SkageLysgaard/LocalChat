import socket
import threading



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5550))

print("connected...")

filename = input(str("Please enter a filename for the incoming file: "))
file = open(filename, "wb")
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been recieved succsessfully!")


