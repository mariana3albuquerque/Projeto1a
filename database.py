import sqlite3
from dataclasses import dataclass

class Database():
    
    def __init__(self,conexao) -> None:
        self.conn = sqlite3.connect(conexao + '.db')
        self.cur = self.conn.cursor()
        self.res = self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")
    
    def add(self,note):
        insert_query = "INSERT INTO note (title, content) VALUES (?, ?)"
        values = (note.title, note.content)
        self.cur.execute(insert_query, values)
        self.conn.commit()

    def get_all(self):
        notes = []
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id,title,content)
            notes.append(note)
        return notes
    def get(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, title, content FROM note WHERE id = ?', (note_id,))
        row = cursor.fetchone()
        note = Note(id=row[0], title=row[1], content=row[2])
        return note
    
    def update(self, entry):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE note SET title = ?, content = ? WHERE id = ?', (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM note WHERE id = ?', (note_id,))
        self.conn.commit()
    
@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
        