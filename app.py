from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cadastros = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
    erro = None

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()

        if not nome:
            erro = "Informe seu nome."
        else:
            cadastros.append(nome)
            return redirect(url_for("lista"))

    return render_template("cadastro.html", erro=erro)


@app.route("/lista")
def lista():
    return render_template("lista.html", cadastros=cadastros)