# planora_app/__init__.py
from flask import Flask, render_template, redirect, url_for, session,flash
from flask_pymongo import PyMongo
import os

mongo = PyMongo()

def create_app():
    # Set template_folder to the outer "templates"
    app = Flask(
        __name__,
        static_folder='static',
        template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    )

    # Config
    app.config['SECRET_KEY'] = 'your-secret-key-change-this'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/planora_db'

    mongo.init_app(app)

    from planora_app.auth import auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        return redirect(url_for('auth.login'))
        # return render_template('index.html')

    # @app.route('/dashboard')
    # def dashboard():
    #     if 'user_id' not in session:
    #         return redirect(url_for('auth.login'))
    #     return render_template('index.html', username=session.get('username'))

    # return app

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            flash("Please login first!", "warning")
            return redirect(url_for('auth.login'))
        return render_template('dashboard.html', username=session.get('username'))
    return app


app = Flask(__name__)

# Import blueprints AFTER app is created
from planora_app.auth.routes import auth_bp

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")


# # ------------------------------------------------------------------------
# @app.route('/')
# def home():
#     # When user visits root, redirect to login page
#     return redirect(url_for('auth.login'))

# --------------------------------------------------------------------------------------------

# from flask import Flask, render_template, redirect, url_for, session, flash
# from flask_pymongo import PyMongo
# import os

# mongo = PyMongo()

# def create_app():
#     app = Flask(
#         __name__,
#         static_folder='static',
#         template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
#     )

#     # Config
#     app.config['SECRET_KEY'] = 'your-secret-key-change-this'
#     app.config['MONGO_URI'] = 'mongodb://localhost:27017/planora_db'

#     mongo.init_app(app)

#     # Import and register blueprint
#     from planora_app.auth import auth_bp
#     app.register_blueprint(auth_bp)

#     # ------------------- Routes -------------------

#     # Root: if logged in -> dashboard, else -> login
#     @app.route('/')
#     def index():
#         if 'user_id' in session:
#             return redirect(url_for('dashboard'))
#         return redirect(url_for('auth.login'))

#     # Protected dashboard
#     @app.route('/dashboard')
#     def dashboard():
#         if 'user_id' not in session:
#             flash("Please login first!", "warning")
#             return redirect(url_for('auth.login'))
#         return render_template('dashboard.html', username=session.get('username'))

#     return app
