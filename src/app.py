from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Webserver 🚀</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2f2f2f, #9e9e9e);
                color: #f5f5f5;
                text-align: center;
                padding: 80px;
                margin: 0;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
                color: #ffffff;
            }
            p {
                font-size: 1.2rem;
                opacity: 0.9;
                color: #e0e0e0;
            }
            .emoji {
                font-size: 3rem;
                margin-bottom: 10px;
            }
            footer {
                position: absolute;
                bottom: 10px;
                width: 100%;
                font-size: 0.9rem;
                opacity: 0.6;
                color: #cccccc;
            }
        </style>
    </head>
    <body>
        <div class="emoji">🧠⚙️</div>
        <h1>Hello Felix!</h1>
        <p>Your Flask webserver is running smoothly inside Docker 🐳</p>
        <footer>Cloud DevOps Powered | Flask + Docker</footer>
    </body>
    </html>
    """
    return html_content


@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "flask-app", "uptime": "OK"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
