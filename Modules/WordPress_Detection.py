import requests

def Is_WordPress(url):
    Api_Key = "w43u2hdtv0t1mbb60321aakv8zbvqj0k2f682afp1y3r7b6rlrq0262bd250ibho20zsa6"
    Api_Url = f"https://whatcms.org/APIEndpoint/Detect?key={Api_Key}&url={url}"
    response = requests.get(Api_Url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if data.get("result", {}).get("name") == "WordPress":
            return "Is WordPress"
        else:
            return "No WordPress"
  


