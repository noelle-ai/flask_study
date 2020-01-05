# < 1 > 기초
from flask import Flask
# Flask class를 임포트, 이 클래스의 인스턴스가 나의 WSGI 어플리케이션
# 첫번째 인자는 이 어플리케이션의 이름, 단일 모듈을 사용할 때는 이처럼 __name__을 사용;
# 어플리케이션으로 시작되는지 혹은 모듈로 임포트되는지에 따라 이름이 달라짊에 주의
app = Flask(__name__)
# Flask class의 인스턴스를 생성; 인자로 모듈이나 패키지의 이름을 넣는다
# 이 이름은 플라스크에서 팀플릿이나 정적파일을 찾을 때 필요
@app.route('/')
# route() 데코레이터는 Flask의 어떤 URL이 나의 커스텀 함수를 실행시키는지 알려 준다
def hello_world():
    return 'Hi ! '
# 작성된 함수의 이름은 그 함수에 대한 URL을 생성하는 데에 사용되고,
# 사용자 브라우저에 보여줄 메시지를 리턴
if __name__ == '__main__':
    app.run()
# run() 함수가어플리케이션을 로컬서버로 실행
# 소스파일을 모듈이 아닌 python 인터프리터를 이용해서 직접 실행한다면
# if __name__ == '__main__': 의 해당 문장은 실행 중인 서버가
# 현재 동작되는 유일한 서버라는 것을 보장함

#  - - - - - - - - - - - - 정리 - - - - - - - - - - - -
# 01 [ 주의 ] `flask.py`로 호출하면, Flask 자체와 충돌 난다.
# 02 [ 서버의 접근 권한 ] - 기본적으로 외부에서 접근 가능한 서버이다
# 현재 서버는 네트워크상에 있는 다른 컴퓨터에서 접근이 안 되고
# 나의 로컬서버에서만 접근 가능
# 이것이 기본설정인 이유는 디버그모드상에서
# 다른 어플리케이션의 사용자가 임의의 파이썬코드를
# 나의 로컬에서 실행할 수 있기 때문 - 위험
# 03 [ 권한 변경 ]
# debug 모드를 해제하거나
# 나의 네트워크상에 있는 사용자들을 신뢰한다면,
# 간단히 run() 메소드의 호출을 변경해서 서버의 접근을 오픈할 수 있음
# app.run(host='0.0.0.0') - 해당 코드는 모든 public IP가 접근가능도록 설정

# < 2 > 라우팅
@app.route('/routing')
def hello():
    return 'Hello World'

# < 3 > 라우팅 - 변수 규칙
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/url01/')
def projects():
    return 'The project page 01'
@app.route('/url02')
def about():
    return 'The about page 02'
# URL 정의 01 뒷 슬래쉬(trailing slash) 포함 / 02 미포함
# 01은 파일시스템의 폴더와 유사; 뒷 슬래쉬 없이 URL에 접근하면, Flask가 뒷 슬래쉬를 가진 정규 URL로 고쳐줌
# 02은 Unix계열의 파일의 경로와 유사; 뒷 슬래쉬를 포함해서 URL에 접근하면 404”페이지를 찾지 못함” 에러를 유발

# < 4 > 템플릿
from flask import render_template

@app.route('/template/')
@app.route('/template/<name>')
def hello(name=None):
    return render_template('template_test.html', name=name)
# Flask는 templates 폴더에서 템플릿을 찾는다
# 01 모듈로 어플리케이션을 개발했다면 이 폴더는 그 모듈 옆에 위치하고
# 02 패키지로 개발했다면 그 패키지 안에 위치
# * EX 01
# /application.py
# /templates
#     /template_test.html
# * EX 02
# /application
#     /__init__.py
#     /templates
#         /template_test.html
# 템플릿 안에서도 request,:class:~flask.session 와 g [1] 객체에 접근할 수 있음