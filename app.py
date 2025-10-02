<<<<<<< HEAD
=======
# from flask import Flask,render_template
# from planora_app.extensions import get_db

# app = Flask(__name__)
# app.secret_key = "dummy_key_for_testing"

# @app.route("/")
# def home():
#     db = get_db()
#     users_count = db.users.count_documents({})
#     return f"Users in DB: {users_count}"


# if __name__ == "__main__":
#     app.run(debug=True)

from planora_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

>>>>>>> 69acf346a534693072f84e091c7dfafa6036be5e
