class Email:
    # Create a constructor to identify the email contents, from address and to initialse has been read and is spam as false
    def __init__(self, email_contents, from_address):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

     # Create a function called mark as read to change has been read to true
    def mark_as_read(self):
        self.has_been_read = True
    
     # Create a function called mark as spam to change is spam to true
    def mark_as_spam(self):
        self.is_spam = True

 # Create a list called inbox
inbox = []
 # Create a function called add email and add the email address and email contents to the list
def add_email(email_address, email_contents):
    email = Email(email_address, email_contents)
    inbox.append(email)
 # Create a function called get_count to count the number of messages in the inbox (Store)
def get_count():
    return len(inbox)
 # Create a function to return the contents of an email in the list then mark the email as read
def get_email(i):
    if 0 <= i < len(inbox):
        email = inbox[i]
        email.mark_as_read()
        print(email)
        return email
    else:
        print("This index is invalid")

 # Create a function called get_unread_emails to create a list of unread emails
def get_unread_emails():
    unread_emails = []
    for i in inbox:
        if not i.has_been_read:
            unread_emails.append(i)
    return unread_emails

 # Create a function called get_spam_emails to create a list of spam emails
def get_spam_emails():
    spam_emails = []
    for i in inbox:
        if i.is_spam:
            spam_emails.append(i)
            print(f"spam emails: {i.email_contents}")
    return spam_emails

 # Create a function to delete an email from the inbox
def delete():
    if len(inbox) > 0:
        return inbox.pop()
    else:
        print("Sorry, there are no emails to delete")

 # Use the functions created to create a while loop and if statements based on the users choice
user_choice = ""
while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        print(get_unread_emails)
    elif user_choice == "mark spam":
        print(get_spam_emails)
    elif user_choice == "send":
        email_add = input("Enter your email address: ")
        email_cont = input("Enter the contents of the email: ")
        add_email(email_add, email_cont)
        print("Your email was sent")
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
