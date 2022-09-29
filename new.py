import asyncio
from time import time
from elarian import Elarian, Customer
client = Elarian(
    org_id='el_org_eu_JGwmDi',
    app_id='el_app_9VsDJx',
    api_key='el_k_test_a20e15d06ab1481f81002e366356e8d8e0c0229b96f86d72f48edd1990861be2'
)

whatsapp_channel = {
    'number': '+254711361595',
    'channel': 'whatsapp'
}

payment_channel = {
    'number': '53410',
    'channel': 'cellular'
}

purse_id = 'el_prs_Zj0C06'