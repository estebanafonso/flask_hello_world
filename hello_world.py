from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"


@app.route("/hello/<name>")
def name_page(name):
    name = name.title()
    return render_template('template.html', page_name=name)

@app.route("/jedi/<first>/<last>")
def jedi_name_html(first,last):
    jedi_name = last[:3] + first[:2]
    jedi_name = jedi_name.title()
    
    return render_template('jedi_template.html', jedi_name=jedi_name)
    


'''
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            '''
            
if __name__ == '__main__':
    print("Hello, world!")
    app.run(debug=True, host="0.0.0.0", port=8080)