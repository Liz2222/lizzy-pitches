from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField


class ReviewForm(FlaskForm):

    title = StringField('Review title')
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')
