from flask import Flask, render_template, request, session, redirect, url_for
from utils import *
import time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

# rank function
@app.route('/func1', methods=['POST','GET'])
def func1():
    print('----')
    website = request.args.get('website')
    print(request.args)
    keywords = request.args.getlist('customFieldName[]')
    keyword_list = request.args.getlist('customFieldValue[]')
    keywords.extend(keyword_list)
    print(website)
    print(keywords)
    print('----')
    output_dict = {}
    if len(keywords) >= 1:
        for i in keywords:
            ret = url_keyword_rank(website, i)
            output_dict[i] = ret
            print('sleep')
            time.sleep(2)
            print('sleep over')
        print(output_dict)

    else:
        ret = url_keyword_rank(website, keywords[0])
        output_dict[i] = ret
    # df = url_keyword_rank(website, keywords)
    # print(df.to_dict(orient='records'))
    return render_template('output.html', output_dict = output_dict)

@app.route('/seo_audit', methods=['POST','GET'])
def seo_audit():
    print(request.method)
    if request.method == 'POST':
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
        
        return render_template('output_orig.html', DOMAIN_REDIRECTION_op = DOMAIN_REDIRECTION_op, 
                                          ROBOTS_op = ROBOTS_op, ret_title = ret_title, ret_title_len = ret_title_len,
                                          gtag_op = gtag_op, sitemap_op_table = [sitemap_op.to_html(classes='data')], sitemap_op_titles=sitemap_op.columns.values)

    else:
        return render_template('seo_audit_html.html')

if __name__ == "__main__":
    app.run(debug=False)