## 数据推送工具（增）

### 日结数据

*   **原型**
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Yvenve5ewmKj0loy/img/17e44e68-d9b9-4dca-ad4f-5743a56947ad.png)
    
*   **业务规则**
    

1.  日期选择框默认值为昨天；
    
2.  用户选择日期， 点击【生成文件并推送】，提示“即将重新生成日结数据文件（{所选日期}）并推送，是否继续？”；
    
    1.  只可选择小于当日的日期；
        
    2.  提示中{所选日期}格式为：yyyy-mm-dd
        
3.  用户确认后，
    
    1.  提示“开始推送，请关注监控大屏或登录 SFTP 确认是否推送成功。”
        
    2.  生成对应日期的日结数据文件并推送到指定 sftp，参考：[《Vegas 2.0 系统对接需求（日结数据）》](https://alidocs.dingtalk.com/i/nodes/pYLaezmVN6aYBbpQS3DY1Q0XVrMqPxX6?utm_scene=team_space)
        

### 财务数据

*   **原型**
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Yvenve5ewmKj0loy/img/04f54efe-68a5-4fb5-93d3-a0bba3c099ac.png)
    
*   **业务规则**
    

1.  日期选择框默认值为昨天，月份选择框默认值为上个月；
    
2.  用户选择日期， 点击【生成文件并推送】，提示“即将重新生成财务数据日文件（{所选日期}）并推送，是否继续？”；或用户选择月份， 点击【生成文件并推送】，提示“即将重新生成财务数据月文件（{所选月份}）并推送，是否继续？”；
    
    1.  日文件只可选择小于当日的日期；
        
    2.  月文件只可选择小于当月的月份；
        
    3.  提示中，{所选日期}格式为：yyyy-mm-dd；{所选月份}格式为：yyyy-mm；
        
3.  用户确认后，
    
    1.  提示“开始推送，请关注监控大屏或登录 SFTP 确认是否推送成功。”
        
    2.  生成对应日期或月份的财务数据文件并推送到指定 sftp，参考：[《Vegas 2.0 系统对接需求（财务数据）》](https://alidocs.dingtalk.com/i/nodes/bva6QBXJwO7PgEvpCaQLo5BoJn4qY5Pr?utm_scene=team_space)
        

### 明细数据

*   **原型**
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Yvenve5ewmKj0loy/img/6eab4e7b-c054-4b00-a69c-d7be62b4160c.png)
    
*   **业务规则**
    

1.  日期选择框默认值为昨天；
    
2.  用户选择日期， 点击【生成文件并推送】，提示“即将重新生成明细数据文件（{所选日期}）并推送，是否继续？”；
    
    1.  只可选择小于当日的日期；
        
    2.  提示中{所选日期}格式为：yyyy-mm-dd
        
3.  用户确认后，
    
    1.  提示“开始推送，请关注监控大屏或登录 SFTP 确认是否推送成功。”
        
    2.  生成对应日期的明细数据文件并推送到指定 sftp，参考：[《Vegas 2.0 系统对接需求（明细数据）》](https://alidocs.dingtalk.com/i/nodes/np9zOoBVBQrX0kO5swzeAkogW1DK0g6l?utm_scene=team_space)
        

## 容器工具（增）

### 失败容器查询

*   **原型**
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Yvenve5ewmKj0loy/img/70c57c88-becf-4333-86bf-2fb3337e914e.png)
    
*   **业务规则**
    

1.  页面显示北单系统所有失败的容器信息（含 k8s 的），包括：Pod名称、命名空间、状态、失败原因、重启次数、创建时间，以及容器数量；按命名空间、创建时间正序排列；
    
2.  点击【刷新列表】，刷新当前页面；
    
3.  点击【打开容器管理页】，在新标签页打开指定链接，该链接地址可配置。（优先级低）