def parse_order(text):
    if not isinstance(text, str) or ':' not in text:
        return None, 0
    try:
        parts = text.split(':', 1)
        size = parts[0].strip().upper()
        copies = int(parts[1])
        return size, copies
    except (ValueError, IndexError):
        return None, 0

def file_size_average(sizes_csv):
    if not isinstance(sizes_csv, str) or not sizes_csv.strip():
        return 0
    values = []
    for r in sizes_csv.split(','):
        try:
            values.append(int(r.strip()))
        except ValueError:
            pass
    if not values:
        return 0
    return sum(values) // len(values)

def payable_amount(text):
    if not isinstance(text, str) or '|' not in text:
        return 0.0
    try:
        parts = text.split('|', 1)
        amount = float(parts[0])
        discount = float(parts[1])
        total = amount * 1.18 - discount
        return max(total, 0.0)
    except ValueError:
        return 0.0

def main():
    print("==== Running parse_order ====")
    user_input = input("Enter print size:copies (e.g. 4x6:25): ")
    result = parse_order(user_input)
    print("Size and Copies:", result)

    print("\n==== Running file_size_average ====")
    user_input = input("Enter file sizes in MB as CSV (e.g. 4,8,12): ")
    result = file_size_average(user_input)
    print("Average File Size:", result)

    print("\n==== Running payable_amount ====")
    user_input = input("Enter amount|discount (e.g. 450|50): ")
    result = payable_amount(user_input)
    print("Payable Amount:", result)

if __name__ == "__main__":
    main()