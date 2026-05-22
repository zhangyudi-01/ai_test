# docs 目录说明

`docs/` 用于保存需求输入资料和迭代辅助资料，不直接等同于 OpenSpec change。

## 子目录职责

| 目录 | 职责 |
| --- | --- |
| `requirements/` | 只放原始 PRD、附件、需求输入资料。这里的文件是业务事实来源，不是整理后的基线资产。 |
| `iterations/` | 只放迭代输入包、差异识别辅助资料。这里的文件可用于分析迭代变化，但不等于 OpenSpec change。 |

## 当前基线入口

当前竞猜赛事运营系统业务需求基线以以下目录为准：

`openspec/changes/build-jingcai-ops-business-baseline/`

后续推进业务基线时，应在该 OpenSpec change 下维护 proposal、design、tasks、delta specs 和 `business-baseline/` 资产，不应直接把 `docs/iterations/` 当成交付目录。
