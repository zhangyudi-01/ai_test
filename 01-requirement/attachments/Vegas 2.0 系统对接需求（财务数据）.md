# Vegas 2.0 系统对接需求（财务数据）

版本更新记录

| **版本** | **更新时间** | **整理者** | **更新描述** |
| --- | --- | --- | --- |
| 0.1 | 2023/10/23 | 余庶捷 | 完成初稿 |

# 概述

根据总局中心要求，为支撑其财务管理、资金结算与财政部数据上报等相关工作，北单系统提供北单游戏相关的财务数据，定期上传至 G3 系统。本文档描述了北单系统和 G3 系统之间关于财务数据上传的接口需求，作为系统研发和测试的依据。

# 名词释义

### （1）常规奖等

常规奖等，指游戏规则中设置的奖等。

### （2）派奖

派奖，指使用游戏调节基金进行的活动，如加奖。派奖产生的弃奖转入公益金。

### （3）促销

促销，指使用业务费进行的活动，如赠票。促销产生的弃奖返还业务费。

# 接口定义

财务数据以数据文件的方式进行交互，采用 CSV 格式文件，包含日文件和月度文件两类。

文件首行为统计行，日文件规则为： \[年月日(yyyyMMdd)\],\[数据总条数\]，如：20200521,123456；月度文件规则为：\[年月(yyyyMM)\],\[数据总条数\]，如：202005,123456。

第二行为字段定义行，其他为数据行。

如果数据行的某字段没有相应数据对应，需在该字段的位置填0。

日文件如果整个文件均没有相应数据对应，需传明细为空的文件。

## 日文件

### ifs-c-day-stats 文件

