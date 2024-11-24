salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
months_count = 0

while True:
    money_capital = money_capital + spend - salary
    spend = spend * (1 + increase)
    months_count += 1
    if months_count == months:
        break

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
