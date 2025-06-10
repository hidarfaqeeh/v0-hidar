"""
نقطة دخول البوت الرئيسية
Main entry point for the bot
"""

from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "status": "✅ نشط",
            "message": "🤖 بوت تيليجرام يعمل على Vercel",
            "version": "1.0.0",
            "endpoints": {
                "webhook": "/api/webhook",
                "setup": "/api/setup",
                "health": "/"
            }
        }
        
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
    
    def do_POST(self):
        """Handle POST requests"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {"status": "ok", "message": "POST request received"}
        self.wfile.write(json.dumps(response).encode('utf-8'))
