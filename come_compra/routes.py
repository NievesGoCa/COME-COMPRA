from come_compra import app

@app.route("/")
def index():
    return "Flask funcionando"