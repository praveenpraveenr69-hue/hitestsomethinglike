# calculator.py
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time (years): "))

    si = calculate_simple_interest(p, r, t)
    print(f"The Simple Interest is: {si}")
