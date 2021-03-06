import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAADAw8AK4VYBALW3qErXKpddAeXFf7lQgYV61F2qfI2L3ewaVv0v0jz2vdy0hKQKyJz4ZCtT21IPJ3PcAKGEFcpFM0uFiJqXNNLIoiRnKjRuXKfjt7HPtwSIoOU6KvLXKVfED92hHtlXQqlYzTPlnyZBDKxAO4pblIWcB0ZCPh487Y8fpoF"
                
#ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
   
    payload = {
        "recipient": {"id": id},
        "message": { 
            "attachments":{
                "type": "image",
                "payload": {
                    "url": img_url,
                    "is_reusable":true
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

    


"""
def send_button_message(id, text, buttons):
    pass
"""
