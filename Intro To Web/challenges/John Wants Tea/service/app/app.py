from flask import Flask, request, make_response, render_template
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'  

def generate_jwt(admin_status):
    token = jwt.encode({'admin': admin_status, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def decode_jwt(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['admin']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def set_cookie(response, key, value, secure=False, httponly=True):
    response.set_cookie(key, value, secure=secure, httponly=httponly)
    return response

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    if not request.cookies.get('session'):
        token = generate_jwt('false')
        response = set_cookie(response, 'session', token)
    return response

@app.route('/admin')
def admin():
    token = request.cookies.get('session')
    admin_status = decode_jwt(token)
    
    if admin_status == 'true':
        return render_template('admin.html')
    else:
        return render_template('nonAdmin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')