import tkinter as tk
from tkinter import ttk

class FitnessApp:
    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura
        self.objetivos = {
            "Perder peso": ["Corrida", "Treino de resistência", "Dieta balanceada"],
            "Ganhar massa muscular": ["Levantamento de peso", "Treino de hipertrofia", "Dieta rica em proteínas"],
            "Condicionamento cardiovascular": ["Ciclismo", "Natação", "Treino aeróbico"],
            "Competição": ["Treino específico para a modalidade", "Treino de força", "Dieta personalizada"]
        }

    def gerar_treino_semanal(self, objetivo):
        # Lógica para gerar um treino semanal com base no objetivo
        # Aqui você pode personalizar a lógica com base nas preferências e metas específicas
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        treino_semanal = {dia: objetivo for dia in dias_semana}
        return treino_semanal

class FitnessAppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fitness App")
        self.geometry("600x400")

        self.nome_label = ttk.Label(self, text="Nome:")
        self.peso_label = ttk.Label(self, text="Peso (kg):")
        self.idade_label = ttk.Label(self, text="Idade:")
        self.altura_label = ttk.Label(self, text="Altura (m):")

        self.nome_entry = ttk.Entry(self)
        self.peso_entry = ttk.Entry(self)
        self.idade_entry = ttk.Entry(self)
        self.altura_entry = ttk.Entry(self)

        self.nome_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.peso_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.idade_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.altura_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        self.peso_entry.grid(row=1, column=1, padx=10, pady=5)
        self.idade_entry.grid(row=2, column=1, padx=10, pady=5)
        self.altura_entry.grid(row=3, column=1, padx=10, pady=5)

        self.objetivo_label = ttk.Label(self, text="Objetivo:")
        self.objetivo_combobox = ttk.Combobox(self, values=["Perder peso", "Ganhar massa muscular", "Condicionamento cardiovascular", "Competição"])
        self.objetivo_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.objetivo_combobox.grid(row=4, column=1, padx=10, pady=5)

        self.calcular_button = ttk.Button(self, text="Calcular Treino", command=self.exibir_treino)
        self.calcular_button.grid(row=5, column=0, columnspan=2, pady=10)

    def exibir_treino(self):
        nome = self.nome_entry.get()
        peso = float(self.peso_entry.get())
        idade = int(self.idade_entry.get())
        altura = float(self.altura_entry.get())
        objetivo = self.objetivo_combobox.get()

        app = FitnessApp(nome, peso, idade, altura)
        treino = app.gerar_treino_semanal(app.objetivos[objetivo])

        resultado_window = tk.Toplevel(self)
        resultado_window.title("Treino Semanal")
        resultado_window.geometry("600x400")

        resultado_text = tk.Text(resultado_window, wrap=tk.WORD, height=20, width=60)
        resultado_text.grid(row=0, column=0, padx=10, pady=10)

        for dia, exercicios in treino.items():
            resultado_text.insert(tk.END, f"{dia}:\n")
            for exercicio in exercicios:
                resultado_text.insert(tk.END, f"{exercicio}\n")
            resultado_text.insert(tk.END, "\n")

        resultado_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = FitnessAppGUI()
    app.mainloop()
