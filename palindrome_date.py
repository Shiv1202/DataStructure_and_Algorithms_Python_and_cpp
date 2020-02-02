import datetime

today = str(datetime.date.today())
today = today.split("-")
today = "".join(today)
if today == today[::-1]:
    print("First Palindromic Date After 909 Years. The next will come in 101 years on 12/12/2121.")
else:
    print("Sorry! Next Palindromic Date will come 12/12/2121.")