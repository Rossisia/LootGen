import random
from tabulate import tabulate

class LootBox:
    def __init__(self, name: str, drop_rates: dict):
        self.name = name
        self.drop_rates = drop_rates  # предмет -> вероятность (0..1)

    def open(self) -> str:
        rand = random.random()
        cumulative = 0.0
        for item, prob in self.drop_rates.items():
            cumulative += prob
            if rand < cumulative:
                return item
        return "ничего"  # на случай ошибки округления

def main():
    # Сундук с лутом: предметы и их вероятности
    box = LootBox("Обычный сундук", {
        "меч": 0.3,
        "щит": 0.2,
        "зелье": 0.4,
        "редкий самоцвет": 0.1
    })

    print(f"Открываем {box.name} 10 раз:")
    results = []
    for i in range(1, 11):
        item = box.open()
        results.append([i, item])

    # Красивый вывод таблицы через стороннюю библиотеку
    headers = ["Попытка", "Выпавший предмет"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()