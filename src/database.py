import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, database_name):
        self.database = 'src/data/'+database_name+'.db'
        self.conn = sqlite3.connect(self.database)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT NOT NULL)""")

    def add(self, note: Note):
        query = """INSERT INTO note(title,content) 
        VALUES (?,?)"""
        self.conn.execute(query,(note.title,note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        return [Note(id=x,title=y,content=z) for x,y,z in cursor]

    def update(self, entry):
        query = """UPDATE note SET title = ?,content = ? WHERE id = ?"""
        self.conn.execute(query,(entry.title,entry.content,entry.id))
        self.conn.commit()

    def delete(self, note_id):
        query = """DELETE FROM note WHERE id = ?"""
        self.conn.execute(query,(note_id,))
        self.conn.commit()