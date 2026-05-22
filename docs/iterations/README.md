# iterations 目录说明

`docs/iterations/` 用于保存迭代输入包和差异识别辅助资料。

## 当前资料

| 目录 | 职责 |
| --- | --- |
| `r09_iteration_pack/` | R09 迭代输入包，用于记录本轮迭代范围、模块变更和差异识别线索。 |

## 使用边界

- `r09_iteration_pack/` 是迭代输入资料，不是 OpenSpec change。
- 文件中如果出现“生成测试方案 / 测试用例”的表述，只表示这些资料可服务测试工作流。
- 当前 `openspec/changes/build-jingcai-ops-business-baseline/` 是业务需求基线 change，不允许把测试方案、测试用例、自动化、测试报告混入该 change。
- 后续如果要做 R09 测试交付，应新建独立测试类 OpenSpec change。
