import numpy as np
import pandas as pd
import os
import kagglehub

class Actividad3:
    def __init__(self):
        self.ruta_raiz = os.path.abspath(os.getcwd())
        self.ruta_act2 = os.path.join(self.ruta_raiz, "src", "ejercicios", "actividad_3")

        datos = {
            "n_punto": list(range(1, 13)),
            "detalle": [
                "Crea un DataFrame frutas que luzca así",
                "Crea un DataFrame ventas_frutas con los datos indicados",
                "Crea una Serie utensilios con los datos indicados",
                "", "", "", "", "", "", "", "", ""
            ],
            "resultado": [0] * 12
        }
        self.df = pd.DataFrame(datos)
        self.df["resultado"] = self.df["resultado"].astype(object)

    def punto_1(self):
        df_frutas = pd.DataFrame([[20, 50]], columns=["Granadilla", "Tomates"])
        resultado_str = df_frutas.to_string(index=False)
        self.df.loc[0, "resultado"] = resultado_str
        print(df_frutas)

    def punto_2(self):
        ventas_frutas = pd.DataFrame(
            [[20, 50], [49, 100]],
            index=["ventas 2021", "ventas 2022"],
            columns=["Granadilla", "Tomates"]
        )
        resultado_str = ventas_frutas.to_string()
        self.df.loc[1, "resultado"] = resultado_str
        print(ventas_frutas)

    def punto_3(self):
        utensilios = pd.Series(
            ["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
            index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
            name="Cocina"
        )
        resultado_str = utensilios.to_string()
        self.df.loc[2, "resultado"] = resultado_str
        print(utensilios)

    def punto_4(self):
        path = kagglehub.dataset_download("zynicide/wine-reviews")
        print("Path to dataset files:", path)

    def punto_5(self):
        self.df.loc[4, "resultado"] = len(self.df) + 4

    def punto_6(self):
        self.df.loc[5, "resultado"] = "punto_5.csv"

    def punto_7(self):
        self.df.loc[6, "resultado"] = len(self.df) + 6

    def punto_8(self):
        self.df.loc[7, "resultado"] = len(self.df) + 7

    def punto_9(self):
        self.df.loc[8, "resultado"] = len(self.df) + 8

    def punto_10(self):
        self.df.loc[9, "resultado"] = len(self.df) + 9

    def punto_11(self):
        self.df.loc[10, "resultado"] = len(self.df) + 10

    def punto_12(self):
        self.df.loc[11, "resultado"] = len(self.df) + 11

    def ejecutar(self):
        self.punto_1()
        self.punto_2()
        self.punto_3()
        self.punto_4()
        self.punto_5()
        self.punto_6()
        self.punto_7()
        self.punto_8()
        self.punto_9()
        self.punto_10()
        self.punto_11()
        self.punto_12()

        self.df.to_csv("actividad3.csv", index=False)
        print("Resultados guardados en actividad3.csv")

act = Actividad3()
act.ejecutar()
