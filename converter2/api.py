import requests

MS_API_POST_URL = "http://192.168.0.109/convert/"
source_file = "samplepptx.pptx"
target_format = "pptx"

file_content = {'input_file': open(source_file, 'rb')}
data_content = {'target_format': target_format}
res = requests.post(MS_API_POST_URL, data=data_content, files=file_content)
