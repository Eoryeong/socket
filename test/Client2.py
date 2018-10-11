# import socket,sys
#
# HOST = '192.168.0.6'
# PORT = 8887
#
# c = socket.socket7(socket.AF_INET,socket.SOCK_STREAM)
# c.connect((HOST,PORT))
# print("환영합니다!")
# while 1:
#     data = input("Message : ")
#     c.send(data.encode('utf-8'))
#
#     data = c.recv(1024)
#     if not data: break
#
#     print("Received Message :", data.decode('utf-8'))
# c.close()