def calculate_earnings(total_earnings):
    for x in range(1, total_earnings):
        petya_catch = total_earnings - x - 18
        vasya_catch = total_earnings - petya_catch

        if vasya_catch - petya_catch == 14:
            return (petya_catch, vasya_catch)

    return None


total_earnings = 90000

earnings = calculate_earnings(total_earnings)
if earnings:
    print("Петя заработал:", earnings[0], "рублей")
    print("Вася заработал:", earnings[1], "рублей")
else:
    print("Невозможно определить заработок каждого")