from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash



auth_bp = Blueprint("auth", __name__, template_folder="templates")


# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;
# - a rota /logout.
@auth.bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        senha_hash = generate_password_hash(senha)

        usuario = Usuario(nome=nome, email=email, senha_hash=senha_hash)

        redirect(url_for(login))

        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("auth.registro"))

    return render_template("registro.html")


@auth.bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        if usuario and check_password_hash(
            usuario.senha_hash, senha,
        ):

            session["usuario_id"] = usuario.id

            return redirect("index.html")


        flash("Implemente o login com session.")
        return redirect(url_for("login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():

    session.pop('usuario_id')
    
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))
