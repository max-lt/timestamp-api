import psycopg2

from flask import Flask, jsonify
app = Flask(__name__)

import os

db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Check if env set
if db_host is None or db_name is None or db_user is None or db_password is None:
    print('Please set all env variables: DB_HOST, DB_NAME, DB_USER, DB_PASSWORD', flush=True)
    exit(1)

@app.route('/')
def hello_world():
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    cur = conn.cursor()
    cur.execute("SELECT uid, username, role FROM users.accounts WHERE username='max_t' ;")

    # Take fist row from the result
    res = cur.fetchone()
    cur.close()

    # Print result to console
    print(res, flush=True)

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
