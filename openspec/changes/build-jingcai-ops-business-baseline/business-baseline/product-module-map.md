# 产品模块地图

基线版本：`BASE-JCOPS-2026-04-22-V1`

## 模块清单

| 模块ID | 一级模块 | 二级子域/页面簇 | 模块职责 | 关键业务对象 | 主要来源回指 |
| --- | --- | --- | --- | --- | --- |
| `MOD-GLOBAL` | 登录与全局能力 | 登录、改密、令牌绑定、权限控制、通知 | 负责账号登录、身份验证器绑定、会话有效期、访问控制和顶部通知中心 | `OBJ-ACCOUNT`、`OBJ-AUTH-DEVICE`、`OBJ-NOTICE` | `PRD章节 | §登录/修改密码/通知 (L101-L148, L2816-L2825)` |
| `MOD-RISK` | 风险管理 | 球队黑名单、赛事黑名单、操作记录 | 负责对高风险球队/赛事做拉黑与移除，并保留操作原因和记录 | `OBJ-BLACKLIST-RECORD`、`OBJ-COMPETITION`、`OBJ-TEAM` | `PRD章节 | §风险管理 (L149-L231)` |
| `MOD-SCHEDULE` | 北单赛程管理 | 奖期、批次管理、草稿管理、草稿比对、正式详情、文件提交 | 负责北单奖期、赛程批次、草稿编排、正式赛程生成、赛程文件提交和回执处理 | `OBJ-DRAW-PERIOD`、`OBJ-SCHEDULE-BATCH`、`OBJ-MATCH`、`OBJ-SUBMISSION-RECORD` | `PRD章节 | §北单赛程管理 (L232-L1281)` |
| `MOD-MONITOR` | 比赛监控 | 比赛赛程监控、监控记录、赛果审核、赛果确认、截图、进程信息 | 负责对比赛状态、监控记录、赛果审核确认和截图证据进行管理 | `OBJ-MATCH`、`OBJ-MONITOR-RECORD`、`OBJ-RESULT-CONFIRM` | `PRD章节 | §比赛监控 (L1282-L1536)` |
| `MOD-ABNORMAL` | 异常管理 | 事件管理、告警管理、预警管理、备注 | 负责异常事件、告警、预警的浏览、核实、确认和备注补充 | `OBJ-EVENT`、`OBJ-ALERT`、`OBJ-WARNING` | `PRD章节 | §异常管理 (L1537-L1681)` |
| `MOD-CHANGE` | 变更管理 | 异常变更、处理操作页、变更详情、导出 | 负责对异常后的业务变更进行处理、作废、完成确认、导出和回执上传 | `OBJ-CHANGE-RECORD`、`OBJ-RECEIPT-FILE` | `PRD章节 | §变更管理 (L1682-L1860)` |
| `MOD-DRAW` | 开奖管理 | 奖期赛果管理、赛果批次管理、赛果批次详情、开奖计划 | 负责赛果批次编排、开奖计划管理、开奖游戏调整和赛果文件提交 | `OBJ-DRAW-BATCH`、`OBJ-MATCH-RESULT-FILE`、`OBJ-MATCH` | `PRD章节 | §开奖管理 (L1861-L2105)` |
| `MOD-FILE` | 数据文件管理 | 提交记录、提交详情、文件作废 | 负责线上/线下提交记录的查询、详情查看和作废回写 | `OBJ-SUBMISSION-RECORD`、`OBJ-FILE-VOID` | `PRD章节 | §数据文件管理 (L2106-L2146)` |
| `MOD-BASE-COMP` | 基础信息管理-赛事与赛季 | 赛事管理、赛季详情、赛季匹配、赛季关联球队 | 负责赛事、赛季的创建、修改、详情、匹配，以及赛季级球队关联 | `OBJ-COMPETITION`、`OBJ-SEASON`、`OBJ-SEASON-TEAM-ALIAS` | `PRD章节 | §基础信息管理 / 赛事管理 (L2147-L2338)` |
| `MOD-BASE-TEAM` | 基础信息管理-球队 | 球队管理、球队匹配、球队导入 | 负责标准化球队主数据维护、数据源匹配和批量导入 | `OBJ-TEAM`、`OBJ-TEAM-MATCH-RELATION` | `PRD章节 | §基础信息管理 / 球队管理 (L2339-L2474)` |
| `MOD-MATCHDATA` | 比赛数据维护 | 比赛信息管理、导入/匹配、数据源比赛看板 | 负责标准化比赛主数据维护，以及纳米/同行来源比赛视图 | `OBJ-MATCH`、`OBJ-COMPETITION`、`OBJ-SEASON` | `PRD章节 | §比赛数据维护 (L2475-L2652)` |
| `MOD-USER` | 用户管理 | 账号管理、角色管理、系统权限 | 负责账号生命周期、角色定义和权限配置 | `OBJ-ACCOUNT`、`OBJ-ROLE`、`OBJ-PERMISSION-BUNDLE` | `PRD章节 | §用户管理 + §系统权限 (L2653-L2815)` |
| `MOD-OPLOG` | 操作日志 | 操作日志列表、接口动作审计 | 负责记录模块级操作行为与接口映射 | `OBJ-OPERATION-LOG` | `PRD章节 | §操作日志 (L2554-L2652)` |

## 模块边界说明

- `MOD-SCHEDULE` 与 `MOD-DRAW` 的边界：
  - `MOD-SCHEDULE` 负责“赛程生成、开售、赛程文件提交”
  - `MOD-DRAW` 负责“赛果批次、开奖计划、赛果文件提交”
- `MOD-BASE-COMP` 与 `MOD-BASE-TEAM` 的边界：
  - 前者以赛事/赛季为中心
  - 后者以球队主数据为中心
- `MOD-MATCHDATA` 只负责标准化比赛主数据维护和来源看板，不负责赛程批次编排。
- `MOD-GLOBAL` 不代表独立业务域，但承载登录、鉴权、通知等所有模块共享能力。

## 外部补充说明

- PRD 中“产品结构 / 信息结构 / 功能结构”未给出正文内容，无法仅靠文档还原完整 IA 树，相关布局细节统一标记为 `依赖外部原型补充`。
- 赛程批次、告警详情、变更处理、开奖计划等复杂页面的具体视觉布局依赖原型链接 #1 和多个钉钉附件补充。
