from flask import Flask 
app = Flask(__name__)

app.route('/' ,methods=['GET'])
def show():
    return "hello world dinesh is here ...."

if __name__=="__main__":
          app.run()