*   **文件说明**
    
    自然日统计数据。
    
    包含售票时间、兑奖时间在统计日期的数据。
    
    区分终端和兑奖处统计数据，即 BRANCH\_ID 与 TERMINAL\_ID、SHOP\_ID 互斥， TERMINAL\_ID 不为空，表示终端兑奖， BRANCH\_ID 不为空，则表示兑奖处兑奖。
    
    按分中心各生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明**<br>**（终端）** | **示例**<br>**（终端）** | **字段说明**<br>**（兑奖处）** | **示例**<br>**（兑奖处）** |
    | --- | --- | --- | --- | --- |
    | REPORT\_DATE | 统计日期 | 20230928 | 统计日期 | 20230928 |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID | 11 | G3 分中心 ID | 11 |
    | TECH\_SYSTEM\_ID | 技术系统 ID，北单系统为 53 | 53 | 技术系统 ID，北单系统为 53 | 53 |
    | GAME\_NO | 传 GAME\_ID | 200 | 传 GAME\_ID | 200 |
    | GAME\_ID | 游戏编号 | 200 | 游戏编号 | 200 |
    | DRAW\_ID | 传 DRAW\_NO | 23095 | 传 DRAW\_NO | 23095 |
    | DRAW\_NO | 奖期编号 | 23095 | 奖期编号 | 23095 |
    | TERMINAL\_ID | 传 SHOP\_ID | 72465660 | 固定传空 |  |
    | SHOP\_ID | G3 实体店 ID | 72465660 | 固定传空 |  |
    | CHANNEL\_TYPE\_CODE | 投注渠道类型<br>固定传 1 ，即传统终端投注 | 1 | 投注渠道类型<br>固定传 1 ，即传统终端投注 | 1 |
    | SALE\_LOTTERY\_CNT | 实体店销售票数（不包含取消， 包含退票，下同） | 47 | 固定传 0 | 0 |
    | SALE\_STAKE\_CNT | 实体店销售注数 | 3015 | 固定传 0 | 0 |
    | SALE\_AMOUNT | 实体店销售金额 | 6030 | 固定传 0 | 0 |
    | STS\_PAID\_LOTTERY\_CNT | 实体店自兑奖票数<br>传 PAID\_LOTTERY\_CNT | 1 | 固定传 0 | 0 |
    | STS\_PAID\_STAKE\_CNT | 实体店自兑奖注数<br>传 PAID\_STAKE\_CNT | 27 | 固定传 0 | 0 |
    | STS\_PAID\_AMOUNT | 实体店自兑奖金额<br>传 PAID\_AMOUNT | 67.74 | 固定传 0 | 0 |
    | STO\_PAID\_LOTTERY\_CNT\_SAMEPC | （同省）本实体店兑其他实体店中奖票数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_STAKE\_CNT\_SAMEPC | （同省）本实体店兑其他实体店中奖注数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_AMOUNT\_SAMEPC | （同省）本实体店兑其他实体店中奖金额<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_LOTTERY\_CNT\_DIFFPC | （跨省）本实体店兑其他实体店中奖票数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_STAKE\_CNT\_DIFFPC | （跨省）本实体店兑其他实体店中奖注数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_AMOUNT\_DIFFPC | （跨省）本实体店兑其他实体店中奖金额<br>固定传 0 | 0 | 固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT\_NORMAL | 实体店兑奖票数（常规奖等） | 1 | 固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_NORMAL | 实体店兑奖注数（常规奖等） | 27 | 固定传 0 | 0 |
    | PAID\_AMOUNT\_NORMAL | 实体店兑奖金额（常规奖等） | 67.74 | 固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT\_PFRC | 实体店兑奖票数（派奖奖等） | 0 | 固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_PFRC | 实体店兑奖注数（派奖奖等） | 0 | 固定传 0 | 0 |
    | PAID\_AMOUNT\_PFRC | 实体店兑奖金额（派奖奖等） | 0 | 固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT\_PFP | 实体店兑奖票数（促销奖等） | 0 | 固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_PFP | 实体店兑奖注数（促销奖等） | 0 | 固定传 0 | 0 |
    | PAID\_AMOUNT\_PFP | 实体店兑奖金额（促销奖等） | 0 | 固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT | 实体店兑奖票数（常规+派奖+促销） | 1 | 固定传 0 | 0 |
    | PAID\_STAKE\_CNT | 实体店兑奖注数（常规+派奖+促销） | 27 | 固定传 0 | 0 |
    | PAID\_AMOUNT | 实体店兑奖金额（常规+派奖+促销） | 67.74 | 固定传 0 | 0 |
    | BRANCH\_ID | 固定传空 |  | 兑奖处 ID | 0 |
    | BRANCH\_PAID\_LOTTERY\_CNT\_SAMEPC | 固定传 0 | 0 | （同省）兑奖处兑奖票数<br>传 BRANCH\_PAID\_LOTTERY\_CNT | 8 |
    | BRANCH\_PAID\_STAKE\_CNT\_SAMEPC | 固定传 0 | 0 | （同省）兑奖处兑奖注数<br>传 BRANCH\_PAID\_STAKE\_CNT | 74138 |
    | BRANCH\_PAID\_AMOUNT\_SAMEPC | 固定传 0 | 0 | （同省）兑奖处兑奖金额<br>传 BRANCH\_PAID\_AMOUNT | 279603.58 |
    | BRANCH\_PAID\_LOTTERY\_CNT\_DIFFPC | 固定传 0 | 0 | （跨省）兑奖处兑奖票数<br>固定传 0 | 0 |
    | BRANCH\_PAID\_STAKE\_CNT\_DIFFPC | 固定传 0 | 0 | （跨省）兑奖处兑奖注数<br>固定传 0 | 0 |
    | BRANCH\_PAID\_AMOUNT\_DIFFPC | 固定传 0 | 0 | （跨省）兑奖处兑奖金额<br>固定传 0 | 0 |
    | BRANCH\_PAID\_TAX | 固定传 0 | 0 | 兑奖处兑奖税金 | 55920.73 |
    | BRANCH\_PAID\_LOTTERY\_CNT\_NORMAL | 固定传 0 | 0 | 兑奖处兑奖票数（常规奖等） | 8 |
    | BRANCH\_PAID\_STAKE\_CNT\_NORMAL | 固定传 0 | 0 | 兑奖处兑奖注数（常规奖等） | 74138 |
    | BRANCH\_PAID\_AMOUNT\_NORMAL | 固定传 0 | 0 | 兑奖处兑奖金额（常规奖等） | 279603.58 |
    | BRANCH\_PAID\_LOTTERY\_CNT\_PFRC | 固定传 0 | 0 | 兑奖处兑奖票数（派奖奖等） | 0 |
    | BRANCH\_PAID\_STAKE\_CNT\_PFRC | 固定传 0 | 0 | 兑奖处兑奖注数（派奖奖等） | 0 |
    | BRANCH\_PAID\_AMOUNT\_PFRC | 固定传 0 | 0 | 兑奖处兑奖金额（派奖奖等） | 0 |
    | BRANCH\_PAID\_LOTTERY\_CNT\_PFP | 固定传 0 | 0 | 兑奖处兑奖票数（促销奖等） | 0 |
    | BRANCH\_PAID\_STAKE\_CNT\_PFP | 固定传 0 | 0 | 兑奖处兑奖注数（促销奖等） | 0 |
    | BRANCH\_PAID\_AMOUNT\_PFP | 固定传 0 | 0 | 兑奖处兑奖金额（促销奖等） | 0 |
    | BRANCH\_PAID\_LOTTERY\_CNT | 固定传 0 | 0 | 兑奖处兑奖票数（常规+派奖+促销） | 8 |
    | BRANCH\_PAID\_STAKE\_CNT | 固定传 0 | 0 | 兑奖处兑奖注数（常规+派奖+促销） | 74138 |
    | BRANCH\_PAID\_AMOUNT | 固定传 0 | 0 | 兑奖处兑奖金额（常规+派奖+促销） | 279603.58 |
    | STS\_REFUND\_LOTTERY\_CNT | 实体店实退票数 | 0 | 固定传 0 | 0 |
    | STS\_REFUND\_STAKE\_CNT | 实体店实退注数 | 0 | 固定传 0 | 0 |
    | STS\_REFUND\_AMOUNT | 实体店实退金额 | 0 | 固定传 0 | 0 |
    | STO\_REFUND\_LOTTERY\_CNT | 本实体店退其他实体店票数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_REFUND\_STAKE\_CNT | 本实体店退其他实体店注数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_REFUND\_AMOUNT | 本实体店退其他实体店金额<br>固定传 0 | 0 | 固定传 0 | 0 |
    | BRANCH\_REFUND\_LOTTERY\_CNT | 固定传 0 | 0 | 兑奖处实退票数 | 0 |
    | BRANCH\_REFUND\_STAKE\_CNT | 固定传 0 | 0 | 兑奖处实退注数 | 0 |
    | BRANCH\_REFUND\_AMOUNT | 固定传 0 | 0 | 兑奖处实退金额 | 0 |
    
    ### ifs-draw-sale-close 文件
    
