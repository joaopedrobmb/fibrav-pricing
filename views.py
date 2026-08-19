from flask import render_template, request, redirect
from app import app, db, Quotation
import numpy as np


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        quotation_content = request.form["client"]
        new_quotation = Quotation(client=quotation_content)

        try:
            db.session.add(new_quotation)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your quotation."

    else:
        quotations = Quotation.query.order_by(Quotation.created_at).all()
        return render_template("index.html", quotations=quotations)


@app.route("/calculation", methods=["POST", "GET"])
def calculation():
    volume = None
    print(volume)
    if request.method == "POST":
        diameter = int(request.form["diameter"])
        length = int(request.form["cylindrical-length"])

        def calculate_shell_volume(diameter, length):
            return np.pi * (diameter / 2) ** 2 * length

        volume = calculate_shell_volume(diameter, length)

        return render_template("calculation.html", volume=volume)
    else:
        return render_template("calculation.html", volume=volume)
