from flask import Blueprint, render_template, request

from . import db
from .models import Booking

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html", page="home")


@main.route("/services")
def services():
    return render_template("services.html", page="services")


@main.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        form_data = request.form
        return render_template(
            "booking.html",
            page="booking",
            form_data=form_data,
            submitted=True,
        )
    return render_template("booking.html", page="booking", submitted=False)


@main.route("/about")
def about():
    sample_bookings = (
        Booking.query.order_by(Booking.created_at.desc()).limit(3).all()
        if db.session.bind
        else []
    )
    return render_template("about.html", page="about", recent_bookings=sample_bookings)
