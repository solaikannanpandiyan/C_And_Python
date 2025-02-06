from abc import ABC, abstractmethod

# ====================================================
# Account and Its Concrete Subclasses
# ====================================================

class Account(ABC):
    def __init__(self, account_number: str, balance: float = 0.0):
        self._account_number = account_number  # encapsulated attribute
        self._balance = balance                # encapsulated attribute

    @property
    def account_number(self):
        return self._account_number

    def get_balance(self) -> float:
        return self._balance

    @abstractmethod
    def deposit(self, amount: float):
        """Deposit amount into the account."""
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        """Withdraw amount from the account."""
        pass

    def __str__(self):
        return f"Account({self._account_number}): Balance: {self._balance:.2f}"


class SavingsAccount(Account):
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"[SavingsAccount {self._account_number}] Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise Exception("Insufficient funds in Savings Account.")
        self._balance -= amount
        print(f"[SavingsAccount {self._account_number}] Withdrew {amount}. New balance: {self._balance}")

    def __str__(self):
        return f"SavingsAccount({self._account_number}): Balance: {self._balance:.2f}"


class CheckingAccount(Account):
    OVERDRAFT_LIMIT = 100  # Simple overdraft limit for demonstration

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"[CheckingAccount {self._account_number}] Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if (self._balance - amount) < -CheckingAccount.OVERDRAFT_LIMIT:
            raise Exception("Insufficient funds in Checking Account (overdraft limit reached).")
        self._balance -= amount
        print(f"[CheckingAccount {self._account_number}] Withdrew {amount}. New balance: {self._balance}")

    def __str__(self):
        return (f"CheckingAccount({self._account_number}): Balance: {self._balance:.2f} "
                f"(Overdraft Limit: {CheckingAccount.OVERDRAFT_LIMIT})")


# ====================================================
# Customer
# ====================================================

class Customer:
    def __init__(self, customer_id: int, name: str):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []  # Association: A customer can have multiple accounts

    def add_account(self, account: Account):
        self.accounts.append(account)
        print(f"[Customer {self.customer_id}] Added account {account.account_number}.")

    def total_balance(self) -> float:
        return sum(account.get_balance() for account in self.accounts)

    def __str__(self):
        if self.accounts:
            accounts_info = "\n    ".join(str(account) for account in self.accounts)
        else:
            accounts_info = "No accounts"
        return (f"Customer {self.customer_id}: {self.name}\n"
                f"  Total Balance: {self.total_balance():.2f}\n"
                f"  Accounts:\n    {accounts_info}")


# ====================================================
# Abstract Bank and Concrete Implementation
# ====================================================

class AbstractBank(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abstractmethod
    def add_account(self, customer_id: int, account: Account):
        pass

    @abstractmethod
    def get_account(self, account_number: str) -> Account:
        pass

    @abstractmethod
    def transfer_within_bank(self, from_account_number: str, to_account_number: str, amount: float):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Bank(AbstractBank):
    def __init__(self, name: str):
        self.name = name
        self.customers = {}  # Maps customer ID to Customer instance
        self.accounts = {}   # Maps account number to Account instance

    def add_customer(self, customer: Customer):
        if customer.customer_id in self.customers:
            raise Exception("Customer already exists in the bank.")
        self.customers[customer.customer_id] = customer
        print(f"[Bank {self.name}] Added customer {customer.customer_id} - {customer.name}.")

    def add_account(self, customer_id: int, account: Account):
        if customer_id not in self.customers:
            raise Exception("Customer does not exist in the bank.")
        self.customers[customer_id].add_account(account)
        self.accounts[account.account_number] = account
        print(f"[Bank {self.name}] Linked account {account.account_number} to customer {customer_id}.")

    def get_account(self, account_number: str) -> Account:
        if account_number not in self.accounts:
            raise Exception("Account not found in this bank.")
        return self.accounts[account_number]

    def transfer_within_bank(self, from_account_number: str, to_account_number: str, amount: float):
        print(f"[Bank {self.name}] Initiating internal transfer of {amount} from {from_account_number} to {to_account_number}.")
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"[Bank {self.name}] Internal transfer completed.")

    def __str__(self):
        result = f"Bank: {self.name}\n"
        if not self.customers:
            result += "  No customers in the bank.\n"
        else:
            result += "Customers:\n"
            for customer in self.customers.values():
                result += f"  {str(customer)}\n"
        return result


