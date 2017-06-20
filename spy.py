from steganography.steganography import Steganography
from datetime import datetime,timedelta
from spy_details import friends,Chat_message,Spy,spy






STATUS_MESSAGES = ["Be Happy!!!", "Never feel shy to try something new!!!","be confident!!!"]
print "Let's get started!!!"




question = raw_input("Continue as %s [Y/N]" %(spy.name))


def read_chat_history():
    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def select_friend():
    item_number = 1
    for friend in friends:
        print "%d.%s %s aged %d having rating %.2f is online" %(item_number,friend.salutation,friend.name,friend.age,friend.rating)
        item_number = item_number+1
    friend_choice = raw_input("Choose a friend from above mentioned!!!")
    friend_position = int(friend_choice)-1
    return friend_position


def add_friend():
    new_friend = Spy("","",0,0.0)

    new_friend.name = raw_input("Whats the name of your friend?")
    new_friend.salutation = raw_input("What should we call your friend: Mr. or Ms.?")
    new_friend.name = "%s %s" %(new_friend.salutation,new_friend.name)
    new_friend.age = raw_input("Whats the age of your friend?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Whats the rating of your friend?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.rating > 0 and new_friend.age > 18:
        friends.append(new_friend)
        print "Friend Added!!!"
    else:
        print("Sorry! We cant add friend with the provided information..!!")
    return len(friends)


def add_status(current_status):
    update_status =  None

    if spy.current_status!=None:

        print "Your current_status is %s" %(spy.current_status)
    else:
        print "No current status"
    default = raw_input("Do you want to add status from previous ones?[y/n]")



    if default.upper() == "N":
        new_status = raw_input("Whats your new status?")
        if len(new_status) > 0:
            STATUS_MESSAGES.append(new_status)
            update_status = new_status
        else:
            print "You have entered an incorrect status!!!"



    elif default.upper() == "Y":
        item_position = 1
        for message in STATUS_MESSAGES:
            print "%d. %s" %(item_position, message)
            item_position  = item_position+1
        msg_selection = int(raw_input("Select status from above displayed!!"))
        if len(STATUS_MESSAGES)>=msg_selection:
            update_status = STATUS_MESSAGES[msg_selection-1]


    else:
        print "You choose an invalid option!! Press either Y or N!!"

    print "Your updated status is %s" %(update_status)
    return(update_status)


def send_msg():
    friend_choice = select_friend()
    original_image = raw_input("Whats the name of file?")
    text = raw_input("What do you want to hide?")
    output_path = "images.jpg"
    Steganography.encode(original_image,output_path,text)

    new_chat = Chat_message(text, True)
    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"




def read_msg():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = Chat_message(secret_text,False)
    friends[sender].chats.append(new_chat)


    print "Your secret message is %s" %(secret_text)

def start_chat(spy):
    current_status=None
    spy.name = spy.salutation +" "+spy.name
    if spy.age < 50 and spy.age >12:
        print "Authentication completed!!! \nWelcome %s, Glad to see you again" %(spy.name)
        show_menu = True
        while show_menu:
            menu_choices = "What you want to do :\n1.Update status\n2.Add a friend\n3.Send a message\n4.Read a message\n5.Read chat history\n6.Exit  "
            menu_choice = raw_input(menu_choices)
            menu_choice = int(menu_choice)
            if menu_choice == 1:
                current_status=add_status(current_status)

            elif menu_choice == 2:
               number_friends =  add_friend()
               print "Number of friends are %d" %(number_friends)



            elif menu_choice == 3:
                send_msg()

            elif menu_choice == 4:
                read_msg()

            elif menu_choice == 5:
                read_chat_history()


            else:
                print "Exiting the application"
                show_menu = False
    else:
        print "Sorry!! You are not of the correct age.."

if question.upper() == "Y":
    start_chat(spy)
else:
    spy.name = raw_input("Whats your name?")
    spy.salutation = raw_input("What should we call you: Mr. or Ms.?")
    spy.age = raw_input("Whats your age?")
    spy.age = int(spy.age)
    spy.ratings = raw_input("Whats your ratings?")
    spy.ratings = float(spy.ratings)
    if len(spy.name) > 0:
        print "Welcome %s!!!" %(spy.name)
        start_chat(spy)
    else:
        print "Enter a valid spy name!!"


