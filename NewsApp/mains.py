import requests
import send_email

lst_news = []
api_key = "pub_dcf3f37432ff4244a8289bfec98f797c"
url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q=Automotive%20news"

request = requests.get(url)
content = request.json()

print(content['results'])


for result in content['results']:
    lst_news.append(result["title"])

send_email.send_email("\n".join(lst_news))