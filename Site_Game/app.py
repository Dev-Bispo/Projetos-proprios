from flask import Flask, url_for,redirect,request,render_template

app = Flask(__name__) 

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    email = request.form.get(email)
    return render_template('login.html')

@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    render_template('cadsatro.html')

@app.route('/notificacoes', methods=['GET','POST'])
def notificacoes():
    render_template('notificacoes.html')  

@app.route('/configuracao', methods=['GET','POST'])
def configuracao():
    render_template('configuracao.html')