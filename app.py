import re 
import pandas as pd  
import matplotlib.pyplot as plt  

def contar_palabras(archivo):
    # Abrimos el archivo en modo lectura ('r') y lo leemos como texto
    with open(archivo, 'r', encoding='utf-8') as file:
        texto = file.read()

    # Utilizamos una expresión regular para encontrar todas las palabras en el texto y las convertimos a minúsculas
    palabras = re.findall(r'\w+', texto.lower())
    
    num_total_palabras = len(palabras)  # Contamos el número total de palabras en el texto
    
    # Creamos una serie pandas con las palabras y contamos la frecuencia de cada una
    contador = pd.Series(palabras).value_counts()
    return contador, num_total_palabras

def visualizar_palabras_frecuentes(contador, num_palabras=10, num_total_palabras=None):
    # Obtenemos las 'num_palabras' palabras más frecuentes y las almacenamos en una nueva serie
    top_palabras = contador.head(num_palabras)
    
    # Invertimos el orden para que las palabras más frecuentes aparezcan arriba
    top_palabras = top_palabras[::-1]
    
    # Creamos un gráfico de barras horizontales con las palabras más frecuentes
    top_palabras.plot(kind='barh')
    
    plt.xlabel('Frecuencia')
    plt.ylabel('Palabra')
    plt.title('Palabras más frecuentes')
    
    # Invertimos el eje y para mostrar la palabra más frecuente en la parte superior
    plt.gca().invert_yaxis()
    
    if num_total_palabras is not None:
        plt.text(num_total_palabras/20, -1, f"Total de palabras: {num_total_palabras}", ha='left', va='center')
    
    # Mostramos el gráfico
    plt.show()

if __name__ == "__main__":
    archivo = "texto.txt" 
    contador, num_total_palabras = contar_palabras(archivo)  # Contamos las palabras en el archivo
    visualizar_palabras_frecuentes(contador, num_total_palabras=num_total_palabras)  # Visualizamos las palabras más frecuentes en un gráfico de barras
