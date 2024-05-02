import json
import time
import random
import string
from io import BytesIO
from fake_useragent import UserAgent
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

ua = UserAgent()
# Your existing code

def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        proxies = file.readlines()
    proxies = [proxy.strip() for proxy in proxies]
    return proxies

proxies_file_path = 'proxyscrape_premium_http_proxies(8).txt'
proxies = read_proxies_from_file(proxies_file_path)

def get_random_proxy(proxies):
    return random.choice(proxies)

@app.post("/api/image_translate")
async def image_translate(image_url: str):
    try:
        img_url = image_trans(image_url)
        return {"translated_image_url": img_url}
    except Exception as e:
        print(e,'error hai')
        raise HTTPException(status_code=500, detail=str(e))

def image_trans(urp):
    # Your image translation function

      
      
      def get_random_proxy(proxies):
       return random.choice(proxies)
      def image_send(image_buffer):
      # Define the URL
              def generate_random_string(length):
                return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

              random_length = random.randint(5, 15)


              proxy = get_random_proxy(proxies)
              proxy = {'http': proxy, 'https': proxy} 
              url = "https://ichigoreader.com/translate/as-reader-format"
              agentwa=ua.random
              # Define the headers
              headers = {
                  "authority": "ichigoreader.com",
                  "accept": "*/*",
                  "accept-language": "en-US,en;q=0.9",
                  "cookie": "_0d8a7=http://108.181.186.204:8080",
                  "origin": "https://ichigoreader.com",
                  "referer": "https://ichigoreader.com/upload",
                  "sec-ch-ua": '"Chromium";v="122", "Not(A;Brand";v="24", "Google Chrome";v="122"',
                  "sec-ch-ua-mobile": "?0",
                  "sec-ch-ua-platform": '"Windows"',
                  "sec-fetch-dest": "empty",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-site": "same-origin",
                  "user-agent": agentwa,
              }
              
              # Define the file path
              
      
              # Extract file name without extension
             
              random_snippet = generate_random_string(random_length)
           
             
              # Open the image file
             
                  # Define the data payload
              payload = {
                      "file": (f'{random_snippet[:6]}.jpg',  image_buffer.getvalue(), f"image/.jpg"),
                    "fingerprint": (None, f"U1EIFJhZyVvbihUTSkgR3JhcGhpY3MgKDB4MDAwMDE2MzgpIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpLTEyLTgteW5k{random_snippet}WZpbmVkLTIwMC11bmRlZmluZWQtNGctZmFsc2UtLTMzMA"[:-len(str(random_snippet))]+"=="),
          }
              
                  # Send the POST request
              try:
               response = requests.post(urlheaders=headers,proxies=proxy ,files=payload)
               print(response.text)
               job_id = json.loads(response.text)['jobId']
              except:
                  
                      try:  
                          proxy = get_random_proxy(proxies)
                          proxy = {'http': proxy, 'https': proxy} 
                          response = requests.post(url,headers=headers,proxies=proxy,files=payload)
                          print(response.text)
                          job_id = json.loads(response.text)['jobId']
                          
                      except:
      
                           return 'no quuw'    
              # Print the response
              
              print(response.text)
              img_urlm=f'https://ichigoreader.com/translate/as-reader-format/download?jobId={job_id}'
              tmop=0
              while True:
                    if tmop==10:
                        break
                    
                    url = "https://ichigoreader.com/translate/as-reader-format/get"
                    # Define the query parameters
                    params = {
                        "jobId": json.loads(response.text)['jobId']
                    }
                    # Define the headers
                    headers = {
                        "authority": "ichigoreader.com",
                       
                        "user-agent": agentwa,
                    }
                    # Send the GET request
                    response = requests.get(url, params=params, headers=headers)
                    # Print the response
                    status=json.loads(response.text)['status']
                    if status=='processing':
                          time.sleep(2)
                          print('process')
                          tmop+=1
                          pass
                    else:
                          print('done')
                          return img_urlm
                        
                          
      
      
      # # to get result
      def urlpop(urp):
                  ua = UserAgent()
                  global end
                  headers = {
      
                                  "user-agent": ua.random,
                              }
      
                  response = requests.get(urp,headers=headers)
      
                          # Check if the request was successful (status code 200)
                  if response.status_code == 200:
                      # Get the content of the response (image data)
                      image_data = response.content
                      # Specify the path where you want to save the image
                      # You can change the file name and extension as needed
                      # Open a file in binary write mode and write the image data to it
                     
                      image_buffer = BytesIO()
                      image_buffer.write(image_data)
                    
                      return image_send(image_buffer)
                  else:
                              print("Failed to download the image.")
                              end='start'
                              print(response.text)   
      return urlpop(urp)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

