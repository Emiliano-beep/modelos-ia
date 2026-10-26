from langchain_ollama import ChatOllama

class ModeloLlama:
    def __init__(self):
        # Conectamos con el nombre que acabamos de registrar en Ollama
        self.modelo = ChatOllama(model="llama3.2-local", temperature=0.1)
        
    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.content