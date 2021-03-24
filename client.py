from socket import create_connection
import threading

nickname = input("Choose a nickname: ")
client = create_connection(("localhost", 5550))

#the old way:
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("localhost", 5550))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                pass
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start() 
