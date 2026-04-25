from flask import Flask, render_template, request, redirect, url_for, send_file, session
import os

app = Flask(__name__)
app.secret_key = "SENTINEL_X_SECRET_KEY"

# بيانات تجريبية (يتم استبدالها بقاعدة بيانات لاحقاً)
users_db = {
    "admin": {"points": 100, "daily_claimed": False, "referred_by": None}
}

# قائمة المنتجات والأدوات المرفوعة
TOOLS = [
    {"id": 1, "name": "BLAK WINDOW", "file": "BLAK WINDOW.py", "price": 50},
    {"id": 2, "name": "DDOS WXLE v2.0", "file": "DDOS_wxle_v2.0.py", "price": 80},
    {"id": 3, "name": "IPGRAM Extractor", "file": "IPGRAM.py", "price": 40},
    {"id": 4, "name": "CyberShield Toolkit", "file": "password_WXLE_toolkit.py", "price": 100},
]

COURSES = [
    {"id": 5, "name": "إتقان الاختراق الأخلاقي", "category": "Hacking", "price": 200},
    {"id": 6, "name": "التداول من الصفر للاحتراف", "category": "Trading", "price": 150},
    {"id": 7, "name": "البرمجة الشاملة Python", "category": "Programming", "price": 120},
]

@app.route('/')
def index():
    if 'user' not in session:
        session['user'] = "admin" # تجريبي
    user_data = users_db[session['user']]
    return render_template('index.html', user=user_data, tools=TOOLS, courses=COURSES)

@app.route('/daily_gift')
def daily_gift():
    user = session['user']
    if not users_db[user]['daily_claimed']:
        users_db[user]['points'] += 20
        users_db[user]['daily_claimed'] = True
    return redirect(url_for('index'))

@app.route('/download/<int:tool_id>')
def download_tool(tool_id):
    tool = next((t for t in TOOLS if t['id'] == tool_id), None)
    if tool and users_db[session['user']]['points'] >= tool['price']:
        users_db[session['user']]['points'] -= tool['price']
        # إرسال الملف مباشرة كما هو موجود في النظام
        return send_file(tool['file'], as_attachment=True)
    return "نقاط غير كافية!", 403

if __name__ == '__main__':
    app.run(debug=True)
