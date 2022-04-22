from flask import Flask


app = Flask(__name__)


@app.route('/<int:number>/')
def show_incr_number(number):
    return str(number + 1)


if __name__ == '__main__':
    app.run()
