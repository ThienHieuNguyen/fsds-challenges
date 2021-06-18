from flask import Flask, request
from server_aux import verify_webhook, is_user_message, respond


FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'vd_bot'# <paste your verify token here>
PAGE_ACCESS_TOKEN = "EAAmETuRDoiwBAIwMo0FZAbouPi88Ai1ZATZC3cC4h4zjoZAP9dIWFsk5bDHZCd43wTXGuoNqwuzk9T3OoyuXh4JKmD3WxYofIDqShOoIZANH3ttMNAfm6CsjTaFAnthK3etEHj3ZCdHVZCnzjkiDgwFUTk7Wow8sh7bB1kdbv0ZAoTwZDZD"

app = Flask(__name__)


# route to listen and respond to Messenger
#https://vivabot.serveo.net/webhook
@app.route("/webhook", methods=['GET','POST'])
def listen():
    print("entering listen function")
    """This is the main function flask uses to listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        print("GET method")
        return verify_webhook(request, VERIFY_TOKEN)

    if request.method == 'POST':
        print("POST method")
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text, FB_API_URL, PAGE_ACCESS_TOKEN)

        return "ok"



# route to test that your flask app is running
#https://vivabot.serveo.net/test
@app.route("/test")
def test():
    return "Your messenger app is running"


# route to check the feedback of a specific query:
#https://vivabot.serveo.net/test_query?query=hello
@app.route("/test_query")
def test_query():
    sender_id = "admin"
    query = request.args.get('query', default = "", type = str)
    print("test_query", query)
    return respond(sender_id, query, FB_API_URL, PAGE_ACCESS_TOKEN)
