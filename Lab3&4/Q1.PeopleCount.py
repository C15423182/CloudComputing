""""
C15423182
Cian Sinclair
Cloud Computing Lab 3&4, Question 1
"""
import requests
url = requests.get('https://swapi.co/api/people/')
counter = 0 #Counter variable

while True:
    for item in url.json().get('results'):
        counter += 1

    nexturl = url.json().get('next')

    try:
        url = requests.get(nexturl)

    except:
        break

print ("Number of People:" , counter)