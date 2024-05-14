import sys
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize your Pyrogram client
app = Client("your_bot_token")

# Define the start command handler
@app.on_message(filters.command(["start"]))
async def start_command(client, message):
    # Create inline keyboard buttons
    button_group = InlineKeyboardButton("Add me to your group", url="https://t.me/your_group_link")
    button_support = InlineKeyboardButton("Support", callback_data="support")
    button_dev = InlineKeyboardButton("Dev", url="https://t.me/cooltechdud")

    # Create inline keyboard markup with the buttons
    reply_markup = InlineKeyboardMarkup(
        [[button_group], [button_support], [button_dev]]
    )

    # Send the start message with the inline keyboard
    await message.reply_text("Welcome to the bot! How can we assist you?", reply_markup=reply_markup)

# Define the callback query handler
@app.on_callback_query()
async def callback_query_handler(client, query):
    if query.data == "support":
        # Respond to the support button callback
        await query.answer("Opening support group...")
        await query.message.reply_text("Join our support group:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support Group", url="https://t.me/XBOTSUPPORTS"), InlineKeyboardButton("Back", callback_data="back")]]))
    elif query.data == "back":
        # Respond to the back button callback
        await query.answer()
        await query.message.delete()
        await start_command(client, query.message)

# Run the bot
if len(sys.argv) > 1 and sys.argv[1] == "add":
    app.run()
