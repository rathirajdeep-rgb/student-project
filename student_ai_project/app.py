from flask import Flask
from flasgger import Swagger
from student_ai_project.controllers.student_controller import student_bp
from student_ai_project.utils.logger import setup_logger
from student_ai_project.utils.error_handler import register_error_handlers


app = Flask(__name__)

# Setup logger
logger = setup_logger()

register_error_handlers(app)

# Swagger config
swagger = Swagger(app)

# Register controller
app.register_blueprint(student_bp)

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)