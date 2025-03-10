import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Actividad2:
    def __init__(self):
        self.resultados = []
    
    def ejercicio_1(self):
        array = np.arange(10, 30)
        self.resultados.append(("Ejercicio 1", array.tolist()))
        return array
    
    def ejercicio_2(self):
        matriz = np.ones((10, 10))
        suma = matriz.sum()
        self.resultados.append(("Ejercicio 2", suma))
        return suma
    
    def ejercicio_3(self):
        array1 = np.random.randint(1, 11, 5)
        array2 = np.random.randint(1, 11, 5)
        producto = array1 * array2
        self.resultados.append(("Ejercicio 3", producto.tolist()))
        return producto
    
    def ejercicio_4(self):
        matriz = np.fromfunction(lambda i, j: i + j, (4, 4))
        inversa = np.linalg.pinv(matriz)  # Se usa pseudo-inversa para evitar error
        self.resultados.append(("Ejercicio 4", inversa.tolist()))
        return inversa
    
    def ejercicio_5(self):
        array = np.random.rand(100)
        max_index = np.argmax(array)
        min_index = np.argmin(array)
        self.resultados.append(("Ejercicio 5 - Máximo", max_index))
        self.resultados.append(("Ejercicio 5 - Mínimo", min_index))
        return max_index, min_index
    
    def ejercicio_6(self):
        array1 = np.ones((3, 1))
        array2 = np.ones((1, 3))
        resultado = array1 + array2
        self.resultados.append(("Ejercicio 6", resultado.tolist()))
        return resultado
    
    def ejercicio_7(self):
        matriz = np.random.randint(1, 10, (5, 5))
        submatriz = matriz[1:3, 1:3]
        self.resultados.append(("Ejercicio 7", submatriz.tolist()))
        return submatriz
    
    def ejercicio_8(self):
        array = np.zeros(10)
        array[3:7] = 5
        self.resultados.append(("Ejercicio 8", array.tolist()))
        return array
    
    def ejercicio_9(self):
        matriz = np.random.randint(1, 10, (3, 3))
        invertida = matriz[::-1]
        self.resultados.append(("Ejercicio 9", invertida.tolist()))
        return invertida
    
    def ejercicio_10(self):
        array = np.random.rand(10)
        seleccionados = array[array > 0.5]
        self.resultados.append(("Ejercicio 10", seleccionados.tolist()))
        return seleccionados
    
    def ejercicio_11(self):
        x = np.random.rand(100)
        y = np.random.rand(100)
        plt.scatter(x, y, color='blue', alpha=0.5)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Gráfico de Dispersión")
        plt.grid(True)
        plt.savefig("grafico_dispersion.png")  # Guardar el gráfico
        plt.show()
        self.resultados.append(("Ejercicio 11", "Grafico guardado"))
    
    def ejecutar_todos(self):
        self.ejercicio_1()
        self.ejercicio_2()
        self.ejercicio_3()
        self.ejercicio_4()
        self.ejercicio_5()
        self.ejercicio_6()
        self.ejercicio_7()
        self.ejercicio_8()
        self.ejercicio_9()
        self.ejercicio_10()
        self.ejercicio_11()
        
        df = pd.DataFrame(self.resultados, columns=["# Ejercicio", "Valor"])
        df.to_excel("actividad_2.xlsx", index=False)
        print("Resultados guardados en actividad_2.xlsx")

# Crear instancia y ejecutar todo
actividad = Actividad2()
actividad.ejecutar_todos()