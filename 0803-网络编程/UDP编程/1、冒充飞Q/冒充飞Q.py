"""

TCP 是建立可靠的的连接,并且通信双方都可以以流的形式发送数据。相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包。但是能不能到达就不知道了。

虽然UDP传输数据不可靠，但它的优点是和TCP相比，速度快，对于要求不高的数据可以使用UDP

"""
# ----------------------------------------------------------不可行

import socket
import time


str = "aspiring"

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect(('192.168.0.105', 2425))
udp.send(str.encode("uft-8"))
#
# while True:
#     udp.send("aspiring send a message".encode('utf-8'))
#     time.sleep(1)
#
#
#























