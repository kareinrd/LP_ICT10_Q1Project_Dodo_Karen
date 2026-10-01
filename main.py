from pyscript import display, document

def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = " "
    category = document.getElementById("category").value
    product_name = document.getElementById("prod_name").value
    stock_qty = document.getElementById("quantity").value
    sku = f"{category[:3].upper()}-{product_name[:4].upper()}-{stock_qty}"
    display("SKU: ", sku, target='sku_output')


def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    subtotal = (
        float(prod1.value) * prod1.checked +
        float(prod2.value) * prod2.checked +
        float(prod3.value) * prod3.checked +
        float(prod4.value) * prod4.checked +
        float(prod5.value) * prod5.checked
    )
    tax = subtotal * 0.12
    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>Tax: ₱{tax:.2f}</p>
    <p><strong>Total: ₱{subtotal + tax:.2f}</strong></p>
    """
    document.getElementById("show").innerHTML = receipt
