from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://s3.amazonaws.com/rapgenius/cats-animals-kittens-background.jpg">
    """
    return html.format(name.title())
    
@app.route("/jedi/<first>/<last>")
def jedi_name_html(first,last):
    jedi_name = last[:3] + first[:2]
    
    html = """
    <p>
        Your jedi name is {}.
    
    </p>
    """
    
    return html.format(jedi_name.title())



if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))