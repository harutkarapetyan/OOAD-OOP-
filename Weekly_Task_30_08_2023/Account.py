import datetime

class TimeZone:
    def __init__(self, name, offset_jam, offset_rope):
        self.name = name
        self.offset_jam = offset_jam
        self.offset_rope = offset_rope

class Account:
    interest_rate = 0.0  
    
    def __init__(self, account_number, first_name, last_name, timezone = None, starting_balance = 0):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.timezone = timezone
        self.balance = starting_balance
        self.transaction_id = 0

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def create_confirmation_number(self, transaction_type, timestamp_utc):
        self.transaction_id += 1
        if self.timezone:
            time = timestamp_utc + datetime.timedelta(hours = self.timezone.offset_jam, minutes = self.timezone.offset_rope)
        else:
            time = timestamp_utc
        return f"{transaction_type}-{self.account_number}-{time.strftime('%Y%m%d%H%M%S')}-{self.transaction_id}"

    def deposit(self, money):
        if money <= 0:
            return "X-Invalid-Deposit-Money"
        self.balance += money
        timestamp_utc = datetime.datetime.utcnow()
        confirmation_number = self.create_confirmation_number("D", timestamp_utc)
        return confirmation_number

    def withdraw(self, money):
        if money <= 0 or self.balance < money:
            return "X-Insufficient-Funds"
        self.balance -= money
        timestamp_utc = datetime.datetime.utcnow()
        confirmation_number = self.create_confirmation_number("W", timestamp_utc)
        return confirmation_number

    def deposit_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount
        timestamp_utc = datetime.datetime.utcnow()
        confirmation_number = self.create_confirmation_number("I", timestamp_utc)
        return confirmation_number

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def parse_confirmation_code(confirmation_code:str, timezone = None):
        args = confirmation_code.split('-')
        if len(args) != 4:
            return None
        
        transaction_type, account_number, timestamp_str, transaction_id = args
        timestamp_utc = datetime.datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')

        if timezone:
            time = timestamp_utc + datetime.timedelta(hours = timezone.offset_jam, minutes = timezone.offset_rope)
        else:
            time = timestamp_utc

        result = {
            'account_number': account_number,
            'transaction_code': transaction_type,
            'transaction_id': int(transaction_id),
            'time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'time_utc': timestamp_utc.strftime('%Y-%m-%dT%H:%M:%S') }
        
        return result

timezone = TimeZone("GTM", +4, 0)
account = Account(14, "Emma", "Sletkin", timezone, 520)
Account.set_interest_rate(0.5)


ls = []
x = account.deposit(5000)
print(f"Confirmation: {x}")
ls.append(x)

x = account.withdraw(3000)
print(f"Confirmation: {x}")
ls.append(x)

x = account.deposit_interest()
print(f"Confirmation: {x}")
ls.append(x)
for i in ls:
    print(Account.parse_confirmation_code(i, timezone))


