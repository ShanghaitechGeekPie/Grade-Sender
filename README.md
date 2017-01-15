# Grade-Sender
成绩邮件推送脚本

# Usage

```
python3 mail.py
```

数据来自grade.dat文件，请参照示例。
发件邮箱信息请在mail.py中设置。DEBUG为True默认为发送到发件人邮箱以供测试。使用时请记得改为False。
因为系统有每分钟限发5封邮件的限制，所以每5封邮件自动等待一分钟。
