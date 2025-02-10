from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Datetime with microseconds:", now)
print("Datetime without microseconds:", without_microseconds)
