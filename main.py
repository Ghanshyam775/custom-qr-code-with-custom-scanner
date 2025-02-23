from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask, render_template
from qr_code_generator.app import qr_app  # Import QR Code Generator app
from scanner.app import scanner_app  # Import Scanner app

# Main Flask app
main_app = Flask(__name__)

# Combine the apps using DispatcherMiddleware
main_app.wsgi_app = DispatcherMiddleware(
    main_app.wsgi_app,
    {
        '/qrcode': qr_app,  # QR Code Generator app accessible via /qrcode
        '/scanner': scanner_app,  # QR Code Scanner app accessible via /scanner
    }
)

@main_app.route('/')
def index():
    # Simple homepage with links to the QR Code Generator and Scanner apps
    return """
    <h1>Welcome to the Combined Application</h1>
    <p>QR Code Generator: <a href="/qrcode">Go to QR Code Generator</a></p>
    <p>QR Code Scanner: <a href="/scanner">Go to QR Code Scanner</a></p>
    """

if __name__ == "__main__":
    # Start the Flask application
    main_app.run(host="0.0.0.0", port=3000)