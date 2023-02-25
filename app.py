from flask import Flask, render_template, url_for, request, redirect, jsonify

app = Flask(__name__)

@app.route('/', methods=['get'])
def main0():
    ## ip 고유 번호
    return render_template('bot_v3.html')

if __name__ == "__main__":
    port ='5238'
    host = '0.0.0.0'

    app.run(host=host, port=port, debug=True)
