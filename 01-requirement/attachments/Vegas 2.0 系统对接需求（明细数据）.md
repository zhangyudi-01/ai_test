# Vegas 2.0 系统对接需求（明细数据）

版本更新记录

| **版本** | **更新时间** | **整理者** | **更新描述** |
| --- | --- | --- | --- |
| 0.1 | 2023/10/18 | 余庶捷 | 完成初稿 |
| 0.2 | 2023/10/23 | 余庶捷 | 更新 active、game\_def、game\_selection\_template 文件的固定传值规则 |
| 0.3 | 2023/10/24 | 余庶捷 | 更新 loc 文件的固定传值规则 |
| 0.4 | 2023/10/25 | 余庶捷 | 更新 clerk、game\_draw 文件的固定传值规则 |
| 0.5 | 2023/10/31 | 余庶捷 | 更新 clerk\_daily\_report 文件的时间范围 |
| 0.6 | 2024/5/20 | 余庶捷 | 更新 clerk 的登录密码传值规则 |
| 0.7 | 2025/11/25 | 余庶捷 | 1、更新 matchup、team、league 传值规则，适配赛事球队关联结构的调整<br>2、增加game\_draw\_stats\_prz\_lvl 文件，推送开奖 SP 值 |
| 0.8 | 2025/12/11 | 余庶捷 | 修正 loc 文件中 P\_LOC\_ID 传值规则 |
| 0.9 | 2025/12/25 | 余庶捷 | 增加 ticket\_win\_amount 文件推送 |

# 概述

根据总局中心竞猜处要求，为支持对竞猜型彩票进行市场跟踪分析，北单系统按自然日汇总销售票、中奖票、取消票等交易明细数据和近3个月的奖期、比赛等业务表信息，定期上传至 G3 系统。本文档描述了北单系统和 G3 系统之间关于明细数据上传的接口需求，作为系统研发和测试的依据。

