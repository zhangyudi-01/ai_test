# 页面 / 功能清单

基线版本：`BASE-JCOPS-2026-04-22-V1`

说明：

- 本清单覆盖 PRD 中显式出现的页面、弹窗、详情页、配置页与待定页。
- `类型` 取值：`列表页` / `详情页` / `弹窗` / `配置页` / `看板页` / `待定页` / `全局能力`
- 关联角色为空时写 `-`，表示 PRD 未直接绑定角色或由权限体系统一控制。

## 全局能力

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-GLOBAL-001` | `MOD-GLOBAL` | 登录页 | 全局能力 | 账号、密码、令牌输入与登录校验 | 全角色 | `OBJ-ACCOUNT`、`RULE-GEN-013` | `PRD章节 | §登录 (L101-L137)` |
| `PAGE-GLOBAL-002` | `MOD-GLOBAL` | 强制/主动修改密码弹窗 | 弹窗 | 首次登录、密码过期或主动改密 | 全角色 | `OBJ-ACCOUNT`、`RULE-MOD-USER-001` | `PRD章节 | §修改密码 (L138-L147)` |
| `PAGE-GLOBAL-003` | `MOD-GLOBAL` | 身份验证器绑定弹窗 | 弹窗 | 绑定腾讯身份验证器并校验令牌 | 全角色 | `OBJ-AUTH-DEVICE`、`RULE-GEN-015` | `PRD章节 | §登录 / 身份验证器逻辑 (L118-L137)` |
| `PAGE-GLOBAL-004` | `MOD-GLOBAL` | 顶部通知列表 | 全局能力 | 展示未读通知、按类型筛选、关闭即标记已读 | 全角色 | `OBJ-NOTICE` | `PRD章节 | §通知 (L2816-L2825)` |

## 风险管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-RISK-001` | `MOD-RISK` | 球队黑名单列表 | 列表页 | 查询、查看、批量移除球队黑名单 | `ROLE-SCHEDULE` | `OBJ-BLACKLIST-RECORD`、`OBJ-TEAM` | `PRD章节 | §风险管理 / 球队黑名单 / 列表 (L150-L172)` |
| `PAGE-RISK-002` | `MOD-RISK` | 添加球队黑名单弹窗 | 弹窗 | 搜索球队、批量添加黑名单并填写原因 | `ROLE-SCHEDULE` | `OBJ-BLACKLIST-RECORD`、`RULE-MOD-RISK-001` | `PRD章节 | §风险管理 / 球队黑名单 / 添加弹窗 (L173-L192)` |
| `PAGE-RISK-003` | `MOD-RISK` | 赛事黑名单列表 | 列表页 | 查询、查看、批量移除赛事黑名单 | `ROLE-SCHEDULE` | `OBJ-BLACKLIST-RECORD`、`OBJ-COMPETITION` | `PRD章节 | §风险管理 / 赛事黑名单 / 列表 (L193-L205)` |
| `PAGE-RISK-004` | `MOD-RISK` | 添加赛事黑名单弹窗 | 弹窗 | 搜索赛事、批量添加赛事黑名单 | `ROLE-SCHEDULE` | `OBJ-BLACKLIST-RECORD`、`OBJ-COMPETITION` | `PRD章节 | §风险管理 / 赛事黑名单 / 添加弹窗 (L205-L216)` |
| `PAGE-RISK-005` | `MOD-RISK` | 风险操作记录列表 | 列表页 | 查询黑名单操作记录、查看操作原因 | `ROLE-SCHEDULE` | `OBJ-OPERATION-LOG` | `PRD章节 | §风险管理 / 操作记录 (L217-L231)` |

