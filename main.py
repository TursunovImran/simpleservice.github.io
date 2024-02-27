from flask import Flask, request

app: Flask = Flask(__name__)


@app.get('/')
def processing_numbarr() -> str:
    name = request.args.get('name')
    message = request.args.get('message')
    return f"Привет, {name}! Твое сообщение: {message}"

if __name__ == "__main__":
    app.run()
  
