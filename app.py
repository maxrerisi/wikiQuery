from flask import Flask, render_template, request, redirect, url_for
from search_function import get_queries, get_result

app = Flask(__name__)

radio_choices = ['Option 1', 'Option 2', 'Option 3']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['text_input']
        # return f'You entered: {user_input}, and selected: {selected_option}'
        request.method = "GET"
        return redirect(url_for('radios', user_input=user_input))
    return render_template('index.html')

@app.route('/radios', methods=['GET', 'POST'])
def radios():
    user_input = request.args.get('user_input')  # Get the text input from the query parameter
    options = get_queries(user_input)
    if request.method == 'POST':
        selected_option = request.form['radio_option']
        return render_template('out_file.html', radio_choices=options, result=get_result(selected_option, "Industry"), site=get_result(selected_option, "Website"), user_input=user_input)
    return render_template('radios.html', radio_choices=options)

if __name__ == '__main__':
    app.run(debug=True)