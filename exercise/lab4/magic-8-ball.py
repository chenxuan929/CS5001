import random
RESPONSES = ['As I see it, yes.', ' Ask again later.', 'Better not tell you now.',

            'Cannot predict now.', 'Concentrate and ask again.',

            'Don’t count on it.', 'It is certain.',

            'It is decidedly so.', 'Most likely.', 'My reply is no.',

            'My sources say no.', 'Outlook not so good.',

            'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.',

            'Very doubtful.', 'Without a doubt.', 'Yes.',

            'Yes – definitely.', 'You may rely on it.']

def main():
    print(" Welcome to Magic 8 Ball.")
    print(" Enter your question, and I will prognosticate an answer for you!")  
    

    while True:
        question = input(" What is your question (:q: to quit)?")
        if question.lower()== ':q:':
            break

        answer = random.choice(RESPONSES)
        print(f" {answer}")
       
main()
