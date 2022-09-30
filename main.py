from email import message
import sys,time,os
from twilio.rest import Client 
import flask
import os
from flask import send_from_directory,render_template, request, redirect, url_for
from flask_wtf import Form

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    telephone = request.args.get('telephone')
    sms_message = request.args.get('message')
    if telephone!=None and sms_message!=None:
        account_sid = 'AC110b053229169c1d12b2778af7f24ae1' 
        auth_token = '1fe21396471a8d2738a135f35fe36e3f' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create( 
                                    from_='+14422495091', 
                                    messaging_service_sid='MG81689e51f15d3f45aac3fe9be0ca0703', 
                                    body=str(sms_message),      
                                    to="+"+str(telephone)
                                ) 
        
        print(message.sid)
        print (str(telephone))
        return "Message sent Successfully\n"+ str(message.sid) 
    else:
        return "Invalid Telephone and message GET values"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
"""
telephone = sys.argv[1]
account_sid = 'AC110b053229169c1d12b2778af7f24ae1' 
auth_token = 'ef7300dea18a795e9757eaae69b63165' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+14422495091', 
                              messaging_service_sid='MG81689e51f15d3f45aac3fe9be0ca0703', 
                              body='Test Message',      
                              to=telephone 
                          ) 
 
print(message.sid)
"""