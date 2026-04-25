from flask import Flask, render_template, send_file, session, jsonify
import os

app = Flask(__name__)
app.secret_key = "WXL_E_SECRET_KEY"

# الأدوات التي أرسلتها (ربط مباشر بالملفات)
MY_TOOLS = [
    {"id": 1, "name": "IPGRAM VIP", "file": "IPGRAM.py", "points": 40, "desc": "سحب معلومات الآيبي عبر انستغرام"},
    {"id": 2, "name": "DDOS WXLE v2", "file": "DDOS_wxle_v2.0.py", "points": 80, "desc": "نظام هجوم قوي ومتطور"},
    {"id": 3, "name": "CyberShield Toolkit", "file": "password_WXLE_toolkit.py", "points": 100, "desc": "أدوات فحص وتشفير شاملة"},
    {"id": 4, "name": "WebAnalyzer Pro", "file": "WebAnalyzer Pro v1.4.RUSS.py", "points": 60, "desc": "تحليل ثغرات المواقع باحترافية"}
]

@app.route('/')
def home():
    # هدية البداية 100 نقطة
    if 'points' not in session:
        session['points'] = 100
    return render_template('index.html', tools=MY_TOOLS, points=session['points'])

@app.route('/download/<int:tool_id>')
def download(tool_id):
    tool = next((t for t in MY_TOOLS if t['id'] == tool_id), None)
    if tool and session['points'] >= tool['points']:
        session['points'] -= tool['points']
        return send_file(tool['file'], as_attachment=True)
    return "Insufficient Points", 403

if __name__ == '__main__':
    app.run(debug=True, port=5000)
