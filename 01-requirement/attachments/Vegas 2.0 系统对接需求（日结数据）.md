# Vegas 2.0 系统对接需求（日结数据）

版本更新记录

| **版本** | **更新时间** | **整理者** | **更新描述** |
| --- | --- | --- | --- |
| 0.1 | 2023/10/12 | 余庶捷 | 完成初稿 |
| 0.2 | 2023/10/13 | 余庶捷 | 字段说明区分销售员记录和兑奖处记录 |
| 0.3 | 2023/10/16 | 余庶捷 | 更新兑奖处记录中部分注数和金额的默认值 |
| 0.4 | 2023/10/27 | 余庶捷 | 更新销售员记录中的终端 ID 取值规则 |
| 0.5 | 2023/10/30 | 余庶捷 | 更新注数的取整规则 |
| 0.6 | 2024/3/29 | 余庶捷 | 更新销售员记录中的终端 ID 取值规则 |

# 概述

由于实体店的额度和北单游戏的交易分别在 G3 和北单系统中进行管理，为避免产生双方系统数据不一致的情况，北单系统每天将实体店的日销售统计数据（以下称日结数据）上传至 G3 系统，供 G3 系统进行对账。本文档描述了北单系统和 G3 系统之间关于日结数据上传的接口需求，作为系统研发和测试的依据。

参考：[《数据加载服务与第三方系统接口文档》](https://alidocs.dingtalk.com/i/nodes/P0MALyR8kwMaPEB2fmyMLbd183bzYmDO?utm_scene=team_space)

# 名词释义

无

# 接口定义

日结数据以数据文件的方式进行交互。

文件生成规则参考：[《北单运维管理平台PRD文档》](https://alidocs.dingtalk.com/i/nodes/MyQA2dXW7zQGkx4jSwDAbrgo8zlwrZgb?utm_scene=team_space&iframeQuery=anchorId%3Duu_llewvkda923hxpbebm)

## Report 文件

*   **文件说明**
    
    CSV 格式文件，包含各销售员的销售、取消、兑奖等数据，或各兑奖处的兑奖数据。
    
*   **数据项**
    
    | **字段名** | **字段说明**<br>**（销售员交易信息）** | **字段说明**<br>**（兑奖处兑奖信息）** |
    | --- | --- | --- |
    | BranchID | 兑奖处 ID，固定传空（空字符) | 兑奖处 ID |
    | SiteID | 实体店 ID，固定传空（空字符) | 实体店 ID，固定传空（空字符) |
    | ClerkID | 销售员 ID，固定传空（空字符) | 销售员 ID，固定传空（空字符) |
    | ReportDate | 日期，即日结数据所在的日期<br>格式为“yyyy-MM-dd” | 日期，即日结数据所在的日期<br>格式为“yyyy-MM-dd” |
    | SaleLotteryCnt | 销售票数，统计售票时间在统计日期内的数据，须减去取消数据，无须减应退数据，下同 | 固定传 0 |
    | SaleStakeCnt | 销售注数 | 固定传 0 |
    | SaleAmount | 销售金额 | 固定传 0 |
    | SelfCancelLotteryCnt | 取消票数，统计取消时间在统计日期内的数据，下同 | 固定传 0 |
    | SelfCancelStakeCnt | 取消注数 | 固定传 0 |
    | SelfCancelAmount | 取消金额 | 固定传 0 |
    | RdcCancelLotteryCnt | 中心取消票数，统计该销售员销售的票（无售票时间限制）被分中心和兑奖处取消，且取消时间在统计日期内的数据，下同 | 固定传 0 |
    | RdcCancelStakeCnt | 中心取消注数 | 固定传 0 |
    | RdcCancelAmount | 中心取消金额 | 固定传 0 |
    | SelfToSelfPaidLotteryCnt | 兑奖票数，统计兑奖时间在统计日期内的数据，不含实退数据，含活动兑奖数据，下同 | 固定传 0 |
    | SelfToSelfPaidStakeCnt | 兑奖注数，取整至小数点后 4 位，取整方式为截取<br>数据为 0 时，传 0.00 | 固定传 0.00 |
    | SelfToSelfPaidAmount | 兑奖金额 | 固定传 0.00 |
    | SelfToOtherPaidLotteryCnt | 代兑票数，固定传 0 | 固定传 0 |
    | SelfToOtherPaidStakeCnt | 代兑注数，固定传 0 | 固定传 0 |
    | SelfToOtherPaidAmount | 代兑金额，固定传 0 | 固定传 0 |
    | OtherToSelfPaidLotteryCnt | 通兑票数，固定传 0 | 固定传 0 |
    | OtherToSelfPaidStakeCnt | 通兑注数，固定传 0 | 固定传 0 |
    | OtherToSelfPaidAmount | 通兑金额，固定传 0 | 固定传 0 |
    | RdcToSelfPaidLotteryCnt | 中心兑奖票数，统计该销售员销售的票（无售票时间限制）被被分中心或兑奖处兑奖（含退票和活动兑奖数据），且兑奖时间在统计日期内的数据，下同 | 固定传 0 |
    | RdcToSelfPaidStakeCnt | 中心兑奖注数，取整至小数点后 4 位，取整方式为截取<br>数据为 0 时，传 0.00 | 固定传 0.00 |
    | RdcToSelfPaidAmount | 中心兑奖金额 | 固定传 0.00 |
    | VoidLotteryCnt | 实退票数，固定传 0 | 固定传 0 |
    | VoidStakeCnt | 实退注数，统计兑奖时间在统计日期内的数据，下同 | 固定传 0 |
    | VoidAmount | 实退金额 | 固定传 0 |
    | RefundLiabilityLotteryCnt | 应退票数，固定传 0 | 固定传 0 |
    | RefundLiabilityStakeCnt | 应退注数，统计该销售员销售的票（无售票时间限制）在统计日期内开奖产生的应退数据，下同 | 固定传 0 |
    | RefundLiabilityAmount | 应退金额 | 固定传 0 |
    | WinLotteryCnt | 中奖票数，统计日期内有奖期变更为开始兑奖状态时，传该销售员整个奖期的中奖数据（含活动中奖），无则传 0，下同 | 固定传 0 |
    | WinStakeCnt | 中奖注数，取整至小数点后 4 位，取整方式为截取<br>数据为 0 时，传 0.00 | 固定传 0.00 |
    | WinAmount | 中奖金额 | 固定传 0.00 |
    | BranchPaidLotteryCnt | 固定传 0 | 兑奖处兑奖票数 |
    | BranchPaidStakeCnt | 固定传 0 | 兑奖处兑奖注数 |
    | BranchPaidAmount | 固定传 0 | 兑奖处兑奖金额 |
    | QuitAmount | 弃奖金额，统计日期内有奖期变更为结束兑奖状态时，传该销售员整个奖期的弃奖数据（不含活动弃奖），无则传 0 | 固定传 0.00 |
    | SelfPaidAmount | 可自兑金额，固定传 0 | 固定传 0 |
    | UnVoidAmount | 逾期未退金额，统计日期内有奖期变更为结束兑奖状态时，传该销售员整个奖期的逾期未退数据，无则传 0 | 固定传 0.00 |
    | TaxAmount | 固定传 0 | 扣税金额，即兑奖票中对应的上税金额 |
    | TerminalID | 终端 ID<br>传该实体店下统计日期内有交易数据的最大终端 ID，统计日期内无交易数据时，取统计日期前 100 天内有交易数据的最大终端 ID | 固定传 0 |
    | LogonID | G3 登录账号 ID，即北单系统的销售员，对应 g3\_clerk\_id | 固定传 0 |
    | GameNO | 游戏编码，北单游戏传 1530001 | 游戏编码，北单游戏传 1530001 |
    
