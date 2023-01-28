# SigmaNuker - A Discord Spam Bot

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Discord](https://img.shields.io/discord/744502805644075013.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/744502805644075013)

## Description

SigmaNuker is a powerful Discord spam bot that allows you to easily flood channels with messages. It features an advanced configuration system that allows you to customize the bot to your needs.

## Features

- Proxies support
- Spamming in multiple channels
- Customizable messages
- Webhook support

## Configuration

To configure the bot, you need to create a config.json file in the root directory with the following format:

```json
{
    "TOKEN": "Token",
    "PROXIES": false,
    "SPAM_PRN": true,
    "WEBHOOK_NAME": "test",
    "MESSAGE": "@everyone test",
    "AMMOUNT_OF_CHANNELS": 1,
    "MESSAGES_PER_CHANNEL": 1,
    "CHANNEL_NAME": "test"
}
