from flask_mail import Mail, Message, current_app
from flask import Blueprint

app = Blueprint('mail', __name__)

@app.route('/mail')
def mail():
    current_app.config['MAIL_SERVER'] = 'smtp.qq.com' # 以QQ邮箱为例
    current_app.config['MAIL_PORT'] = 587
    current_app.config['MAIL_USERNAME'] = '1562555013@qq.com'
    current_app.config['MAIL_PASSWORD'] = 'agruhtsnobwlhbab'

    mail = Mail(current_app)

    msg = Message(
        subject="Hello World!", # 邮件标题
        body="test!", # 正文内容
        sender="1562555013@qq.com", # 发送者
        recipients=["1562555013@qq.com"] # 收件人
    )

    mail.send(msg)
    return '发送完毕'