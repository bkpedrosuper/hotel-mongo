from flask import render_template
from factory import config_app, register_routes
from flask_pymongo import PyMongo

app, db, mongo = config_app()
app = register_routes(app)

@app.route('/')
def initiate():  # put application's code here
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
