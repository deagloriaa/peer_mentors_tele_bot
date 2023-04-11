import telegram.ext
import emoji
import random

Token = "6021588172:AAHdSY5pDVMakknJJrv8ZAeGZDdTEf0EwAg"

updater = telegram.ext.Updater("6021588172:AAHdSY5pDVMakknJJrv8ZAeGZDdTEf0EwAg", use_context = True)

dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text(
        """
Hi! Welcome to SIM Peer Mentors Bot! \U0001F917

We Care, Share, and Grow!
Feel free to talk to us whenever you need a listening ear! \U0001F4AD

Type /help to see available commands!
        """)

def help(update, context):
    update.message.reply_text(
        """
Available commands:
/start -> Welcome message
/help -> Available commands
/motd -> Message of the day
/talktopm -> Schedule a session with a Peer Mentor
/counselling -> Schedule a session with our Counsellors
/swc -> Introduction to Student Wellness Center
/info -> SIM Peer Mentors' contact and information
/livechat -> 
        """
    )

def motd(update, context):
    messages = ["You got this.", "Good luck today! I know you will do great.",
                "Sending major good vibes your way.", "Keep on keeping on!",
                "We know this will not be easy, but we also know you have got what it takes to get through it.",
                "You are doing exactly what you should be doing. Hang in there.",
                "You are making a big change, and that is a really big deal.",
                "Stay strong and remember how many people care about you. (We are one of them!)",
                "It is okay not to be okay.",
                "Just wanted to send you a smile today.",
                "Whenever you find yourself doubting how far you can go, just remember how far you have come.",
                "Do not be ashamed of a scar. It simply means you were stronger than whatever tried to hurt you",
                "Hey, little fighter, soon things will be brighter.",
                "This too shall pass.",
                "There is much more ahead of you. You will get through this.",
                "Everything will be ok at the end, if it is not ok, it is not the end.",
                "Be gentle with yourself. You are doing the best you can!",
                "Someday, you will become filled with so much happiness that it heals every part of you.",
                "In the middle of every difficulty lies opportunity.",
                "Sometimes people seem to be doing better than you. They may seem to be way ahead of you in hitting some goals that you may not be close to achieving, but never be bothered by it. Just keep on working hard and carrying on with the steady pace that works best for you.",
                "Great things never come from comfort zones.",
                "Do not worry about all of the steps. Begin.",
                "Failure is success in progress.",
                "Be the change that you wish to see in the world.",
                "Tough times never last, but tough people do.",
                "If you cannot fly, then run; if you cannot run, then walk; if you cannot walk, then crawl, but whatever you do, you have to keep moving forward.",
                "Just because you fail once does not mean you are gonna fail at everything."]
    update.message.reply_text(random.choice(messages))


def talktopm(update, context):
    update.message.reply_text(""" 
    To schedule a session with a Peer Mentor, please fill this form: 
https://forms.office.com/Pages/ResponsePage.aspx?id=T8GRqvmA60KWcB1aN1SmltFiaLzrC_lGs8r6PdB0ArFUM0NRME1LVFM4SDk3TUVETjZTVEQ3RE8wSS4u&origin=QRCode
    """)

def counselling(update, context):
    update.message.reply_text("""
    To schedule a counselling session with our Professional Counsellor, please fill the following form:
https://forms.office.com/pages/responsepage.aspx?id=T8GRqvmA60KWcB1aN1SmljFHFZzhuFhCorCHE80gCrJUQ1RIQVg3Skw2SlU1M1ZFN1FWRkRRRUdaSy4u
    """)

def swc(update, context):
    update.message.reply_text(""" 
    What can I do at Student Wellness Center? 
Find out more at: https://www.instagram.com/p/Cpt2FRDBlP1/
    """)

def info(update, context):
    update.message.reply_text("""
To find out more about us, kindly visit us at:

\U0001F310 Website: https://project1095.simge.edu.sg/student-care/peer-support/

\U0001F4F8 Instagram: https://www.instagram.com/sim_peermentors/ 

\U0001F3DA Venue: SIM HQ, B.2.11
\U0001F570 Operation Hours: 1 PM - 5 PM (Weekdays, excluding PH)

For further enquiries:
\U0001F4E9 Email: simpeermentors@sim.edu.sg
    """)

def livechat(update, context):
    update.message.reply_text(""" 
    Note: 
- Any messages beyond our operating time (1-5 PM on weekdays) will not be responded.
- All messages in this conversation will be kept for training purposes.
    """)

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
dispatcher.add_handler(telegram.ext.CommandHandler('motd',motd))
dispatcher.add_handler(telegram.ext.CommandHandler('talktopm',talktopm))
dispatcher.add_handler(telegram.ext.CommandHandler('counselling',counselling))
dispatcher.add_handler(telegram.ext.CommandHandler('swc',swc))
dispatcher.add_handler(telegram.ext.CommandHandler('info',info))
dispatcher.add_handler(telegram.ext.CommandHandler('livechat',livechat))

updater.start_polling()

updater.idle()