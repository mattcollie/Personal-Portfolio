from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    import datetime
    years = datetime.date.today().year - 2015

    return render_template('index.html', years=years)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=1234)
