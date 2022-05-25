from flask import Flask, render_template, request, url_for
from jinja2 import Markup
# from pyecharts.globals import CurrentConfig

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader('./templates'))

from pyecharts import options as opts
from pyecharts.charts import Bar

# import pandas as pd

from data.read_data import *

app = Flask(__name__)


# 1900 - 1999 的老电影
# movies_g = read_from_csv()


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/distribution')
def render_analysis():
    return 'distrib'

@app.route('/year')
def render_year():
    c = year_count()
    return c.dump_options_with_quotes()

@app.route('/works')
def render_works():
    return 'works'

@app.route('/type')
def render_type():
    return 'types'

@app.route('/most-evaluators')
def most_evaluator():
    t = evaluator_count()
    return Markup(t.render_embed())



if __name__ == '__main__':
    app.run(debug=True)