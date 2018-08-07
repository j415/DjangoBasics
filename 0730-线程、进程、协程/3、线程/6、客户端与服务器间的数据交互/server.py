import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.105', 8000))
server.listen(5)


def run(ck):
    data = clientSocket.recv(1024)
    print("客户端说：" + data.decode('utf-8'))
    # sendData = input("输入返回给客户端的数据")
    clientSocket.send("aspiring  jianchibuxie".encode('utf-8'))

print("服务器启动成功，等待客户端的连接")
while True:
    clientSocket, clientAddress = server.accept()

    t= threading.Thread(target=run, args=(clientSocket,))
    t.start()