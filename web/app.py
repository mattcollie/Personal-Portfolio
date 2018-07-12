from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email', None)
        subject = request.form.get('subject', None)
        message = request.form.get('message', None)
        with open("contact.txt", "a") as file:
            file.writelines([
                'email: {}\n'.format(email),
                'subject: {}\n'.format(subject),
                'message: {}\n'.format(message),
                '\n'
            ])

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=1234)
