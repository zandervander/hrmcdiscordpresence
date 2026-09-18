import time
from pypresence import Presence

client_id = "1547720245555363942"
RPC = Presence(client_id)
RPC.connect()

print("Discord presence is running.")

while True:
    RPC.update(
        details="High Rock Military Corps (.gg/highrock)",
        state="Conducting Operations"
    )
    time.sleep(15)

    # dont mess with anything or it wont work anymore (other than the print think u can customize that but leave the quotation
    # marks)
