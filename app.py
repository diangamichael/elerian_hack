import asyncio
from elarian import Elarian


client = Elarian(
    org_id="el_org_eu_u90EC6",
    app_id="el_app_efuX1k",
    api_key="el_k_test_b726fb9eea646bd0d6d4c26d2f3c4ec80a3f23daa0ff050ac32eb696fa3c70c0"
)

def on_connected():
  print("App is running!")

async def start():
    client.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
    client.set_on_connected(on_connected)
    await client.connect()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()