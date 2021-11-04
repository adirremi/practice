import getpass
from flask import Flask, request



app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/home', methods=['GET'])
def home():

    username = getpass.getuser()
    print(username)
    return "<h1>User Computer Name</h1><p>{username}.</p>".format(username=username)



app.run(host="0.0.0.0", port=5001, debug=True)



print("adi")



