from flask import Flask
import base64

app = Flask(__name__)

@app.route("/")
def GET_hello():

    return 'hello'

@app.route("/commanderEd")
def GET_cmd():
    with open('command','r') as ifile:
        message = ifile.read()
    return message

@app.route("/robotcommand/<path:subpath>")
def waiting(subpath):

    with open('command','w') as ofile:
        ofile.write(subpath)
    return ""

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=80)
