from flask import Flask, render_template, request, url_for
# from pyecharts.globals import CurrentConfig

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader('./templates'))

from pyecharts import options as opts
from pyecharts.charts import Bar

import pandas as pd

from data.read_data import *

app = Flask(__name__)


# 1900 - 1999 的老电影
# movies = read_from_csv()





@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/counts')
def render_style():
    c = year_count()
    return c.dump_options_with_quotes()

@app.route('/data')
def arrange_data():
    return 'data'



if __name__ == '__main__':
    app.run(debug=True)