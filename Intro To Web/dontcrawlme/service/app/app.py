from flask import Flask, request, make_response, render_template, send_from_directory

rightSecret = 'Chingmilichong'

app = Flask(__name__)

 

@app.route('/', methods=['GET','POST'])
def index():
    result = None
    if request.method == 'POST':
        entered_secret = request.form.get('secret')
        if entered_secret == rightSecret:
            result = "NULL{1_ju5t_13@rn1_r0b0t5}"  
        else:
            result = "Incorrect, try again"
    return render_template('index.html', result=result)
  

@app.route('/robots.txt', methods=['GET'])
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/admin')
def admin():
        return render_template('admin.html')

@app.route('/key')
def key():
    return render_template('key.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 2022)
