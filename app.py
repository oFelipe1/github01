from flask import Flask, render.template
app = Flask('__name__')

@app.route(/)
def index( ):
    return render.template(index.html)


