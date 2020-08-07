from factories import create_app
from flask_cors import CORS

app = create_app()
CORS(app, supports_credentials=True)

app.run(
    host='0.0.0.0', 
    port='5000', 
    ssl_context=('factories/config/server.crt', 'factories/config/server.key')
)