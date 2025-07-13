from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/youtube")
def youtube():
    return render_template("youtube.html")

@app.route("/netflix")
def netflix():
    return render_template("netflix.html")

@app.route("/love")
def love():
    return render_template("love.html")

@app.route("/jio_mart")
def smart_mart():
    return render_template("smart_mart.html")

@app.route("/fillif")
def fitlif():
    return render_template("fitlif.html")

@app.route("/health")
def health():
    return render_template("health.html")







if __name__ == '__main__':  
   app.run(host="0.0.0.0" , port="5000")  
