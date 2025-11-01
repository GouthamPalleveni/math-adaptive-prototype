def adjust_difficulty(records, current_level):
    if len(records) < 2:
        return current_level

    last_two = records[-2:]
    correct_answers = sum(1 for r in last_two if r["correct"])

    levels = ["Easy", "Medium", "Hard"]
    i = levels.index(current_level)

    if correct_answers == 2 and i < 2:
        return levels[i + 1]
    elif correct_answers == 0 and i > 0:
        return levels[i - 1]
    return current_level
