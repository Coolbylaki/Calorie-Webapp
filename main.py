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
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html", calories_form=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temp = temperature.Temperature(calories_form.country.data, calories_form.city.data).get()
        calories_day = calorie.Calorie(weight=float(calories_form.weight.data),
                                       height=float(calories_form.height.data),
                                       age=float(calories_form.age.data),
                                       temperature=float(temp))
        bmi = calories_day.calculate()

        return render_template("calories_form_page.html",
                               result=True,
                               calories=bmi,
                               calories_form=calories_form,
                               )


class CaloriesForm(Form):
    weight = StringField("Weight: ")
    height = StringField("Height: ")
    age = StringField("Age: ")

    city = StringField("City: ")
    country = StringField("Country: ")

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view("home_page"))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view("calories_form_page"))

app.run(debug=True)
