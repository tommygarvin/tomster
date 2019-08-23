# Import modules from packages
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from datetime import datetime

# Create an instance of web app
app = Flask(__name__)
api = Api(app)

# Messages dictionary
MESSAGES = {
    'message1': {'message': 'Any pizza can be a personal pizza'},
    'message2': {'message': 'Be excellent to each other'},
    'message3': {'message': 'Did you ever hear the Tragedy of Darth Plagueis the wise?'},
}

# Define function that will abort if not found
def abort_if_not_exist(message_id):
    if message_id not in MESSAGES:
        abort(404, message="message {} does not exist".format(message_id))

# Set parsing
parser = reqparse.RequestParser()
parser.add_argument('message')

# Class for organizing message list functions
class MessageList(Resource):
    def get(self):
        return MESSAGES

    def post(self):
        args = parser.parse_args()
        message_id = int(max(MESSAGES.keys()).lstrip('message')) + 1
        message_id = 'message%i' % message_id
        MESSAGES[message_id] = {'message': args['message']}
        return MESSAGES[message_id], 201

# Class for organizing message functions
class Message(Resource):
    def get(self, message_id):
        abort_if_not_exist(message_id)
        payload = MESSAGES[message_id]
        payload.update({'timestamp': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')})
        return payload

    def delete(self, message_id):
        abort_if_not_exist(message_id)
        del MESSAGES[message_id]
        return '', 204
    
    def put(self, message_id):
        args = parser.parse_args()
        message = {'message': args['message']}
        MESSAGES[message_id] = message
        return message, 201
        
# Health Check
@app.route('/')
def root():
    return "Health Check", 200
        
# Set the api resource routing
api.add_resource(MessageList, '/api/v1/messagelist')
api.add_resource(Message, '/api/v1/messages/<message_id>')

# Run the app and enable debug
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
