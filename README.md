# python_demo
python_demo

1. ekitchen config
build lang 指定语言，现在 python2.7 不填为 nodejs

commands 指定 pip 安排 requirements.txt 内指定的每三方依赖，`-t .` 安装到本地也是有必要的
```
{
  "appid": "python_demo",
  "services": [
    {
      "serviceName": "demo_py",
      "funcs": [
        {
          "functionName": "hello",
          "handler": "main.hello",
          "runtime": "python2.7"
        }
      ]
    }
  ],
  "build": {
    "lang": "python2.7",
    "commands": [
      "pip install -r requirements.txt -t ."
    ]
  }
}
```

2. requirements.txt
```
requests
```

3. main.py
```
import requests

def hello(event, context):
    url = 'https://api.ipify.org/?format=json'

    raw = requests.get(url)
    print raw

    result = raw.json()
    print result

    return result
```
