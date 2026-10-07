def evaluate(target, guess):
    result = ["gray"] * len(guess)

    # First, mark exact matches and remove those target occurrences.
    remaining = {}
    for ch in target:
        remaining[ch] = remaining.get(ch, 0) + 1

    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[ch] -= 1

    # Then, mark non-exact letters only while an unused
    # occurrence remains in the target.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result