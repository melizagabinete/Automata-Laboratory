#no1
accepted_no1 = {"101", "1000", "110101"}
rejected_no1 = {"100", "110", "1001"}

#no2
accepted_no2 = {"aa", "aaba", "ab"}
rejected_no2 = {"aab", "abb", "aba"}

def check_string(s, choice):
    if choice == "1":
        if s in accepted_no1:
            return "Accepted"
        elif s in rejected_no1:
            return "Rejected"
        else:
            return "Not in the example"
    elif choice == "2":
        if s in accepted_no2:
            return "Accepted"
        elif s in rejected_no2:
            return "Rejected"
        else:
            return "Rejected"
    else:
        return "Try again."

if __name__ == "__main__":
    while True:
        choice = input("Choose no to answer (1 or 2), or 'x' to quit: ").strip()
        if choice.lower() == 'x':
            break
        if choice not in ("1", "2"):
            print("Invalid choice. Please enter 1, 2, or x.")
            continue
        user_input = input("Enter your string: ").strip()
        result = check_string(user_input, choice)
        print(result)