from bpx.bpx import *
from config import api_key, api_secret, SOL_QUANTITY, DELAY
import time
import random


bpx = BpxClient()
bpx.init(api_key, api_secret)


print(bpx.depositAddress('Solana'))
print(bpx.balances())


bpx.debug = False
counter = 0
quantity = round(SOL_QUANTITY, 2)


while True:
    try:
        try:
            buy_response = bpx.ExeOrder('SOL_USDC', 'Bid', 'Limit', 'IOC', f'{quantity}')
            createdAt = buy_response['createdAt']
            executedQuantity = buy_response['executedQuantity']
            status = buy_response['status']
            print(f'ПОКУПКА createdAt: {createdAt}, executedQuantity: {executedQuantity}, status: {status}')

            time.sleep(random.randint(0, DELAY))

            sell_response = bpx.ExeOrder('SOL_USDC', 'Ask', 'Limit', 'IOC', f'{quantity}')
            createdAt = sell_response['createdAt']
            executedQuantity = sell_response['executedQuantity']
            status = sell_response['status']
            
            print(f'ПРОДАЖА createdAt: {createdAt}, executedQuantity: {executedQuantity}, status: {status}')
        except Exception as e:
            print('Change BUY/SELL')
            sell_response = bpx.ExeOrder('SOL_USDC', 'Ask', 'Limit', 'IOC', f'{quantity}')
            createdAt = sell_response['createdAt']
            executedQuantity = sell_response['executedQuantity']
            status = sell_response['status']
            
            print(f'createdAt: {createdAt}, executedQuantity: {executedQuantity}, status: {status}')

        counter += 1
        
        print('\n')
        print('------------------------------------------------------------')
        print(f'Итерация №{counter} успешно выполнена\nSELL/BUY {quantity} SOL')
        print('------------------------------------------------------------')
        print('\n')
        time.sleep(random.randint(0, DELAY))
    except Exception as e:
        quantity = round(quantity - 0.01, 2)
        print(f"Ошибка итерации № {counter} выставляю количество сделки {quantity} SOL")

        if quantity <= 0:
            break
