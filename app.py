import os
from flask import Flask
# if local env. import env.py, otherwise not
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Michael"


# 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
            # don't forget to change debug = false later onwards, when testing is complete