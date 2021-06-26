from flask import Flask, redirect, url_for, request, render_template
import requests
import json
from urllib.request import urlopen
app = Flask(__name__, template_folder= 'templates')
context_set = ""
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        val = str(request.args.get('text'))
        data = json.dumps({"sender": "Rasa","message": val})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
        res = res.json()
        val = res[0]['text']
    return val
    # return render_template('index.html', val=val)

@app.route('/data_news', methods=['GET', 'POST'])
def news():
    url = request.args.get('url')
    print(url)
    response = urlopen(url)
    data_json = json.loads(response.read())
    print(data_json)
if __name__ == '__main__':
  app.run(debug=True)