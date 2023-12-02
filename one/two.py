from flask import Flask
from flask import render_template


app=Flask(__name__)
@app.route('/')
def home():
    
    return render_template('home.html')



@app.route('/add')
def add():
    return render_template ("add.html")


@app.route('/list')
def wow():
    return render_template ("list.html")



if __name__=="__main__":
    app.run()