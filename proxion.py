from flask import Flask,request
import requests as re
import urllib.parse


app=Flask(__name__)

site = 'https://google.com'
@app.route('/')
def index():
	m = request.args.to_dict()
	return re.get(site,headers={'User-Agent': request.headers.get('User-Agent')}, params = m).text

@app.route('/<path:p>',methods=['POST','GET','HEAD'])
def index2(p):
	return re.get(site + '/' + p).text

app.run(debug=True)