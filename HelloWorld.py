from flask import Flask, render_template

app = Flask(__name__)

# 创建了网址 /show/info 和 函数 index 的对应关系
# 当用户访问此网址会自动执行对应函数
@app.route("/show/info")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
