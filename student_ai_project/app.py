from flask import Flask
from student_ai_project.controllers.student_controller import student_bp

app = Flask(__name__)

# Register controller
app.register_blueprint(student_bp)

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)