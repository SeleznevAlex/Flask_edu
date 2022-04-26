from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<float:num>/')
def index(num):
    return render_template('3_1_index.html',
                           number=num*2,
                           text='Ваше число {}, умноженное на 2: {}'.format(num, num*2)
                           )


if __name__ == '__main__':
    app.run()
