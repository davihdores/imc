import tkinter as tk
from tkinter import messagebox, ttk


class CalculadoraIMC:
    """Organiza a interface e as operações de cálculo do IMC."""

    def __init__(self, janela: tk.Tk) -> None:
        self.janela = janela
        self.janela.title("Cálculo do IMC - Indice de Massa Corporal")
        self.janela.geometry("690x350")
        self.janela.minsize(650, 330)

        self.nome = tk.StringVar()
        self.endereco = tk.StringVar()
        self.altura = tk.StringVar()
        self.peso = tk.StringVar()
        self.resultado = tk.StringVar(value="Resultado")

        self.montar_tela()

    def montar_tela(self) -> None:
        area = ttk.Frame(self.janela, padding=18)
        area.pack(fill="both", expand=True)
        area.columnconfigure(1, weight=1)
        area.columnconfigure(2, weight=1)

        ttk.Label(area, text="Nome do Paciente:").grid(
            row=0, column=0, sticky="w", pady=8, padx=(0, 12)
        )
        campo_nome = ttk.Entry(area, textvariable=self.nome)
        campo_nome.grid(row=0, column=1, columnspan=2, sticky="ew", pady=8)

        ttk.Label(area, text="Endereço Completo:").grid(
            row=1, column=0, sticky="w", pady=8, padx=(0, 12)
        )
        ttk.Entry(area, textvariable=self.endereco).grid(
            row=1, column=1, columnspan=2, sticky="ew", pady=8
        )

        ttk.Label(area, text="Altura (cm):").grid(
            row=2, column=0, sticky="w", pady=8, padx=(0, 12)
        )
        ttk.Entry(area, textvariable=self.altura, width=20).grid(
            row=2, column=1, sticky="ew", pady=8, padx=(0, 14)
        )

        ttk.Label(area, text="Peso (kg):").grid(
            row=3, column=0, sticky="w", pady=8, padx=(0, 12)
        )
        ttk.Entry(area, textvariable=self.peso, width=20).grid(
            row=3, column=1, sticky="ew", pady=8, padx=(0, 14)
        )

        painel = ttk.LabelFrame(area, text="Resultado do IMC", padding=12)
        painel.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=5)
        ttk.Label(
            painel, textvariable=self.resultado, anchor="center", justify="center",
            wraplength=210, font=("Arial", 11)
        ).pack(fill="both", expand=True)

        botoes = ttk.Frame(area)
        botoes.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(32, 0))
        botoes.columnconfigure(0, weight=1)
        botoes.columnconfigure(1, weight=1)
        botoes.columnconfigure(2, weight=1)

        ttk.Button(botoes, text="Calcular", command=self.calcular).grid(
            row=0, column=0, padx=5, sticky="ew"
        )
        ttk.Button(botoes, text="Reiniciar", command=self.reiniciar).grid(
            row=0, column=1, padx=5, sticky="ew"
        )
        ttk.Button(botoes, text="Sair", command=self.janela.destroy).grid(
            row=0, column=2, padx=5, sticky="ew"
        )
        campo_nome.focus()

    @staticmethod
    def classificar_imc(indice: float) -> str:
        """Classificação de IMC usada como referência para adultos."""
        if indice < 18.5:
            return "Abaixo do peso"
        if indice < 25:
            return "Peso normal"
        if indice < 30:
            return "Sobrepeso"
        if indice < 35:
            return "Obesidade grau I"
        if indice < 40:
            return "Obesidade grau II"
        return "Obesidade grau III"

    def calcular(self) -> None:
        try:
            # Aceita tanto vírgula quanto ponto como separador decimal.
            altura_cm = float(self.altura.get().strip().replace(",", "."))
            peso_kg = float(self.peso.get().strip().replace(",", "."))
        except ValueError:
            messagebox.showwarning(
                "Dados inválidos", "Informe valores numericos para altura e peso."
            )
            return

        if not (50 <= altura_cm <= 250) or not (2 <= peso_kg <= 500):
            messagebox.showwarning(
                "Verifique os dados informados",
                "Informe sua altura entre 50 e 250 cm e um peso entre 2 e 500 kg."
            )
            return

        altura_m = altura_cm / 100
        indice = peso_kg / (altura_m ** 2)
        classificacao = self.classificar_imc(indice)
        pessoa = self.nome.get().strip()
        saudacao = f"{pessoa}\n" if pessoa else ""

        self.resultado.set(
            f"{saudacao}IMC: {indice:.2f}\n{classificacao}".replace(".", ",")
        )

    def reiniciar(self) -> None:
        self.nome.set("")
        self.endereco.set("")
        self.altura.set("")
        self.peso.set("")
        self.resultado.set("Resultado")


def main() -> None:
    janela = tk.Tk()
    CalculadoraIMC(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
