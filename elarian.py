import asyncio
from elarian import Elarian

client = Elarian(
    org_id = "el_org_eu_BvjqWZ",
    app_id = "el_app_efuX1k",
    api_key = "el_k_test_2c18a8411151d558e5b1bb422c24a270e544cf1866c2a8e8970bd0df5d287b5d")

def on_connected():
    print("App is running!")    

async def start():
    client.set_on_connection_error(lambda err: print(f"Connection error: {err}"))  
    client.set_on_connected(on_connected)
    await client.connect()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()