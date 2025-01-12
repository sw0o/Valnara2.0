import requests

def Is_WordPress(url):
    Api_Key = "w43u2hdtv0tlmbb60321aakv8zbvqj0k2f682afp1y3r7b6rlrq0262bd250ibho20zsa6"
    Api_Url = f"https://whatcms.org/APIEndpoint/Detect?key={Api_Key}&url={url}"
    response = requests.get(Api_Url).json()
    if response.get('result', {}).get('name') == "WordPress":
        return "WordPress Detected"
    else:
        return "WordPress Not Detected"


