from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def processing_numbarr():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('index.html', name=name, message=message)

if __name__ == "__main__":
    app.run()
  
