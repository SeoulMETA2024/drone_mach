import socketio

# 비동기 서버를 위한 Socket.IO 서버 생성
sio = socketio.Server(async_mode='threading')
app = socketio.WSGIApp(sio)

# 클라이언트가 연결되었을 때
@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")

# 클라이언트가 메시지를 보냈을 때
@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    # 클라이언트에게 메시지 응답
    sio.send(sid, "Hello from server!")

# 클라이언트가 연결을 끊었을 때
@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")

# 서버 실행
if __name__ == '__main__':
    from eventlet import wsgi
    import eventlet
    print("Starting Socket.IO server on port 5000")
    wsgi.server(eventlet.listen(('', 5000)), app)
