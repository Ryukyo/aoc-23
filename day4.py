with open('day4.txt', 'r') as f:
    card_value_total = 0
    for idx, line in enumerate(f.readlines()):
        parts = line.split("|")

        winning_numbers = {int(num) for num in parts[0].split() if num.isdigit()}
        existing_numbers = {int(num) for num in parts[1].split() if num.isdigit()}

        count_matches = len(set(winning_numbers) & set(existing_numbers))
        if count_matches > 0:
            card_value_total += 2 ** (count_matches - 1)
    print(card_value_total)