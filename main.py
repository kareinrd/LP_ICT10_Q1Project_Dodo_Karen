from pyscript import display, document


def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = " "
    category = document.getElementById("category").value
    product_name = document.getElementById("prod_name").value
    stock_qty = document.getElementById("quantity").value
    sku = f"{category[:3].upper()}-{product_name[:4].upper()}-{stock_qty}"
    display("SKU: ", sku, target='sku_output')


def create_order(e):
    products = (
        document.getElementById(f"item{number}")
        for number in range(1, 6)
    )
    subtotal = sum(
        float(product.value)
        for product in products
        if product.checked
    )
    tax = subtotal * 0.12
    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>Tax: ₱{tax:.2f}</p>
    <p><strong>Total: ₱{subtotal + tax:.2f}</strong></p>
    """
    document.getElementById("show").innerHTML = receipt