import email
import poplib

def read_email():

    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('vp708u@gmail.com')
    pop_conn.pass_('loveamita')
    print('connection is done')
    print(pop_conn.list())
    print(pop_conn.context)
    print(pop_conn.welcome)
    print(pop_conn.getwelcome())

    for i in range(1, len(pop_conn.list()[1]) + 1):
        messages = pop_conn.retr(i)
        print(pop_conn.retr(i))
                    # Concat message pieces:

    print('message is retriving')

    # messages = ["\n".join(mssg[1]) for mssg in messages]
    # print (messages)
    # Parse message intom an email object:
    # messages = [email.parser.Parser().parsestr(mssg) for mssg in messages]
    # for message in messages:
    #     print
    #     message['subject']

    pop_conn.quit()
    return True

s = read_email()



