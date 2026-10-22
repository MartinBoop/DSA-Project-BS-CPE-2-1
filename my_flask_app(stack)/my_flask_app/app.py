import math
from flask import Flask, render_template, request

from ds.linked_list import LinkedList
from ds.stack import Stack

app = Flask(__name__)


my_list = LinkedList()
my_stack = Stack()


# ---------- Routes ----------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        result = request.form.get('inputString', '').upper()
    return render_template('touppercase.html', result=result)


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result, error = None, None
    if request.method == 'POST':
        try:
            r = float(request.form.get('radius', ''))
            if r < 0:
                raise ValueError
            result = round(math.pi * r * r, 2)
        except ValueError:
            error = "Please enter a radius of 0 or more."
    return render_template('circle.html', result=result, error=error)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result, error = None, None
    if request.method == 'POST':
        try:
            b = float(request.form.get('base', ''))
            h = float(request.form.get('height', ''))
            if b < 0 or h < 0:
                raise ValueError
            result = round(0.5 * b * h, 2)
        except ValueError:
            error = "Please enter a base and height of 0 or more."
    return render_template('triangle.html', result=result, error=error)


@app.route('/works/linked-list', methods=['GET', 'POST'])
def linked_list():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()
        if not value:
            message = "Type a value first."
        elif action == 'head':
            my_list.insert_head(value)
            message = f"Added {value} to the front."
        elif action == 'tail':
            my_list.insert_tail(value)
            message = f"Added {value} to the end."
        elif action == 'delete':
            ok = my_list.delete(value)
            message = f"Deleted {value}." if ok else f"{value} isn't in the list."
        elif action == 'search':
            found = my_list.search(value)
            message = f"Found {value}!" if found else f"{value} isn't in the list."
    return render_template('linkedlist.html', items=my_list.to_list(), message=message)


@app.route('/works/stack', methods=['GET', 'POST'])
def stack():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()
        if action == 'push':
            if not value:
                message = "Type a value first."
            else:
                my_stack.push(value)
                message = f"Pushed {value} onto the stack."
        elif action == 'pop':
            if my_stack.is_empty():
                message = "The stack is empty, nothing to pop."
            else:
                message = f"Popped {my_stack.pop()}."
        elif action == 'peek':
            if my_stack.is_empty():
                message = "The stack is empty."
            else:
                message = f"Top of the stack is {my_stack.peek()}."
    return render_template('stack.html', items=my_stack.to_list(), message=message)

app.run(host="127.0.0.1", port=5001, debug=True, use_reloader=False)

if __name__ == "__main__":
    app.run(debug=True)
