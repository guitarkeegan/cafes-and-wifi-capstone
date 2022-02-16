from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL


class NewListingForm(FlaskForm):
    name = StringField("User Name", validators=[DataRequired()])
    location = StringField("Cafe Address", validators=[DataRequired()])
    img_url = StringField("Website URL", validators=[DataRequired(), URL()])
    map_url = StringField("Map URL (ex. from Google Maps)", validators=[DataRequired(), URL()])
    coffee_price = SelectField("Price of Coffee", choices=["💰💰💰💰", "💰💰💰", "💰💰", "💰"], validate_choice=True)
    has_wifi = BooleanField("Has Wifi")
    has_sockets = BooleanField("Has Sockets")
    has_toilet = BooleanField("Has Restroom")
    can_take_calls = BooleanField("Can take Calls")
    seats = SelectField("Number of Seats", choices=["50+", "40-50", "30-40", "20-30", "10-20", "0-10"],
                        validate_choice=True)
    location = StringField("Part of City", validators=[DataRequired()])
    submit = SubmitField("Submit Listing")
