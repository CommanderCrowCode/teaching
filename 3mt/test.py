import requests
import json
import base64
with open('sunisa.mp3', 'rb') as fh:
    content = fh.read()
res = requests.post(
    'https://demo.api.gowajee.ai/speech-to-text/transcribe',
    data=json.dumps({
			"audioData": base64.encodebytes(content).decode('utf-8')
		}),
    headers={
      'Content-type': 'application/json',
      'x-api-key':'HW^8BiXeacvSTDhft*L9aTnkcSLh^XdRcrX9n8zf#WxjAFNZ%QhLDPPkG*a5LVyt'
    }
)

with open('gowajee.txt', 'w') as file:
  file.write(res["results"]["transcript"])
