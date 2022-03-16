from email.policy import default
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)
load_dotenv()

print(os.getenv('DATABASE_URL'))

app.config.update(
    SECRET_KEY = 'mysecret',
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(app)

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return 'The id is {}, name is {}'.format(self.id, self.name)

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    #Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id')) 

    def __init__(self, title, author,avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self) -> str:
        return '{} by {}'.format(self.title, self.author)
        
@app.route('/')
def root():
    return 'Hello Flask'

@app.route('/new/')
def query_string(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </>'.format(name)

# strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'


# rendering templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

movie_list = ['Perfume', 'Back to the Future', 'Matrix','Batman','Rey leon']
movies_dict = {'spiderman': 5.7,
    'King Kong': 0.25,
    'Jumanjy': 1.89,
    'Beaty & Beast': 7.1,
    'The Mask': 3.5,
    'Bodyguard': 2.1,
    'Titanic': 4.2,
    'Superman': 2.9}

#Jinja templates
@app.route('/watch')
def top_movies():
    return render_template('movies.html', movies=movie_list,name = 'George')

@app.route('/tables')
def movies_plus():
    return render_template('table_data.html', movies=movies_dict,name='Melissa')

@app.route('/filters')
def filter_data():
    return render_template('filter_data.html', movies=movies_dict, name=None, film=' a christmas for melissa')

@app.route('/macros')
def jinja_macros():
    return render_template('using_macros.html', movies=movies_dict)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)