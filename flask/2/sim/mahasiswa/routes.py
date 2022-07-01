from flask import Flask, render_template, redirect, url_for, Blueprint
from sim.mahasiswa.forms import Mahasiswa_F

rmahasiswa = Blueprint('rmahasiswa',__name__)

@rmahasiswa.route("/")
def home():
    return render_template("home.html")


@rmahasiswa.route("/about")
def about():
    return render_template("about.html")


@rmahasiswa.route("/data_mahasiswa", methods=['GET', 'POST'])
def data_m():
    form = Mahasiswa_F()
    if form.validate_on_submit():
        return redirect(url_for('rmahasiswa.data_m'))
    return render_template("data-mahasiswa.html", form=form)


@rmahasiswa.route("/artikel/<info>")
def artikel_info(info):
    return "halaman artikel " + info
