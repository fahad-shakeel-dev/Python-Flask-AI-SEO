# from flask import Blueprint, render_template
#
# auth_bp = Blueprint('auth', __name__)
#
# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('auth/login.html')
#
# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     return render_template('auth/signup.html')



#
# from flask import Blueprint, render_template, request, jsonify, redirect, url_for
# from werkzeug.security import generate_password_hash, check_password_hash
# import psycopg2
# from dotenv import load_dotenv
# import os
# import logging
#
# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
#
# # Load environment variables
# load_dotenv()
#
# # Database connection
# def get_db_connection():
#     try:
#         conn = psycopg2.connect(
#             dbname=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             host=os.getenv("DB_HOST"),
#             port=os.getenv("DB_PORT")
#         )
#         logger.debug("Database connection established")
#         return conn
#     except Exception as e:
#         logger.error(f"Database connection failed: {str(e)}")
#         raise
#
# auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')
#
# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         data = request.get_json()
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
#
#         name = data.get('name')
#         email = data.get('email')
#         password = data.get('password')
#         confirm_password = data.get('confirmPassword')
#
#         logger.debug(f"Received JSON data: name={name}, email={email}, password={password}, confirm={confirm_password}")
#
#         if not all([name, email, password, confirm_password]):
#             return jsonify({'error': 'Missing required fields'}), 400
#
#         if password != confirm_password:
#             return jsonify({'error': 'Passwords do not match'}), 400
#
#         if len(password) < 6:
#             return jsonify({'error': 'Password must be at least 6 characters'}), 400
#
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#
#         conn = get_db_connection()
#         cur = conn.cursor()
#         try:
#             cur.execute(
#                 "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
#                 (name, email, hashed_password)
#             )
#             conn.commit()
#             logger.debug("User registered successfully")
#             return jsonify({'message': 'User registered successfully', 'redirect': '/auth/login'})
#         except psycopg2.IntegrityError as e:
#             conn.rollback()
#             logger.error(f"IntegrityError: {str(e)}")
#             return jsonify({'error': 'Email already exists'}), 400
#         except Exception as e:
#             conn.rollback()
#             logger.error(f"Exception: {str(e)}")
#             return jsonify({'error': str(e)}), 500
#         finally:
#             cur.close()
#             conn.close()
#
#     return render_template('auth/signup.html')
#
# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         data = request.get_json()
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
#
#         email = data.get('email')
#         password = data.get('password')
#
#         if not all([email, password]):
#             return jsonify({'error': 'Missing required fields'}), 400
#
#         conn = get_db_connection()
#         cur = conn.cursor()
#         try:
#             cur.execute("SELECT * FROM users WHERE email = %s", (email,))
#             user = cur.fetchone()
#             if user and check_password_hash(user[3], password):
#                 return jsonify({'message': 'Login successful', 'redirect': '/dashboard'})
#             else:
#                 return jsonify({'error': 'Invalid email or password'}), 401
#         except Exception as e:
#             logger.error(f"Exception: {str(e)}")
#             return jsonify({'error': str(e)}), 500
#         finally:
#             cur.close()
#             conn.close()
#
#     return render_template('auth/login.html')





#
# from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
# from werkzeug.security import generate_password_hash, check_password_hash
# import psycopg2
# from dotenv import load_dotenv
# import os
# import logging
#
# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
#
# # Load environment variables
# load_dotenv()
#
# # Database connection
# def get_db_connection():
#     try:
#         conn = psycopg2.connect(
#             dbname=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             host=os.getenv("DB_HOST"),
#             port=os.getenv("DB_PORT")
#         )
#         logger.debug("Database connection established")
#         return conn
#     except Exception as e:
#         logger.error(f"Database connection failed: {str(e)}")
#         raise
#
# auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')
#
# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         data = request.get_json()
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
#
#         name = data.get('name')
#         email = data.get('email')
#         password = data.get('password')
#         confirm_password = data.get('confirmPassword')
#
#         logger.debug(f"Received JSON data: name={name}, email={email}, password={password}, confirm={confirm_password}")
#
#         if not all([name, email, password, confirm_password]):
#             return jsonify({'error': 'Missing required fields'}), 400
#
#         if password != confirm_password:
#             return jsonify({'error': 'Passwords do not match'}), 400
#
#         if len(password) < 6:
#             return jsonify({'error': 'Password must be at least 6 characters'}), 400
#
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#
#         conn = get_db_connection()
#         cur = conn.cursor()
#         try:
#             cur.execute(
#                 "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
#                 (name, email, hashed_password)
#             )
#             conn.commit()
#             logger.debug("User registered successfully")
#             return jsonify({'message': 'User registered successfully', 'redirect': '/auth/login'})
#         except psycopg2.IntegrityError as e:
#             conn.rollback()
#             logger.error(f"IntegrityError: {str(e)}")
#             return jsonify({'error': 'Email already exists'}), 400
#         except Exception as e:
#             conn.rollback()
#             logger.error(f"Exception: {str(e)}")
#             return jsonify({'error': str(e)}), 500
#         finally:
#             cur.close()
#             conn.close()
#
#     return render_template('auth/signup.html')
#
# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         data = request.get_json()
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
#
#         email = data.get('email')
#         password = data.get('password')
#
#         if not all([email, password]):
#             return jsonify({'error': 'Missing required fields'}), 400
#
#         conn = get_db_connection()
#         cur = conn.cursor()
#         try:
#             cur.execute("SELECT * FROM users WHERE email = %s", (email,))
#             user = cur.fetchone()
#             if user and check_password_hash(user[3], password):
#                 session['user_id'] = user[0]  # Save user ID in session
#                 return jsonify({'message': 'Login successful', 'redirect': '/dashboard'})
#             else:
#                 return jsonify({'error': 'Invalid email or password'}), 401
#         except Exception as e:
#             logger.error(f"Exception: {str(e)}")
#             return jsonify({'error': str(e)}), 500
#         finally:
#             cur.close()
#             conn.close()
#
#     return render_template('auth/login.html')











from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        logger.debug("Database connection established")
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirmPassword')

        logger.debug(f"Received JSON data: name={name}, email={email}, password={password}, confirm={confirm_password}")

        if not all([name, email, password, confirm_password]):
            return jsonify({'error': 'Missing required fields'}), 400

        if password != confirm_password:
            return jsonify({'error': 'Passwords do not match'}), 400

        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password)
            )
            conn.commit()
            logger.debug("User registered successfully")
            return jsonify({'message': 'User registered successfully', 'redirect': '/auth/login'})
        except psycopg2.IntegrityError as e:
            conn.rollback()
            logger.error(f"IntegrityError: {str(e)}")
            return jsonify({'error': 'Email already exists'}), 400
        except Exception as e:
            conn.rollback()
            logger.error(f"Exception: {str(e)}")
            return jsonify({'error': str(e)}), 500
        finally:
            cur.close()
            conn.close()

    return render_template('auth/signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'error': 'Missing required fields'}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cur.fetchone()
            if user and check_password_hash(user[3], password):
                session['user_id'] = user[0]  # Save user ID in session
                return jsonify({'message': 'Login successful', 'redirect': '/dashboard'})
            else:
                return jsonify({'error': 'Invalid email or password'}), 401
        except Exception as e:
            logger.error(f"Exception: {str(e)}")
            return jsonify({'error': str(e)}), 500
        finally:
            cur.close()
            conn.close()

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    return redirect('/')