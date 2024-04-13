from flask import Flask
from views import book_blueprint
from database import db
from models import Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/postgres'

db.init_app(app)

app.register_blueprint(book_blueprint)


def init_db():
    db.create_all()
    # Add your books here
    books = [
        {'name': 'Pride and Prejudice', 'author': 'Jane Austen',
         'description': 'A classic novel of manners, it follows the development of Elizabeth Bennet, the protagonist, as she deals with issues of manners, upbringing, morality, education, and marriage in the society of the landed gentry of early 19th-century England.',
         'book_count': 10},
        {'name': '1984', 'author': 'George Orwell',
         'description': 'A dystopian novel set in Airstrip One, formerly Great Britain, a province of the superstate Oceania, in a world of perpetual war, omnipresent government surveillance, and public manipulation.',
         'book_count': 15},
        {'name': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky',
         'description': 'A novel by the Russian author Fyodor Dostoevsky. It was first published in the literary journal The Russian Messenger in twelve monthly installments during 1866.',
         'book_count': 7},
        {'name': 'Hamlet', 'author': 'William Shakespeare',
         'description': 'The tragedy of Hamlet, Prince of Denmark, often shortened to Hamlet, is a tragedy written by William Shakespeare sometime between 1599 and 1601.',
         'book_count': 5},
        {'name': 'One Hundred Years of Solitude', 'author': 'Gabriel García Márquez',
         'description': 'An acclaimed novel by Gabriel García Márquez that tells the multi-generational story of the Buendía family, whose patriarch, José Arcadio Buendía, founded the town of Macondo.',
         'book_count': 12},
        {"name": "Scaling Up", "author": "Verne Harnish",
         "description": "How a Few Companies Make It...and Why the Rest Don't", "book_count": 10},
        {"name": "Foundations of Scalable Systems Designing Distributed Architectures", "author": "Ian Gorton",
         "description": "Designing Distributed Architectures", "book_count": 7},
        {"name": "The Art of Scalability", "author": "Martin L. Abbott and Michael T. Fisher",
         "description": "Scalable Web Architecture, Processes, and Organizations for the Modern Enterprise",
         "book_count": 5},
        {"name": "The DevOps Handbook", "author": "Gene Kim, Jez Humble, Patrick Debois, and John Willis",
         "description": "How to Create World-Class Agility, Reliability & Security in Technology Organizations",
         "book_count": 15},
        {"name": "Effective DevOps", "author": "Jennifer Davis and Ryn Daniels",
         "description": "Building a Culture of Collaboration, Affinity, and Tooling at Scale", "book_count": 20},
        {"name": "The Phoenix Project", "author": "Gene Kim, Kevin Behr, and George Spafford",
         "description": "A Novel About IT, DevOps, and Helping Your Business Win", "book_count": 30},
        {"name": "Mastering Bitcoin", "author": "Andreas Antonopoulos",
         "description": "Unlocking Digital Cryptocurrencies", "book_count": 25},
        {"name": "The Internet of Money, Volumes 1 - 3", "author": "Andreas Antonopoulos",
         "description": "A collection of talks about why Bitcoin matters on a global scale", "book_count": 18},
        {"name": "Blockchain Revolution", "author": "Don Tapscott and Alex Tapscott",
         "description": "How the Technology Behind Bitcoin Is Changing Money, Business, and the World",
         "book_count": 12},
        {"name": "Big Data: A Revolution That Will Transform How We Live, Work, and Think",
         "author": "Viktor Mayer-Schönberger and Kenneth Cukier",
         "description": "A look at the future of data-driven innovation", "book_count": 22},
        {"name": "Big Data: Concepts, Technology and Architecture", "author": "Lakshmana Kumar Ramasamy and Firoz Khan",
         "description": "A comprehensive guide to big data concepts, technologies, and applications", "book_count": 14},
        {"name": "The Truth Machine", "author": "Paul Vigna and Michael J. Casey",
         "description": "The Blockchain and the Future of Everything", "book_count": 16},
        {"name": "The God of Small Things", "author": "Arundhati Roy",
         "description": "The story of the tragic and forbidden love between the young and beautiful Rahel and the charming and enigmatic Velutha.",
         "book_count": 10},
        {"name": "A Fine Balance", "author": "Rohinton Mistry",
         "description": "A gripping story of four unlikely people whose lives come together during a time of political turmoil soon after the government declares a 'State of Internal Emergency'.",
         "book_count": 8},
        {"name": "The White Tiger", "author": "Aravind Adiga",
         "description": "A darkly humorous perspective of India’s class struggle in a globalized world as told through a retrospective narration from Balram Halwai, a village boy.",
         "book_count": 12},
        {"name": "Midnight’s Children", "author": "Salman Rushdie",
         "description": "A novel of magical realism that explores India's transition from British colonialism to independence and the partition of India.",
         "book_count": 7},
        {"name": "The Namesake", "author": "Jhumpa Lahiri",
         "description": "An exploration of the themes of cultural identity, immigrant isolation, love and marriage from the perspective of Gogol Ganguli, a young man of Indian-American descent.",
         "book_count": 9},
        {"name": "A Suitable Boy", "author": "Vikram Seth",
         "description": "A panoramic tale of post-independence India that explores the intertwining lives of four large families and the protagonist, Lata's search for a suitable boy for marriage.",
         "book_count": 6},
        {"name": "Malgudi Days", "author": "R.K. Narayan",
         "description": "A collection of short stories by R.K. Narayan set in the fictional town of Malgudi.",
         "book_count": 15},
        {"name": "The Inheritance of Loss", "author": "Kiran Desai",
         "description": "A novel set in the Himalayas, New York City, and Cambridge, exploring the lives of characters affected by the Nepalese insurgency.",
         "book_count": 11}

    ]
    # Check if the database is empty
    if Book.query.first() is None:
        for book in books:
            db.session.add(Book(**book))
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
