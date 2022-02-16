from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import NewListingForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import desc, delete, select
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
# engine = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Bootstrap(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Cafes = Base.classes.cafe



# class Cafes(db.Model):
#     __tablename__ = "cafe_posts"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False, unique=True)
#     map_url = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(500), nullable=False)
#     location = db.Column(db.String(250), nullable=False)
#     has_sockets = db.Column(db.Boolean, nullable=False)
#     has_toilet = db.Column(db.Boolean, nullable=False)
#     has_wifi = db.Column(db.Boolean, nullable=False)
#     can_take_calls = db.Column(db.Boolean, nullable=False)
#     seats = db.Column(db.String(250), nullable=False)
#     coffee_price = db.Column(db.String(250), nullable=False)


    # db.create_all()


@app.route("/", methods=["GET", "POST"])
def homepage():
    form = NewListingForm()
    if form.validate_on_submit():
        new_listing = Cafes(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        db.session.add(new_listing)
        db.session.commit()
        return redirect(url_for("results"))
    return render_template("index.html", form=form)


@app.route("/results/<string:search>", methods=["GET", "POST"])
def results(search):
    # cafes = db.session.query(Cafes).all()
    if search == "seats":
        cafes = db.session.query(Cafes).order_by(Cafes.seats.desc())
        return render_template("results.html", all_cafes=cafes)
    if search == "has_sockets":
        cafes = db.session.query(Cafes).order_by(Cafes.has_sockets.desc())
        return render_template("results.html", all_cafes=cafes)
    if search == "has_toilet":
        cafes = db.session.query(Cafes).order_by(Cafes.has_toilet.desc())
        return render_template("results.html", all_cafes=cafes)
    if search == "has_wifi":
        cafes = db.session.query(Cafes).order_by(Cafes.has_wifi.desc())
        return render_template("results.html", all_cafes=cafes)
    if search == "can_take_calls":
        cafes = db.session.query(Cafes).order_by(Cafes.can_take_calls.desc())
        return render_template("results.html", all_cafes=cafes)
    if search == "coffee_price":
        cafes = db.session.query(Cafes).order_by(Cafes.has_sockets.asc())
        return render_template("results.html", all_cafes=cafes)
    else:
        return redirect(url_for("homepage"))


@app.route("/delete/<int:post_id>")
def delete(post_id):
    post_to_delete = db.session.query(Cafes).get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("homepage"))


@app.route("/login")
def login():
    return render_template("sign-in.html")


if __name__ == "__main__":
    app.run(debug=True)
