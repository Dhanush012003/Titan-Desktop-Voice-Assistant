import random


Hello = ('hello', 'hey', 'hii', 'hi', 'hay','hello there')
reply_Hello = ('Hello, I am Titan. How I want to assist you?', "Hey, What's Up?", "Hii, what can I do for you?", "Hello, Nice To Meet You Again.", "Of Course Sir, Hello.", "Yes, How can I assist You?", "Hello there, How do i want to assist you?")

Bye = ('bye', 'exit', 'sleep', 'sign off', 'stop', 'turn off')
reply_bye = ('Bye... See You Soon..', "Ok Bye... Until next time", "Ok.. See You Soon..", "Signing off now bye.", "Okay..See you soon..", "Okay...bye..")

How_Are_You = ('how are you', 'are you fine')
reply_how = ('I Am Fine.', "Absolutely Fine.", "I'm Fine.", "Thanks For Asking.")

nice = ('thanks', 'thanks titan', 'good', 'nice')
reply_nice = ('Thanks.', "Oh, It's Okay.", "Thanks To You.")

Functions = ['what can you do', 'what is your ability', 'what is your abilities', 'things you can do']
reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks, How Can I Help You?', 'I Can Call Your G.F.', 'I Can Message Your Mom That You Are Not Studying.', 'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Instagram, Facebook, etc!', 'Let Me Ask You First, How Can I Help You?', 'If You Want Me To Tell My Features, Call: Print Features!')

sorry_reply = ("Sorry, That's Beyond My Abilities.", "Sorry, I Can't Do That.", "Sorry, That's Above Me.")


def ChatterBot(Text):
    Text = str(Text)

    if any(word in Text.lower() for word in Hello):
        reply = random.choice(reply_Hello)
    elif any(word in Text.lower() for word in Bye):
        reply = random.choice(reply_bye)
    elif any(word in Text.lower() for word in How_Are_You):
        reply = random.choice(reply_how)
    elif any(word in Text.lower() for word in nice):
        reply = random.choice(reply_nice)
    elif any(word in Text.lower() for word in Functions):
        reply = random.choice(reply_Functions)
    else:
        reply = random.choice(sorry_reply)

    return reply


# Testing the ChatterBot function
# user_input = "Hello Titan, how are you doing today?"
# bot_response = ChatterBot(user_input)
# print("Bot Response:", bot_response)
