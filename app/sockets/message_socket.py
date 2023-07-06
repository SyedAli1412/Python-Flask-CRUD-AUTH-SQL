from flask_socketio import Namespace
from app.models.models import Message
from app import socketio
from flask import request
class MessageSocket(Namespace):
    users = {}  # Maintaining the local object here for list of users


    @socketio.on('sign_in')
    def user_sign_in(data):
        print("Data:", data)
        MessageSocket.users[request.sid] = data.get('name')
        socketio.emit('current_users', MessageSocket.users)
        print('New User sign in!\The users are:', MessageSocket.users)

    @socketio.on('disconnect')
    def on_disconnect(self):
        MessageSocket.users.pop(request.sid, 'No user found')
        socketio.emit('current_users', MessageSocket.users)
        print("User disconnected!\nThe users are: ", MessageSocket.users)

    @socketio.on('message')
    def messaging(message):
        message['from'] = request.sid
        recipient_name = message['to']
        recipient_sid = None
        for sid, name in MessageSocket.users.items():
            if name == recipient_name:
                recipient_sid = sid
                break

        if recipient_sid:
            socketio.emit('message', message, room=request.sid)
            socketio.emit('message', message, room=recipient_sid)
            message_save = {'message': message['text'], 'sender_id': message['sender_id'],
                            'receiver_id': message['receiver_id']}
            print("Message:", message_save)
            message_to_save = Message(**message_save)
            return message_to_save.create()



