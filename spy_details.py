from datetime import datetime

class Spy:
    def __init__(self,name,age,salutation,rating):
        self.name = name
        self.age = age
        self.salutation = salutation
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None




class Chat_message:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Kajal',23,'Ms.',4.7)

friend_one = Spy('Priya',34,'Ms.',3.7)

friend_two = Spy('Vihaan',49,'Mr.',4.9)

friend_three = Spy('prem',23,'Mr.',5.8)

friends = [friend_one, friend_two, friend_three]








