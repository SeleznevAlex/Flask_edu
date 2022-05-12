from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    news = {}
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if content == '' or title == '' or content == None or title == None:
            abort(404)
        else:
            news[title] = content
        return render_template('index.html', news=news)


if __name__ == '__main__':
    app.run()
