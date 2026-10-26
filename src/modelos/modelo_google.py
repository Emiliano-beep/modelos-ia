from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


class ModeloGoogle:
    def __init__(self):
        load_dotenv() # Cargar variables de entorno desde el archivo .venv
        self.modelo = ChatGoogleGenerativeAI(model="gemini-3.5-flash-litle")

    def generar_respuestas(self,promt):
        respuesta= self.modelo.invoke(promt)
        return respuesta.text