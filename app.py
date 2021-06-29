from flask import Flask, redirect, url_for, request, render_template
import requests
import json
from urllib.request import urlopen
app = Flask(__name__, template_folder= 'templates')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    dataBody=request.json
    for data in dataBody:
        try:
            val= data["message"]
            data = json.dumps({"sender": "Rasa","message": val})
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
            res = res.json()
            val = res[0]['text']
            return val
        except Exception:
            print("An exception occurred")
if __name__ == '__main__':
  app.run(debug=True)