from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class Prompt_Roles:
    def __init__(self):
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.1)

    def generar_respuesta(self):
        plantilla = ChatPromptTemplate.from_messages({
            ("system",
             """
             Eres un profesor de universidad de programacion.messages=
             
             Instrucciones:
                - Responde siempre en español.
                - Utiliza un lenguaje sencillo.
                - Explica los conceptos paso a paso.
                - Incluye un ejemplo en python.
                - No utilices tecnisismos inecesarios.
             """
             ),
             ("human",
              "Explicame el siguiente tema: {tema}")
                 
        })
        mensaje = plantilla.invoke({"tema": "estructura condicionales"})
        respuesta = self.modelo.invoke(mensaje)
        return respuesta.text


        