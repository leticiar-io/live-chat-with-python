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
   titulo = ft.Text("ZapZap")

   #popup
   titulo_janela = ft.Text("Bem-vindo ao ZapZap!")
   campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

   def iniciar_chat(evento):
      pagina.remove(titulo)
      pagina.remove(botao_iniciar)
      janela.open = False
      
      pagina.update()

   botao_enviar = ft.ElevatedButton("Entrar no chat", on_click=iniciar_chat)
   janela = ft.AlertDialog(
      title=titulo_janela, 
      content=campo_nome_usuario, 
      actions=[botao_enviar]
   )

   def iniciar_chat(evento):
      pagina.dialog = janela
      janela.open = True
      pagina.update()

   botao_iniciar = ft.ElevatedButton("Iniciar o chat", on_click=iniciar_chat)

   pagina.add(titulo)
   pagina.add(botao_iniciar)


# 3. Rodar o aplicativo
ft.app(main, view=ft.WEB_BROWSER)
