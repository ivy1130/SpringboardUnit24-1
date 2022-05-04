from app import app
from models import db, Pet

# Create all tables
db.drop_all()
db.create_all()

# If tables aren't empty, empty them
Pet.query.delete()

# Add sample data
cutie = Pet(name='Cutie', species='dog', photo_url='https://www.rd.com/wp-content/uploads/2020/06/GettyImages-185330333-edit.jpg')
spine = Pet(name='Spine', species='porcupine', photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Crazy_eyes_the_porcupine.jpg/1920px-Crazy_eyes_the_porcupine.jpg')

# Add new objects to session
db.session.add_all([cutie, spine])

# Commit
db.session.commit()