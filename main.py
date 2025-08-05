import time
import random

from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/slow-image')
def slow_image():
    def generate():
        with open('static/image.jpeg', 'rb') as f:
            chunk_size = 4096
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk
                chunk_size = random.randint(0, 4096)
                time.sleep(2)

    return Response(generate(), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
