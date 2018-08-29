class User:

	def __init__(self):
		# dicionario { ID : {atributos} }
		self.users = {}
		# contador de ID
		self.id = 0


	# adicionar usuarios
	def add_user(self, name, email, phone, address, tags = []):
		self.id = self.id + 1
		self.users[self.id] = {'name' : name, 'email' : email, 'phone' : phone, 'address' : address, 'tags' : tags}

	# buscar usuarios
	def search_user(self, id = 0, name = '', email = '', tags = ''):
		found = []
		#busca por ID
		if id != 0:
			found.append(id)

		# busca por nome
		if name != '':
			for uid, uatt in self.users.items():
				if name in uatt['name']:
					found.append(uid)

		# busca por email
		if email != '':
			for uid, uatt in self.users.items():
				if email in uatt['email']:
					found.append(uid)

		# busca por tags
		if tags:
			for uid, uatt in self.users.items():
				if tags in uatt['tags']:
					found.append(uid)
		return found

	def del_user(self, id):
		del self.users[id]