# ====================================================
# Abstract Transaction System and Its Implementations
# ====================================================

class TransactionSystem(ABC):
    @abstractmethod
    def add_bank(self, bank: AbstractBank):
        pass

    @abstractmethod
    def transfer_across_banks(self, from_bank_name: str, from_account_number: str,
                                to_bank_name: str, to_account_number: str, amount: float):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Concrete implementation: Standard inter-bank transfers.
class BankingSystem(TransactionSystem):
    def __init__(self):
        self.banks = {}  # Maps bank name to Bank instance

    def add_bank(self, bank: AbstractBank):
        if bank.name in self.banks:
            raise Exception("Bank with this name already exists.")
        self.banks[bank.name] = bank
        print(f"[BankingSystem] Added bank: {bank.name}.")

    def transfer_across_banks(self, from_bank_name: str, from_account_number: str,
                                to_bank_name: str, to_account_number: str, amount: float):
        print(f"[BankingSystem] Initiating transfer of {amount} from {from_account_number} (Bank: {from_bank_name}) "
              f"to {to_account_number} (Bank: {to_bank_name}).")
        if from_bank_name not in self.banks or to_bank_name not in self.banks:
            raise Exception("One or both specified banks do not exist.")
        from_bank = self.banks[from_bank_name]
        to_bank = self.banks[to_bank_name]
        from_account = from_bank.get_account(from_account_number)
        to_account = to_bank.get_account(to_account_number)
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"[BankingSystem] Transfer across banks completed.")

    def __str__(self):
        result = "Banking System:\n"
        if not self.banks:
            result += "  No banks available."
        else:
            for bank in self.banks.values():
                result += str(bank) + "\n"
        return result


# UPI Transaction System implementation
class UPITransactionSystem(TransactionSystem):
    def __init__(self):
        self.banks = {}  # Maps bank name to Bank instance

    def add_bank(self, bank: AbstractBank):
        if bank.name in self.banks:
            raise Exception("Bank with this name already exists in UPI system.")
        self.banks[bank.name] = bank
        print(f"[UPITransactionSystem] Added bank: {bank.name}.")

    def transfer_across_banks(self, from_bank_name: str, from_account_number: str,
                                to_bank_name: str, to_account_number: str, amount: float):
        print(f"[UPI Transaction] Initiating UPI transfer of {amount} from {from_account_number} (Bank: {from_bank_name}) "
              f"to {to_account_number} (Bank: {to_bank_name}).")
        if from_bank_name not in self.banks or to_bank_name not in self.banks:
            raise Exception("One or both specified banks do not exist in UPI system.")
        from_bank = self.banks[from_bank_name]
        to_bank = self.banks[to_bank_name]
        from_account = from_bank.get_account(from_account_number)
        to_account = to_bank.get_account(to_account_number)
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"[UPI Transaction] UPI transfer completed.")

    def __str__(self):
        result = "UPI Transaction System:\n"
        if not self.banks:
            result += "  No banks available."
        else:
            for bank in self.banks.values():
                result += str(bank) + "\n"
        return result


