from website import WebsiteScrapper 


ed = WebsiteScrapper("https://edwarddonner.com")
print(ed.title)
print(ed.text)
print("----------------------------------------------")
print(ed.system_prompt)
print(ed.user_prompt)
print(ed.messages)

print(ed.summarize())
