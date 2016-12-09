from flask import Flask, request, render_template, redirect, jsonify
from db import Db
import re
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with Db() as db:
        init_tables(db)
        if request.method == 'POST':
            url = request.form['url']
            if url and re.search("^https?://", url, re.I):
                insert_images(db, url)
                db.commit()
                return 'SUCCESS'
            else:
                return 'FAILURE'
        else:
            cursor = select_images(db)
            result = None
            if cursor.rowcount != 0:
                result = random.sample(cursor.fetchall(), 1)[0][0]

            if request.args.get('json', ''):
                return jsonify({
                        'result': result
                    })
            else:
                if result:
                    return redirect(result)
                else:
                    return

def init_tables(db):
    db.execute('''
    create table if not exists images (
        id integer primary key autoincrement,
        url text not null unique
    )
    ''')

def select_images(db):
    return db.execute('''
    select url from images
    ''')

def insert_images(db, url):
    return db.execute('''
    insert or ignore into images(url) values(?)
    ''', [url])
