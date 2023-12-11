
comandos_git = '''

Iniciar o Repositório Local: git init

Verificar a Conexão: git remote -v

Push (Envio): git push -u origin main

Pull (Recebimento) : git pull origin main

Atualizar (Sincronizar): git fetch origin

Diferenças : git diff main origin/main

Adicionar: git add .

Criar um Commit : git commit -m "MENSAGEM_DE_COMMIT"

'''

h1 = 1080
w1 = 1920

h2 = 600
w2 = 1024

height = h2  / h1

width = w2 / w1

titulo = {'width': 123, 'height':116}
botoes = {'width': 212, 'height':272}
geradores = {'width': 190, 'height':1304}
transformadores = {'width': 131, 'height':1005}
reles = {'width': 150, 'height':781}

# calculo de proporção de tamanho de ajuste de imagem

print('Proporção Titulo: ',int(titulo['width']* width), int(titulo['height']* height))
print('Proporção Botoes: ',int(botoes['width']* width), int(botoes['height']* height))