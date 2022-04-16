from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from Calorie_Webapp import calorie, temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):

    def get(self):
        pass


app.add_url_rule('/',
                 view_func=HomePage.as_view("home_page"))
app.add_url_rule('/calories_form_page',
                 view_func=CaloriesFormPage.as_view("calories_form_page"))

app.run(debug=True)
