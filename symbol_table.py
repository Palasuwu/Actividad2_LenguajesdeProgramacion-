class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name):
        if name not in self.symbols:
            self.symbols[name] = {"apariciones": 1}
        else:
            self.symbols[name]["apariciones"] += 1

    def display(self):
        print("\n" + "="*50)
        print(" - "*50)
        print(f"{'TABLA DE SIMBOLOS ':^50}")
        print("-" * 50)
        print(f"{'Identificador':<30} | {'Frecuencia'}")
        print("-" * 50)
        for name, data in self.symbols.items():
            print(f"{name:<30} | {data['apariciones']}")
        print("="*50)