## 北单赛程管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-SCH-001` | `MOD-SCHEDULE` | 赛程批次管理列表 | 列表页 | 管理奖期、导出备注、进入批次管理 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-DRAW-PERIOD`、`OBJ-SCHEDULE-BATCH` | `PRD章节 | §北单赛程管理 / 赛程批次管理列表 (L232-L295)` |
| `PAGE-SCH-002` | `MOD-SCHEDULE` | 新建/编辑奖期弹窗 | 弹窗 | 创建或编辑奖期的开售、停售、开奖时间与开售游戏 | `ROLE-SCHEDULE` | `OBJ-DRAW-PERIOD` | `PRD章节 | §北单赛程管理 / 奖期相关规则 (L232-L295)` |
| `PAGE-SCH-003` | `MOD-SCHEDULE` | 批次管理页 | 配置页 | 新建批次、调整批次序号、查看批次详情 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-SCHEDULE-BATCH` | `PRD章节 | §北单赛程管理 / 批次管理 (L296-L约600)` |
| `PAGE-SCH-004` | `MOD-SCHEDULE` | 草稿管理页 | 配置页 | 添加/删除比赛、转移赛程、调整顺序、配置开售游戏和让球 | `ROLE-SCHEDULE` | `OBJ-SCHEDULE-BATCH`、`OBJ-MATCH` | `PRD章节 | §北单赛程管理 / 草稿管理 (L约600-L约920)` |
| `PAGE-SCH-005` | `MOD-SCHEDULE` | 草稿比对页 | 配置页 | 比对草稿、保存草稿、生成正式版 | `ROLE-SCHEDULE` | `OBJ-SCHEDULE-BATCH`、`RULE-MOD-SCH-006` | `PRD章节 | §北单赛程管理 / 草稿比对 (L约920-L约1020)` |
| `PAGE-SCH-006` | `MOD-SCHEDULE` | 正式详情页 | 详情页 | 查看正式赛程、导出、提交文件、上传回执、作废正式赛程 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-SCHEDULE-BATCH`、`OBJ-SUBMISSION-RECORD` | `PRD章节 | §北单赛程管理 / 正式详情 (L约1020-L约1160)` |
| `PAGE-SCH-007` | `MOD-SCHEDULE` | 开奖时间草稿页 | 配置页 | 对正式赛程补充开奖时间草稿配置 | `ROLE-SCHEDULE` | `OBJ-SCHEDULE-BATCH`、`OBJ-MATCH` | `PRD章节 | §北单赛程管理 / 开奖时间草稿 (L约1160-L约1220)` |
| `PAGE-SCH-008` | `MOD-SCHEDULE` | 开奖时间比对页 | 配置页 | 比对开奖时间草稿并生成正式版 | `ROLE-SCHEDULE` | `OBJ-SCHEDULE-BATCH` | `PRD章节 | §北单赛程管理 / 开奖时间比对 (L约1220-L1281)` |

