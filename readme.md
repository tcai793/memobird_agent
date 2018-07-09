# Memobird Agent

![py2][py2] ![py3][py3] [中文][chinese_version]

Memobird Agent is an open-source API designed to print documents on [Memobird][memobird]. This API is accomplished by reverse engineering of its official APP.

Texts, pictures, QR Codes and internal stickers can be printed using only a few lines of code.

## Installation
```bash
pip install memobird_agent
```

## Usage
```python
import memobird_agent

document = memobird_agent.Document()
document.add_text(text="Test Text", bold=0, font_size=1, underline=0)
document.add_picture(path_to_image)
document.add_qrcode("Text to be encoded into the QR Code")
document.add_text(sticker_id)


user_id = memobird_agent.Util.get_user_id(username="username", password="password")
memobird_agent.Util.bind_machine(smart_guid=smart_guid, user_id=user_id)
document.print(smart_guid, user_id, to_user_id)
```

## Examples
### Simple Examples
#### Print text
```python
import memobird_agent

document = memobird_agent.Document()
document.add_text("Text to print")
document.print(smart_guid, user_id, to_user_id)
```

## FAQ
####Q: What are the three parameters for `Document.print()`? How can I obtain them?

A: Those are information about the sender and the receiver. Detailed descriptions are listed below:
 
`smart_guid` is the 16-hex-digit hardware ID of the printer which can be found by long-pressing the button on the machine for six seconds. 

`user_id` is the user ID of the sender, which can be obtained by using `memobird_agent.Util.get_user_id(username, password)`.

`to_user_id` is an **optional** parameter which represents the receiver's machine ID. (Defaults to be same as the `user_id`)


####Q: I called `document.print()` with correct parameters. Why the machine does not print my document?

A: To print a document on a specific machine, that machine must be binded to the user. Two methods are available: Use the official APP, or use the builtin function `memobird_agent.Util.bind_machine(smart_guid, user_id)`.


## Comments
Issues and Pull Requests are welcomed.

## Roadmap
### v2.5
1. Provide API to change status of the LED and buzzer.


### v3.x
1. Provide more functionalities.

[py2]:https://img.shields.io/badge/Python-2.x-brightgreen.svg "python2"
[py3]:https://img.shields.io/badge/Python-3.x-brightgreen.svg "python3"
[chinese_version]:https://github.com/tcai793/memobird_agent/blob/master/readme_cn.md "English Version"
[memobird]:https://www.memobird.shop/ "Memobird Description"
