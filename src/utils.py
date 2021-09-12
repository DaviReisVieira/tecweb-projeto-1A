import json
from json import encoder
import os
from database import Database, Note

def extract_route(request):
    filename=''
    if len(request.split())>0:
        filename = request.split()[1][1:]
    return filename

def read_file(path):
    filename, file_extension = os.path.splitext('/path/to/somefile.ext')
    extensions_list = [".txt", ".html", ".css", ".js"]
    if file_extension in extensions_list:
        file = open(path, "rt")
        return file.read()
    else:
        file = open(path, "rb")
        return file.read()

def load_data(banco):
    db = Database(banco)
    notes:list[Note] = db.get_all()
    return notes

def load_template(filepath):
    f = open('src/templates/'+filepath, 'r', encoding="utf-8")
    content = f.read()
    f.close()
    return content

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == "":
        skip = ""
    else:
        skip = "\n"
    if isinstance(body,str):
        body = body.encode()
    return ("HTTP/1.1 "+f"{code} "+reason+skip+headers+"\n\n").encode()+body
    
def add_to_database(params, banco):
    db = Database(banco)
    db.add(Note(title=params['title'], content=params['content']))
    notes:list[Note] = db.get_all()
    return notes

def remove_from_database(params, banco):
    db = Database(banco)
    db.delete(params['id'])
    notes:list[Note] = db.get_all()
    return notes

def update_database(params, banco):
    db = Database(banco)
    db.update(Note(title=params['title'], content=params['content'], id=params['id']))
    notes:list[Note] = db.get_all()
    return notes