# ATM Transaction System implementation
class ATMTransactionSystem(TransactionSystem):
    def __init__(self):
        self.banks = {}  # Maps bank name to Bank instance

    def add_bank(self, bank: AbstractBank):
        if bank.name in self.banks:
            raise Exception("Bank with this name already exists in ATM system.")
        self.banks[bank.name] = bank
        print(f"[ATMTransactionSystem] Added bank: {bank.name}.")

    def transfer_across_banks(self, from_bank_name: str, from_account_number: str,
                                to_bank_name: str, to_account_number: str, amount: float):
        # ATM transactions typically do not support inter-bank transfers.
        raise NotImplementedError("ATM Transaction System does not support inter-bank transfers.")

    def atm_withdraw(self, bank_name: str, account_number: str, amount: float):
        if bank_name not in self.banks:
            raise Exception(f"Bank {bank_name} not found in ATM system.")
        bank = self.banks[bank_name]
        account = bank.get_account(account_number)
        print(f"[ATM Transaction] Initiating ATM withdrawal of {amount} from account {account_number} (Bank: {bank_name}).")
        account.withdraw(amount)
        print(f"[ATM Transaction] ATM withdrawal completed.")

    def atm_deposit(self, bank_name: str, account_number: str, amount: float):
        if bank_name not in self.banks:
            raise Exception(f"Bank {bank_name} not found in ATM system.")
        bank = self.banks[bank_name]
        account = bank.get_account(account_number)
        print(f"[ATM Transaction] Initiating ATM deposit of {amount} to account {account_number} (Bank: {bank_name}).")
        account.deposit(amount)
        print(f"[ATM Transaction] ATM deposit completed.")

    def __str__(self):
        result = "ATM Transaction System:\n"
        if not self.banks:
            result += "  No banks available."
        else:
            for bank in self.banks.values():
                result += str(bank) + "\n"
        return result


# ====================================================
# Example Usage
# ====================================================

if __name__ == '__main__':
    # Create two banks and some customers/accounts
    bank_a = Bank("Bank A")
    bank_b = Bank("Bank B")

    customer_1 = Customer(1, "John Doe")
    customer_2 = Customer(2, "Jane Smith")

    bank_a.add_customer(customer_1)
    bank_b.add_customer(customer_2)

    account_a1 = SavingsAccount("A001", 1000)    # Savings Account in Bank A
    account_b1 = CheckingAccount("B001", 500)     # Checking Account in Bank B

    bank_a.add_account(customer_1.customer_id, account_a1)
    bank_b.add_account(customer_2.customer_id, account_b1)

    # ----- Using BankingSystem for inter-bank transfers -----
    print("\n=== Banking System Transaction ===")
    banking_system = BankingSystem()
    banking_system.add_bank(bank_a)
    banking_system.add_bank(bank_b)
    # Transfer 200 from account A001 (Bank A) to account B001 (Bank B)
    banking_system.transfer_across_banks("Bank A", "A001", "Bank B", "B001", 200)
    print(banking_system)

    # ----- Using UPITransactionSystem for inter-bank transfers -----
    print("\n=== UPI Transaction ===")
    upi_system = UPITransactionSystem()
    upi_system.add_bank(bank_a)
    upi_system.add_bank(bank_b)
    # Transfer 50 from account A001 (Bank A) to account B001 (Bank B) via UPI
    upi_system.transfer_across_banks("Bank A", "A001", "Bank B", "B001", 50)
    print(upi_system)

    # ----- Using ATMTransactionSystem for ATM withdrawals and deposits -----
    print("\n=== ATM Transaction ===")
    atm_system = ATMTransactionSystem()
    # For ATM transactions, we can add a bank (say, Bank A)
    atm_system.add_bank(bank_a)
    # Perform an ATM withdrawal of 100 from account A001
    atm_system.atm_withdraw("Bank A", "A001", 100)
    # Perform an ATM deposit of 150 to account A001
    atm_system.atm_deposit("Bank A", "A001", 150)
    print(atm_system)

    # Display final states
    print("\n=== Final States ===")
    print(account_a1)
    print(account_b1)
    print(customer_1)
    print(customer_2)
    print(bank_a)
    print(bank_b)
