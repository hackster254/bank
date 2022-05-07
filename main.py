from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)

app.config['uploads'] = '/Users/Karira/Downloads/new bank app/static/uploads'

from werkzeug.utils import secure_filename

@app.route('/upload', methods=['POST', 'GET'])


def upload_text():

    if request.method == "POST":
    
      textFile = request.files['avatar']
      #print(request.files)
      if textFile.filename == '':
          print("File name is invalid")
          return redirect(request.url)
    
      filename = secure_filename(textFile.filename)

      basedir = os.path.abspath(os.path.dirname(__file__))

      textFile.save(os.path.join(basedir, app.config['uploads'], filename))

      return render_template('main.html')

        
    return render_template("main.html")


app.run(port=5000)