## 比赛监控

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-MON-001` | `MOD-MONITOR` | 比赛赛程监控列表 | 列表页 | 查询标准化比赛、进入监控、赛果审核、确认与备注 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MATCH`、`OBJ-MONITOR-RECORD` | `PRD章节 | §比赛监控 / 比赛列表 (L1284-L1353)` |
| `PAGE-MON-002` | `MOD-MONITOR` | 填写监控记录 | 弹窗 | 补充异常类型、异常原因、备注等监控记录 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MONITOR-RECORD` | `PRD章节 | §比赛监控 / 填写监控记录 (L1354-L1378)` |
| `PAGE-MON-003` | `MOD-MONITOR` | 赛果审核 | 弹窗 | 审核比赛赛果，判断是否进入确认流程 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-RESULT-CONFIRM` | `PRD章节 | §比赛监控 / 赛果审核 (L1379-L1401)` |
| `PAGE-MON-004` | `MOD-MONITOR` | 赛果确认 | 弹窗 | 对比确认赛果并保存确认结果 | `ROLE-MONITOR-LEAD` | `OBJ-RESULT-CONFIRM`、`RULE-MOD-MON-003` | `PRD章节 | §比赛监控 / 赛果确认 (L1402-L1426)` |
| `PAGE-MON-005` | `MOD-MONITOR` | 批量确认 / 赛果回退 | 弹窗 | 对赛果执行批量确认或回退 | `ROLE-MONITOR-LEAD` | `OBJ-RESULT-CONFIRM` | `PRD章节 | §比赛监控 / 批量确认、赛果回退 (L1427-L1457)` |
| `PAGE-MON-006` | `MOD-MONITOR` | 上传截图 / 查看截图 | 功能单元 | 上传比赛截图证据、查看或删除截图 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MONITOR-ATTACHMENT` | `PRD章节 | §比赛监控 / 上传截图、查看截图 (L1458-L1461)` |
| `PAGE-MON-007` | `MOD-MONITOR` | 比赛进程信息 | 详情页 | 查看比赛进程、状态节点和赛果相关过程信息 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MATCH` | `PRD章节 | §比赛监控 / 比赛进程信息 (L1462-L1498)` |
| `PAGE-MON-008` | `MOD-MONITOR` | 备注 / 赛果表区间段 | 功能单元 | 维护监控备注和赛果表区间段信息 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MONITOR-RECORD` | `PRD章节 | §比赛监控 / 备注、赛果表区间段 (L1499-L1520)` |
| `PAGE-MON-009` | `MOD-MONITOR` | 赛果确认记录 | 列表页 | 查询历史赛果确认记录 | `ROLE-MONITOR-LEAD` | `OBJ-RESULT-CONFIRM` | `PRD章节 | §比赛监控 / 赛果确认记录 (L1521-L1536)` |

## 异常管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-ABN-001` | `MOD-ABNORMAL` | 事件列表 | 列表页 | 查询异常事件总览 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-EVENT` | `PRD章节 | §异常管理 / 事件列表 (L1539-L1563)` |
| `PAGE-ABN-002` | `MOD-ABNORMAL` | 告警列表 | 列表页 | 查询告警、区分核实状态和确认状态 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-ALERT` | `PRD章节 | §异常管理 / 告警列表 (L1564-L1589)` |
| `PAGE-ABN-003` | `MOD-ABNORMAL` | 告警核实 | 弹窗 | 对告警执行核实动作 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-ALERT` | `PRD章节 | §异常管理 / 告警核实 (L1590-L1611)` |
| `PAGE-ABN-004` | `MOD-ABNORMAL` | 异常确认 | 弹窗 | 对核实后的异常执行确认 | `ROLE-MONITOR-LEAD` | `OBJ-ALERT`、`OBJ-EVENT` | `PRD章节 | §异常管理 / 异常确认 (L1612-L1636)` |
| `PAGE-ABN-005` | `MOD-ABNORMAL` | 告警详情 / 备注 | 详情页 | 查看单条告警详情并补充备注 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-ALERT` | `PRD章节 | §异常管理 / 告警详情、备注 (L1637-L1652)` |
| `PAGE-ABN-006` | `MOD-ABNORMAL` | 预警列表 / 预警详情 / 备注 | 列表页 | 查询预警、查看详情并补充备注 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-WARNING` | `PRD章节 | §异常管理 / 预警管理 (L1653-L1681)` |

## 变更管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-CHG-001` | `MOD-CHANGE` | 异常变更列表 | 列表页 | 查询异常变更、导出公告表和变更单、上传回执 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-CHANGE-RECORD` | `PRD章节 | §变更管理 / 异常变更列表 (L1684-L1786)` |
| `PAGE-CHG-002` | `MOD-CHANGE` | 处理操作页 | 配置页 | 新建处理、处理作废、完成确认、取消完成状态 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-CHANGE-RECORD` | `PRD章节 | §变更管理 / 处理操作页 (L1787-L1854)` |
| `PAGE-CHG-003` | `MOD-CHANGE` | 异常变更详情 | 详情页 | 查看单条变更详情和关联信息 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-CHANGE-RECORD` | `PRD章节 | §变更管理 / 异常变更详情 (L1855-L1860)` |

## 开奖管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-DRAW-001` | `MOD-DRAW` | 奖期赛果管理 | 列表页 | 查询奖期赛果、进入赛果批次和开奖计划 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-DRAW-BATCH`、`OBJ-MATCH` | `PRD章节 | §开奖管理 / 奖期赛果管理 (L1863-L1966)` |
| `PAGE-DRAW-002` | `MOD-DRAW` | 赛果批次管理 | 列表页 | 新建、编辑、删除、排序赛果批次 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-DRAW-BATCH` | `PRD章节 | §开奖管理 / 赛果批次管理 (L1967-L2043)` |
| `PAGE-DRAW-003` | `MOD-DRAW` | 赛果批次详情 | 详情页 | 范围添加/计划添加比赛、删除、修改开奖游戏、查看异常 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-DRAW-BATCH`、`OBJ-MATCH` | `PRD章节 | §开奖管理 / 赛果批次详情 (L2044-L2052)` |
| `PAGE-DRAW-004` | `MOD-DRAW` | 开奖计划 | 列表页 | 查看或查询开奖计划关联内容 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-DRAW-BATCH` | `PRD章节 | §开奖管理 / 开奖计划 (L2053-L2105)` |
| `PAGE-DRAW-005` | `MOD-DRAW` | 提交赛果文件 | 弹窗 | 提交赛果文件并回写批次开奖状态和比赛状态 | `ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MATCH-RESULT-FILE`、`OBJ-SUBMISSION-RECORD` | `PRD章节 | §开奖管理 / 提交赛果文件 (L2053-L2105)` |

