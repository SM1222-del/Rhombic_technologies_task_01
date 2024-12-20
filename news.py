"""
pip install requests
"""
import requests
from keys import*

api_address=f"https://newsapi.org/v2/everything?q=tesla&from=2024-11-20&sortBy=publishedAt&apiKey={key}"

json_data=requests.get(api_address).json()

#list to take only titles
li=[]

def news():
    print("Yeah sure,I can read news for you.")
    for i in range(3):
        li.append("number 1"+str(i+1)+","+json_data["articles"][i]["title"]+".")

        return li

