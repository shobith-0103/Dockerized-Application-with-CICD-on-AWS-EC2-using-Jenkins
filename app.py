from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Colorful Website</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: green;
        }
        header {
            background: rgba(0,0,0,0.3);
            padding: 20px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
        }
        .container {
            padding: 40px;
            text-align: center;
        }
        .card {
            background: brown;
            color: #333;
            padding: 20px;
            margin: 20px auto;
            width: 300px;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        button {
            background: #667eea;
            border: none;
            color: red;
            padding: 10px 20px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #764ba2;
        }
        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: rgba(0,0,0,0.3);
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>🚀 Whatever it takes!! </header>

    <div class="container">
        <h2>Hello!</h2>
        <p>This website is created using <b>Python Flask</b></p>

        <div class="card">
            <h3>About</h3>
            <p>This is a simple colorful website with Python backend.</p>
            <button>Click Me</button>
        </div>
    </div>

    <footer>Made with ❤️ using Python</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

