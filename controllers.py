from crypt import methods
from datetime import datetime
from werkzeug.security import check_password_hash
from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from flask_security import login_required
from app import app
from models import *
# from forms import News, RegisterForm, LoginForm
import xmltodict, json, xmljson
import requests
from datetime import datetime

from models import LoanRequest
from forms import LoanRequest1,CardRequest

# Index page
@app.route('/', methods=['GET', 'POST'])
def index():
    time = datetime.now().strftime('%m.%d.%Y')
    # data = requests.get(f'https://www.cbar.az/currencies/{time}.xml')
    data = requests.get('https://www.cbar.az/currencies/06.12.2022.xml')
    xpars = xmltodict.parse(data.text)
    str_json = json.dumps(xpars)
    json_converted = json.loads(str_json)    
    usd = "{:.4f}".format(float(json_converted['ValCurs']['ValType'][1]['Valute'][0]['Value']))       
    eur = "{:.4f}".format(float(json_converted['ValCurs']['ValType'][1]['Valute'][1]['Value'])) 
    news = News().query.order_by(News.created_at.desc()).all()[:3]
    if request.method == "POST":
        search_input = request.form['search']
        searches = News.query.filter(News.title.contains(search_input) | News.news_content.contains(search_input))
        if searches.count() > 0:
            return render_template("/search.html", searches = searches)
        else:
            return render_template("/search.html")
    return render_template('home.html', active='home', nav=True, usd_get=usd, eur_get=eur, usd_sales="{:.4f}".format(float(float(usd)*1.001+0.02)), eur_sales="{:.4f}".format(float(float(eur)*1.001+0.02)), news=news)


# Search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    search_input = request.form['search']
    if request.method == "POST":
        searches = News.query.filter(News.title.contains(search_input) | News.news_content.contains(search_input))
        return render_template("/search.html", searches = searches)
    return render_template("/search.html")


# News page
@app.route('/news', methods=['GET', 'POST'])
def news():
    
    news = News().query.all()[:6]
    count_news = len(news) 
    if request.method == 'POST':
        value = int(request.form['count-news'])
        news = News().query.all()[:value+6]   
        count_news = len(news)
        return render_template('news.html', news=news, count_news = count_news)
    return render_template('news.html', news=news, count_news = count_news)


# News details page
@app.route('/news/<int:id>', methods=['GET', 'POST'])
def news_detail(id):
    news = News.query.filter(News.id == id).first()
    news_time = news.created_at
    print(type(news_time))
    if request.method == "POST":
        search_input = request.form['search']
        if search_input:
            searches = News.query.filter(News.title.contains(search_input) | News.news_content.contains(search_input))
        if searches.count() > 0:
            return render_template("/search.html", searches = searches)
        else:
            return render_template("/search.html")
    else:
        return render_template('news-details.html', new=news, news_time = news_time.strftime('%-d %B %Y'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Credit page
@app.route('/credits', methods=['GET', 'POST'])
def credits():
    post_data = request.form
    print(post_data)
    form = LoanRequest1()
    if request.method == 'POST':
        form = LoanRequest1(data=post_data)
        if form.validate_on_submit():
            print(form.first_name.data)
            loan = LoanRequest(first_name=post_data['first_name'], last_name=post_data['last_name'], job=post_data['job'], prefix=post_data['prefix'], p_number=post_data['p_number'])
            print(loan)
           
            LoanRequest.add(loan)
    return render_template('credits.html', form=form)
    
# Card page
@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return render_template('cards.html')
    
# Depotist page
@app.route('/deposits', methods=['GET', 'POST'])
def deposits():
    return render_template('deposits.html')

# Card Info page
@app.route('/card-info', methods=['GET', 'POST'])
def card_info():
    post_data = request.form
    print(post_data)
    form = CardRequest()
    if request.method == 'POST':
        form = CardRequest(data=post_data)
        if form.validate_on_submit():
            card = CardRequest(card=form.card.data, first_name=form.first_name.data, last_name=form.last_name.data, branch=form.branch.data, code=form.code.data, prefix=form.prefix.data, p_number=form.p_number.data)
            card.add()
    return render_template('cards-info.html')
    
