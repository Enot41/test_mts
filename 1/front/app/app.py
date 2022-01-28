from flask import Flask, render_template, request
import requests
import socket

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
        if request.method == 'POST':
                        number_1 = int(request.form['number_1'])
                        number_2 = int(request.form['number_2'])
                        calc = number_1 + number_2
                        params = (
                        ('number_1', number_1),
                        ('number_2', number_2),
                        )
                        front_hostname = (socket.gethostname())
                        resp = requests.get('http://192.168.240.3:5000/calc', params=params)
                        back_calc = (resp.json())
                        hostname = requests.get('http://192.168.240.3:5000/hostname')
                        back_hostname = (hostname.text)
                        return render_template("index.html", calc = calc, back_calc = back_calc, back_hostname = back_hostname, front_hostname = front_hostname)

        elif request.method == 'GET':
                return render_template("index.html")
        return render_template("index.html", calc = calc)

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0')

