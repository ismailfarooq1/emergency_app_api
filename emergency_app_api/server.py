from flask import Flask, request
from flask_jsonpify import jsonify
from flask_restful import Resource, Api

from twilio.rest import Client

from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
api = Api(app)

# Twilio
account_sid = 'AC97e6c9c31b3524bb4e8ee5dfbc4a17b6'
auth_token = '7afa61880a41c451ddeedd378bbd6b69'
client = Client(account_sid, auth_token)

# class User(Resource):
#     @app.route('/users/get')
#     def get() :
#         if (request.args.get('id')) :
#             # 
#         else :
#             return False

#     @app.route('/users/post')
#     def post():
#         # 

#     @app.route('/users/put')
#     def put():
#         if (request.args.get('id')) :
#             # 
#         else :
#             return False

#     @app.route('/users/delete')
#     def delete():
#         if (request.args.get('id')) :
#             # 
#         else :
#             return False






class Twilio(Resource):
    @app.route('/send_sms')
    def send_sms():
        if(request.args.get('number')):
            number = request.args.get('number') 
            number = number[1:]
            number = '+92' + number
            print(number)
            message = client.messages \
                .create(
                    body="\nIsmail's API BITCHES 2!!!",
                    #  messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                    from_='+16467603049',
                    to=number
                )
            return {'message_sid' : message.sid}
        


if __name__ == '__main__':
    app.run(debug=True)
