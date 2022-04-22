from flask import Flask

app = Flask(__name__)


@app.route('/<math_operation>/')
def route_calc(math_operation, i=1, j=0):
    while str(math_operation[i]).isdigit():
        i += 1
    first_num = int(math_operation[0:i])
    while str(math_operation[j]).isdigit():
        j -= 1
    second_num = int(math_operation[j+1:])
    operation = math_operation[i:j+1]

    if operation == '+':
        return str(first_num + second_num)
    elif operation == '-':
        return str(first_num - second_num)
    elif operation == '**':
        return str(first_num ** second_num)
    elif operation == '*':
        return str(first_num * second_num)
    elif operation == ':':
        return str(first_num / second_num)
    else:
        return 'Unknown operation'


if __name__ == '__main__':
    app.run()
