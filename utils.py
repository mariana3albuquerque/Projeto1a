import json

def extract_route(request):
    linhas = request.split(" ")
    return linhas[1][1:]

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