from flask import Flask, request, url_for, render_template
from PyDictionary import PyDictionary
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        unknown_word = request.form["unknown-word"]
        dictionary = PyDictionary()
        meanings = dictionary.meaning(unknown_word)
        synonums = dictionary.synonym(unknown_word)
        context = {
            "meanings" : meanings,
            "synonums": synonums,
            "word": unknown_word,
        }
        if context["meanings"] is None:
            context["empty_response"] = True
        else:
            context["empty_response"] = False
        
        return render_template('index.html', context= context)
    

if __name__=='__main__':
    app.run()