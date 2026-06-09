# 北单游戏维护工具个人业务理解

## 项目背景
这个项目其实只是一个管理的页面，核心业务功能已经在之前都实现了，它主要是给中心技术部运维人员，当由于硬件（如光驱、盘片）、网络或逻辑错误导致封存验奖任务失败时，通过该工具手动干预、重新触发任务，以确保业务闭环。


这个项目其实只是一个管理的页面，核心业务功能已经在之前都实现了，我主要负责了之前的Kafka实时推送、SFTP-明细推送、实时SFTP推送的测试，
可以参考[北单运维管理平台PRD文档.md](../02-history-requirements/%E5%8C%97%E5%8D%95%E8%BF%90%E7%BB%B4%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0PRD%E6%96%87%E6%A1%A3.md)
这个文档中讲述了Kafka实时推送、实时SFTP推送、SFTP-明细推送的运转逻辑，其中在[attachments](../02-history-requirements/attachments)目录下也对各个逻辑做了详细的描述。

这次只需要关注 00-global/00-source-materials/01-current-requirement/REQ-当前迭代需求-v1.md 的内容即可
