from datetime import datetime, timedelta

current_date = datetime.today()
new_date = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date five days ago:", new_date.strftime("%Y-%m-%d"))
