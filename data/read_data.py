import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.components import Table

def read_from_csv():
    raw_movie = pd.read_csv(
        'data/movie.csv', 
        usecols=[
            '标题', 
            '年份',
            '导演',
            '主演',
            '类型',
            '语言',
            '片长',
            '总评分',
            '评价人数'
        ], 
        dtype=str
    )
    raw_movie.dropna(how='all', inplace=True)
    return raw_movie[ ('1900' <= raw_movie['年份']) & (raw_movie['年份'] < '2000') ]


movies_g = read_from_csv()
usecols = movies_g.columns.tolist()


def evaluate_distribution():
    """\
    根据评分数量，评分均值画出折线图，柱状图
    根据图表对分布定性
    """
    pass
    
def year_count():
    """
    按年份制作一个柱状图和折线图的合成图
    """
    movies = movies_g.dropna(subset='年份')
    
    movies_count = {
        '1905以前': movies[  movies['年份'] < '1905' ].count()[0],
        '1905-1948': movies[ ('1905' <= movies['年份']) & (movies['年份'] <= '1948')].count()[0],
        '1949-1966': movies[ ('1949' <= movies['年份']) & (movies['年份'] <= '1966')].count()[0],
        '1967-1999': movies[ ('1967' <= movies['年份']) & (movies['年份']) ].count()[0],
    }
    counts = [int(i) for i in movies_count.values()]
    ave = [
        counts[0],
        counts[1] // 43,
        counts[2] // 17,
        counts[3] // 32
    ]
    c = (
        Bar()
        .add_xaxis(list(movies_count.keys()))
        .add_yaxis(
            series_name='数量',
            y_axis=counts,
            stack='stack0',
            gap='0%'
        )
        .add_yaxis(
            series_name='年平均',
            y_axis=ave,
            is_selected=False,
            stack='stack1',
            gap='0%'
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='老电影数量统计',
                subtitle='1900-1999'
            ),
            yaxis_opts=opts.AxisOpts(name="数量/部"),
            xaxis_opts=opts.AxisOpts(name="时间"),
            tooltip_opts=opts.TooltipOpts(
                trigger='axis',
                axis_pointer_type='cross'
                # formatter='{a}: {c}'
            )
        )
    )
    l = (
        Line()
        .add_xaxis(list(movies_count.keys()))
        .add_yaxis(
            series_name='',
            y_axis=counts,
            label_opts=opts.LabelOpts(
                is_show=False
            )
        )
    )
    return c.overlap(l)


def works_count():
    """
    按导演作品数量制作一个pie图
    """
    movies_count = movies_g.groupby('导演').count()
    
def type_count():
    """
    柱状图+折线图
    按类型分类
    然后照烂片率从高到低排序
    烂片率：算法未定
    """
    pass

def evaluator_count():
    """
    做一个表格
    评价人数最多的前50部电影
    """
    movies = movies_g[['标题', '总评分', '评价人数']]
    movies.dropna(how='any', inplace=True)
    for i in movies.index:
        movies.at[i, '评价人数'] = int(''.join([j for j in movies.at[i, '评价人数'] if 48<=ord(j)<=57]))
    movies.sort_values('评价人数', inplace=True, ascending=False)
    movies = movies.head(50)
    headers = ['电影名', '总评分', '评价人数']
    rows = [
        [t, r, e] for _, t, r, e in movies[['标题', '总评分', '评价人数']].itertuples()
    ]
    t = (
        Table()
        .add(headers, rows)
    )
    return t


if __name__ == '__main__':
    # c = year_count()
    # c.render() # 会在运行路径生成一个render.html
    
    from icecream import ic
    # ic.disable()
    # ic(evaluate_distribution().render())
    ic(year_count().render())
    # ic(works_count().render())
    # ic(type_count().render())
    # ic(evaluator_count().render())
