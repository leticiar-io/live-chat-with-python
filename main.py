# Título 
# Botao iniciar zap
   # popup 
   # Título: Bem vindo ao zap
   # Campo de texto - Escreva seu nome no chat
   # Botão: Entrar no chat
      # Sumir com o título zap
      # Fechar a janela (popup)
      # Carregar o chat 
         # As mensagens que já foram enviadas
         # Campo de texto
         # Botão enviar

# Flet - Cria o front e o back junto

# Sempre que formos fazer o sistema com flet, devemos: 
# 1. Importar o flet
import flet as ft

# 2. Criar a função principal do seu aplicativo
def main(pagina):
   # criar funcionalidades 
   titulo = ft.Text("Bem-vindo(a) ao ZapZap!")
   botao_iniciar = ft.ElevatedButton("Iniciar o chat")
   pagina.add(titulo)
   pagina.add(botao_iniciar)


# 3. Rodar o aplicativo
ft.app(main)
