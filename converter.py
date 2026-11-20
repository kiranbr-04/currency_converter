print("1. INR to USD")
print("2. USD to INR")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    inr = float(input("Enter INR: "))
    ex_rate = inr/93.36
    print(f"USD:, {ex_rate:.2f}")

elif choice == 2:
    usd = float(input("Enter USD: "))
    print("INR:", usd * 93.36)

elif choice == 3:
    print('EXIT')

else:
    print("Invalid choice")
