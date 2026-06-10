 # 项目全局上下文生成流程 - 执行步骤

## 流程概览

本文档记录项目全局上下文文档的生成和审核流程，确保生成的文档符合粗粒度理解要求。

---

## 步骤 1：生成提示词草稿

**执行者**：AI-1  
**输入**：`00-generate-prompt-draft.prompt.md`  
**输出**：`project-context-prompt.draft.md`

**任务描述**：
根据提示词要求，生成一份用于"项目全局上下文理解"的专业提示词草稿。

**关键要求**：
1. 明确禁止详细拆分需求
2. 明确禁止生成测试点和测试用例
3. 明确禁止用历史资料覆盖当前需求
4. 明确当前需求是最高依据
5. 明确项目上下文只做粗粒度理解
6. 明确输出内容应控制在简洁范围
7. 明确不确定内容必须标记为待确认
8. 明确历史资料只作为背景索引，不展开详细分析


---

## 步骤 2：审核提示词草稿

**执行者**：AI-2  
**输入**：`02-project-context-prompt-review.prompt.md` + `project-context-prompt.draft.md`  
**输出**：审核意见

**审核重点**：
- 提示词有没有跑偏
- 有没有要求 AI 做太细
- 有没有把项目上下文阶段变成详细需求分析
- 有没有明确当前需求最高优先级
- 有没有禁止历史资料覆盖当前需求
- 有没有要求不确定内容进入待确认

**输入资料参考**：
1. `context-source-register.md`
2. `raw-requirement.md`
3. `REQ-当前迭代需求-v1.md`
4. `human-understanding.md`
5. 业务模块说明（如有）

---

## 步骤 3：修改并确认提示词

**执行者**：人工  
**输入**：审核意见 + `project-context-prompt.draft.md`  
**输出**：`01-project-context-prompt.final.md`

**操作**：
1. 根据 AI-2 的审核意见修改 `project-context-prompt.draft.md`
2. 修改完成后重命名为 `01-project-context-prompt.final.md`

---

## 步骤 4：生成项目全局上下文文档

**执行者**：AI-1  
**输入**：`01-project-context-prompt.final.md`  
**输出**：`03-project-context.ai.md`

**提示词**：
```
请严格按照 01-project-context-prompt.final.md 的要求，生成 project-context.ai.md。
```

**输入资料**：
1. `context-source-register.md`
2. `raw-requirement.md`
3. `REQ-当前迭代需求-v1.md`
4. `human-understanding.md`
5. `business-modules-overview.md`

---

## 步骤 5：审核项目全局上下文文档

**执行者**：AI-2  
**输入**：`04-review-context-ai.prompt.md` + `03-project-context.ai.md`  
**输出**：审核意见

**审核检查项**：
1. ✅ 是否把文档写得过于详细
2. ✅ 是否提前做了原子需求拆解
3. ✅ 是否提前生成了测试点、测试方案、测试用例
4. ✅ 是否把历史资料当成当前需求依据
5. ✅ 是否明确当前需求是最高依据
6. ✅ 是否明确后续详细分析入口
7. ✅ 是否明确不确定内容要进入待确认

---

## 步骤 6：修改上下文文档

**执行者**：人工  
**输入**：审核意见 + `03-project-context.ai.md`  
**输出**：修改后的 `03-project-context.ai.md`

**操作**：
根据 AI-2 的审核意见修改文档

---

## 步骤 7：人工确认/微调

**执行者**：人工  
**输入**：修改后的 `03-project-context.ai.md`  
**输出**：审核记录

**审核重点**：
- 未进行原子需求拆分
- 未提前生成测试方案
- 未提前生成测试用例
- 已明确当前需求为最高依据
- 已明确历史资料只作为背景参考
- 已明确后续详细分析进入原子需求拆分和模块逻辑拆解阶段

**人工修正记录**：
如有修改，记录修改内容

---

## 步骤 8：生成最终版本

**执行者**：人工  
**输入**：确认后的 `03-project-context.ai.md`  
**输出**：`00-project-context.md`

**操作**：
人工确认没问题后，在 `00-global/` 目录下生成最终版本 `00-project-context.md`

---

## 文件命名规范

### 提示词文件
- `00-generate-prompt-draft.prompt.md` - 生成提示词草稿的提示词
- `01-project-context-prompt.final.md` - 最终确认的提示词
- `02-project-context-prompt-review.prompt.md` - 审核提示词的提示词
- `04-review-context-ai.prompt.md` - 审核上下文文档的提示词

### 生成文件
- `03-project-context.ai.md` - AI生成的上下文文档
- `00-project-context.md` - 最终确认版（存放在 `00-global/` 目录）

### 过程文件
- `执行步骤.md` - 本文件，记录完整流程

---

## 质量控制关键点

### 第一道关卡：提示词审核
确保提示词本身不会引导AI做过细的分析

### 第二道关卡：文档审核
确保生成的文档符合粗粒度要求

### 第三道关卡：人工确认
最终人工把关，确保文档质量

---

## 当前状态

- ✅ 步骤1：已完成（`01-project-context-prompt.final.md`）
- ✅ 步骤2：已完成（`02-project-context-prompt-review.prompt.md`）
- ✅ 步骤3：已完成（最终版已生成）
- ✅ 步骤4：已完成（`03-project-context.ai.md`）
- ⏳ 步骤5：待执行
- ⏳ 步骤6：待执行
- ⏳ 步骤7：待执行
- ⏳ 步骤8：待执行

---

**更新日期**：2026-06-10
