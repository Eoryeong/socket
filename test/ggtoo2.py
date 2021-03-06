import socket, sys, math
import socketserver
import threading

HOST = '192.168.0.6'
PORT = 7777
lock = threading.Lock() # syncronized 동기화 진행하는 스레드 생성
                        # 1 채팅 서버로 입장한 사용자의 등록
                        # 2 채팅을 종료하는 사용자의 퇴장 관리
                        # 3 사용자가 입장하고 퇴장하는 관리
                        # 4 사용자가 입력한 메세지를 채팅 서버에 접속한 모두에게 전송

class UserManager: # 사용자관리 및 채팅 메세지 전송을 담당하는 클래스

    def __init__(self):
        self.users = {} # 사용자의 등록 정보를 담을 사전 {사용자 이름 : (소켓, 주소)...

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('이미 등록된 사용자입니다.\n'.encode())
            return None

        # 새로운 사용자를 등록함
        lock.acquire() # 스레드 동기화를 막기위한 락
        self.users[username] = (conn, addr)
        lock.release() # 업데이트 후 락 해제

        self.sendMessageToAll('[%s]님이 입장했습니다.' %username)
        print('+++ 대화 참여 수 [%d]' %len(self.users))

        return username
    def removeUser(self, username): # 사용자를 제거하는 함수
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll('[%s]님이 퇴장했습니다.' %username)
        print('--- 대화 참여자 수 [%d]' %len(self.users))

    def messageHandler(self, username, msg): # 전송한 msg를 처리하는 부분
        if msg[0] !='/': # 보낸 메세지의 첫문자가 '/'가 아니면
            self.sendMessageToAll('[%s] %s' %(username, msg))
            return
        
        if msg.strip() == '/quit' : # 보낸 메세지가 'quit'이면
            self.removeUser(username)
            return -1
        
    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())
            
class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()
    
    def handle(self): # 클라이언트가 접속시 클라이언트 주소 출력
        print('[%s] 연결됨' %self.client_address[0])
        
        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        
        except Exception as e:
                print(e)
        print('[%s] 접속종료' %self.client_address[0])
        self.userman.removeUser(username)
        
    def registerUsername(self):
        while True:
            self.request.send('로그인ID:'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username
            
class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():
    print('+++ 채팅 서버를 시작합니다.')
    print('+++ 채팅 서버를 끝내려면 Ctrl-C를 누르세요.')
    
    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 채팅서버를 종료합니다.---')
        server.shutdown()
        server.server_close()
        
runServer()
        
        
# def string_xor(data, key):
#     j = 0 
#     result = ''
#
#     for i in range(len(data)):
#         result += chr(ord(data[i]) ^ ord(key[j]))
#         j += 1
#         if (j == len(key)):
#             j = 0
#         return result

# key = "password"
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 7777))
# s.listen(1)
#
# print('Socket Listen Start')
#
# connector, addr = s.accept()
#
# print("누군가가 들어왔습니다.")
# while 1:
#     data = connector.recv(1024)
#     if not data: break
#
#     # decryptMessage = string_xor(data.decode('utf-8'), key)
#     print("Received Message :", data.decode('utf-8'))
#
#     data = input("Message : ")
#     # encryptMessage = string_xor(data, key)
#     connector.send(data.encode('utf-8'))
#
# s.close()
