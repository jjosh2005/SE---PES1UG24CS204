
RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}


def units_consumed(reading):
    if not isinstance(reading, str):
        raise ValueError("Reading must be a string")

    parts = reading.split(":")

    if len(parts) != 2:
        raise ValueError("Expected previous:current format")

    try:
        previous = int(parts[0].strip())
        current = int(parts[1].strip())
    except ValueError:
        raise ValueError("Meter readings must be integers")

    if previous < 0 or current < 0:
        raise ValueError("Readings cannot be negative")

    if current < previous:
        raise ValueError("Current reading cannot be less than previous")

    return current - previous


def daily_average(units_csv):
    if not isinstance(units_csv, str):
        raise ValueError("Input must be a string")

    if not units_csv.strip():
        raise ValueError("Input cannot be empty")

    parts = units_csv.split(",")

    if any(not part.strip() for part in parts):
        raise ValueError("Empty CSV values are not allowed")

    try:
        units = [int(u.strip()) for u in parts]
    except ValueError:
        raise ValueError("Daily units must be integers")

    if any(u < 0 for u in units):
        raise ValueError("Daily units cannot be negative")

    return round(sum(units) / len(units), 2)


def tariff_rate(code):
    if not isinstance(code, str):
        raise ValueError("Tariff code must be a string")

    parts = code.split("-")

    if len(parts) != 2:
        raise ValueError("Expected CATEGORY-SLAB format")

    category = parts[0].strip().upper()
    slab = parts[1].strip().upper()

    if category not in RATES:
        raise ValueError("Invalid tariff category")

    if slab not in SLAB:
        raise ValueError("Invalid tariff slab")

    return RATES[category] * SLAB[slab]


def main():
    print("==== Running units_consumed ====")
    try:
        user_input = input(
            "Enter meter readings as previous:current (e.g. 1200:1350): "
        )
        print("Units Consumed:", units_consumed(user_input))
    except ValueError as e:
        print("Input Error:", e)

    print("\n==== Running daily_average ====")
    try:
        user_input = input("Enter daily units as CSV (e.g. 5,7,6): ")
        print("Daily Average:", daily_average(user_input))
    except ValueError as e:
        print("Input Error:", e)

    print("\n==== Running tariff_rate ====")
    try:
        user_input = input("Enter a tariff code (e.g. DOM-A): ")
        print("Rate per Unit:", tariff_rate(user_input))
    except ValueError as e:
        print("Input Error:", e)


if __name__ == "__main__":
    main()

