from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def Home():
    return render_template("pages/index.html")

@app.route('/left-sidebar.html')
def left():
    return render_template("pages/left-sidebar.html")

@app.route('/right-sidebar.html')
def right():
    return render_template("pages/right-sidebar.html")


@app.route('/no-sidebar.html')
def no_sidebar():
    return render_template("pages/no-sidebar.html")


if __name__ == '__main__':
    app.run(debug=True)