参考：[《北单明细数据同步规则》](https://alidocs.dingtalk.com/i/nodes/1R7q3QmWe2KkbEgvSmP5gMl3VxkXOEP2?utm_scene=team_space)

# 名词释义

无

# 接口定义

明细数据以数据文件的方式进行交互，采用 CSV 格式文件，根据不同文件的数据量不同，分别采用全量数据上传、增量数据上传等方式，此外，结合 V2 升级的内容，还存在部分特殊上传规则的文件和空文件（仅包含字段名）。

以下任意文件按照约定规则抽取时若不存在对应数据，需生成一个空文件。

文件生成规则参考：[《北单运维管理平台PRD文档》](https://alidocs.dingtalk.com/i/nodes/MyQA2dXW7zQGkx4jSwDAbrgo8zlwrZgb?utm_scene=team_space&iframeQuery=anchorId%3Duu_llg8zsouwqgoc5jnhts)

**PS：**G3 系统加载文件时按字段顺序进行文件解析，因此新增字段须放最后，不可调整现有字段顺序，否则 G3 系统须同时变更。

## 全量上传的文件

将北单系统中对应的以下信息的全量数据生成数据文件并上传。

### active 文件

*   **文件说明**
    
    营销活动配置信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | ACTIVE\_ID | 活动 ID | 201109 |
    | ACTIVE\_NAME | 活动名称 | 云浮11月促销 |
    | GAME\_ID | V1 游戏编号列表 | 200,270 |
    | RDC\_ID | V1 分中心 ID | 20 |
    | TOTO\_PRIZE\_AMT | 活动预算，货币单位：元 | 500000 |
    | WARN\_AMT | 预警金额，货币单位：元 |  |
    | ENTRY\_NAME | 过关方式/场次数列表<br>与 SELECT\_TYPE 联合使用，当表示过关方式时，n 代表 n 串 1，0 为不限 | 6,7 |
    | RETURN\_TYPE | 活动规则，包含：1、固定百分比派送，2、满M送N，3、大于等于M送N | 2 |
    | RETURN\_PCT | 派送比例，RETURN\_TYPE 不为 1 时为空（V1）<br>固定传空 |  |
    | ACTIVE\_STATUS | 活动状态，包含： 0、结束时间未修改，3、结束时间已修改（V1）<br>固定传 0 | 0 |
    | ACTIVE\_YEAR | 活动年 | 2020 |
    | CREATE\_TIME | 创建时间 | 2020-11-20 16:47:25 |
    | PRZ\_LVL | 活动奖等 | 9998 |
    | PAID\_END\_TIME | 活动奖品兑奖结束时间，可空 | 2020-12-12 23:59:59 |
    | P\_COUNT\_NAME | 活动计奖程序名称（V1）<br>固定传空 |  |
    | TOTO\_AMT | 活动规则中的 M | 1000 |
    | PRIZE\_AMT | 活动规则中的 N | 200 |
    | BEGIN\_TIME | 活动开始时间 | 2020-11-23 00:00:00 |
    | END\_TIME | 活动结束时间<br>传 V2 的 actual\_end\_time，若 actual\_end\_time 为空，则传 end\_time | 2020-11-30 23:59:59 |
    | COUNTRY\_TYPE | 交互类型，包含： 0、 活动数据不传总局中心，1、 活动数据传总局中心 | 1 |
    | COUNT\_PRIZE\_AMT | 奖品应派金额 | 602800 |
    | ACTIVE\_TYPE | 促销类型，包含：1、中奖票促销，2、销售票促销 | 1 |
    | SELECT\_TYPE | 与 ENTRY\_NAME 联合使用，包含：1、根据过关方式，2、根据场次数（V1）<br>固定传 1 | 1 |
    | TOTO\_AMT1 | 活动规则中的 M1（V1）<br>固定传空 |  |
    | TOTO\_AMT2 | 活动规则中的 M2（V1）<br>固定传空 |  |
    | F\_ACTIVE\_ID | 父活动 ID，多级活动时使用，0：表示使用自己活动预算，非0：表示共享该活动 ID 的预算（V1）<br>固定传空 |  |
    | TERM\_TEXT | 终端弹框信息，销售票促销专用 |  |
    | LOC\_LIST | V1 地区 ID 列表<br>和 RDC\_ID 联合使用，为 0 时表示不限制地区 | 2021 |
    | END\_TIME\_TYPE | 活动结束方式，包含：now、立即结束，235959、当天结束（V1） |  |
    | REMARK | 活动描述 | 云浮体彩北京单场赠票活动，每中1000元送200元体育彩票 |
    | IF\_TAX | 计税标识，包含：0、不计税，1、计税 | 0 |
    | PRIZE\_TYPE | 派送类型，包含：1、赠票，2、派奖（V1）<br>固定传 1 | 1 |
    | TOP\_PRIZE\_AMT | 单票奖品金额上限，为 0 时表示不限 | 0 |
    
    注：（V1）表示在 V2 系统可能不存在对应数据，传固定值即可。
    
    ### country\_branch\_operator 文件
    
*   **文件说明**
    
    兑奖处用户信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | OPERATOR\_BJ\_ID | V1 兑奖处用户 ID | 84 |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID | 44 |
    | BRANCH\_ID | G3 兑奖处 ID | 911 |
    | OPERATOR\_ID | G3 兑奖处用户 ID | 1000051960 |
    | OPERATOR\_NAME | G3 兑奖处用户名称 | linx |
    | CREATE\_DATE | 创建时间 | 2022-05-19 16:37:18 |
    
    ### game\_def 文件
    
*   **文件说明**
    
    游戏配置信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | GAME\_ID | 游戏编号 | 200 |
    | GAME\_VER | 游戏版本（V1）<br>固定传 1 | 1 |
    | GAME\_TEMPLATE\_ID | 游戏模板编号（V1）<br>固定传空 |  |
    | GAME\_NAME | 游戏名称 | 胜平负 |
    | GAME\_STATUS | 游戏状态，包含：0、停用，1、启用 | 1 |
    | GAME\_BEGIN\_TIME | 游戏生效时间（V1）<br>固定传空 |  |
    | GAME\_END\_TIME | 游戏失效时间（V1）<br>固定传空 |  |
    | STAKE\_PRICE | 单注价格 | 2 |
    | MAX\_LOTTERY\_AMT | 单票最大投注金额 | 20000 |
    | RETURN\_PCT | 返奖比例 | 65 |
    | ADJ\_FUND\_PCT | 调节基金比例 | 0 |
    | ADJ\_FUND | 调节基金累计值，取整至小数点后 6 位，取整方式为四舍五入 | 3643926.78074 |
    | PKG\_NAME | V1 程序包名称（V1）<br>固定传空 |  |
    | SELECTION\_TYPE | 投注类型，包含：0、M选N无特别号，1、M选N有特别号，2、红蓝球投注，3、M场过N关，4、排列型无特别号，5、足球彩票，6、排列型有特别号，7、M场过单关，8、排列类剔重（V1）<br>固定传 3 | 3 |
    | PLAYER\_SELECTION\_CNT | 单注投注个数（V1）<br>固定传空 |  |
    | RESULT\_CNT | 开奖结果个数（V1）<br>固定传空 |  |
    | TIME\_FLAG | 定时标志（V1）<br>固定传 0 | 0 |
    | MATCHUP\_TYPE | 赛程表类型，包含：0、不使用赛程表，1、使用赛程表，不分关销售、计奖，2、使用赛程表，分关销售、计奖，4、使用单场赛程表（V1）<br>固定传 2 | 2 |
    | ASCII\_OFFSET | 起始编码偏移量（V1）<br>固定传 0 | 0 |
    | MAX\_DRAW\_CNT | 最大同时销售奖期数 | 1 |
    | RULE\_DESC | 规则描述（V1）<br>固定传空 |  |
    | GAME\_DESC | 游戏描述（V1）<br>固定传空 |  |
    | TERM\_DESC | 终端描述（V1）<br>固定传空 |  |
    | PARENT\_GAME\_ID | 父游戏编号（V1）<br>固定传空 |  |
    | COMPAT\_FLAG | 兼容标志（V1）<br>固定传 0 | 0 |
    | COMM\_ID | 佣金 ID（V1）<br>传 GAME\_ID 值 | 200 |
    | ADVANCE\_END\_SALE\_INTERVAL | 停售时间向前偏移量（V1）<br>固定传空 |  |
    | POSTPONE\_BEGIN\_PAID\_INTERVAL | 开始兑奖时间向后偏移量（V1）<br>固定传空 |  |
    | TIME\_SERVICE\_START\_TIME | 定时服务运行时间（V1）<br>固定传空 |  |
    | RISK\_CTL | 风控标志（V1）<br>固定传空 |  |
    | ADD\_CHANCE\_MULTIPLE | 追加投注倍数（V1）<br>固定传空 |  |
    | ADD\_PRZ\_MULTIPLE | 追加奖金倍数（V1）<br>固定传空 |  |
    | RESULT\_TIE\_FLAG | 开奖结果并列标志（V1）<br>固定传空 |  |
    | TEAM\_USE\_TYPE | 球队使用方式，包含：0、不使用主客队，1、只使用主队，2、使用主客队（V1）<br>固定传 2 | 2 |
    | TRUNC\_TYPE | 取整方式，包含：0、取整到元，2、取整到分，可空（V1）<br>固定传空 |  |
    | MAX\_SIM\_SALE\_DRAW\_CNT | 同时在售最多期数（V1）<br>固定传空 |  |
    | MAX\_DRAW\_SHOP\_SALE\_TICKET\_CNT | 单期单店最大销售票数（V1）<br>固定传空 |  |
    | IF\_REWARD | 派奖标志，包含：0、派奖，1、不派奖（V1）<br>固定传空 |  |
    | COUNTRY\_GAME\_ID | G3 游戏 ID | 4160 |
    | COUNTRY\_GAME\_NO | G3 游戏编号 | 1530001 |
    
    ### game\_selection\_template 文件
    
*   **文件说明**
    
    投注选项配置信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | GAME\_ID | 游戏编号 | 200 |
    | GAME\_VER | 游戏版本（V1）<br>固定传 1 | 1 |
    | ASCII\_NO | ASCII 编码 | 3 |
    | SELECTION\_NAME | 选项名称 | 0 |
    | SELECTION\_RULE | 选项规则（V1）<br>固定传空 |  |
    
    ### loc 文件
    
*   **文件说明**
    
    地区信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | LOC\_ID | V1 地区编号 | 1002 |
    | LOC\_NAME | 地区名称 | 西城 |
    | LOC\_TYPE | 地区类型，包含：0、国家，1、省，2、市，3、县 | 2 |
    | DEL\_FLAG | 删除标志（V1）<br>固定传 0 | 0 |
    | P\_LOC\_ID | 上级地区编号，可空（V1）<br>~~固定传空~~<br>传 rdc\_id 对应的 old\_rdc\_id | 10 |
    
    ### nation 文件
    
*   **文件说明**
    
    国家信息（V1）。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | NATION\_ID | 国家编号 | 40 |
    | NATION\_NAME | 国家名称 | 中国 |
    | NATION\_ABBR | 名称缩写 | CHN |
    
    ### rdc 文件
    
*   **文件说明**
    
    彩票中心信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | RDC\_ID | V1 中心 ID | 10 |
    | RDC\_NAME | 中心名称 | 北京 |
    | RDC\_FULL\_NAME | 中心全称，可空 |  |
    | BANK\_INT\_TYPE | 银行接口类型，包含：0、不支持，1、支持，2、部分支持（V1）<br>固定传 1 | 1 |
    | SHOP\_DEFAULT\_INIT\_QUOTA | 店初始额度，可空（V1）<br>固定传空 |  |
    | BI\_SUSPEND\_BEGIN\_DATE | 银行接口暂停开始日期，可空（V1）<br>固定传空 |  |
    | BI\_SUSPEND\_BEGIN\_TIME | 银行接口暂停开始时间，可空（V1）<br>固定传空 |  |
    | BI\_SUSPEND\_END\_DATE | 银行接口暂停截止日期，可空（V1）<br>固定传空 |  |
    | BI\_SUSPEND\_END\_TIME | 银行接口暂停截止时间，可空（V1）<br>固定传空 |  |
    | RDC\_BRANCH\_TYPE | 分支站类型，包含：0、不支持，1、支持，可空（V1）<br>固定传空 |  |
    | RDC\_COMM\_TYPE | 佣金转额度类型，包含：0、不支持，1、支持（V1）<br>固定传 1 | 1 |
    | RDC\_AWARD\_TYPE | 奖励下发类型，包含：0、不支持，1、支持（V1）<br>固定传 1 | 1 |
    
    ### rdc\_operator 文件
    
*   **文件说明**
    
    彩票中心用户信息。（V1）
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | OPERATOR\_BJ\_ID | 中心用户 ID | 2 |
    | RDC\_ID | V1 分中心 ID | 10 |
    | LOC\_ID | V1 地区编号 | 10 |
    | OPERATOR\_ID | 中心用户编号 | 1001 |
    | OPERATOR\_NAME | 中心用户名称 | admin |
    | CREATE\_DATE | 创建时间 | 2018-10-31 14:01:25 |
    
    ### toto\_dict 文件
    
*   **文件说明**
    
    数据字典信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DICT\_KEY | 字典键 | DRAW\_STATUS |
    | DICT\_VALUE | 字典值 | 0 |
    | DICT\_DESC | 字典描述 | 新建 |
    
    ## 增量上传的文件
    
    将北单系统中对应的以下信息的增量数据生成数据文件并上传。
    
    ### cancel\_ticket 文件
    
*   **文件说明**
    
    取消票信息。
    
    只传取消时间在统计日期，且取消成功的票信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 359397 |
    | TICKET\_NO | 彩票序列号 | 023781359192351441555159 |
    | CLERK\_ID | 销售员 ID | 58448 |
    | PASSWORD | 票密码 | 950,kswEKbhAZNFSXF14zF8l5pVgqjY |
    | SALE\_TIME | 售票时间 | 2023-10-11 21:00:48 |
    | CHANCES | 注数 | 8 |
    | SELECTION | 投注内容，需转换成可读格式 | 5+5+x+\[23\]1+2~\[24\]2+3~\[29\]3~\[30\]1~\[31\]2+3 |
    | MULTIPLE | 倍数 | 2 |
    | CANCEL\_TYPE | 取消类型 | 2 |
    | CANCEL\_TIME | 取消时间 | 2023-10-11 21:01:57 |
    | CANCEL\_OPERATOR\_ID | 操作员 ID | 58448 |
    | ADD\_FLAG | 追加标志（V1）<br>固定传空 |  |
    | BNO | 最小场次号 | 23 |
    | ENO | 最大场次号 | 31 |
    | TRANSACTION\_ID | 事务 ID | 100048332 |
    | CANCEL\_REASON | 取消原因 |  |
    
    ### clerk\_daily\_report 文件
    
*   **文件说明**
    
    销售员日统计信息。
    
    只传报表日期大于等于统计日期减 30 天的信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | CLERK\_ID | 销售员 ID | 85407 |
    | RPT\_DATE | 报表日期 | 2023-09-12 |
    | SALE\_TICKET\_CNT | 销售票数，统计该销售员销售的且售票时间在报表日期内的数据，需减去回滚数据，下同 | 3 |
    | SALE\_CHANCES | 销售注数 | 125 |
    | CLERK\_CANCEL\_TICKET\_CNT | 销售员取消票数，统计该销售员取消的且取消时间在报表日期内的数据，下同 |  |
    | CLERK\_CANCEL\_CHANCES | 销售员取消注数 |  |
    | CLERK\_CANCELED\_TICKET\_CNT | 销售员被取消票数，统计该销售员销售的票中，取消时间在报表日期内，且取消类型为终端取消的数据，下同 |  |
    | CLERK\_CANCELED\_CHANCES | 销售员被取消注数 |  |
    | RDC\_CANCEL\_TICKET\_CNT | 中心取消票数，统计该销售员销售的票中，取消时间在报表日期内，且取消类型为分中心取消和兑奖处取消的数据，下同 |  |
    | RDC\_CANCEL\_CHANCES | 中心取消注数 |  |
    | CLERK\_PAID\_TICKET\_CNT | 销售员兑奖票数，统计该销售员兑奖的且兑奖时间在报表日期内的数据（不含退票和活动奖品），下同 | 1 |
    | CLERK\_PAID\_CHANCES | 销售员兑奖注数 | 4 |
    | CLERK\_PAID\_AMT | 销售员兑奖金额 | 49.93 |
    | RDC\_PAID\_TICKET\_CNT | 中心兑奖票数，统计该销售员销售的票中，兑奖时间在报表日期内，且兑奖类型为分中心兑奖和兑奖处兑奖的数据（不含退票和活动奖品），下同 |  |
    | RDC\_PAID\_CHANCES | 中心兑奖注数 |  |
    | RDC\_PAID\_AMT | 中心兑奖金额 |  |
    | WITHDRAW\_AMT | 应退金额，统计该销售员销售的票中，开奖时间在报表日期内产生的应退金额 |  |
    | COMM\_ID | 佣金 ID（V1）<br>传 GAME\_ID 值 | 240 |
    | WITHDRAWED\_AMT | 销售员实退金额，统计兑奖时间在报表日期内的该销售员实退金额 | 0 |
    | RDC\_WITHDRAWED\_AMT | 中心实退金额，统计该销售员销售的票中，兑奖时间在报表日期内，且兑奖类型为分中心兑奖和兑奖处兑奖的实退金额 |  |
    
    ### ticket 文件
    
*   **文件说明**
    
    销售票信息。
    
    只传售票时间在统计日期的票信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 359397 |
    | TICKET\_NO | 彩票序列号 | 023611911951298777221436 |
    | CLERK\_ID | 销售员 ID | 42318 |
    | PASSWORD | 票密码 | da87,yDawbDPQieVEmDP90dkKqecEWv0 |
    | SALE\_TIME | 售票时间 | 2023-10-11 21:21:16 |
    | CHANCES | 注数 | 22 |
    | SELECTION | 投注内容，需转换成可读格式 | 6+4+5+6+x+\[20\]1~\[21\]1~\[22\]1~\[23\]3~\[24\]1~\[25\]3 |
    | MULTIPLE | 倍数 | 1 |
    | ADD\_FLAG | 追加标志（V1）<br>固定传空 |  |
    | BNO | 最小场次号 | 20 |
    | ENO | 最大场次号 | 25 |
    | TRANSACTION\_ID | 事务 ID | 100210728 |
    
    ### undo\_ticket 文件
    
*   **文件说明**
    
    回滚票信息。
    
    只传回滚时间在统计日期，且回滚成功的票信息。
    
*   **数据项**
    

| **字段名** | **字段说明** | **示例** |
| --- | --- | --- |
| DRAW\_ID | 奖期 ID | 359397 |
| TICKET\_NO | 彩票序列号 | 023611911951298777221436 |
| GAME\_ID | 游戏编号 | 200 |
| GAME\_VER | 游戏版本（V1）<br>固定传 1 | 1 |
| UNDO\_TIME | 回滚时间 | 2023-10-11 12:02:12 |
| TERM\_ID | 回滚的终端编号，对应 V2 的 term\_no | 4407030320101 |
| CLERK\_ID | 销售员 ID | 107180 |
| PASSWORD | 票密码 | 189a8,g5jP+TVvEWtL9vb4zGKNL1x83w4 |
| SALE\_TIME | 售票时间 | 2023-10-11 11:07:44 |
| CHANCES | 注数 | 1 |
| SELECTION | 投注内容，需转换成可读格式 | 2+2+x+\[18\]3~\[19\]1 |
| MULTIPLE | 倍数 | 50 |
| SALE\_DRAW\_CNT | 销售期数（V1）<br>固定传 1 | 1 |
| PAID\_DRAW\_CNT | 已兑奖期数（V1）<br>固定传 0 | 0 |
| TOTAL\_DRAW\_CNT | 总期数（V1）<br>固定传 1 | 1 |
| SALE\_DRAW\_LIST | 销售奖期列表（V1）<br>固定传空 |  |
| PAID\_DRAW\_LIST | 兑奖奖期列表（V1）<br>固定传空 |  |
| RENEW\_CLERK\_ID | 补打票销售员 ID（V1）<br>固定传空 |  |
| OLD\_TICKET\_NO | 原彩票序列号（V1）<br>固定传空 |  |
| UNDO\_TYPE | 回滚标志，包含：0、其他回滚，1、回滚销售票成功，2、回滚兑奖票成功，3、回滚销售票失败，4、回滚兑奖票失败（V1）<br>固定传 1 | 1 |
| CONFIRM\_FLAG | 确认标志（V1）<br>固定传 0 | 0 |
| UNDO\_ERR\_ID | 回滚原因的错误码 | 3108 |
| UNDO\_ERR\_DESC | 回滚原因的错误描述 | ccpos request to cancel the bet |
| UNDO\_FAILED\_ERR\_ID | 回滚失败的错误码 |  |
| ADD\_FLAG | 追加标志（V1）<br>固定传空 |  |
| BNO | 最小场次号 | 18 |
| ENO | 最大场次号 | 19 |
| TRANSACTION\_ID | 事务 ID | 100134701 |

### ticket\_with\_win\_amount 文件（增）

*   **文件说明**
    
    销售票中奖信息。
    
    只传票最终场次（eno）的开奖时间在统计日期的销售票的中奖信息。
    
*   **数据项**
    

| **字段名** | **字段说明** | **示例** |
| --- | --- | --- |
| DRAW\_ID | 奖期 ID | 359397 |
| TICKET\_NO | 彩票序列号 | 023611911951298777221436 |
| WIN\_AMOUNT | 中奖金额（不含退票金额），未中奖时为 0.00 | 123.45 |
| VOID\_AMOUNT | 退票金额，无退票时为 0.00 | 2.00 |

## 空文件

因 V2 系统不存在以下信息，按字段要求生成空数据文件并上传。

### draw\_ticket 文件

*   **文件说明**
    
    多期票信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** |
    | --- | --- |
    | DRAW\_ID | 奖期 ID |
    | TICKET\_NO | 彩票序列号 |
    | GAME\_ID | 游戏编号 |
    | GAME\_VER | 游戏版本 |
    | CLERK\_ID | 销售员 ID |
    | PASSWORD | 登录密码 |
    | SALE\_TIME | 售票时间 |
    | CHANCES | 注数 |
    | SELECTION | 投注内容 |
    | MULTIPLE | 倍数 |
    | SALE\_DRAW\_CNT | 销售期数 |
    | PAID\_DRAW\_CNT | 已兑奖期数 |
    | TOTAL\_DRAW\_CNT | 总期数 |
    | SALE\_DRAW\_LIST | 销售奖期列表 |
    | PAID\_DRAW\_LIST | 兑奖奖期列表 |
    | RENEW\_CLERK\_ID | 补打票销售员 ID |
    | OLD\_TICKET\_NO | 原彩票序列号 |
    | ADD\_FLAG | 追加标志 |
    | BNO | 最小场次号 |
    | ENO | 最大场次号 |
    
    ### his\_draw\_ticket 文件
    
*   **文件说明**
    
    历史多期票信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** |
    | --- | --- |
    | DRAW\_ID | 奖期 ID |
    | TICKET\_NO | 彩票序列号 |
    | GAME\_ID | 游戏编号 |
    | GAME\_VER | 游戏版本 |
    | CLERK\_ID | 销售员 ID |
    | PASSWORD | 票密码 |
    | SALE\_TIME | 售票时间 |
    | CHANCES | 注数 |
    | SELECTION | 投注内容 |
    | MULTIPLE | 倍数 |
    | SALE\_DRAW\_CNT | 销售期数 |
    | PAID\_DRAW\_CNT | 已兑奖期数 |
    | TOTAL\_DRAW\_CNT | 总期数 |
    | SALE\_DRAW\_LIST | 销售奖期列表 |
    | PAID\_DRAW\_LIST | 兑奖奖期列表 |
    | RENEW\_CLERK\_ID | 补打票销售员 ID |
    | OLD\_TICKET\_NO | 原彩票序列号 |
    | ADD\_FLAG | 追加标志 |
    | BNO | 最小场次号 |
    | ENO | 最大场次号 |
    
    ### kzc\_ticket 文件
    
*   **文件说明**
    
    快中彩游戏销售票信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** |
    | --- | --- |
    | DRAW\_ID | 奖期 ID |
    | TICKET\_NO | 彩票序列号 |
    | CLERK\_ID | 销售员 ID |
    | PASSWORD | 票密码 |
    | SALE\_TIME | 售票时间 |
    | CHANCES | 注数 |
    | SELECTION | 投注内容 |
    | MULTIPLE | 倍数 |
    | ADD\_FLAG | 追加标志 |
    | BNO | 最小场次号 |
    | ENO | 最大场次号 |
    | TRANSACTION\_ID | 事务 ID |
    
    ### ticket\_prize 文件
    
*   **文件说明**
    
    销售票促销活动奖品明细。
    
*   **数据项**
    
    | **字段名** | **字段说明** |
    | --- | --- |
    | DRAW\_ID | 奖期 ID |
    | TICKET\_NO | 彩票序列号 |
    | CLERK\_ID | 销售员 ID |
    | SHOP\_ID | V1 实体店 ID，对应 V2 的 shop\_no |
    | GAME\_ID | 游戏编号 |
    | ACTIVE\_ID | 活动 ID |
    | MNO\_CNT | 场次数 |
    | SALE\_AMT | 票面金额 |
    | PRIZE\_AMT | 奖品金额 |
    | SALE\_TIME | 售票时间 |
    
    ## 特殊规则文件
    
    ### shop 文件
    
*   **文件说明**
    
    实体店信息。
    
    拥有相同 shop\_no 的实体店只上传最新的一条记录，即优先取启用且未删除状态的实体店对应的信息，若无，则取 shop\_id 最大的实体店对应的信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | SHOP\_ID | V1 实体店 ID，对应 V2 的 shop\_no | 4406006234 |
    | RDC\_ID | V1 中心 ID | 20 |
    | LOC\_ID | V1 地区编号 | 2006 |
    | SHOP\_NAME | 实体店名称 | 4406006234 |
    | SHOP\_TYPE | V1 实体店级别，包含：1、Ａ级专卖店，2、Ｂ级专卖店，3、三级专卖店，4、四级专卖店，5、五级专卖店（V1）<br>固定传 1 | 1 |
    | DEL\_FLAG | 删除标志 | 1 |
    | AVAIL\_QUOTA | 可用额度（V1）<br>固定传 0 | 0 |
    | CREDIT\_QUOTA | 信用额度（V1）<br>固定传 0 | 0 |
    | SALE\_COMM\_PCT | 销售佣金比例（V1）<br>固定传 0 | 0 |
    | PAID\_COMM\_PCT | 兑奖佣金比例（V1）<br>固定传 0 | 0 |
    | PHONE | 电话，可空 |  |
    | EMAIL | EMAIL，可空（V1）<br>固定传空 |  |
    | FAX | 传真，可空（V1）<br>固定传空 |  |
    | ADDRESS | 实体店地址 | 南雄市老虎塘路口西 |
    | ZIP\_CODE | 邮编，可空（V1）<br>固定传空 |  |
    | CERTIFICATE\_TYPE | 代销者证件类型，包含：0、其他，1、身份证，2、护照，3、军官证，40、文职干部，50、警官证，60、士兵证，70、户口本，90、营业执照（V1）<br>固定传空 |  |
    | CERTIFICATE\_NO | 证件号码，可空（V1）<br>固定传空 |  |
    | SHOP\_OWNER | 代销者姓名，可空 |  |
    | SHOP\_CATEGORY | V1 实体店类型，包含：0、普通专卖店，1、兑大奖专卖店，2、特级专卖店，3、旗舰专卖店，4、旗舰专卖店B，5、电话投注店，6、国家专卖店（V1）<br>固定传 6 | 6 |
    | TEMP\_QUOTA\_LIMIT | 临时额度限额（V1）<br>固定传 0 | 0 |
    | SHOP\_STATUS | 实体店状态 | 0 |
    | MOBILE | 手机号，可空（V1）<br>固定传空 |  |
    | SHOP\_BANK\_INT\_TYPE | 银行接口类型，包含：0、不支持，1、支持（V1）<br>固定传 1 | 1 |
    | BRANCH\_ID | 分支站ID，可空（V1）<br>固定传空 |  |
    | SHOP\_PRINT\_STATUS | 安全加固状态，包含：0、加固启用，1、加固停用（V1）<br>固定传 0 | 0 |
    | SHOP\_COMM\_TYPE | 佣金类型，包含：0、不支持，1、支持（V1）<br>固定传 0 | 0 |
    
    ### term 文件
    
*   **文件说明**
    
    终端信息。
    
    只传 3.4.1 中实体店下的终端记录。
    
    存在重复的 term\_no 时，优先取未撤销且未删除状态的终端对应的信息，若无，则取 term\_id 最大的终端对应的信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | TERM\_ID | V1 终端 ID，对应 V2 的 term\_no | 4401031470101 |
    | SHOP\_ID | V1 实体店 ID，对应 V2 的 shop\_no | 4401031470 |
    | SOFT\_ID | 软件ID（V1）<br>固定传 999 | 999 |
    | PASSWORD | 终端密码 | 92743916 |
    | TERM\_STATUS | 终端状态 | 1 |
    | DEL\_FLAG | 删除标志 | 0 |
    | TERM\_IP | 终端IP地址（V1）<br>固定传空 |  |
    | UPDATABLE\_FLAG | 软件更新标志（V1）<br>固定传 1 | 1 |
    | CURRENT\_VER | 当前版本 | 600600 |
    
    ### clerk 文件
    
*   **文件说明**
    
    销售员信息。
    
    只传 3.4.1 中实体店下的销售员记录。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | CLERK\_ID | V2 销售员 ID | 33821 |
    | SHOP\_ID | V1 实体店 ID，对应 V2 的 shop\_no | 1101033003 |
    | LOGIN\_SERVER\_ID | 登录的服务器 ID（V1）<br>固定传空 |  |
    | LOGIN\_TERM\_ID | 登录的 V1 终端 ID，对应 V2 的 term\_no | 1101033003101 |
    | CLERK\_NO | 销售员编号 | 001 |
    | CLERK\_NAME | 销售员姓名，可空 |  |
    | PASSWORD | 登录密码，固定传 111111 | 111111 |
    | CLERK\_TYPE | V1 销售员类型，包含：0、店长，1、销售员 | 0 |
    | CLERK\_STATUS | V1 销售员状态，包含：0、停用，1、启用 | 1 |
    | SESSION\_TOKEN | 会话令牌<br>固定传空 |  |
    | LAST\_TICKET\_NO | 销售员售出的最后一张彩票票号，可空<br>固定传空 |  |
    | TICKET\_COUNTER | 票计数<br>固定传 0 | 0 |
    | DEL\_FLAG | 删除标志 | 0 |
    | AVAIL\_QUOTA | 可用额度（V1）<br>固定传 0 | 0 |
    | CANCEL\_LIMIT | 取消单票限额，取该实体店下最大终端 ID 对应的限额 | 1000 |
    | PAY\_LIMIT | 兑奖单票限额，取该实体店下最大终端 ID 对应的限额 | 100000 |
    | CERTIFICATE\_TYPE | 证件类型，包含：0、其他，1、身份证，2、护照，3、军官证，40、文职干部，50、警官证，60、士兵证，70、户口本，90、营业执照（V1）<br>固定传 0 | 0 |
    | CERTIFICATE\_NO | 证件号码（V1）<br>固定传空 |  |
    | CANCEL\_TIMEOUT | 取消时限，取该实体店下最大终端 ID 对应的限额 | 300 |
    | WEB\_FLAG | 网站标志（V1）<br>固定传 0 | 0 |
    | RDC\_PAY\_FLAG | 分中心兑奖标志（V1）<br>固定传空 |  |
    
    ### win\_ticket 文件
    
*   **文件说明**
    
    中奖票信息。
    
    只传统计日期内发生开奖和兑奖行为的奖期的所有中奖票信息。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 359393 |
    | TICKET\_NO | 彩票序列号 | 028287742340431811173051 |
    | WIN\_PRZ\_LVL | 中奖场次 | 43 |
    | CLERK\_ID | 销售员 ID | 105887 |
    | PASSWORD | 票密码 | 300e,7d/3N2ayfmXMGcngA0fbyQ/jBcw |
    | SALE\_TIME | 售票时间 | 2023-10-06 11:57:32 |
    | CHANCES | 注数 | 36 |
    | SELECTION | 投注内容，需转换成可读格式 | 3+1+3+x+\[36\]2+3+4~\[43\]3+5+6~\[50\]2+3+4 |
    | MULTIPLE | 倍数 | 1 |
    | PRZ\_CNT | 中奖注数 | 1 |
    | PRZ\_AMT | 中奖金额 | 8.69 |
    | TAX\_AMT | 上税金额 | 0 |
    | PAID\_TYPE | 兑奖类型，包含：1、分中心兑奖，2、终端兑奖，3、兑奖处兑奖，未兑奖时为空 | 2 |
    | PAID\_TIME | 兑奖时间 | 2023-10-07 10:49:00 |
    | WINNER\_NAME | 兑奖者姓名（V1）<br>固定传空 |  |
    | CERTIFICATE\_TYPE | 兑奖者证件类型（V1）<br>固定传空 |  |
    | CERTIFICATE\_NO | 兑奖者证件号码V1）<br>固定传空 |  |
    | PAID\_OPERATOR\_ID | 兑奖操作员 ID | 105887 |
    | ADD\_FLAG | 追加标志（V1）<br>固定传空 |  |
    | WITHDRAW\_AMT | 退票金额 | 0 |
    | BNO | 最小场次号 | 36 |
    | ENO | 最大场次号 | 50 |
    | TRANSACTION\_ID | 事务 ID | 100043759 |
    | WINNER\_ID | 兑奖者 ID（V1）<br>固定传空 |  |
    | PAYMENT\_TYPE | 支付方式 |  |
    
    ### win\_ticket\_prize 文件
    
*   **文件说明**
    
    中奖票促销活动奖品明细。
    
    只传统计日期内未止兑的所有中奖票促销活动数据。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 25082 |
    | TICKET\_NO | 彩票序列号 | 023611911951298777221436 |
    | WIN\_PRZ\_LVL | 活动奖品对应的奖等 | 9994 |
    | CLERK\_ID | 销售员 ID | 2301261 |
    | MONEY | 票面金额 | 198 |
    | ENO | 最大场次号 | 20 |
    | PRZ\_CNT | 游戏中奖注数 | 99 |
    | PRZ\_AMT | 游戏中奖金额 | 128.7 |
    | PAID\_TYPE | 兑奖类型，包含：1、分中心兑奖，2、终端兑奖，3、兑奖处兑奖，未兑奖时为空 | 2 |
    | PAID\_TIME | 兑奖时间 | 2023-10-11 11:07:44 |
    | PAID\_OPERATOR\_ID | 兑奖操作员 ID | 20161 |
    | PRIZE\_AMT | 活动奖品金额 | 1280 |
    | PRIZE\_CNT | 活动奖品注数 | 64 |
    | ACTIVE\_ID | 活动 ID | 211001 |
    | PRIZE\_TAX | 活动上税金额 | 0 |
    
    ### game\_draw 文件
    
*   **文件说明**
    
    奖期信息。
    
    只传奖期开奖时间在统计日期前 3 个月内的数据。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 359313 |
    | GAME\_ID | 游戏编号 | 200 |
    | GAME\_VER | 游戏版本（V1）<br>固定传 1 | 1 |
    | DRAW\_NO | 奖期编号 | 23072 |
    | SALE\_BEGIN\_TIME | 开售时间 | 2023-07-04 10:00:00 |
    | SALE\_END\_TIME | 停售时间 | 2023-07-11 06:00:00 |
    | DRAW\_TIME | 开奖时间 | 2023-07-11 10:30:00 |
    | PAID\_BEGIN\_TIME | 兑奖开始时间 | 2023-07-04 23:25:01 |
    | PAID\_END\_TIME | 兑奖结束时间 | 2023-09-11 23:59:59 |
    | DRAW\_STATUS | 奖期状态 | 7 |
    | DRAW\_RESULT | 开奖结果，需转换成可读格式（V1） | 1~1~3~3~3~2~1~2~1~2~3~\*~1 |
    | DRAW\_TYPE | 奖期类型 | 0 |
    | SUSPEND\_FLAG | V1 奖期暂停状态，包含：0、奖期正常，1、销售暂停，兑奖正常，2、销售正常，兑奖暂停，3、销售暂停，兑奖暂停（V1）<br>V2 到 V1 的对应关系如下：<br>0、4 -> 0<br>1、5 -> 1<br>2、6 -> 2<br>3、7 -> 3 | 0 |
    | ORIG\_RESULT | 原始开奖结果（V1）<br>固定传空 |  |
    | DRAW\_LICENSE\_QUOTA | 奖期总许可额度（V1）<br>固定传空 |  |
    | MAIN\_LEAGUE\_NAME | 主要赛制名（V1）<br>固定传空 |  |
    | IF\_REWARD | 派奖标志（V1）<br>固定传空 |  |
    | ACTIVE\_ID | 活动 ID（V1）<br>固定传空 |  |
    
    ### game\_draw\_stats\_clerk\_paid 文件
    
*   **文件说明**
    
    销售员场次兑奖统计信息。
    
    只传 3.4.6 中对应奖期的数据。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 359322 |
    | CLERK\_ID | 销售员 ID | 39506 |
    | DRAW\_PRZ\_LVL | 中奖场次 | 47 |
    | WIN\_CHANCES | 中奖注数，统计该销售员销售的该奖期该中奖场次的数据（不含退票和活动奖品），下同 | 113 |
    | WIN\_AMT | 中奖金额 | 1526.39 |
    | CLERK\_PAID\_CHANCES | 销售员兑奖注数，统计该销售员兑奖的该奖期该中奖场次的数据（不含退票和活动奖品），下同 | 113 |
    | CLERK\_PAID\_AMT | 销售员兑奖金额 | 1526.39 |
    | RDC\_PAID\_CHANCES | 中心兑奖注数，统计该销售员销售的该奖期该中奖场次的中奖票中，兑奖类型为分中心兑奖和兑奖处兑奖的数据（不含退票和活动奖品），下同 |  |
    | RDC\_PAID\_AMT | 中心兑奖金额 |  |
    | WITHDRAW\_AMT | 应退金额，统计该销售员销售的该奖期票中，该中奖场次的退票金额 | 0 |
    | WITHDRAWED\_AMT | 销售员实退金额，统计该销售员兑奖的该奖期该中奖场次的退票金额 | 0 |
    | RDC\_WITHDRAWED\_AMT | 中心实退金额，统计该销售员销售的该奖期票中，兑奖类型为分中心兑奖和兑奖处兑奖的该中奖场次的退票金额 |  |
    
    ### game\_draw\_stats\_clerk\_sale 文件
    
*   **文件说明**
    
    销售员奖期统计信息。
    
    只传 3.4.6 中对应奖期的数据。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | CLERK\_ID | 销售员 ID | 26547 |
    | DRAW\_ID | 奖期 ID | 359321 |
    | SALE\_TICKET\_CNT | 销售票数，统计该销售员销售的该奖期的数据，需减去回滚数据，下同 | 53 |
    | SALE\_CHANCES | 销售注数 | 1679 |
    | CLERK\_CANCEL\_TICKET\_CNT | 销售员取消票数，统计该销售员取消的该奖期的数据，下同 | 1 |
    | CLERK\_CANCEL\_CHANCES | 销售员取消注数 | 50 |
    | RDC\_CANCEL\_TICKET\_CNT | 中心取消票数，统计该销售员销售的该奖期票中，取消类型为分中心取消和兑奖处取消的数据，下同 |  |
    | RDC\_CANCEL\_CHANCES | 中心取消注数 |  |
    | CLERK\_PAID\_TICKET\_CNT | 销售员兑奖票数，统计该销售员兑奖的该奖期的数据（不含退票和活动奖品），下同 | 7 |
    | CLERK\_PAID\_CHANCES | 销售员兑奖注数 | 182 |
    | CLERK\_PAID\_AMT | 销售员兑奖金额 | 1311.51 |
    | RDC\_PAID\_TICKET\_CNT | 中心兑奖票数，统计该销售员销售的该奖期票中，兑奖类型为分中心兑奖和兑奖处兑奖的数据（不含退票和活动奖品），下同 |  |
    | RDC\_PAID\_CHANCES | 中心兑奖注数 |  |
    | RDC\_PAID\_AMT | 中心兑奖金额 |  |
    | WITHDRAW\_AMT | 应退金额，统计该销售员销售的该奖期票中的退票金额 | 208 |
    | WITHDRAWED\_AMT | 销售员实退金额，统计该销售员兑奖的该奖期的退票金额 | 208 |
    | RDC\_WITHDRAWED\_AMT | 中心实退金额，统计该销售员销售的该奖期票中，兑奖类型为分中心兑奖和兑奖处兑奖的退票金额 |  |
    
    ### matchup 文件（改）
    
*   **文件说明**
    
    赛程信息。
    
    只传 3.4.6 中对应奖期的数据。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | DRAW\_ID | 奖期 ID | 359313 |
    | MATCHUP\_NO | 场次编号 | 7 |
    | HOST\_TEAM\_ID | 主队 ID | 72789 |
    | GUEST\_TEAM\_ID | 客队 ID | 72796 |
    | SALE\_END\_TIME | 停售时间 | 2023-07-05 06:00:00 |
    | DRAW\_FLAG | 开奖标志 | 1 |
    | HANDICAP | 让球 | \-1 |
    | MATCHUP\_DESC | 比赛描述 |  |
    | SELECTION\_CNT | 选项数（V1）<br>固定传空 |  |
    | SP\_FLAG | SP 值标志 | 1 |
    | MATCHUP\_STATUS | 开售状态 | 2 |
    | MATCHUP\_TIMESTAMP | 时间戳 | 1688527070 |
    | LEAGUE\_ID | 比赛所属赛事 ID | 5025 |
    
    ### team 文件（改）
    
*   **文件说明**
    
    球队信息。
    
    只传 3.4.9 中的赛程里使用的球队数据。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | TEAM\_ID | 球队 ID | 72774 |
    | LEAGUE\_ID | 球队所属赛事 ID<br>固定传空 | ~~5025~~ |
    | TEAM\_NAME | 球队简称 | 科罗拉多急流 |
    | TEAM\_FULL\_NAME | 球队全称 | 科罗拉多急流 |
    | DEL\_FLAG | 删除标志 | 0 |
    | TEAM\_DESC | 球队描述 |  |
    | NATION\_ID | 球队所属国家 ID（V1）<br>固定传空 |  |
    | TEAM\_TIMESTAMP | 时间戳 | 1676878976 |
    
    ### league 文件（改）
    
*   **文件说明**
    
    赛事信息。
    
    ~~只传 3.4.10 中的球队所属的赛事数据。~~
    
    只传 3.4.9 中的赛程里使用的赛事数据。
    
*   **数据项**
    

| **字段名** | **字段说明** | **示例** |
| --- | --- | --- |
| LEAGUE\_ID | 赛事 ID | 4776 |
| LEAGUE\_NAME | 赛事简称 | 23-24墨超 |
| LEAGUE\_FULL\_NAME | 赛事全称 | 23-24赛季墨西哥足球超级联赛 |
| LEAGUE\_TYPE | 运动项目 | 1 |
| HIDE\_FLAG | 隐藏标志（V1）<br>固定传 0 | 0 |
| SELECTION\_TYPE | 投注类型，包含：0、M选N无特别号，1、M选N有特别号，2、红蓝球投注，3、M场过N关，4、排列型无特别号，5、足球彩票，6、排列型有特别号，7、M场过单关，8、排列类剔重（V1）<br>固定传 3 | 3 |

### game\_draw\_stats\_prz\_lvl 文件（增）

*   **文件说明**
    
    奖期计奖结果统计信息。
    
    只传 3.4.6 中对应奖期的数据。
    
*   **数据项**
    

| **字段名** | **字段说明** | **示例** |
| --- | --- | --- |
| DRAW\_ID | 奖期ID | 359313 |
| DRAW\_PRZ\_LVL | 奖期奖等级别 | 999 |
| TOTAL\_CHANCES | 本场总投注注数 | 11111.123456789012 |
| RIGHT\_CHANCES | 本场总命中注数 | 11111.123456789012 |
| WIN\_SP | 开奖 SP 值 | 2.123456789012 |
| WIN\_STAKE\_AMT | 单注中奖金额 | 3.1234 |
| WIN\_CHANCES | 中奖注数 | 11111.123456789012 |
| WIN\_AMT | 中奖金额 | 1111111.12 |
| PAID\_CHANCES | 兑奖注数 | 11111.123456789012 |
| PAID\_AMT | 兑奖金额 | 1111111.12 |
| WITHDRAW\_AMT | 应退票金额 | 10 |
| WITHDRAWED\_AMT | 实退票金额 | 10 |
| WIN\_SELECTION\_CHANCES | 中奖的投注注数 | 111 |
| PAID\_SELECTION\_CHANCES | 兑奖的投注注数 | 111 |

## 其他文件

### total\_record 文件（改）

*   **文件说明**
    
    汇总信息。
    
    统计同批上传的各文件的数据条数。
    
*   **数据项**
    

| **字段名** | **字段说明** | **示例** |
| --- | --- | --- |
| \- | 文件名 | game\_draw |
| \- | 数据条数 | 90 |

# 附录

无