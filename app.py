from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')

    return render_template(
        'index.html',
        status="OK - App is running",
        about="This is a DevOps Flask App",
        name=name
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)