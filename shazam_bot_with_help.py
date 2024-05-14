from pyrogram import Client, filters

# Initialize your Pyrogram client
app = Client("your_bot_token")

# Define the help command handler
@app.on_message(filters.command(["help"]))
async def help_command(client, message):
    # Define the help message with usage format
    help_message = (
        "Welcome to the bot!\n\n"
        "To use this bot, you can send the following commands:\n"
        "/start - Start using the bot\n"
        "/help - Show this help message\n"
        "/shazam - Identify a song by sending a voice message\n"
        "\n"
        "Usage format:\n"
        "To identify a song, simply send a voice message to the bot.\n\n"
        "To start the bot, run the following command in your terminal:\n"
        "`python shazam_bot.py`"
    )

    # Send the help message to the user
    await message.reply_text(help_message, parse_mode="markdown")

# Run the bot
app.run()
