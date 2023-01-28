# SigmaNuker - A Discord Spam Bot

![SigmaNuker](https://i.imgur.com/9zTvI7S.png)

### About
SigmaNuker is a simple Discord spam bot that allows you to send a specified message to a specified number of channels. It also supports proxies for sending messages anonymously. 

### Features
- Ability to send a specified message to multiple channels
- Proxies support for anonymous messaging
- Option to print sent messages
- Customizable webhook name
- Option to change the channel name
- Option to change the number of messages per channel

### Requirements
- Python 3.8 or higher
- Discord API token
- Proxies (optional)

### Installation
- Clone the repository
- Run `pip install -r requirements.txt` to install the dependencies
- Create a `config.json` file in the root directory and add the following details:
```json
{
    "TOKEN": "Your Discord bot token",
    "PROXIES": false,
    "SPAM_PRN": true,
    "WEBHOOK_NAME": "SigmaNuker",
    "MESSAGE": "@everyone Spamming with SigmaNuker",
    "AMMOUNT_OF_CHANNELS": 1,
    "MESSAGES_PER_CHANNEL": 1,
    "CHANNEL_NAME": "spam-channel"
}
