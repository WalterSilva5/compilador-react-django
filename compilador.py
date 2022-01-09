import os
import shutil
from sys import path
path_atual = str(list(path)[0])


def exec_build():
    ajusta_pagina_index()
    mover_arquivos()
    
def ajusta_pagina_index():
    pagina_index_path = path_atual + "/dist/index.html"
    arquivo_pagina = open(pagina_index_path, "r")
    texto_pagina = arquivo_pagina.readlines()
    novo_texto = []
    arquivo_pagina.close()

    for linha in texto_pagina:
        #remove linha que contenha svg
        if "svg" in linha:
            continue
        #ajusta href ou src para formato django
        if "href" in linha:
            linha = linha.replace("href=\"", "href=\"{% static 'nome_django_app")
        if "src" in linha:
            linha = linha.replace("src=\"", "src=\"{% static 'nome_django_app")
        if ".js" in linha:
            linha = linha.replace(".js", ".js\' %}")
        if ".css" in linha:
            linha = linha.replace(".css", ".css\' %}")
        novo_texto.append(linha)
        
    #escreve novo arquivo
    novo_arquivo = open(pagina_index_path, "w")
    novo_arquivo.writelines(novo_texto)
    novo_arquivo.close()
        
def mover_arquivos():
    path_api_assets = path_atual.replace("nome_web_app",
                                  "teste")+"/nome_django_app/static/nome_django_app/assets"
    if os.path.exists(path_api_assets):
        shutil.rmtree(path_api_assets)
    
    #mover assets para api
    shutil.copytree(path_atual+"/dist/assets", path_api_assets)
    
    
    path_api_templates = path_atual.replace("nome_web_app",
                                  "teste")+"/nome_django_app/templates/"
    #mover index.html para pasta de templates
    shutil.copy(path_atual+"/dist/index.html", path_api_templates)     
    
if __name__ == "__main__":
    exec_build()
    
