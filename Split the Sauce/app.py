from flask import Flask
from flask import request
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import re
import requests

app = Flask(__name__)

@app.errorhandler(404)
def notfound(e):
	return index()

@app.route('/robots.txt', methods=['GET','POST'])
def robots():
	return "User-agent: * <br><br> Disallow: /login <br> &ensp;&ensp;&ensp;&ensp;&ensp; &ensp;&ensp;&ensp;&ensp;/flag"

@app.route('/flag', methods=['GET','POST'])
def flag(data="Lol, this is not that much easier"):
	return data

@app.route('/', methods=['GET', 'POST'])
def index():
	try:
		if dict(request.headers)['Transfer-Encoding'] == "chunked" :
			headers=str(request.stream.read(2048),"latin-1")
			headers = headers.splitlines()
			for i in headers:
				if i.find("GET")==-1 and i.find("POST")==-1:
					headers.pop(headers.index(i))
				else:
					break
			header=[head for head in headers if head != ""]
			url = header[0].split()[2].split("/")[0].lower()+"://"+header[1].split(":",1)[1].strip()+header[0].split()[1]
			headers={head.split()[0].strip():head.split()[1].strip() for head in header[1:] }
			print(url)
			if "/flag" in url:
				return flag("dc9111{y0U_G0t_Th4t_$0y_S4uC3}")
			return requests.get(url,headers=headers,verify=False)
	except:
		pass
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Kudos, Great Job XDDD"
		
@app.route('/login', methods=['GET','POST'])
def do_admin_login():
	if request.method == "POST":
		if request.form['password'] != '' and request.form['username'] != '':
			session['logged_in'] = True
	return index()

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=45054)
