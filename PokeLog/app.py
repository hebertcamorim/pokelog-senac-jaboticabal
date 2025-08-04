from flask import Flask, render_template, request
import requests

app = Flask(__name__)
BASE_URL = "https://pokeapi.co/api/v2"

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_data = None
    endpoint_url = ""

    if request.method == "POST":
        nome = request.form.get("nome", "").strip().lower()
        if nome:
            endpoint_url = f"{BASE_URL}/pokemon/{nome}"
            try:
                res = requests.get(endpoint_url)
                res.raise_for_status()
                dados = res.json()
                pokemon_data = {
                    "id": dados["id"],
                    "nome": dados["name"],
                    "tipos": [t["type"]["name"] for t in dados["types"]],
                    "habilidades": [a["ability"]["name"] for a in dados["abilities"]],
                    "sprite": dados["sprites"]["front_default"]
                }
            except requests.RequestException:
                pokemon_data = "erro"

    return render_template("index.html", pokemon=pokemon_data, endpoint=endpoint_url)

if __name__ == "__main__":
    app.run(debug=True)