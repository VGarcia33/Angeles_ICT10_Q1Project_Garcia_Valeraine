from flask import Flask, render_template, request

app = Flask(__name__)

sku_counter = 1

def generate_sku(product_name: str, category: str, stock_quantity: int, sequence_num: int):
    name_code = product_name.strip().upper()[:3]
    cat_code = category.strip().upper()[:3]
    seq_code = f"{sequence_num:03d}"

    sku = f"{name_code}-{cat_code}-{seq_code}"

    return {
        "sku": sku,
        "product_name": product_name,
        "category": category,
        "stock_quantity": stock_quantity
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def handle_generation():
    global sku_counter

    category = request.form.get('category')
    product_name = request.form.get('product')
    
    quantity_raw = request.form.get('quantity') or request.form.get('stock_quantity')
    quantity = int(quantity_raw) if quantity_raw and quantity_raw.isdigit() else 0
    
    result = generate_sku(
        product_name=product_name,
        category=category,
        stock_quantity=quantity,
        sequence_num=sku_counter
    )
    
    sku_counter += 1
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
