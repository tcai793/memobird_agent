# Memobird Agent

![py2][py2] ![py3][py3]

Memobird Agent 是一个开源的咕咕机打印API，它基于对官方App的逆向分析。

使用寥寥数行代码就可以实现自定义文本，图片，二维码和内置贴画的打印。
## Usage
To be completed

## Installation
```bash
pip install memobird_agent
```
## Examples
通过如下代码可以实现对文本的打印。
```python
import memobird_agent

document = memobird_agent.Document()
document.add_text("需要打印的文字")
document.print(GUID, userID, toUserID)
```

## FAQ
Q: `Document.print()`里的三个参数都是什么？应该如何获取？

A: GUID是长按设备六秒后印出文档里的16个字符的字符串。userID是发送者的用户ID，现阶段只能通过截获数据包得到。toUserID是一个可选项，表示了接收者的用户ID，现阶段也只能通过截获数据包来取得。在下一大版本的软件中会加入通过用户名和密码自动获取userID的功能。

Q: 为什么输入了GUID，userID后无法打印？

A: userID必须与设备绑定后才可以打印，绑定需在官方App内操作。下一大版本的软件中会加入直接绑定的功能。

## Comments
若有问题或者建议欢迎提Issue以及Pull Request来讨论。

## Roadmap
### v2.x
在第二个大版本内要实现
1. 提供登录API并获取userID
2. 提供绑定机器的API
3. 将网络部分分出去

[py2]:https://img.shields.io/badge/Python-2.x-brightgreen.svg "python2"
[py3]:https://img.shields.io/badge/Python-3.x-brightgreen.svg "python3"