## 北单实时推送服务-SFTP推送工具

#### 配置项

- 文件上传本地路径：/share/realtime_sftp
- 文件上传sftp路径：/share/realtime_sftp
- 定时服务配置的推送时间：整点推送，范围0点至23点

#### 本次涉及改动的文件

- matchup文件、team文件、league文件、loc文件

#### 获取数据范围

> **统计日期**：`当前日期`  - `14`  day
>
> **全量**

- matchup文件、team文件、league文件获取数据范围为`统计日期` 
- loc文件获取数据范围为全量

#### 文件命名

##### csv文件命名

文件名+".csv"，例如matchup.csv，所有csv文件压缩为一个压缩包

##### zip文件命名

bjdc_yyyymmddhh.zip，例如bjdc_2021102200.zip

#### 文件上传

##### 本地上传

上传至本地服务器中，按照本地服务器配置路径上传：/share/realtime_sftp，本地存储路径路径管理：

![image-20251219170005578](C:\Users\15216\AppData\Roaming\Typora\typora-user-images\image-20251219170005578.png)

##### sftp上传

sftp上传：按照配置的路径上传/share/realtime_sftp，不分日期，直接将zip都存到realtime_sftp目录下

#### end文件生成

最终在zip文件上传成功后，再在同级目录中生成同名文件bjdc_yyyymmddhh.end