## 数据文件管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-FILE-001` | `MOD-FILE` | 提交记录列表 | 列表页 | 查询线上/线下文件提交记录和状态 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(查询) | `OBJ-SUBMISSION-RECORD` | `PRD章节 | §数据文件管理 / 提交记录列表 (L2108-L2125)` |
| `PAGE-FILE-002` | `MOD-FILE` | 提交记录详情 | 详情页 | 按文件类型展示提交详情 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(查询) | `OBJ-SUBMISSION-RECORD` | `PRD章节 | §数据文件管理 / 提交记录详情 (L2126-L2130)` |
| `PAGE-FILE-003` | `MOD-FILE` | 文件作废弹窗 | 弹窗 | 作废文件并回传空 json zip 到原 sftp 目录 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD` | `OBJ-FILE-VOID`、`RULE-MOD-FILE-002` | `PRD章节 | §数据文件管理 / 文件作废 (L2131-L2146)` |

## 基础信息管理：赛事与赛季

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-BASE-001` | `MOD-BASE-COMP` | 赛事列表 | 列表页 | 查询赛事、查看详情、修改、进入匹配和赛季信息 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-COMPETITION` | `PRD章节 | §基础信息管理 / 赛事列表 (L2149-L2166)` |
| `PAGE-BASE-002` | `MOD-BASE-COMP` | 新建赛事 | 弹窗 | 创建赛事主数据 | `ROLE-SCHEDULE` | `OBJ-COMPETITION` | `PRD章节 | §基础信息管理 / 新建赛事 (L2167-L2184)` |
| `PAGE-BASE-003` | `MOD-BASE-COMP` | 赛事详情 | 详情页 | 查看赛事信息、匹配状态、最新赛季 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-COMPETITION` | `PRD章节 | §基础信息管理 / 赛事详情 (L2185-L2191)` |
| `PAGE-BASE-004` | `MOD-BASE-COMP` | 修改赛事 | 弹窗 | 编辑赛事非冻结字段 | `ROLE-SCHEDULE` | `OBJ-COMPETITION` | `PRD章节 | §基础信息管理 / 修改赛事 (L2192-L2198)` |
| `PAGE-BASE-005` | `MOD-BASE-COMP` | 匹配赛事 | 配置页 | 关联贝泰/纳米/同行赛事 | `ROLE-SCHEDULE` | `OBJ-COMPETITION`、`OBJ-SOURCE-MATCH` | `PRD章节 | §基础信息管理 / 匹配赛事 (L2199-L2222)` |
| `PAGE-BASE-006` | `MOD-BASE-COMP` | 赛季详情 | 详情页 | 查看赛季信息、匹配状态和已关联球队 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-SEASON`、`OBJ-SEASON-TEAM-ALIAS` | `PRD章节 | §基础信息管理 / 赛季详情 (L2223-L2235)` |
| `PAGE-BASE-007` | `MOD-BASE-COMP` | 新建赛季 | 配置页 | 创建赛季、自动评级、获取上赛季信息并继续匹配 | `ROLE-SCHEDULE` | `OBJ-SEASON` | `PRD章节 | §基础信息管理 / 新建赛季 (L2236-L2275)` |
| `PAGE-BASE-008` | `MOD-BASE-COMP` | 修改赛季 | 配置页 | 编辑赛季非冻结字段 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-SEASON` | `PRD章节 | §基础信息管理 / 修改赛季 (L2276-L2282)` |
| `PAGE-BASE-009` | `MOD-BASE-COMP` | 关联球队 | 配置页 | 给赛季关联球队、设置赛季别名、获取上赛季球队/纳米球队 | `ROLE-SCHEDULE` | `OBJ-SEASON-TEAM-ALIAS`、`OBJ-TEAM` | `PRD章节 | §基础信息管理 / 关联球队 (L2283-L2317)` |
| `PAGE-BASE-010` | `MOD-BASE-COMP` | 匹配赛季 | 配置页 | 匹配赛季或阶段，支持智能匹配 | `ROLE-SCHEDULE` | `OBJ-SEASON`、`OBJ-SOURCE-MATCH` | `PRD章节 | §基础信息管理 / 匹配赛季 (L2318-L2338)` |

