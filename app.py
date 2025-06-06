from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    with open("data/cotacoes.json", encoding="utf-8") as f:
        cotacoes = json.load(f)
    return render_template("index.html", cotacoes=cotacoes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
