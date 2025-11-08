from flask import Flask, jsonify, Response


app = Flask(__name__)


# ------------------------------
# HTML Route (Main Page)
# ------------------------------
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
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #e0eafc, #cfdef3);
                color: #1a1a1a;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            .container {
                background: rgba(255, 255, 255, 0.25);
                backdrop-filter: blur(20px);
                border-radius: 20px;
                padding: 50px 60px;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                max-width: 600px;
                width: 90%;
                position: relative;
            }
            .profile-img {
                width: 130px;
                height: 130px;
                border-radius: 35%;
                object-fit: cover;
                border: 3px solid rgba(255, 255, 255, 0.5);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
                margin-bottom: 20px;
            }
            h1 {
                font-size: 2.5rem;
                color: #2c3e50;
                margin-bottom: 10px;
                font-weight: 700;
            }
            p {
                font-size: 1.15rem;
                color: #444;
                margin-bottom: 30px;
                line-height: 1.6;
            }
            .emoji {
                font-size: 2.8rem;
                margin-bottom: 15px;
                display: block;
            }
            footer {
                position: absolute;
                bottom: 15px;
                width: 80%;
                text-align: center;
                font-size: 0.9rem;
                color: #555;
                opacity: 0.8;
            }
            .btn {
                display: inline-block;
                background: linear-gradient(90deg, #667eea, #764ba2);
                color: white;
                padding: 12px 25px;
                border-radius: 30px;
                text-decoration: none;
                font-size: 1rem;
                font-weight: 500;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background: linear-gradient(90deg, #5a67d8, #6b46c1);
                transform: translateY(-3px);
                box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
            }
            @media (max-width: 600px) {
                .container {
                    padding: 40px 30px;
                }
                h1 {
                    font-size: 2rem;
                }
                p {
                    font-size: 1rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="/static/facebook_profile.jpg" alt="Felix" class="profile-img">

            <div class="emoji">🧠⚙️</div>
            <h1>Hello Felix!</h1>
            <p>Your Flask App is running flawlessly inside Docker 🐳<br>
               Fully automated. Secure. Cloud-native. 🚀
            </p>
            <a href="/health" class="btn">Check Health</a>
            <footer>Cloud DevOps Powered | Flask + Docker + AWS</footer>
        </div>
    </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')


# ------------------------------
# Health Check Endpoint
# ------------------------------
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-app",
        "uptime": "OK"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
