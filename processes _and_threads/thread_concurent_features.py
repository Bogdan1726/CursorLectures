from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
import time


def calculation():
    start = time.time()
    print('Starting the calculation')
    [x ** 2 for x in range(2000000)]
    print(f'Calculation time: {time.time() - start}')


def enter_username():
    username = input('Enter your name: ')
    start = time.time()
    greeting = f'Hello {username}'
    print(greeting)
    print(f'Enter username: {time.time() - start}')


start = time.time()
enter_username()
calculation()
print(f'Single thread total time: {time.time() - start}\n\n')


start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(calculation)
    pool.submit(enter_username)

print(f'Two threads total time: {time.time() - start}')

# # Two process
# start = time.time()
# processes = Process(target=calculation())
# processes.start()
# enter_username()
# processes.join()  # waits fro the process to finish
#
# print(f'Two thread total time: {time.time() - start}\n\n')
