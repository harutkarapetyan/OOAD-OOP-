
class Is_valid:
    
    def mail(self,mail):
        if len(mail) > 10 and len(mail) < 50:
           if mail[-9:] == "@email.ru" or mail[-10:] == "@gmail.com":
               return True
        return False   
             

    def URL(self,URL):
        if len(URL) > 9 and len(URL) < 50:
            if URL[:3] == "www" and (URL[-3:] == "com" or URL[-2:] == "ru"):
                return True
        return False
     
    def Date(self, date):
        """prototayp >>> 01.01.2001 """
        aggregat = date.split(".")
        if len(aggregat) == 3:
            day = aggregat[0]
            month = aggregat[1]
            year = aggregat[2]
            if day.isdigit() and month.isdigit() and year.isdigit():
                day = int(day)
                month = int(month)
                year = int(year)
                if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2023:
                    return True
        return False

    def Number(self,number):
        for i in number:
            if i.isdigit():
                return True
        return False    

    def Credit_Card_Number(self,numeric):
        if len(numeric) == 16:
            for i in numeric:
                if i.isdigit():
                    return True
        return False
    
   
    def Phone_Number(self, number):
        """Only Armenian Phone Number"""
        if len(number) == 9:
            if number[0] == "0":
                for i in number:
                    if i.isdigit():
                        return True
        elif len(number) == 12:
            if number[:4] == "+374":
                for i in range(5, len(number)):
                    if number[i].isdigit():
                        return True
        return False



obj = Is_valid()
flag = True

while flag:
    try:
        x = int(input("for Emal 1, for URL 2, for Date 3, for Number 4, for Credit_card_number 5, for Phone_number 6, for Exit 7 "))
    except ValueError:
        print("Write integer")
        continue

    if x == 1:
        mail = input("Write mail ")
        print(obj.mail(mail))
    elif x == 2:
        URL = input("Write URL ")
        print(obj.URL(URL))
    elif x == 3:
        date = input("Write Date ")
        print(obj.Date(date))
    elif x == 4:
        number = input("Write number ")
        print(obj.Number(number))
    elif x == 5:
        credit_number = input("Write Credit_card_number ")
        print(obj.Credit_Card_Number(credit_number))
    elif x == 6:
        phone_number = input("Write phone_number ")
        print(obj.Phone_Number(phone_number))
    elif x == 7:
        flag = False
    else:
        break