*   **文件说明**
    
    奖期止售数据。
    
    包含统计日期内变更为开始兑奖状态的奖期数据。
    
    按分中心各生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID | 11 |
    | GAME\_NO | 游戏编号 <br>传 GAME\_ID | 200 |
    | DRAW\_NO | 奖期编号 | 23095 |
    | SALE\_BEGIN\_TIME | 开售时间 | 2023-09-26 10:00:00 |
    | SALE\_END\_TIME | 停售时间 | 2023-09-30 23:30:00 |
    | RETURN\_PCT | 返奖比例<br>(返奖比例+公益金比例+发行费比例=1) | 0.65 |
    | ADJUST\_FUND\_PCT | 调节基金比例 | 0 |
    | COMMONWEAL\_FUND\_PCT | 公益金比例 | 0.22 |
    | ISSUE\_COST\_PCT | 发行费比例 | 0.13 |
    | NDC\_ISSUE\_COST\_PCT | 发行机构发行费比例 | 0.005 |
    | TERMINAL\_ID | 传 SHOP\_ID | 1001180060 |
    | SHOP\_ID | G3 实体店 ID | 1001180060 |
    | CHANNEL\_TYPE\_CODE | 投注渠道类型<br>固定传 1 ，即传统终端投注 | 1 |
    | SALE\_LOTTERY\_CNT | 净销售票数（不包含取消和退票，下同） | 128 |
    | SALE\_STAKE\_CNT | 净销售注数 | 12416 |
    | SALE\_AMOUNT | 净销售金额 | 24832 |
    
    ### ifs-draw-prized 文件
    
