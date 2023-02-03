import requests
import time
from termcolor import colored
from pystyle import Colors, Center, Colorate, Write

def send_message(webhook_url, message, profile_picture_url, proxy=None):
  data = {
    "content": message,
    "avatar_url": profile_picture_url
  }

  proxies = {"http": proxy, "https": proxy} if proxy else None
  response = requests.post(webhook_url, json=data, proxies=proxies)
  if response.status_code != 204:
    if response.status_code == 429:
      # Rate limited
      print("You got ratelimited. Please add a bigger delay.")
      return False
    else:
      print("Failed to send message:", response.text)
      return False
  return True


banner = Center.XCenter("""
             
  ██████  ██▓  ▄████  ███▄ ▄███▓ ▄▄▄        ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██▒ ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██░░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▓   ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ▒ ░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ▒ ░░ ░   ░ ░      ░     ░   ▒   ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
      ░   ░        ░        ░         ░  ░      ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                                                                                      
                           Made by WebUwU :3 |  join server discord.gg/boobss\n\n
""")
print(Colorate.Vertical(Colors.red_to_purple, banner, 2))

while True:
    webhook_url = Write.Input("Enter the webhook URL: ", color=Colors.red_to_purple, interval=0.0600, input_color=Colors.red)
    if not webhook_url:
        # URL is empty, ask again
        Write.Print("Invalid URL. Please enter a valid Discord webhook URL",Colors.red_to_purple, interval=0.0025)
        print()
        continue
    if not (webhook_url.startswith("http://") or webhook_url.startswith("https://")):
        # URL is missing a scheme, ask again
        Write.Print("Invalid URL. Please enter a valid Discord webhook URL", Colors.red_to_purple, interval=0.0025)
        print()
        continue
    response = requests.head(webhook_url)
    if response.status_code == 200:
        # URL is valid, continue with the rest of the program
        break
    else:
        # URL is not valid, ask again
        Write.Print("Invalid URL. Please enter a valid Discord webhook URL", Colors.red_to_purple, interval=0.0025)
        print()

#Space 
message = Write.Input("Enter the message to send: ", Colors.red_to_purple, interval=0.0600, input_color=Colors.red)
#Space 
profile_picture_url = Write.Input("Enter the profile picture URL (leave blank to skip): ", Colors.red_to_purple, interval=0.0600)
if profile_picture_url and not profile_picture_url.startswith("http"):
    print(Write.Print("Invalid URL. Skipping...", Colors.red_to_purple))
else:
    send_count = Write.Input("Enter the number of times to send the message (or 'I' for infinite): ", Colors.red_to_purple, interval=0.0400, input_color=Colors.red)
#Space 
while True:
    delay = Write.Input("Enter the delay between messages in milliseconds: ", Colors.red_to_purple, interval=0.0500, input_color=Colors.red)
    try:
        int(delay)
        break
    except ValueError:
        pass
#Space        
use_proxy = Write.Input("Use proxy (Y/n)? ", Colors.red_to_purple, interval=0.0600, input_color=Colors.red).lower() == "y"

if use_proxy:
  with open("proxy.txt") as f:
    proxies = f.readlines()
  proxies = list(map(lambda x: x.strip(), proxies))
  proxy_index = 0

if send_count.isdigit():
    # Send the message the specified number of times
    for i in range(int(send_count)):
        if use_proxy and int(delay) < 1000:
            proxy_index = (proxy_index + 1) % len(proxies)
            proxy = proxies[proxy_index]
        else:
            proxy = None
        if not send_message(webhook_url, message, profile_picture_url, proxy):
            break
        time.sleep(int(delay) / 1000)
        Write.Print(f"Message {i+1}/{send_count} sent", Colors.green)
elif send_count.upper() == "I":
    # Send the message indefinitely
    i = 0
    while True:
        if use_proxy and int(delay) < 1000:
            proxy_index = (proxy_index + 1) % len(proxies)
            proxy = proxies[proxy_index]
        else:
            proxy = None
        if not send_message(webhook_url, message, profile_picture_url, proxy):
            break
        time.sleep(int(delay) / 1000)
        i += 1
        print(Write.Print(f"Message {i} sent", Colors.green))
else:
    Write.Print("Invalid input", Colors.red)
