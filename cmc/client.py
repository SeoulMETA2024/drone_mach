import socketio

# Socket.IO 클라이언트 생성
sio = socketio.Client()

# 서버에 연결되었을 때
@sio.event
def connect():
    print("Connected to server")
    sio.send("Hello from client!")

# 서버로부터 메시지를 받았을 때
@sio.on('message')
def on_message(data):
    print(f"Message from server: {data}")

# 서버와 연결이 끊겼을 때
@sio.event
def disconnect():
    print("Disconnected from server")

# 서버에 연결
if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.wait()
