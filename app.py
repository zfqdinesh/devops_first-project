from flask import Flask

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/")
def show():
    return "<p>hello ia m dinesh here .....</p>"


if __name__ == '__main__':  
   app.run(host="0.0.0.0" , port=5000)  