*   **文件说明**
    
    奖期开奖数据。
    
    包含统计日期内变更为开始兑奖状态的奖期数据。
    
    按分中心各生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID | 11 |
    | GAME\_NO | 游戏编号 <br>传 GAME\_ID | 200 |
    | DRAW\_NO | 奖期编号 | 23095 |
    | DRAW\_TIME | 开奖时间 | 2023-10-05 10:30:00 |
    | PAY\_BEGIN\_TIME | 兑奖开始时间 | 2023-09-26 23:25:01 |
    | PAY\_END\_TIME | 兑奖结束时间 | 2023-12-04 23:59:59 |
    | TERMINAL\_ID | 传 SHOP\_ID | 40331560 |
    | SHOP\_ID | G3 实体店 ID | 40331560 |
    | CHANNEL\_TYPE\_CODE | 投注渠道类型<br>固定传 1 ，即传统终端投注 | 1 |
    | WIN\_LOTTERY\_CNT | 中奖票数（常规+派奖+促销） | 5 |
    | WIN\_STAKE\_CNT | 中奖注数（常规+派奖+促销） | 701 |
    | WIN\_AMOUNT | 中奖金额（常规+派奖+促销） | 2623.85 |
    | TAX\_WIN\_AMOUNT | 应税中奖金额（应上税部分的中奖金额，包含，常规+派奖+促销） | 0 |
    | WIN\_LOTTERY\_CNT\_NORMAL | 中奖票数（常规奖等） | 5 |
    | WIN\_STAKE\_CNT\_NORMAL | 中奖注数（常规奖等） | 701 |
    | WIN\_AMOUNT\_NORMAL | 中奖金额（常规奖等） | 2623.85 |
    | WIN\_LOTTERY\_CNT\_PFRC | 中奖票数（派奖奖等） | 0 |
    | WIN\_STAKE\_CNT\_PFRC | 中奖注数（派奖奖等） | 0 |
    | WIN\_AMOUNT\_PFRC | 中奖金额（派奖奖等） | 0 |
    | WIN\_LOTTERY\_CNT\_PFP | 中奖票数（促销奖等） | 0 |
    | WIN\_STAKE\_CNT\_PFP | 中奖注数（促销奖等） | 0 |
    | WIN\_AMOUNT\_PFP | 中奖金额（促销奖等） | 0 |
    | VOID\_LOTTERY\_CNT | 应退票数 | 0 |
    | VOID\_STAKE\_CNT | 应退注数 | 0 |
    | VOID\_AMOUNT | 应退金额 | 0 |
    
    ### ifs-draw-paidclose-bydraw 文件
    
