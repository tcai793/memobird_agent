# Memobird Agent

![py2][py2] ![py3][py3]

Memobird Agent 是一个开源的咕咕机打印API，它基于对官方App的逆向分析。

使用寥寥数行代码就可以实现自定义文本，图片，二维码和内置贴画的打印。

## Installation
```bash
pip install memobird_agent
```

## Usage
```python
import memobird_agent

document = memobird_agent.Document()
document.add_text(text="测试文字", bold=0, font_size=1, underline=0)
document.add_picture(path_to_image)
document.add_qrcode("嵌在二维码的文本")
document.add_text(icon_id)

user_id = memobird_agent.Util.get_user_id(username="username", password="password")
memobird_agent.Util.bind_machine(smart_guid=smart_guid, user_id=user_id)
document.print(smart_guid, user_id, to_user_id)
```

## Examples
### Simple Examples
#### 打印文本
```python
import memobird_agent

document = memobird_agent.Document()
document.add_text("需要打印的文字")
document.print(smart_guid, user_id, to_user_id)
```

## FAQ
Q: `Document.print()`里的三个参数都是什么？应该如何获取？

A: smart_guid是长按设备六秒后印出文档里的16个字符的字符串。user_id是发送者的用户ID。to_user_id是一个可选项，表示了接收者的用户ID。可以通过`memobird_agent.Util.get_user_id(username, password)`来取得用户ID

Q: 为什么输入了正确的smart_guid和user_id后无法打印？

A: smart_guid所属的咕咕机必须与user_id所属的用户绑定后才可以打印，绑定可在官方App内操作，或使用`memobird_agent.Util.bind_machine(smart_guid, user_id)`来绑定。

## Comments
若有问题或者建议欢迎提Issue以及Pull Request来讨论。

## Roadmap
### v2.5
1. 提供设置蜂鸣器与LED的API

### v3.x
1. 提供更多的功能

[py2]:https://img.shields.io/badge/Python-2.x-brightgreen.svg "python2"
[py3]:https://img.shields.io/badge/Python-3.x-brightgreen.svg "python3"
