import math
from flask import Flask, render_template, request

app = Flask(__name__)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, value):
        cur, prev = self.head, None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def search(self, value):
        return value in self.to_list()

    def to_list(self):
        items, cur = [], self.head
        while cur:
            items.append(cur.value)
            cur = cur.next
        return items


my_list = LinkedList()


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

app.run(host="127.0.0.1", port=5001, debug=True, use_reloader=False)

if __name__ == "__main__":
    app.run(debug=True)
