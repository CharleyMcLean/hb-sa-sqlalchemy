"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8).name
# Alternatively:
db.session.query(Brand).get(8).name


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name=='Corvette').filter(Model.brand_name=='Chevrolet').all()
# Alternatively:
db.session.query(Model).filter(Model.name=='Corvette').filter(Model.brand_name=='Chevrolet').all()


# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()
# Alternatively...
db.session.query(Model).filter(Model.year > 1960).all()


# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# Alternatively...
db.session.query(Brand).filter(Brand.founded > 1920).all()


# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Alternatively...
db.session.query(Model).filter(Model.name.like('Cor%')).all()


# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903).filter(Brand.discontinued==None).all()
# Alternatively...
db.session.query(Brand).filter(Brand.founded==1903).filter(Brand.discontinued==None).all()


# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter(db.or_(Brand.founded < 1950 , Brand.discontinued.isnot(None))).all()
# Alternatively...
db.session.query(Brand).filter(db.or_(Brand.founded<1950), Brand.discontinued.isnot(None)).all()


# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Alternatively...
db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models_from_year = db.session.query(Model).filter(Model.year==year).all()

    for model in models_from_year:
        print model.name, model.brand_name, model.brand[0].headquarters

    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     # This is a list of objects.
     all_brands = db.session.query(Brand).all()

     # I am getting an error 'NoneType' object has no attribute 'name'
     # The queries work in the interactive terminal.
     for brand in all_brands:
        if brand.models.name is None:
            print brand.name, "No model name"
        else:
            print brand.name, brand.models.name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
# The returned value is:  <flask_sqlalchemy.BaseQuery object at 0x7fedb27d8d10>
# The datatype is an object.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
# An association table has no meaningful fields, its purpose is to provide a
# link or bridge between two other tables.  

# -------------------------------------------------------------------
# Part 3




def get_models_between(start_year, end_year):
    """Design a function that takes in a start year and end year (two integers),
     and returns a list of objects that are models with years that fall between 
     the start year (inclusive) and end year (exclusive)."""

    # Prepare the integers for querying.
    full_start_year = 1900 + start_year
    full_end_year = 1900 + end_year

    models_between_years = (db.session.query(Model)
                                   .filter(Model.year >= full_start_year)
                                   .filter(Model.year < full_end_year).all())

    return models_between_years