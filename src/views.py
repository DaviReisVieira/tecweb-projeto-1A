from utils import load_data, load_template, add_to_database, build_response, remove_from_database, update_database
import urllib

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            key_value = chave_valor.split('=')
            key = urllib.parse.unquote_plus(key_value[0])
            value = urllib.parse.unquote_plus(key_value[1])
            params[key] = value

        if params['method']=='CREATE':
            add_to_database(params, "banco")
        elif params['method']=='DELETE':
            remove_from_database(params, "banco")
        elif params['method']=='UPDATE':
            update_database(params, "banco")
        
        return build_response(code=303, reason='See Other', headers='Location: /')
 
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id= dados.id, title=dados.title, content=dados.content)
        for dados in load_data('banco')
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes).encode())