*   **文件说明**
    
    奖期止兑奖期级数据。
    
    包含统计日期内变更为结束兑奖状态的奖期数据。
    
    按分中心各生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID | 11 |
    | GAME\_NO | 游戏编号 <br>传 GAME\_ID | 240 |
    | DRAW\_NO | 奖期编号 | 23075 |
    | PAY\_BEGIN\_TIME | 兑奖开始时间 | 2023-07-25 13:25:01 |
    | PAY\_END\_TIME | 兑奖结束时间 | 2023-10-07 23:59:59 |
    | PAID\_LOTTERY\_CNT\_SAMEPC | 兑奖票数（常规+派奖+促销） | 1580 |
    | PAID\_STAKE\_CNT\_SAMEPC | 兑奖注数（常规+派奖+促销） | 90350 |
    | PAID\_AMOUNT\_SAMEPC | 兑奖金额（常规+派奖+促销） | 860604.37 |
    | PAID\_TAX\_AMOUNT\_SAMEPC | 兑奖税金（常规+派奖+促销） | 13704.53 |
    | PAID\_LOTTERY\_CNT\_SAMEPC\_NORMAL | 兑奖票数（常规奖等） | 1580 |
    | PAID\_STAKE\_CNT\_SAMEPC\_NORMAL | 兑奖注数（常规奖等） | 90350 |
    | PAID\_AMOUNT\_SAMEPC\_NORMAL | 兑奖金额（常规奖等） | 860604.37 |
    | PAID\_LOTTERY\_CNT\_SAMEPC\_PFRC | 兑奖票数（派奖奖等） | 0 |
    | PAID\_STAKE\_CNT\_SAMEPC\_PFRC | 兑奖注数（派奖奖等） | 0 |
    | PAID\_AMOUNT\_SAMEPC\_PFRC | 兑奖金额（派奖奖等） | 0 |
    | PAID\_LOTTERY\_CNT\_SAMEPC\_PFP | 兑奖票数（促销奖等） | 0 |
    | PAID\_STAKE\_CNT\_SAMEPC\_PFP | 兑奖注数（促销奖等） | 0 |
    | PAID\_AMOUNT\_SAMEPC\_PFP | 兑奖金额（促销奖等） | 0 |
    | PAID\_LOTTERY\_CNT\_DIFFPC | （跨省）兑奖票数（常规+派奖+促销）<br>固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_DIFFPC | （跨省）兑奖注数（常规+派奖+促销）<br>固定传 0 | 0 |
    | PAID\_AMOUNT\_DIFFPC | （跨省）兑奖金额（常规+派奖+促销）<br>固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT\_DIFFPC\_NORMAL | （跨省）兑奖票数（常规奖等）<br>固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_DIFFPC\_NORMAL | （跨省）兑奖注数（常规奖等）<br>固定传 0 | 0 |
    | PAID\_AMOUNT\_DIFFPC\_NORMAL | （跨省）兑奖金额（常规奖等）<br>固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT\_DIFFPC\_PFRC | （跨省）兑奖票数（派奖奖等）<br>固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_DIFFPC\_PFRC | （跨省）兑奖注数（派奖奖等）<br>固定传 0 | 0 |
    | PAID\_AMOUNT\_DIFFPC\_PFRC | （跨省）兑奖金额（派奖奖等）<br>固定传 0 | 0 |
    | PAID\_LOTTERY\_CNT\_DIFFPC\_PFP | （跨省）兑奖票数（促销奖等）<br>固定传 0 | 0 |
    | PAID\_STAKE\_CNT\_DIFFPC\_PFP | （跨省）兑奖注数（促销奖等）<br>固定传 0 | 0 |
    | PAID\_AMOUNT\_DIFFPC\_PFP | （跨省）兑奖金额（促销奖等）<br>固定传 0 | 0 |
    | PAID\_TAX\_AMOUNT\_DIFFPC | （跨省）兑奖税金<br>固定传 0 | 0 |
    | UNPAID\_LOTTERY\_CNT | 弃奖票数（常规+派奖+促销） | 5 |
    | UNPAID\_STAKE\_CNT | 弃奖注数（常规+派奖+促销） | 271 |
    | UNPAID\_AMOUNT | 弃奖金额（常规+派奖+促销） | 2644.43 |
    | UNPAID\_LOTTERY\_CNT\_NORMAL | 弃奖票数（常规奖等） | 5 |
    | UNPAID\_STAKE\_CNT\_NORMAL | 弃奖注数（常规奖等） | 271 |
    | UNPAID\_AMOUNT\_NORMAL | 弃奖金额（常规奖等） | 2644.43 |
    | UNPAID\_LOTTERY\_CNT\_PFRC | 弃奖票数（派奖奖等） | 0 |
    | UNPAID\_STAKE\_CNT\_PFRC | 弃奖注数（派奖奖等） | 0 |
    | UNPAID\_AMOUNT\_PFRC | 弃奖金额（派奖奖等） | 0 |
    | UNPAID\_LOTTERY\_CNT\_PFP | 弃奖票数（促销奖等） | 0 |
    | UNPAID\_STAKE\_CNT\_PFP | 弃奖注数（促销奖等） | 0 |
    | UNPAID\_AMOUNT\_PFP | 弃奖金额（促销奖等） | 0 |
    | UNPAID\_TO\_COMMONWEAL\_FUND | 弃奖转公益金<br>弃奖金额（常规奖等）与弃奖金额（派奖奖等）之和 | 2644.43 |
    | REFUND\_LOTTERY\_CNT | 实退票数 | 0 |
    | REFUND\_STAKE\_CNT | 实退注数 | 0 |
    | REFUND\_AMOUNT | 实退金额 | 0 |
    | UNREFUND\_LOTTERY\_CNT | 逾期未退票数 | 0 |
    | UNREFUND\_STAKE\_CNT | 逾期未退注数 | 0 |
    | UNREFUND\_AMOUNT | 逾期未退金额 | 0 |
    
    ### ifs-draw-paidclose-byterminal 文件
    
