from flask import Flask, render_template, request

import data

app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get("q")
    products = data.load_products(q=q)
    cate_id = request.args.get("category_id")
    categories = data.load_categories()
    return render_template('index.html', categories=categories, products=products)

@app.route("/product/<int:id>")
def detail(id):
    product = data.load_product_by_id(id)
    return render_template('detail_product.html', product=product)

@app.context_processor
def common_attributes():
    return {
        "categories": data.load_categories()
    }
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
