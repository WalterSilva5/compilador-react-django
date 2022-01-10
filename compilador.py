import os
import shutil
from sys import path
import json
import time

def exec_build(
    master,
    caminho_static,
    caminho_template,
    caminho_react):
    try:
        
        ajusta_pagina_index(
            master,
            caminho_static,
            caminho_template,
            caminho_react)
        mover_arquivos(
                master,
            caminho_static,
            caminho_template,
            caminho_react)
        salvar_configuracoes(master)
        master.erro.set(False)
        master.mensagem.set('Compilado com sucesso')
    except:
        master.mensagem.set('Erro ao compilar')
        master.erro.set(True)
    master.frame_mensagem.refresh()
    
def ajusta_pagina_index(
    master,
    caminho_static,
    caminho_template,
    caminho_react):
    caminho_teste  = "/".join(caminho_react.split('/')[:-1])
    os.chdir(caminho_teste)
    os.system("npm run build")
    pagina_index_path = caminho_react + "/index.html"
    arquivo_pagina = open(pagina_index_path, "r")
    texto_pagina = arquivo_pagina.readlines()
    novo_texto = []
    arquivo_pagina.close()
    nome_do_app = caminho_template.split("/")[-3]
    
    for linha in texto_pagina:
        #remove linha que contenha svg
        if "svg" in linha:
            continue
        #ajusta href ou src para formato django
        if "href" in linha:
            linha = linha.replace("href=\"", "href=\"{% static '"+nome_do_app)
        if "src" in linha:
            linha = linha.replace("src=\"", "src=\"{% static '"+nome_do_app)
        if ".js" in linha and nome_do_app in linha:
            linha = linha.replace(".js", ".js\' %}")
        if ".css" in linha and nome_do_app in linha:
            linha = linha.replace(".css", ".css\' %}")
        novo_texto.append(linha)
        
    #remove arquivo antigo
    try:
        os.remove(pagina_index_path)
    except:
        pass
        
    #escreve novo arquivo
    novo_arquivo = open(pagina_index_path, "w")
    novo_arquivo.writelines(novo_texto)
    novo_arquivo.close()
        
def mover_arquivos(
    master,
    caminho_static,
    caminho_template,
    caminho_react):
    path_api_assets = caminho_static+"/assets"
    if os.path.exists(path_api_assets):
        shutil.rmtree(path_api_assets)
    
    #mover assets para api
    shutil.copytree(caminho_react+"/assets", path_api_assets)
    
    shutil.copy(caminho_react+"/index.html", caminho_template)   
    
def salvar_configuracoes(master):
    caminho_config = path[0]+"/config.json"
    try:
        os.remove()
    except:
        pass
    data = {
        'caminho_static': master.frame_django_static.input_django_static.get(),
        'caminho_template': master.frame_django_template.input_django_template.get(),
        'caminho_react': master.frame_react_static.input_react_dist.get()
    }
    with open(caminho_config, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    exec_build()
    
