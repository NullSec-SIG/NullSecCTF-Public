from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('challenge.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_solution = request.form.get('solution')
    user_agent = request.headers.get('User-Agent')

    if user_agent == 'special_crafted_oranges' and user_solution == 'K3Y':
        return 'Congratulations! NULL{0rang3s_ar3_yummy}'
    else:
        hint = "Hint: Look at the description again. That's your User-Agent Value"
        return f'Sorry, that was incorrect or the User-Agent header is wrong. {hint}'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
