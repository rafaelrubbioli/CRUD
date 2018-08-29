from flask import Flask, abort, render_template, request
from User import *

app = Flask(__name__)
db = User()
db.add_user('rafael', 'rafael@123', 12341234, 'rua avenida', ['feliz', 'divertido'])
db.add_user('fernanda', 'fernanda@123', 12341234, 'rua avenida')
db.add_user('marquito', 'marquito@123', 12341234, 'rua avenida')
db.add_user('rafael rubbioli', 'rafaelr@123', 12341235, 'rua avenida')
db.add_user('rafael da silva', 'rafaels@123', 12341236, 'rua avenida')


# pagina inicial
@app.route('/')
def index():
	return render_template('index.html', users = db, id = 0)

@app.route('/create/', methods = ['POST', 'GET'])
def add():
	if request.method == 'POST':
		result = request.form.to_dict()
		db.add_user(result['name'], result['email'], result['phone'], result['address'], [result['tag']])
		return render_template('add.html')
	else:
		return render_template('create.html')

@app.route('/edit/<int:id>')
def edit(id):
	return render_template('edit.html', id = id)

# pagina de perfil do usuario
@app.route('/user/<int:id>/', methods = ['POST', 'GET'])
def profile(id):
	if request.method == 'POST':
		result = request.form.to_dict()
		if result['name']:
			db.users[id]['name'] = result['name']
		if result['email']:
			db.users[id]['email'] = result['email']
		if result['phone']:
			db.users[id]['phone'] = result['phone']
		if result['address']:
			db.users[id]['address'] = result['address']
		if len( result['tag'] ) != 0 and result['tag'] not in db.users[id]['tags']:
			db.users[id]['tags'].append(result['tag'])
	if db.users.get(id):
		return render_template('profile.html', user = db.users.get(id), id = id)
	else:
		return abort(404, "Usuario nao encontrado")

# pagina de resultados da busca
@app.route('/result/',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form.to_dict()
		found = db.search_user(name = result['name'], email = result['email'], tags = result['tag'])
		return render_template('result.html',result = found, users = db)

app.run(debug = True)
