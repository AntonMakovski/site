from flask import render_template
from flask import Flask as Web
from flask import url_for
from flask import request
import sqlite3 as sql

def index():
    return render_template('exampls.html')
def contacts():
    return render_template('contacts.html')
def coments():
    data = request.form.get('coment')
    if data != None:
        base = sql.connect('data_base.db')
        cursor = base.cursor()
        cursor.execute("""INSERT INTO coments (coments) VALUES (?)""", [data])
        base.commit()

    
    base = sql.connect('data_base.db')
    cursor = base.cursor()
    cursor.execute("SELECT coments FROM coments")

    dat = cursor.fetchall()

    if dat != None:
        data_in = list()
        for element in dat:
            data_in.append(element[0])
    else:
        data_in = ''

    
    return render_template('coments.html', dat=data_in)

app = Web(__name__) 
app.add_url_rule('/index','index',index)
app.add_url_rule('/coments','coments',coments, methods=['GET', 'POST'])
app.add_url_rule('/contacts','contacts',contacts)

if __name__ == "__main__":
    app.run()