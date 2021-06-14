from flask import Flask , render_template
import subprocess , os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/close')
def close():
    subprocess.Popen("TASKKILL /F /IM python.exe")
    return '200'

if __name__ == '__main__':
    subprocess.Popen('npm start', shell=True, cwd='node')
    app.run()