*   **示例**
    
    ```text/x-sql
    BranchID,SiteID,ClerkID,ReportDate,SaleLotteryCnt,SaleStakeCnt,SaleAmount,SelfCancelLotteryCnt,SelfCancelStakeCnt,SelfCancelAmount,RdcCancelLotteryCnt,RdcCancelStakeCnt,RdcCancelAmount,SelfToSelfPaidLotteryCnt,SelfToSelfPaidStakeCnt,SelfToSelfPaidAmount,SelfToOtherPaidLotteryCnt,SelfToOtherPaidStakeCnt,SelfToOtherPaidAmount,OtherToSelfPaidLotteryCnt,OtherToSelfPaidStakeCnt,OtherToSelfPaidAmount,RdcToSelfPaidLotteryCnt,RdcToSelfPaidStakeCnt,RdcToSelfPaidAmount,VoidLotteryCnt,VoidStakeCnt,VoidAmount,RefundLiabilityLotteryCnt,RefundLiabilityStakeCnt,RefundLiabilityAmount,WinLotteryCnt,WinStakeCnt,WinAmount,BranchPaidLotteryCnt,BranchPaidStakeCnt,BranchPaidAmount,QuitAmount,SelfPaidAmount,UnVoidAmount,TaxAmount,TerminalID,LogonID,GameNO
    ,,,"2023-10-10",183,4966,9932,0,0,0,0,0,0,20,180,5664.56,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0,0,0,84,1302,67330.52,0,0,0,0.00,0,0.00,0,168611,101811,1530001
    1211,,,"2023-10-10",0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0.00,0.00,1,187,12691.58,0.00,0,0.00,2143.12,0,0,1530001
    ```
    
*   **补充说明**
    

BranchID 与 LogonID、TerminalID 互斥，即有一方信息为空或 0；每个 ID 对应一条数据；

BranchID 非空时代表兑奖处兑奖信息，只传 ReportDate、BranchPaidLotteryCnt、BranchPaidStakeCnt、BranchPaidAmount、TaxAmount、GameNO，其他字段传 0，固定传空值的除外；只生成 BranchID 大于 0 的数据；

BranchID 为空时代表销售员交易信息，BranchPaidLotteryCnt、BranchPaidStakeCnt、BranchPaidAmount 传 0；

中奖数据和兑奖数据中，常规奖和活动奖品对应的是同一张票，票数不应重复计算；

须包含已删除的实体店及销售员在统计日期内产生的数据；

按分中心生成各自的数据文件。

# 附录

## 游戏编码

| **值** | **描述** |
| --- | --- |
| 1530001 | 北单游戏 |
| 1530002 | 奥运游戏 |
| 1530003 | 快中彩 |