from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
     __tablename__ = 'usuario'
    
     id = db.Column(db.Integer, primary_key=True)
     email = db.Column(db.String(120), unique=True, nullable=False)
     password = db.Column(db.String(80), unique=False, nullable=False)
     name = db.Column(db.String(250), nullable=False)
     favoritousuario = db.relationship('Favorito', backref='usuario', lazy=True)

     def __repr__(self):
        return '<User %r>' % self.id

     def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            # "favorito_id": self.favorito_id,
            "favoritousuario": self.favoritousuario
            # do not serialize the password, its a security breach
        }

class Personaje(db.Model):
    __tablename__ = 'personaje'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    favoritopersonaje = db.relationship('Favorito', backref='personaje', lazy=True)

    
    def __repr__(self):
        return '<Personaje %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "favoritopersonaje": self.favoritopersonaje
        }

class Planeta(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    favoritoplaneta = db.relationship('Favorito', backref='planeta', lazy=True)

    
    def __repr__(self):
        return '<Planeta %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # "favoritoplaneta": self.favoritoplaneta
        }

class Favorito(db.Model):
    __tablename__ = 'favorito'
    id = db.Column(db.Integer, primary_key=True)
    personaje_id = db.Column(db.Integer,  db.ForeignKey('planeta.id'),nullable=True)
    planeta_id = db.Column(db.Integer,  db.ForeignKey('personaje.id'),nullable=True)
    usuario_id = db.Column(db.Integer,  db.ForeignKey('usuario.id'),nullable=False)

    
    def __repr__(self):
        return '<Favorito %r>' % self.id

    def serialize(self):
        query_planeta=Planeta.query.filter_by(id=self.planeta_id).first()
        query_personaje=Personaje.query.filter_by(id=self.personaje_id).first()

        return {
            "id": self.id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            "info_planeta":query_planeta.serialize(),
            "imfo_personaje":query_personaje.serialize(),
            "usuario_id": self.usuario_id
        }