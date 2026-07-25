class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   # public
        self._balance = balance                # protected (by convention)
        self.__pin = "1234"                    # private (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount, pin):
        if pin == self.__pin:   # private variable used internally
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. Remaining balance: {self._balance}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid PIN")

    def show_balance(self):
        print(f"Balance for {self.account_holder}: {self._balance}")

acc = BankAccount("Snehasish", 1000)

print(acc.account_holder)   # ✅ public
print(acc._balance)         # ✅ accessible, but discouraged (protected)
# print(acc.__pin)          # ❌ AttributeError (private)

acc.deposit(500)            # ✅ safe deposit
acc.withdraw(300, "1234")   # ✅ correct PIN
acc.withdraw(200, "9999")   # ❌ wrong PIN
acc.show_balance()

