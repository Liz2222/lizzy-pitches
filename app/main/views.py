from flask import render_template
from ..models import User,Pitch,Comment
from . import main


# Views
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Perfect Pitch'

    # Getting reviews by category
    interview_piches = Pitch.get_pitches('interview')
    product_piches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')


    return render_template('index.html',title = title, interview = interview_piches, product = product_piches, promotion = promotion_pitches)
