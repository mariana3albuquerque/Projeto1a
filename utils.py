import json

def extract_route(request):
     return request.split()[1][1:] if len(request.split()) > 1 else ""

def read_file(path):
    with open(path, "rb") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def load_data(note):
    with open("data/" + note, 'r') as arquivo:
        conteudo = arquivo.read()
    return json.loads(conteudo)

def load_template(archive):
    #devolve uma string com o conteudo do arquivo
    with open("templates/" + archive, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def build_response(body='', code=200, reason='OK', headers=''):
    "Retorna a resposta do servidor"
    if headers == '':
        headers = "Content-Type: text/html; charset=utf-8"
    return (f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}").encode("utf-8")