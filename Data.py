from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

Use below buttons to learn more !

Made By @LG_Bot_Updates 
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="π  Return Home π ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Add Me To Your Group", url="https://t.me/LG_force_subscribe_bot?startgroup=True")],
        [
            InlineKeyboardButton("How to Use Meβ", callback_data="help"),
            InlineKeyboardButton("πͺ About πͺ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ Bot Updates β₯", url="https://t.me/LG_Bot_Updates")],
        [InlineKeyboardButton("π¨ Support Group π¨", url="https://t.me/+bsTf93bUeUM4Yjc1")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001505616678` or `/forcesubscribe -1001375849192`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

β¨ **Available Commands** β¨

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 
A telegram force subscribing bot by @LG_Bot_Updates

Source Code : [Click Here](https://t.me/LG_Bot_Updates)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Bot Updates : @LG_Bot_Updates 

Support Group : [LG Bots Support] (https://t.me/+bsTf93bUeUM4Yjc1) 

Developer : @LG_Bot_Updates 
    """
