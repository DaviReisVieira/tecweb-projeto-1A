from database import Database, Note


db = Database('banco')

# db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
# db.add(Note(title=None, content='Lembrar de tomar água'))

# notes = db.get_all()
# for note in notes:
#     print(note)
#     print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

# db.update(Note(title='Água', content='Lembrar de tomar água!', id=2))
# db.delete(2)