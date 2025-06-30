#создайте класс "банк" который имеет атрибут суммы денег и процентной ставки. 
#Добавьте методы для вычисления процентных начислений и снятия денег.
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
        
    def minus(self, amount): #Снимает указанную сумму денег с баланса, если достаточно средств
        if amount > self.balance:
            print("Недостаточно средств для снятия.")
        else:
            self.balance -= amount
            print(f"Снято: {amount:.2f}. Новый баланс: {self.balance:.2f}")
        
bank_account = Bank(initial_amount=1000, interest_rate=0.05)
bank_account.add_interest()  # Добавить проценты к балансу
bank_account.minus(200)    # Снять деньги