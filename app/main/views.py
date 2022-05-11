from flask import render_template
from . import main


# Views
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
   

    title = 'Home - Welcome to The best Movie Review Website Online'

    
    return render_template('index.html', title = title)
