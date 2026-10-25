import os
from app import create_app
from app.extensions import db

env = os.environ.get('FLASK_ENV', 'development')
app = create_app(env)

# Ensure database tables exist upon start
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n=======================================================")
    print(f"  SHIELD HER — Women's Safety Web Application")
    print(f"  recHERsion'26 Hackathon Edition")
    print(f"  Environment: {env.upper()}")
    print(f"  Running on: http://127.0.0.1:{port}")
    print(f"=======================================================\n")
    app.run(host='127.0.0.1', port=port, debug=(env == 'development'))
