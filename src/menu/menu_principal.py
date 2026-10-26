from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq
from src.modelos.modelo_local import ModeloLocal
from src.modelos.modelo_llama import ModeloLlama
from src.modelos.prompt_01 import Prompt01
from src.modelos.prompt_02 import Prompt_02


import os 
from rich.console import Console
from rich.markdown import Markdown


class MenuPrincipal():
    def __init__(self):
        self.console = Console()
        self.opcion = 0

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("\nPresione Enter para volver al menu...")

    def mostrar_menu(self):
        print("== Menu Principal ===")
        print("1. Modelo Google API KEY")
        print("2. Modelo Groq API KEY")
        print("3. Modelo Local (Ollama)")
        print("4. Modelo Llama")
        print("5. Modelo Prompt01")
        print("6. Modelo Prompt02")
        print("0. Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                modelo_google = ModeloGoogle()
                promt = input("Inngrese su promt: ")
                respuesta = modelo_google.generar_respuestas(promt)
                print("Respuesta del modelo Google:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "2":
                modelo_groq = ModeloGroq()
                promt = input("Ingrese su promt: ")
                respuesta = modelo_groq.generar_respuesta(promt)
                print("Respuesta del modelo Groq:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "3":
                modelo_local = ModeloLocal()
                promt = input("Ingrese su promt: ")
                respuesta = modelo_local.generar_respuesta(promt)
                print("Respuesta del modelo Local:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))


            elif self.opcion == "4":
                modelo_llama = ModeloLlama()
                promt = input("Ingrese su promt: ")
                respuesta = modelo_llama.generar_respuesta(promt)
                print("Respuesta del modelo Llama:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))


            elif self.opcion == "5":
                prompt_01 = Prompt01()
                respuesta = prompt_01.generar_respuesta()
                print("Respuesta del modelo Prompt01:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "6":
                prompt_02 = Prompt_02()
                respuesta = prompt_02.generar_respuesta()
                print("Respuesta del modelo Prompt02:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion == "0":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

            self.pausar()