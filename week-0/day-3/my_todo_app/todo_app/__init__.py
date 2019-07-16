import os

from flask import Flask
from flask import request
from flask import render_template

todo_store = {}

todo_store['depo'] = ['Go for run', 'Listen Rock Music']
todo_store['raj'] = ['Study' , 'Brush']
todo_store['shivang'] = ['Read Book' , 'Play Fifa', 'Drink Coffee']
todo_store['sanket'] = ['Go out' , 'Sleep']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/depo')
    def depo():
        my_todos = ['Go for run', 'Listen Rock Music']
        return todo_view(my_todos)


    @app.route('/raj')
    def raj():
        my_todos = ['Study' , 'Brush']
        return todo_view(my_todos)

    # a simple page that list my todos
    @app.route('/shivang')
    def shivang():
        my_todos = ['Read Book' , 'Play Fifa', 'Drink Coffee']
        return todo_view(my_todos)

    @app.route('/sanket')
    def sanket():
        my_todos = ['Go out' , 'Sleep']
        return todo_view(my_todos)


    def select_todos(name):
        global todo_store
        return todo_store[name]

    def get_todo_by_name(name):
        try:
            return select_todos(name)
        except:
            return None

    def insert_todos(name, todo):
        global todo_store
        temp2 = todo_store[name]
        temp2.append(todo)
        todo_store[name] = temp2
        return

    def add_todo_by_name(name, todo):
        insert_todos(name, todo)
        return

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------')
        print(name)
        print('---------')

        my_todos = get_todo_by_name(name)
        if my_todos == None:
            return render_template('404.html'), 404
        #return todo_view(my_todos)
        else:
            return render_template('todo_view.html', todos = my_todos)



    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')

        add_todo_by_name(name, todo)
        return 'Added Successfully'

    return app
