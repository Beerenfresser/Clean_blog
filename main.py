from flask import Flask,render_template
import requests
app = Flask(__name__)

response = requests.get("https://api.npoint.io/2821217e69fa633f5356").json()
print(response)

@app.route('/')
def hello_world():
    return render_template("index.html",all_posts=response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def make_post(num):
    requested_post = None
    for i in response:
        if i["id"] ==num:
            requested_post = i
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)