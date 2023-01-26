# Discord-Channel-Analysis
Generates trends of discord channels / chats

Discord Channel Analysis parses the output from [Discord Chat Explorer](https://github.com/Tyrrrz/DiscordChatExporter) into readable information.

# How to Use
Ensure you have the latest version of Python installed.

Download the latest release of Discord Channel Analysis. Extract the release to your desired location.

Download [Discord Chat Explorer](https://github.com/Tyrrrz/DiscordChatExporter)

Insert your token into Discord Chat Explorer. Once logged in, navigate to the settings menu and change the date format to `MM-dd-yyyy HH:mm:ss`
Navigate to your desired channel and export the chat in CSV format in the same location as unzipped Discord Channel Analysis.

Modify the settings file in the program directory to specify which stats you'd like to calculate.

Run main.py

Stats will be written to an output file.


Planned statistics:

* Most active users by time period. Can display either messages or percentage of chat.
* Most used emojis, phrases, GIFs (Configure in settings file)
* Chat activity histogram over time
* Most active time of day

# Settings Configuration
To be implemented

# Troubleshooting
To be updated as development ensues
