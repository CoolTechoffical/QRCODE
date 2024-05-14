from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize your Pyrogram client
app = Client("your_bot_token")

# Define a command handler
@app.on_message(filters.command(["shazam"]))
async def shazam_command(client, message: Message):
    # Check if the message contains a voice note
    if message.voice:
        # Get the file ID of the voice note
        voice_file_id = message.voice.file_id
        
        # Send the voice note to the @ShazamBot and get the response
        shazam_response = await app.send_message("shazam", voice_file_id)
        
        # Forward the response to the user
        await message.reply_text(shazam_response.text)
    else:
        # If the message doesn't contain a voice note, prompt the user to send one
        await message.reply_text("Please send a voice message for Shazam to identify.")

# Run the bot
app.run()
