# 仓库目录说明

本仓库同时保存原始需求资料、迭代输入资料和 OpenSpec 变更资产。目录职责如下，避免把原始资料、进行中 change、已归档 change 和主规范混用。

## 目录职责

| 目录 | 职责 |
| --- | --- |
| `docs/requirements/` | 原始需求资料区。用于保存 PRD、附件、需求输入资料，不承载整理后的 OpenSpec change。 |
| `docs/iterations/` | 迭代输入资料区。用于保存迭代输入包、差异识别辅助资料，不等于 OpenSpec change。 |
| `openspec/specs/` | 已生效 OpenSpec 主规范。只保存已经同步生效的主 specs。 |
| `openspec/changes/` | 进行中的 OpenSpec change。每个子目录代表一个尚未归档的变更。 |
| `openspec/changes/archive/` | 已归档历史 change。用于保留完成后的变更历史和交付资产快照。 |
| `openspec/changes/archive/2026-04-22-build-admin-test-baseline/` | 已归档测试基线模板资产，不是原始需求资料。 |
| `openspec/changes/build-jingcai-ops-business-baseline/` | 当前进行中的竞猜赛事运营系统业务需求基线 change。 |

## 当前工作边界

- 原始 PRD 以 `docs/requirements/` 为准。
- 当前业务需求基线以 `openspec/changes/build-jingcai-ops-business-baseline/` 为准。
- 已归档测试基线模板资产只作为历史测试工作流资产保留，不应混入业务需求基线 change。
- 后续若要做测试方案、测试用例、自动化或测试报告，应新建独立测试类 OpenSpec change。
