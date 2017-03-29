from flask import Flask, render_template, request, redirect, url_for
import jinja2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_or_post():
    if request.method == 'GET':
        return get()
    else:
        return post()

def render_front(title = "", art = "", error = ""):
    return render_template("index.html", title = title, art = art, error = error)
    
def get():
    return render_front()

def post():
    title = request.form.get("title")
    art = request.form.get("art")

    if title and art:
        return "Thanks! :D"
    else:
        error = "Oh, oh! We need both infos, baby"
        return render_front(title, art, error)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
