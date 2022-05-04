from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
# app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ughhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

@app.route('/')
def show_home_page():
    """Show home page as a list of pets"""
    pets = Pet.query.all()

    return render_template('list-pets.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_pet_form():
    """Add pet form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or 'https://peoplewithpets.com/wp-content/uploads/2019/07/not_available.jpg'
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} the {species}")
        return redirect('/')
    
    else:
        return render_template('add-pet-form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Show pet details and edit form, handle editing."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    # render pet details page, have edit form input with info from pet

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet.id}')
    
    else:
        return render_template('pet-details.html', pet=pet, form=form)
