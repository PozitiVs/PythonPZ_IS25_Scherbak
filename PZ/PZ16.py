class Bank:
    def __init__(self, initial_amount, interest_rate):
        self.balance = initial_amount
        self.interest_rate = interest_rate
        
    def calculate_interest(self): #Вычисляет и возвращает процентные начисления на текущий баланс
        interest = self.balance * self.interest_rate
        return interest
    
    def add_interest(self): #Добавляет процентные начисления к балансу
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Проценты добавлены: {interest:.2f}. Новый баланс: {self.balance:.2f}")
        
    def withdraw(self, amount): #Снимает указанную сумму денег с баланса, если достаточно средств
        if amount > self.balance:
            print("Недостаточно средств для снятия.")
        else:
            self.balance -= amount
            print(f"Снято: {amount:.2f}. Новый баланс: {self.balance:.2f}")
        
    