import requests
import time
from termcolor import colored

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

webhook_url = input("Enter the webhook URL: ")
message = input("Enter the message to send: ")
profile_picture_url = input("Enter the profile picture URL: ")
send_count = input("Enter the number of times to send the message (or 'I' for infinite): ")
delay = input("Enter the delay between messages in milliseconds: ")
use_proxy = input("Use proxy (Y/n)? ").lower() == "y"

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
    print(colored(f"Message {i+1}/{send_count} sent", "green"))
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
    print(colored(f"Message {i} sent", "green"))
else:
  print("Invalid input")
