from flask import Flask, jsonify
from threading import Thread
import logging

app = Flask('')
logger = logging.getLogger(_name_)

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'bot': 'Venom Crypto Trading Bot',
        'message': 'Bot is active and monitoring 5 signal channels',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    """Detailed health status"""
    return jsonify({
        'status': 'healthy',
        'uptime': 'running',
        'version': '1.0.0',
        'channels': 5
    })

@app.route('/ping')
def ping():
    """Simple ping endpoint"""
    return 'pong'

@app.route('/status')
def status():
    """Bot status"""
    return jsonify({
        'bot_name': 'Venom Crypto Trading Bot',
        'channel': '@VenomCryptoTradingBot',
        'monitoring_channels': [
            'Evening Trader Group',
            'Evening Trader Official',
            'Learn 2 Trade',
            'CryptoSignals.Org',
            'ALTSIGNALS'
        ],
        'status': 'active'
    })

def run():
    """Run Flask server"""
    app.run(host='0.0.0.0', port=8080, debug=False)

def keep_alive():
    """Start server in background thread"""
    t = Thread(target=run)
    t.daemon = True
    t.start()
    logger.info("✅ Keep-alive server started on port 8080")