@app.route('/<float:first_num>/<string:operation>/<float:sec_num>/')
def index(first_num, operation, sec_num):
    return render_template('index.html',
                           first_num=first_num,
                           operation=operation,
                           sec_num=sec_num
                           )
<!--- html----->
template = '''    
    {% if operation == '+' %}
         {{first_num + sec_num}}
    {% elif operation == '-' %}
         {{first_num - sec_num}}
    {% elif operation == ':' %}
        {% if sec_num != 0.0 %}
             {{first_num / sec_num}}
        {% else %}
           Ошибка
        {% endif %}
    {% elif operation == '*' %}
        {{ first_num * sec_num}}
    {% elif operation == '**' %}
        {{ first_num ** sec_num}}
    {% else %}
          Ошибка   
    {% endif %}
    '''