*   **文件说明**
    
    奖期止兑终端级数据。
    
    包含统计日期内变更为结束兑奖状态的奖期数据。
    
    区分终端和兑奖处统计数据，即 BRANCH\_ID 与 TERMINAL\_ID、SHOP\_ID 互斥， TERMINAL\_ID 不为空，表示终端兑奖， BRANCH\_ID 不为空，则表示兑奖处兑奖。
    
    按分中心各生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明**<br>**（终端）** | **示例**<br>**（终端）** | **字段说明**<br>**（兑奖处）** | **示例**<br>**（兑奖处）** |
    | --- | --- | --- | --- | --- |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID | 11 | G3 分中心 ID | 11 |
    | GAME\_NO | 游戏编号 <br>传 GAME\_ID | 200 | 游戏编号 <br>传 GAME\_ID | 210 |
    | DRAW\_NO | 奖期编号 | 23081 | 奖期编号 | 23081 |
    | TERMINAL\_ID | 传 SHOP\_ID | 916323460 | 固定传空 |  |
    | SHOP\_ID | G3 实体店 ID | 916323460 | 固定传空 |  |
    | CHANNEL\_TYPE\_CODE | 投注渠道类型<br>固定传 1 ，即传统终端投注 | 1 | 投注渠道类型<br>固定传 1 ，即传统终端投注 | 1 |
    | STS\_PAID\_LOTTERY\_CNT | 实体店自兑奖票数（常规奖等） | 1 | 固定传 0 | 0 |
    | STS\_PAID\_STAKE\_CNT | 实体店自兑奖注数（常规奖等） | 38 | 固定传 0 | 0 |
    | STS\_PAID\_AMOUNT | 实体店自兑奖金额（常规奖等） | 108.04 | 固定传 0 | 0 |
    | STO\_PAID\_LOTTERY\_CNT\_SAMEPC | （同省）本实体店兑其他实体店中奖票数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_STAKE\_CNT\_SAMEPC | （同省）本实体店兑其他实体店中奖注数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_AMOUNT\_SAMEPC | （同省）本实体店兑其他实体店中奖金额<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_LOTTERY\_CNT\_DIFFPC | （跨省）本实体店兑其他实体店中奖票数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_STAKE\_CNT\_DIFFPC | （跨省）本实体店兑其他实体店中奖注数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_PAID\_AMOUNT\_DIFFPC | （跨省）本实体店兑其他实体店中奖金额<br>固定传 0 | 0 | 固定传 0 | 0 |
    | BRANCH\_ID | 固定传空 |  | 兑奖处 ID | 0 |
    | BRANCH\_PAID\_LOTTERY\_CNT | 固定传 0 | 0 | 兑奖处兑奖票数（常规+派奖+促销） | 2 |
    | BRANCH\_PAID\_STAKE\_CNT | 固定传 0 | 0 | 兑奖处兑奖注数（常规+派奖+促销） | 9206 |
    | BRANCH\_PAID\_AMOUNT | 固定传 0 | 0 | 兑奖处兑奖金额（常规+派奖+促销） | 35715.6 |
    | BRANCH\_PAID\_TAX | 固定传 0 | 0 | 兑奖处兑奖税金 | 7143.12 |
    | BRANCH\_REFUND\_LOTTERY\_CNT | 固定传 0 | 0 | 兑奖处实退票数 | 0 |
    | BRANCH\_REFUND\_STAKE\_CNT | 固定传 0 | 0 | 兑奖处实退注数 | 0 |
    | BRANCH\_REFUND\_AMOUNT | 固定传 0 | 0 | 兑奖处实退金额 | 0 |
    | STS\_REFUND\_LOTTERY\_CNT | 实体店实退票数 | 0 | 固定传 0 | 0 |
    | STS\_REFUND\_STAKE\_CNT | 实体店实退注数 | 0 | 固定传 0 | 0 |
    | STS\_REFUND\_AMOUNT | 实体店实退金额 | 0 | 固定传 0 | 0 |
    | STO\_REFUND\_LOTTERY\_CNT | 本实体店退其他实体店票数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_REFUND\_STAKE\_CNT | 本实体店退其他实体店注数<br>固定传 0 | 0 | 固定传 0 | 0 |
    | STO\_REFUND\_AMOUNT | 本实体店退其他实体店金额<br>固定传 0 | 0 | 固定传 0 | 0 |
    | UNREFUND\_LOTTERY\_CNT | 逾期未退票数 | 0 | 固定传 0 | 0 |
    | UNREFUND\_STAKE\_CNT | 逾期未退注数 | 0 | 固定传 0 | 0 |
    | UNREFUND\_AMOUNT | 逾期未退金额 | 0 | 固定传 0 | 0 |
    
    ### ifs-capital-change 文件
    
