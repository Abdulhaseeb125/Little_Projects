import flask
app = flask.Flask(__name__)
@app.route('/<int:name>')
def server(name):
    number = 4
    if name == 4:
        return "<h1>You found me..</h1>" \
               "<iframe src='https://giphy.com/embed/s50Vsxf1g0CQ9ENVNp'></iframe>"
    elif name < 3:
        return "<h1 style='color:red;'>Too Low....</h1>" 
    elif name > 5:
        return "<h1 style='color:green;'>Too High....</h1>"
    else:
        return "<h1>Close................</h1>" 


if __name__ == "__main__":
    app.run(debug=True)
