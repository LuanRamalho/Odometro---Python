import tkinter as tk
from tkinter import messagebox

class OdometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Odômetro")
        self.root.geometry("400x300")
        self.root.configure(bg="#e1f5fe")  # Fundo azul claro

        self.total_km = 0

        # Label para o título
        title_label = tk.Label(root, text="Odômetro", font=("Arial", 16, "bold"), bg="#0288d1", fg="white")
        title_label.pack(fill="x", pady=10)

        # Label para o total de quilômetros
        self.total_km_label = tk.Label(root, text="Total de Km: 0", font=("Arial", 14), bg="#b3e5fc", fg="black")
        self.total_km_label.pack(pady=20)

        # Frame para entrada de dados
        input_frame = tk.Frame(root, bg="#e1f5fe")
        input_frame.pack(pady=10)

        # Label para quilômetros rodados no dia
        day_km_label = tk.Label(input_frame, text="Km rodados hoje:", font=("Arial", 12), bg="#e1f5fe")
        day_km_label.grid(row=0, column=0, padx=5, pady=5)

        # Entrada de texto para quilômetros rodados no dia
        self.day_km_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.day_km_entry.grid(row=0, column=1, padx=5, pady=5)

        # Botão para adicionar quilômetros
        add_button = tk.Button(root, text="Adicionar", font=("Arial", 12), bg="#0288d1", fg="white", command=self.add_km)
        add_button.pack(pady=10)

    def add_km(self):
        try:
            day_km = float(self.day_km_entry.get())
            if day_km < 0:
                messagebox.showerror("Erro", "Por favor, insira um valor positivo.")
            else:
                self.total_km += day_km
                self.total_km_label.config(text=f"Total de Km: {self.total_km:.0f}")
                self.day_km_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OdometroApp(root)
    root.mainloop()
