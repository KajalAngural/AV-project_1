from steganography.steganography import Steganography       #importing Steganography class from steganography library

from spy_details import friends,Chat_message,Spy,spy        #importing from another file - spy_details





#list of messages
STATUS_MESSAGES = ["Be Happy!!!", "Never feel shy to try something new!!!","be confident!!!"]
print "Let's get started!!!"



#variable asking from the spy to conitnue by the default name or as a new one
question = raw_input("Continue as %s [Y/N]" %(spy.name))





#function for selecting a friend from the available friends and also return the position of selected friend
def select_friend():
    item_number = 1
    for friend in friends:
        print "%d.%s %s aged %d having rating %.2f is online" %(item_number,friend.salutation,friend.name,friend.age,friend.rating)
        item_number = item_number+1
    friend_choice = raw_input("Choose a friend from above mentioned!!!")
    friend_position = int(friend_choice)-1
    return friend_position

#function to add status, spy can select a status from the previous status being displayed or he/she can add a new status
def add_status(current_status):
    update_status =  None

    if spy.current_status!=None:

        print "Your current_status is %s" %(spy.current_status)
    else:
        print "No current status"
    default = raw_input("Do you want to add status from previous ones?[y/n]")



    if default.upper() == "N":      #if spy wants to add new status
        new_status = raw_input("Whats your new status?")
        if len(new_status) > 0:
            STATUS_MESSAGES.append(new_status)
            update_status = new_status
        else:
            print "You have entered an incorrect status!!!"



    elif default.upper() == "Y":        #if spy wants to select status from the previous ones
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


#function to add a friend. Spy adds details of his/her friend and then that friend is added in friends list.
def add_friend():
    new_friend = Spy("","",0,0.0)

    new_friend.name = raw_input("Whats the name of your friend?")
    if len(new_friend.name) > 0 and new_friend.name.isspace() == False:
        new_friend.salutation = raw_input("What should we call your friend: Mr. or Ms.?")
        if new_friend.salutation == "Mr." or new_friend.salutation == "Ms.":
            new_friend.name = new_friend.salutation+ " " +new_friend.name
            new_friend.age = raw_input("Whats the age?")
            new_friend.age = int(new_friend.age)
            new_friend.rating = raw_input("Whats the rating?")
            new_friend.rating = float(new_friend.rating)
            if new_friend.age > 12 and new_friend.rating > 3.5:
                friends.append(new_friend)
                print "New friend added!!"
            else:
                print "Sorry! Can't add the friend with the information provided!!"

        else:
            print "Enter Mr. or Ms."

    else:
        print "Enter valid name!!"

    return len(friends)



#function to send a message, a secret message is hidden inside an image
def send_msg():
    friend_choice = select_friend()
    original_image = raw_input("Whats the name of file?")
    text = raw_input("What do you want to hide?")
    output_path = "images.jpg"
    if len(text) > 10:
        print "You are blocked!!!"

    else:
        Steganography.encode(original_image, output_path, text)

        new_chat = Chat_message(text, True)
        friends[friend_choice].chats.append(new_chat)

        print "Your secret message image is ready!"


#function to read a message
def read_msg():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = Chat_message(secret_text,False)
    friends[sender].chats.append(new_chat)


    print "Your secret message is %s" %(secret_text)



#function to read chat history of a friend. It will show date when the message has been send.
def read_chat_history():
    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)



#main function calling other functions. It will show a menu to the spy and he/she will select an option according to his/her requirements
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
            if menu_choice == 1:        #spy wants to update status
                current_status=add_status(current_status)

            elif menu_choice == 2:      #spy wants to add a friend
               number_friends =  add_friend()
               print "Number of friends are %d" %(number_friends)

            elif menu_choice == 3:      #spy wants to send a message
                send_msg()

            elif menu_choice == 4:      #spy wants to read a message
                read_msg()

            elif menu_choice == 5:      #spy wants to read chat history of a selected friend
                read_chat_history()


            else:                       #spy wants to exit the application
                print "Exiting the application"
                show_menu = False
    else:
        print "Sorry!! You are not of the correct age.."



#executable statements
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


