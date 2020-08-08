from factories import create_app
from flask_cors import CORS

app = create_app()
CORS(app, supports_credentials=True)

app.run(
    host='0.0.0.0', 
    port='5000', 
    ssl_context=(app.config['SSL_CRT_PATH'], app.config['SSL_KEY_PATH'])
)