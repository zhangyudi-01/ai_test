# API / 操作动作映射清单

基线版本：`BASE-JCOPS-2026-04-22-V1`

说明：

- 本清单以 PRD“操作日志 / 已实现操作日志”表为主来源，只记录 PRD 已显式出现的接口与动作。
- 若 PRD 只给出动作名称，未给出接口路径，则 `Method` 和 `Path` 记为 `PRD未提供`。

## 认证与账号 / 角色

| 动作ID | 模块 | UI 动作 | Method | Path | 说明 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- |
| `ACT-AUTH-001` | 登录 | 登录 | `POST` | `/login` | 登录成功时记录 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-AUTH-002` | 登录 | 登出 | `POST` | `/logout` | 登出成功时记录 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-001` | 账号管理 | 新建账号 | `POST` | `/manager_account` | 新建账号弹窗下的创建 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-002` | 账号管理 | 删除账号 | `DELETE` | `/data-backend/manager_account` | 删除确认弹窗下的确定 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-003` | 账号管理 | 修改账号 | `PATCH` | `/data-backend/manager_account` | 修改账号页面下的保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-004` | 账号管理 | 启用账号 | `PATCH` | `/data-backend/manager_account_enable` | 启用弹窗下的确定 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-005` | 账号管理 | 停用账号 | `PATCH` | `/manager_account_disable` | 停用弹窗下的确定 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-006` | 账号管理 | 重置密码 | `PATCH` | `/data-backend/manager_account_password_reset` | 重置密码弹窗下的确定 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-007` | 账号管理 | 主动修改密码 | `PUT` | `/user/change_password` | 主动修改密码弹窗下的保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-USER-008` | 账号管理 | 强制修改密码 | `PUT` | `/user/force_change_password` | 强制修改密码弹窗下的保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-ROLE-001` | 角色管理 | 新建角色 | `POST` | `/data-backend/role` | 新建角色页面下的创建 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-ROLE-002` | 角色管理 | 删除角色 | `DELETE` | `/data-backend/role` | 删除二次确认弹窗下的确定 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-ROLE-003` | 角色管理 | 修改角色 | `PATCH` | `/data-backend/role` | 修改角色页面下的保存 | `PRD表格 | §操作日志 / 已实现操作日志` |

## 赛程批次管理

