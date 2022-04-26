from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<float:raduis>/')
def index(raduis):
    return render_template('index.html',
                           r=raduis,
                           pi=3.14
                           )


if __name__ == '__main__':
    app.run()

# index.html has tag in body <p>Площадь круга с радиусом {{r}} равна {{pi*r*r}}</p>
