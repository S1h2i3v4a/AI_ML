# Lecture 05.10: In-Class Practice Problem: Banking Account System (हिंग्लिश)

## 📌 Module Overview
In-Class banking system ka complete OOP implementation: balance check, deposits, overdraft protection ke saath withdrawals, aur audit logs.

---

## 🔬 Core Concepts Aur Detailed Breakdown
### 1. Banking System Ka OOP Design
Real-world banking account mein:
- Balance negative nahi hona chahiye (overdraft protection).
- Deposit ya Withdraw karte waqt amount positive ($>0$) hona chahiye.
- Har transaction ka ek audit log (history) maintain hona chahiye.

---

## 💻 Python Code Aur Implementation
```python
class BankAccount:
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit rejected: amount must be strictly positive.")
            return False
        self.balance += amount
        self.transactions.append(f"DEPOSIT: +${amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal rejected: amount must be strictly positive.")
            return False
        if amount > self.balance:
            print(f"Withdrawal rejected: Insufficient funds (Available: ${self.balance:.2f}).")
            return False
        self.balance -= amount
        self.transactions.append(f"WITHDRAW: -${amount:.2f}")
        return True

    def get_summary(self) -> str:
        return f"Account [{self.account_number}] | Owner: {self.owner} | Balance: ${self.balance:,.2f}"

acc = BankAccount("ACC-101", "Alice", 500.0)
acc.deposit(200.0)
acc.withdraw(150.0)
acc.withdraw(800.0)  # Should reject
print(acc.get_summary())
```

---

## ⚙️ Complexity Aur Systems Notes
- **Time Complexity:** Method dispatch $\mathcal{O}(1)$ descriptor lookup time leta hai.
- **Space Complexity:** Memory footprint instance attributes aur class namespace par depend karta hai.