| 动作ID | 模块 | UI 动作 | Method | Path | 说明 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- |
| `ACT-SCH-001` | 赛程批次管理 | 新建奖期 | `POST` | `/data-backend/bd-game-draw` | 新建奖期 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-002` | 赛程批次管理 | 奖期编辑 | `PATCH` | `/data-backend/bd-game-draw` | 奖期编辑 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-003` | 赛程批次管理 | 奖期删除 | `DELETE` | `/data-backend/bd-game-draw` | 奖期删除 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-004` | 赛程批次管理 | 导出备注 | `GET` | `/report/game_draw_remark/*` | 导出备注 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-005` | 赛程批次管理 | 新建批次 | `POST` | `/data-backend/bd-batch` | 新建批次 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-006` | 赛程批次管理 | 批次编辑 | `PATCH` | `/data-backend/bd-batch` | 批次编辑 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-007` | 赛程批次管理 | 调整批次序号 | `PATCH` | `/data-backend/bd-batch/batchNo` | 调整批次序号 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-008` | 赛程批次管理 | 草稿比对 | `POST` | `/batch-diff` | 草稿比对 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-009` | 赛程批次管理 | 草稿添加比赛 | `PATCH` | `/batch-matchup-drafts/real-time/add` | 草稿添加比赛 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-010` | 赛程批次管理 | 开奖时间草稿批次添加比赛 | `PATCH` | `/batch-matchup-drafts/real-time/batch/add` | 在开奖时间草稿配置中按批次添加比赛 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-011` | 赛程批次管理 | 草稿删除比赛 | `PATCH` | `/batch-matchup-drafts/real-time/delete` | 草稿删除比赛 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-012` | 赛程批次管理 | 草稿手动调整比赛顺序 | `PATCH` | `/batch-matchup-drafts/real-time/manual-sort-no` | 调整比赛顺序 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-013` | 赛程批次管理 | 草稿手动调整场次号 | `PATCH` | `/batch-matchup-drafts/real-time/matchup-no` | 调整不同游戏的场次号 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-014` | 赛程批次管理 | 草稿其他信息更新 | `PATCH` | `/batch-matchup-drafts/real-time/batch-matchup-drafts` | 更新草稿其他信息 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-015` | 赛程批次管理 | 草稿调整开售游戏 | `PATCH` | `/batch-matchup-drafts/real-time/sales` | 调整比赛开售游戏 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-016` | 赛程批次管理 | 草稿比对保存草稿 | `POST` | `/batch-diff/user-matchup-drafts` | 草稿比对保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-017` | 赛程批次管理 | 草稿比对生成正式版 | `POST` | `/batch-diff/matchup-formal` | 草稿比对生成正式版 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-018` | 赛程批次管理 | 导出正式赛程 | `GET` | `/report/matchup/4` | 批次管理入口导出正式赛程 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-019` | 赛程批次管理 | 删除批次 | `DELETE` | `/data-backend/bd-batch` | 删除批次 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-020` | 赛程批次管理 | 导出初版草稿 | `GET` | `/report/matchup_draft/*` | 导出初版草稿 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-021` | 赛程批次管理 | 导出公告表 | `GET` | `/report/matchup_notice/5` | 导出公告表 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-022` | 赛程批次管理 | 赛程备注 | `POST` | `/data-backend/m-match-remark` | 赛程备注 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-023` | 赛程批次管理 | 草稿保存 | `POST` | `/batch-matchup-drafts` | 草稿保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-024` | 赛程批次管理 | 导入胜负比赛 | `POST` | `/upload/s-match/save` | 导入胜负比赛 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-025` | 赛程批次管理 | 创建比赛 | `PRD未提供` | `PRD未提供` | 操作日志表有动作，无接口路径 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-026` | 赛程批次管理 | 转移赛程 | `POST` | `/batch-matchup-drafts/transfer` | 转移赛程 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-027` | 赛程批次管理 | 导出正式赛程（赛事详情） | `GET` | `/report/matchup/*` | 赛事详情入口导出正式赛程 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-028` | 赛程批次管理 | 正式赛程作废 | `DELETE` | `/data-backend/batch-matchup` | 正式赛程作废 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-029` | 赛程批次管理 | 提交比赛文件 | `POST` | `/data-backend/match_file_submit` | 提交比赛文件 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-030` | 赛程批次管理 | 提交赛事文件 | `POST` | `/data-backend/league_file_submit` | 提交赛事文件 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-SCH-031` | 赛程批次管理 | 提交球队文件 | `POST` | `/data-backend/team_file_submit` | 提交球队文件 | `PRD表格 | §操作日志 / 已实现操作日志` |

## 风险管理与基础信息管理

| 动作ID | 模块 | UI 动作 | Method | Path | 说明 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- |
| `ACT-RISK-001` | 风险管理 | 添加球队黑名单 | `POST` | `/data-backend/m-team-blacklist` | 添加球队黑名单 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-RISK-002` | 风险管理 | 移除球队黑名单 | `DELETE` | `/data-backend/m-team-blacklist` | 移除球队黑名单 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-RISK-003` | 风险管理 | 添加赛事黑名单 | `POST` | `/data-backend/m-competition-blacklist` | 添加赛事黑名单 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-RISK-004` | 风险管理 | 移除赛事黑名单 | `DELETE` | `/data-backend/m-competition-blacklist` | 移除赛事黑名单 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-001` | 基础信息管理 | 新建赛事 | `POST` | `/data-backend/m-competition` | 新建赛事 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-002` | 基础信息管理 | 修改赛事 | `PATCH` | `/data-backend/m-competition` | 修改赛事 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-003` | 基础信息管理 | 匹配赛事 | `POST` | `/data-backend/dimension/relations/competition` | 匹配赛事 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-004` | 基础信息管理 | 新建赛季 | `POST` | `/data-backend/m-season` | 新建赛季 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-005` | 基础信息管理 | 修改赛季 | `PATCH` | `/data-backend/m-season` | 修改赛季 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-006` | 基础信息管理 | 匹配赛季 | `POST` | `/data-backend/dimension/relations/season` | 匹配赛季 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-007` | 基础信息管理 | 关联球队 | `POST` | `/data-backend/r-season-team` | 关联球队 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-008` | 基础信息管理 | 新建球队 | `POST` | `/data-backend/m-team` | 新建球队 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-009` | 基础信息管理 | 修改球队 | `PATCH` | `/data-backend/m-team` | 修改球队 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-010` | 基础信息管理 | 球队匹配 | `POST` | `/data-backend/dimension/relations/team` | 球队匹配 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-BASE-011` | 基础信息管理 | 球队导入 | `POST` | `/upload/m-team/save` | 球队导入 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-MDATA-001` | 比赛数据维护 | 新建比赛 | `POST` | `/data-backend/m-match` | 新建比赛 | `PRD表格 | §操作日志 / 已实现操作日志` |

## 比赛监控 / 异常 / 变更

| 动作ID | 模块 | UI 动作 | Method | Path | 说明 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- |
| `ACT-MON-001` | 比赛监控 | 填写监控记录 | `POST` | `/data-backend/monitor` | 填写监控记录 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-MON-002` | 比赛监控 | 赛果审核 | `POST` | `/data-backend/event-match-check` | 赛果审核 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-MON-003` | 比赛监控 | 赛果确认 | `POST` | `/data-backend/event-match-check/match-result/diff` | 赛果比对确认 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-MON-004` | 比赛监控 | 赛果确认保存 | `POST` | `/data-backend/event-match-check/match-result/confirm` | 赛果确认保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-MON-005` | 比赛监控 | 批量确认 | `PRD未提供` | `PRD未提供` | 赛果批量确认保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-MON-006` | 比赛监控 | 赛果回退 | `PRD未提供` | `PRD未提供` | 赛果回退 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-ABN-001` | 异常管理 | 监控备注 | `POST` | `/data-backend/monitor/remark` | 监控备注 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-ABN-002` | 异常管理 | 告警核实 | `POST` | `/data-backend/event-match-check` | 告警核实 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-ABN-003` | 异常管理 | 异常确认 | `POST` | `/data-backend/event-match-check/event/confirm` | 异常确认 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-CHG-001` | 变更管理 | 导出公告表 | `POST` | `/report/event_notice_export` | 导出变更公告表 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-CHG-002` | 变更管理 | 导出变更单 | `GET` | `/report/change_matchup/6` | 导出变更单 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-CHG-003` | 变更管理 | 新建处理 | `POST` | `/data-backend/abnormal/record` | 新建处理 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-CHG-004` | 变更管理 | 处理作废 | `POST` | `/data-backend/abnormal/voided` | 处理作废 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-CHG-005` | 变更管理 | 完成确认 | `POST` | `/data-backend/abnormal/completed` | 完成确认 | `PRD表格 | §操作日志 / 已实现操作日志` |

## 开奖管理

| 动作ID | 模块 | UI 动作 | Method | Path | 说明 | 来源回指 |
| --- | --- | --- | --- | --- | --- | --- |
| `ACT-DRAW-001` | 开奖管理 | 新建开奖批次 | `POST` | `/data-backend/bd-batch/draw` | 新建开奖批次 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-002` | 开奖管理 | 编辑开奖批次 | `PATCH` | `/data-backend/bd-batch/draw` | 编辑开奖批次 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-003` | 开奖管理 | 删除开奖批次 | `DELETE` | `/data-backend/bd-batch/draw` | 删除开奖批次 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-004` | 开奖管理 | 导出赛果 | `GET` | `/report/matchup_result/7` | 导出赛果 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-005` | 开奖管理 | 调整批次序号 | `PATCH` | `/data-backend/bd-batch/draw/batch-order-no` | 调整开奖批次序号 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-006` | 开奖管理 | 开奖批次添加赛程 | `PATCH` | `/batch-matchup-draw/real-time/add` | 开奖列表添加赛程 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-007` | 开奖管理 | 开奖批次删除赛程 | `PATCH` | `/batch-matchup-draw/real-time/delete` | 开奖列表删除赛程 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-008` | 开奖管理 | 开奖批次更改开奖游戏 | `PATCH` | `/batch-matchup-draw/real-time/draw` | 赛程更改开奖游戏 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-009` | 开奖管理 | 保存批次开奖 | `POST` | `/batch-matchup-draw` | 保存批次开奖 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-010` | 开奖管理 | 开奖时间草稿保存 | `POST` | `/batch-matchup-drafts` | 开奖时间草稿保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-011` | 开奖管理 | 开奖时间草稿比对保存 | `POST` | `/batch-diff/user-matchup-drafts` | 开奖时间草稿比对保存 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-012` | 开奖管理 | 开奖时间草稿比对生成正式版 | `POST` | `/batch-diff/matchup-formal` | 开奖时间草稿比对生成正式版 | `PRD表格 | §操作日志 / 已实现操作日志` |
| `ACT-DRAW-013` | 开奖管理 | 提交赛果文件 | `POST` | `/data-backend/match_result_file_submit` | 提交赛果文件 | `PRD表格 | §操作日志 / 已实现操作日志` |

## 说明

- 本表只覆盖 PRD 已显式给出的“写操作/导出动作”接口，不代表系统完整查询 API 清单。
- 以下动作已确认存在，但接口路径缺失，后续必须补齐：
  - `ACT-SCH-025` 创建比赛
  - `ACT-MON-005` 批量确认
  - `ACT-MON-006` 赛果回退
