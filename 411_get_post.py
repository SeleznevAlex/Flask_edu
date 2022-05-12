import requests


class Order:
    def __init__(self, id, desc, items):
        self.id = id
        self.description = desc
        self.items = items

    def __repr__(self):
        return f'<Order {self.id}: {self.items} - {self.description}>'


orders = {43: Order(43, 'Оплата картой, через почту', ['Кружка', 'Майка', 'Стикеры']),
          69: Order(69, 'Оплата наличными, через почту', ['Медные диски'])}

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["POST"])
def render_send():
    server_message = 'Ошибка'
    try:
        id = int(request.form.get('id'))
        if id in orders:
            id_value = orders.get(id)
            return Order.__repr__(id_value)
        else:
            return server_message
    except ValueError:
        return server_message


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