*   **文件说明**
    
    资金变动明细。
    
    包含资金变更时间在统计日期的数据。
    
    只以主中心身份生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | REPORT\_DATE | 统计日期 | 20230928 |
    | TECH\_SYSTEM\_ID | 技术系统 ID，北单系统为 53 | 53 |
    | FLOW\_ID | 流水号 | 50 |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID<br>固定传 0 | 0 |
    | FUND\_TYPE\_CODE | 基金类型，包含：1、奖池，2、调节基金，3、发行费， 4、公益金，5、一般调节基金<br>只传类型为 2 和 4 的数据 | 2 |
    | FLOW\_TYPE\_CODE | 流向类型，包含：1、转入，2、转出 | 1 |
    | GAME\_NO | 游戏编号 <br>传 GAME\_ID | 200 |
    | DRAW\_NO | 奖期编号 | 23095 |
    | PRIOR\_FLOW\_AMOUNT | 分配前金额，取整至小数点后 6 位，取整方式为四舍五入 | 3639153.840056 |
    | POST\_FLOW\_AMOUNT | 分配后金额，取整至小数点后 6 位，取整方式为四舍五入 | 3639155.197957 |
    | FLOW\_AMOUNT | 分配金额，取整至小数点后 6 位，取整方式为四舍五入 | 1.357902 |
    | FLOW\_GROUP\_CODE | 基金变动类型<br>固定传空 |  |
    | FLOW\_DESCRIPTION | 资金流描述 | (50)调节基金:取整归入 |
    
    ### ifs-game 文件
    
*   **文件说明**
    
    基础游戏信息。
    
    只以主中心身份生成一份文件。
    
*   **数据项**
    
    | **字段名** | **字段说明** | **示例** |
    | --- | --- | --- |
    | REPORT\_DATE | 统计日期 | 20230928 |
    | PROVINCE\_CENTER\_ID | G3 分中心 ID<br>固定传 0 | 0 |
    | TECH\_SYSTEM\_ID | 技术系统 ID，北单系统为 53 | 53 |
    | GAME\_NO | 游戏编号 <br>传 GAME\_ID | 200 |
    | GAME\_NAME | 游戏名称 | 胜平负 |
    | GAME\_STATUS\_CODE | 游戏状态，包含：10、已创建，20、文件已加载，30、已发布，40、已启用，50、已停用，60、已退市 | 40 |
    | GAME\_AREA\_RANGE\_TYPE\_CODE | 游戏区域范围类型，包含：10、地方游戏，20、区域游戏，30、全国游戏<br>固定传 20 | 20 |
    | GAME\_FUND\_RANGE\_TYPE\_CODE | 游戏资金范围类型，包含：10、地方彩池，20、区域彩池，30、全国彩池<br>固定传 20 | 20 |
    | MAIN\_RELATED\_GAME\_NO | 主关联游戏编码<br>固定传空 |  |
    
    ## 月度文件
    
    ### ifs-month-stats 文件
    
