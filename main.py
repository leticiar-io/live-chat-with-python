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

   chat = ft.Column() # chat é uma coluna

   def enviar_mensagem_para_geral(mensagem): 
      texto_chat = ft.Text(mensagem)
      chat.controls.append(texto_chat)

      pagina.update()

   pagina.pubsub.subscribe(enviar_mensagem_para_geral)

   def enviar_mensagem(evento):
      texto_mensagem = campo_mensagem.value
      nome_usuario = campo_nome_usuario.value
      mensagem = f"{nome_usuario}: {texto_mensagem}"
      pagina.pubsub.send_all(mensagem) # envia a mensagem para todos os inscritos
      campo_mensagem.value = ""
      pagina.update()

   campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
   botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

   linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])   

   def entrar_chat(evento):
      pagina.remove(titulo)
      pagina.remove(botao_iniciar)
      janela.open = False

      pagina.add(chat)
      pagina.add(linha_mensagem)
      # append - adicionar no final da lista
      mensagem_entrar_chat = f"{campo_nome_usuario.value} entrou no chat"
      pagina.pubsub.send_all(mensagem_entrar_chat)
      chat.controls.append()

      pagina.update()

   botao_enviar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
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
