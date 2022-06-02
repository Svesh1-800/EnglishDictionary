from flask import request, url_for, render_template, Blueprint
from PyDictionary import PyDictionary

dct = Blueprint('dct', __name__,template_folder="templates",static_folder='static')

@dct.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        flag = True
        unknown_word = request.form["unknown-word"]
        dictionary = PyDictionary()
        meanings = dictionary.meaning(unknown_word)
        synonums = dictionary.synonym(unknown_word)

        # get rid of '('
        for key,value in meanings.items():
           
            good_translated = list()
            for ind,value in enumerate(value):
                splited = value.split('(')
                print(splited)
                if len(splited[0])!=0:
                    if splited[0][0]!='(':
                        good_translated.append(splited[0])
            if len(good_translated)==0:
                print("si")
                del meanings[key]
            else:
                meanings[key] = good_translated
        if meanings is None:
            flag= False
            
        context = {
        "meanings" : meanings,
        "synonums": synonums,
        "unknown_word": unknown_word,
        "flag":flag,
        }
        return render_template('index.html',**context )
