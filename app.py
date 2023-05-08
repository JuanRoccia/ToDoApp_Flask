from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todo_list = []

class Task:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

@app.route('/', methods=['GET', 'POST'])
def todo():
    current_input = ""
    if request.method == 'POST':
        task = request.form['task']
        todo_list.append(Task(task))
        current_input = task
        return redirect(url_for('todo'))
    return render_template('index.html',
                          todo_list=todo_list,
                          current_input=current_input)


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    try:
        del todo_list[task_id]
    except IndexError:
        pass
    return redirect(url_for('todo'))

@app.route('/mark_done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    try:
        todo_list[task_id].done = not todo_list[task_id].done
    except IndexError:
        pass
    return redirect(url_for('todo'))
  
if __name__ == '__main__':
  app.run()