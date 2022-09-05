import resource
from flask import Flask # 서버 구현을 위한 Flask rorcp import
# from flask_restx import Resource # Api 구현을 위한 Api 객체를 import

app = Flask(__name__) # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어준다.


@app.route('/hello') # 데코레이터(?) 이용
class HelloWorld(resource):
    def get(self):
        return {"hello":"world!"}

# @app.route('/user/<user_name>/<int:user_id>')
# def user(user_name, user_id):
#     return f'Hello, {user_name}({user_id})!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)