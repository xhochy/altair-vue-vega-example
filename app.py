from flask import Flask, jsonify
from vega_datasets import data

import altair as alt
import random


app = Flask(__name__)
cars = data.cars()

@app.route("/vega-example")
def hello():
    columns = [
        'Acceleration',
        'Cylinders',
        'Horsepower',
        'Miles_per_Gallon',
        'Weight_in_lbs'
    ]
    chart = alt.Chart(cars).mark_point().encode(
        x=random.choice(columns),
        y=random.choice(columns)
    )
    return jsonify(chart.to_dict())
