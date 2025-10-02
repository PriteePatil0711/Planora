# This file makes 'auth' a Python package
# planora_app/auth/__init__.py
from flask import Blueprint

# define blueprint instance
auth_bp = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

# import routes AFTER blueprint creation so route decorators attach to auth_bp
from planora_app.auth import routes  # noqa: F401 (import for side-effects)
