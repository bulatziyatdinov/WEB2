import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<b>ВСЁ РАБОТАЕТ</b>'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=port, host='0.0.0.0')
