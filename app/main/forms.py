from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms.fields.html5 import DateField


class BlogpostForm(FlaskForm):
    category = StringField('Blogpost category',validators=[Required()])
    description_path = TextAreaField('write a blogpost')
    posted = DateField('date and time')

    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    name = StringField("Enter your name")
    email = StringField("Email", validators=[Required()])
    submit= SubmitField('Subscribe')

class CommentForm(FlaskForm):
    description_all = TextAreaField('write a comment')
    submit = SubmitField('Submit')