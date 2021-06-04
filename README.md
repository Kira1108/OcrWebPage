# OcrWebPage



```bash
nohup uvicorn app.main:app --reload --workers 3 &
```

```python
import json
import requests

def get_page_result(json_data):
    url = "http://127.0.0.1:8000/page/"

    headers = {
      'accept': 'application/json',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=json_data)
    
    return json.loads(response.content.decode('utf-8'))
    
json_data = {
  "id": "123",
  "text": [
    "你是傻逼吧",
    "枪支弹药",
    "天气不错哟"
  ],
  "paths": [
    "C:/Users/wanghuan/Desktop/OcrSentence/app/datasets/test_imgs/cece.png"
  ]
}

get_page_result(json_data)
```


```python
{'id': '123',
    'code': 1,
    'img_result': [
        {'path': 'C:/Users/wanghuan/Desktop/OcrSentence/app/datasets/test_imgs/cece.png',
      'is_contain': True,
      'detail': {'你丫就是个傻逼': True,
       '-': False,
       '<-': False,
       '枪支弹药买卖': True,
       '来看一下': False,
       '激情少妇点击观看视频': True,
       '今天天气不错': False
            },
      'status': 'success'
        }
    ],
    'text_result': {'is_contain': True,
     'detail': {'你是傻逼吧': True, '枪支弹药': True, '天气不错哟': False
        }
    }
}
```
