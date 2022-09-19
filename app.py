from flask import Flask
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World CS298- Nick !"

  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)

@app.route('/loop')
def bigLoop():
    that_string = ""
    for num in range(200):
        that_string += "Hello!\n"
    return that_string

if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)
    
