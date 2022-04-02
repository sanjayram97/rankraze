from flask import Flask, render_template, request, session, redirect, url_for
from utils import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/func', methods=['POST'])
def func():
    website = request.form.get("website")
    DOMAIN_REDIRECTION_op = concatenateDom(website)
    email = request.form.get("email")
    company = request.form.get("company")
    url = "https://www."+website+"/"
    ROBOTS_op = robots_df(url)
    gtag_op = gtag(url)
    sitemap_op = sitemap(url)
    ret_title, ret_title_len = title(url)
    print(website)
    print(email)
    print(company)
    return render_template('output.html', DOMAIN_REDIRECTION_op = DOMAIN_REDIRECTION_op, 
                                          ROBOTS_op = ROBOTS_op, ret_title = ret_title, ret_title_len = ret_title_len,
                                          gtag_op = gtag_op, sitemap_op_table = [sitemap_op.to_html(classes='data')], sitemap_op_titles=sitemap_op.columns.values)

if __name__ == "__main__":
    app.run(debug=True)