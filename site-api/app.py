from flask import Flask

app = Flask("Test")

@app.route("/")
def hello():
    return "HELLO WORLD\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
