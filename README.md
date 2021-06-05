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
  "paths": "C:/Users/wanghuan/Desktop/OcrSentence/app/datasets/test_imgs/cece.png"
}

get_page_result(json_data)
```


```python
{
  "id": "234",
  "code": 1,
  "img_result": [
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/testocr.png",
      "is_contain": true,
      "detail": {
        "其中的几个参数含父义如下": false,
        "。 model_name:模型名称": false,
        "即上面表格第一列中的值。默认为 conv-lite-fc": false,
        "。 model epoch:模型迭代次数。默认为 None.表示使用默认的迭代次数值。对于模型名称 conv-lite-fc就是27": false,
        "· cand_alphabet:待识别字符所在的候选集合": false,
        "默认为 None，表示不限定识别字符范围。cnocr.consts中内置了两个候": false,
        "集合:(1)数字和标点NuwMBERs; 2英文字母": false,
        "数字和标点ENG_LETTERS": false,
        "例如对干图片": false,
        "o12345678": false,
        "微信号:slatay%": false,
        "不做约束时识别结果为o12345678;如果加入数字约束时(ocr = CnOcr(cand_alphabet=NUMBERS))，识另": false,
        "果为012345678": false,
        "ro0t:模型文件所在的根目录": true,
        "Linux/Mac下默认值为 ～/.cno cr.表示模型文文件所处文文件夹类以": false,
        "-～ /s。 n Q C 工 / ]  '] ，)/ 一 O 个V= ].t 白= TC": false,
        "Windows 下默认值为 C:\\Users\\<use rname>\\ADDData\\Roaming\\cnocr": true,
        "- 八A.+in--muh 一 r 士心一s-rs -y- -+- 弋-一 —r McA -士=%+2—山一./ s一p 弋": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/src=http___dpic.tiankong.com_2b_m6_QJ6578876123.jpg_x-oss-process=style_show&refer=http___dpic.tiankong.jpg",
      "is_contain": false,
      "detail": {
        "3": false,
        "Flights": false,
        "||nfornati0[": false,
        "航班号": false,
        "计划": false,
        "始发/经停站": false,
        "预开": false,
        "出口": false,
        "状态": false,
        "U": false,
        "CA1430": false,
        "15:25 重庆": false,
        "15:2g": false,
        "": false,
        "到达": false,
        "u万": false,
        "C/A8905": false,
        "115:25大连": false,
        "15:16": false,
        "A一": false,
        "Uf": false,
        "CA1352": false,
        "15:30广州": false,
        "15:40": false,
        "CA\\976": false,
        "15:30新加坡": false,
        "15:53": false,
        "U仄": false,
        "CA181O": false,
        "15:35厦门": false,
        "17:05": false,
        "CA41": false,
        "15:35成都": false,
        "15:32": false,
        "页:5/15": false,
        "本屏航班计划时间:15:25至氯15:35": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/part-00332-91.jpg",
      "is_contain": false,
      "detail": {
        "200": false,
        "400": false,
        "TFEX": false,
        "buoP Los@": false,
        "Vol E": false,
        "fe": false,
        "色@“": false,
        "%Chg": false,
        "88.720了000": false,
        "翅": false,
        "": false,
        "-20.o0%": false,
        "0.4": false,
        "1o.60": false,
        "-7.02%": false,
        "1,6oo": false,
        ".3.74%": false,
        "2,180,300": false,
        "2.06": false,
        "1.26": false,
        "-3.08%": false,
        "17.000": false,
        "-3.03%": false,
        "17,062,700": false,
        "0.33": false,
        "8.1": false,
        "-2.99%": false,
        "43.25": false,
        "30,000": false,
        "43.oo": false,
        "-2.81%": false,
        "-2.73%": false,
        "10.70": false,
        "10.8o": false,
        "1,123,400": false,
        "-2.54%": false,
        "11.40": false,
        "11.50": false,
        "一一一一m": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/WX20210529-151311@2x.png",
      "is_contain": true,
      "detail": {
        "你丫就是个傻逼": true
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/b0c4c1d1abdd593425ed98f7e85b7411.jpeg",
      "is_contain": false,
      "detail": {
        "洛": false,
        "": false,
        "寄陕腿换货到邳醉站": false,
        "省耐安瞬撬": false,
        "逃=e畲参": false,
        "8mm^": false,
        "讶愕号快翅嘛獗赂庆噩": false,
        "妍壹旺提痊两": false,
        "刚棍猜系偏": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/cece.png",
      "is_contain": true,
      "detail": {
        "你丫就是个傻逼": true,
        "-": false,
        "<-": false,
        "枪支弹药买卖": true,
        "来看一下": false,
        "激情少妇点击观看视频": true,
        "今天天气不错": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/src=http___s4.sinaimg.cn_middle_72e58bfc49ad4b3ef5613&690&refer=http___s4.sinaimg.jpg",
      "is_contain": false,
      "detail": {},
      "status": "failed"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/a08b41f4e436dd66da9dfb0ebd35734f.jpeg",
      "is_contain": false,
      "detail": {
        "购怀祖国": false,
        "系灾〖": false,
        "潴训景": false,
        ".": false,
        "mm瓷mm盏嚣盏": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/6253aebeb25a9d5913e1e2894de1145c.jpeg",
      "is_contain": false,
      "detail": {
        "妊又快": false,
        "": false,
        "彩色条幅": false,
        "速度快": false,
        "质量好": false,
        "resn猷耍鞭": false,
        "裹": false,
        "专业条幅制作": false,
        "好又快": false
      },
      "status": "success"
    },
    {
      "path": "/Users/huan/Desktop/OcrWebPage/app/datasets/test_imgs/0933d05f3552d16757dc380af681173e.jpeg",
      "is_contain": false,
      "detail": {
        "密泅防控和落紊虱": false,
        "勤洗手讲起生远野味避聚甥医理匆忌瓤温": false
      },
      "status": "success"
    }
  ],
  "text_result": {
    "is_contain": true,
    "detail": {
      "卧槽": false,
      "傻逼": true
    }
  }
}
```
