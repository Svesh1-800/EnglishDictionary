from flask import Flask, request, url_for, render_template
from PyDictionary import PyDictionary
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        flag = True
        unknown_word = request.form["unknown-word"]
        dictionary = PyDictionary()
        meanings = dictionary.meaning(unknown_word)
        synonums = dictionary.synonym(unknown_word)
       
        if meanings is None:
            flag= False
            
        context = {
        "meanings" : meanings,
        "synonums": synonums,
        "unknown_word": unknown_word,
        "flag":flag,
        }
        return render_template('index.html',**context )


if __name__=='__main__':
    app.run(debug=True)