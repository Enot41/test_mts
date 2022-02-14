from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/calc')
def query_example():
    # if key doesn't exist, returns None
    number_1 = int(request.args.get('number_1'))
    number_2 = int(request.args.get('number_2'))
    number = number_1 + number_2
    return format(number)
@app.route('/hostname')
def hostname():
    hostname = (socket.gethostname())
    return format(hostname)
if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0')