*   **文件说明**
    
    月统计信息。
    
    停售时间在上个月内的奖期，均变更为开始兑奖状态的次日，生成月度文件并上传，其余日期不传。
    
    按分中心各生成一份文件。
    
*   **数据项**
    

| **字段名** | **字段说明** | **示例** |
| --- | --- | --- |
| REPORT\_MONTH | 统计月份 | 202309 |
| PROVINCE\_CENTER\_ID | G3 分中心 ID | 11 |
| TECH\_SYSTEM\_ID | 技术系统 ID，北单系统为 53 | 53 |
| GAME\_NO | 传 GAME\_ID | 270 |
| SPORTS\_TYPE\_CODE | 运动类型（篮球，足球），竞彩特有<br>固定传空 |  |
| SALE\_AMOUNT | 销售金额（售票时间在统计月份的票金额，不包含取消， 包含退票）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 5392316.00 |
| SALE\_AMOUNT\_SETTLED | 净销售金额（停售时间在统计月份的奖期的净销量，不包含取消和退票）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 5829426.00 |
| RETURN\_AMOUNT | 返奖金额（净销售金额 \* 返奖比例），若统计区间内出现不同比例，则根据不同的比例分别统计金额后再计算和值<br>取整至小数点后 4 位，取整方式为四舍五入，不足 4 位时补 0 | 3789126.9000 |
| ISSUE\_COST | 发行费金额（净销售金额 \* 发行费比例），统计区间内出现不同比例，则根据不同的比例分别统计金额后再计算和值<br>取整至小数点后 4 位，取整方式为四舍五入，不足 4 位时补 0 | 757825.3800 |
| NDC\_ISSUE\_COST | 发行机构发行费金额（净销售金额 \* 发行机构发行费比例），统计区间内出现不同比例，则根据不同的比例分别统计金额后再计算和值<br>取整至小数点后 4 位，取整方式为四舍五入，不足 4 位时补 0 | 29147.1300 |
| ADJUST\_AMOUNT | 调节基金计提金额（净销售金额 \* 调节基金比例），统计区间内出现不同比例，则根据不同的比例分别统计金额后再计算和值<br>取整至小数点后 4 位，取整方式为四舍五入，不足 4 位时补 0 | 0.0000 |
| COMMONWEAL\_FUND | 计提公益金（净销售金额 \* 公益金比例），统计区间内出现不同比例，则根据不同的比例分别统计金额后再计算和值<br>取整至小数点后 4 位，取整方式为四舍五入，不足 4 位时补 0 | 1282473.7200 |
| VOID\_AMOUNT | 应退金额（在统计月份内变更为开始兑奖状态的奖期的应退金额）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 0.00 |
| WIN\_AMOUNT | 中奖金额（在统计月份内变更为开始兑奖状态的奖期中奖金额，包含，常规+派奖+促销）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 3337420.87 |
| PAID\_AMOUNT\_SAMEPC | 兑奖金额（兑奖时间在统计月份的兑奖金额，包含，常规+派奖+促销）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 3454726.72 |
| STO\_PROV\_PAID\_AMOUNT | 本省兑他省兑奖金额<br>固定传 0.00 | 0.00 |
| OTS\_PROV\_PAID\_AMOUNT | 他省兑本省兑奖金额<br>固定传 0.00 | 0.00 |
| TAX\_AMOUNT | 兑奖税金（兑奖时间在统计月份的中奖票的上税金额，包含，常规+派奖+促销）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 11576.67 |
| REFUND\_AMOUNT | 实退金额（兑奖时间在统计月份的退票金额）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 0.00 |
| UNREFUND\_AMOUNT | 逾期未退金额（在统计月份内变更为结束兑奖状态的奖期的逾期未退金额）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 0.00 |
| UNPAID\_AMOUNT | 弃奖金额（在统计月份内变更为结束兑奖状态的奖期的弃奖金额，包含，常规+派奖+促销）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 167.57 |
| UNPAID\_TO\_COMMONWEAL\_FUND | 弃奖转公益金（在统计月份内变更为结束兑奖状态的奖期的弃奖金额，包含，常规+派奖）<br>取整至小数点后 2 位，取整方式为四舍五入，不足 2 位时补 0 | 167.57 |

# 附录

无