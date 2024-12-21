from flask import Flask
from flask import request


app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def main():
	return app.send_static_file('index.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5005)