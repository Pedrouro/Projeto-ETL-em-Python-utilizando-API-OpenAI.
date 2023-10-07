import pandas as pd
import openai

openai.api_key = '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'

df = pd.read_csv("usuarios.csv")
df_dict = df.to_dict(orient='records')

def gerar_exercicio(user):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um personal trainer."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['Nome']} sobre uma recomendaçã de exercício fisico. (máximo de 50 caracteres)(a mensagem deve conter o nome da pessoa que sera recomendado o exercicio)"
      }
    ]
  )
    return completion.choices[0].message.content.strip('\"')

for indice, usuario in enumerate(df_dict):
    usuario['Exercicio'] = gerar_exercicio(usuario)
    print(usuario)
    print(usuario['Exercicio'])


df_atualizado = pd.DataFrame(df_dict)

df_atualizado.to_csv('usuarios.csv', index=False)