## 基础信息管理：球队

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-TEAM-001` | `MOD-BASE-TEAM` | 球队列表 | 列表页 | 查询球队、查看详情、修改、匹配、导入 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-TEAM` | `PRD章节 | §基础信息管理 / 球队列表 (L2340-L2355)` |
| `PAGE-TEAM-002` | `MOD-BASE-TEAM` | 新建球队 | 配置页 | 创建球队并继续进入匹配 | `ROLE-SCHEDULE` | `OBJ-TEAM` | `PRD章节 | §基础信息管理 / 新建球队 (L2356-L2383)` |
| `PAGE-TEAM-003` | `MOD-BASE-TEAM` | 球队详情 | 详情页 | 查看球队详情和匹配状态 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-TEAM` | `PRD章节 | §基础信息管理 / 球队详情 (L2384-L2389)` |
| `PAGE-TEAM-004` | `MOD-BASE-TEAM` | 修改球队 | 配置页 | 编辑球队非冻结字段 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(部分) | `OBJ-TEAM` | `PRD章节 | §基础信息管理 / 修改球队 (L2390-L2396)` |
| `PAGE-TEAM-005` | `MOD-BASE-TEAM` | 匹配球队 | 配置页 | 按数据源查询并匹配球队 | `ROLE-SCHEDULE` | `OBJ-TEAM`、`OBJ-SOURCE-MATCH` | `PRD章节 | §基础信息管理 / 匹配球队 (L2397-L2422)` |
| `PAGE-TEAM-006` | `MOD-BASE-TEAM` | 导入球队 | 配置页 | 按模板导入球队并可关联到赛事最新赛季 | `ROLE-SCHEDULE` | `OBJ-TEAM`、`OBJ-SEASON-TEAM-ALIAS`、`FILE-TEAM-IMPORT` | `PRD章节 | §基础信息管理 / 导入球队 (L2423-L2474)` |

## 比赛数据维护

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-MDATA-001` | `MOD-MATCHDATA` | 比赛列表 | 列表页 | 查询标准化比赛、按赛事筛选、进入新增/导入/匹配 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER`(查询) | `OBJ-MATCH` | `PRD章节 | §比赛数据维护 / 比赛列表 (L2477-L2496)` |
| `PAGE-MDATA-002` | `MOD-MATCHDATA` | 添加比赛 | 弹窗 | 手工新增一个或多个比赛 | `ROLE-SCHEDULE` | `OBJ-MATCH`、`OBJ-SEASON`、`OBJ-TEAM` | `PRD章节 | §比赛数据维护 / 添加比赛 (L2497-L2517)` |
| `PAGE-MDATA-003` | `MOD-MATCHDATA` | 导入比赛 | 待定页 | 比赛导入规则尚未给出 | `ROLE-SCHEDULE` | `OBJ-MATCH` | `PRD章节 | §比赛数据维护 / 导入比赛 (L2518-L2519)` |
| `PAGE-MDATA-004` | `MOD-MATCHDATA` | 匹配比赛 | 待定页 | 比赛匹配规则尚未给出 | `ROLE-SCHEDULE` | `OBJ-MATCH` | `PRD章节 | §比赛数据维护 / 匹配比赛 (L2520-L2521)` |
| `PAGE-MDATA-005` | `MOD-MATCHDATA` | 纳米足球比赛看板 | 看板页 | 查看纳米足球来源比赛 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MATCH` | `PRD章节 | §比赛数据维护 / 纳米足球比赛看板 (L2522-L2529)` |
| `PAGE-MDATA-006` | `MOD-MATCHDATA` | 纳米篮球比赛看板 | 看板页 | 查看纳米篮球来源比赛 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MATCH` | `PRD章节 | §比赛数据维护 / 纳米篮球比赛看板 (L2530-L2537)` |
| `PAGE-MDATA-007` | `MOD-MATCHDATA` | 同行足球比赛看板 | 看板页 | 查看同行足球来源比赛 | `ROLE-SCHEDULE`、`ROLE-MONITOR-LEAD`、`ROLE-MONITOR-MEMBER` | `OBJ-MATCH` | `PRD章节 | §比赛数据维护 / 同行足球比赛看板 (L2538-L2545)` |

## 用户管理

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-USER-001` | `MOD-USER` | 账号列表 | 列表页 | 查询账号、查看状态、发起启停/重置/删除/修改 | `具有账号管理权限的角色` | `OBJ-ACCOUNT` | `PRD章节 | §用户管理 / 账号列表 (L2655-L2665)` |
| `PAGE-USER-002` | `MOD-USER` | 添加账号 | 弹窗 | 新建账号并生成初始密码 | `具有账号管理权限的角色` | `OBJ-ACCOUNT` | `PRD章节 | §用户管理 / 添加账号 (L2666-L2674)` |
| `PAGE-USER-003` | `MOD-USER` | 修改账号 | 配置页 | 修改账号角色和属性 | `具有账号管理权限的角色` | `OBJ-ACCOUNT`、`OBJ-ROLE` | `PRD章节 | §用户管理 / 修改账号 (L2675-L2681)` |
| `PAGE-USER-004` | `MOD-USER` | 启停账号 / 删除账号 / 重置密码与验证设备 | 弹窗 | 批量启停、删除停用账号、清除绑定设备并重置密码 | `具有账号管理权限的角色` | `OBJ-ACCOUNT`、`OBJ-AUTH-DEVICE` | `PRD章节 | §用户管理 / 删除账号、启停账号、重置密码 (L2682-L2702)` |
| `PAGE-USER-005` | `MOD-USER` | 角色列表 / 角色详情 | 列表页 | 查询角色并查看角色明细和权限 | `具有角色管理权限的角色` | `OBJ-ROLE`、`OBJ-PERMISSION-BUNDLE` | `PRD章节 | §用户管理 / 角色列表、角色详情 (L2703-L2710)` |
| `PAGE-USER-006` | `MOD-USER` | 添加/修改角色 | 配置页 | 创建或修改角色及其权限 | `具有角色管理权限的角色` | `OBJ-ROLE`、`OBJ-PERMISSION-BUNDLE` | `PRD章节 | §用户管理 / 添加角色、修改角色 (L2711-L2779)` |
| `PAGE-USER-007` | `MOD-USER` | 删除角色 | 弹窗 | 删除未分配给账号的角色 | `具有角色管理权限的角色` | `OBJ-ROLE` | `PRD章节 | §用户管理 / 删除角色 (L2780-L2783)` |
| `PAGE-USER-008` | `MOD-USER` | 系统权限总表 | 功能单元 | 展示全部菜单与功能点定义 | `具有角色管理权限的角色` | `OBJ-PERMISSION-BUNDLE` | `PRD章节 | §系统权限 (L2784-L2815)` |

## 操作日志

| 页面ID | 模块ID | 页面/功能单元 | 类型 | 核心职责 | 关联角色 | 关键对象/规则 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PAGE-LOG-001` | `MOD-OPLOG` | 操作日志列表 | 列表页 | 查询操作模块、操作类型、结果、账号、角色和时间 | `具有操作日志查询权限的角色` | `OBJ-OPERATION-LOG`、`ACT-*` | `PRD章节 | §操作日志 (L2546-L2652)` |

## 补充说明

- `PAGE-MDATA-003` 与 `PAGE-MDATA-004` 明确为 `待定页`，当前基线只记录入口存在和待补事实，不填充具体业务规则。
- 复杂页面的表格列顺序、按钮位置、视觉状态依赖外部原型，具体 UI 呈现统一记为 `依赖外部原型补充`。
