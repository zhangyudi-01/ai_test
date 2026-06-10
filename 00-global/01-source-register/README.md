# 上下文源注册表管理流程

## 流程概览

本文档记录上下文源注册表的创建、更新和维护流程。

---

## 步骤 1：生成上下文源注册表

**执行者**：AI  
**输入**：`00-generate-source-register.prompt.md` + 源材料目录内容  
**输出**：`context-source-register.md`

**提示词**：
```
根据 00-source-materials 目录的内容，
帮我更新 context-source-register.md
其中 api 和 db 的 docs 还没提供，后面找开发补充；
08-business-modules 业务模块后面你可以给我生成，现在先不用。
```

**任务描述**：
- 扫描 `00-source-materials` 目录下的所有文件
- 按照注册表格式记录每个资料源
- 标注资料的权威级别、使用范围、禁止用途
- 对缺失资料明确标注"待补充"状态

---

## 步骤 2：生成资料缺口清单

**执行者**：AI  
**输入**：`01-generate-gap-list.prompt.md` + `context-source-register.md`  
**输出**：`context-source-gap-list.md`

**提示词**：
```
根据 context-source-register.md 和现有目录 00-source-materials 中的文档情况
更新 context-source-gap-list.md
```

**任务描述**：
- 识别注册表中标注为"待补充"的资料
- 分析缺失资料的影响范围
- 制定缺口填补优先级（P0/P1/P2）
- 提供缺口应对策略

---

## 步骤 3：更新注册表

**执行者**：AI  
**输入**：`02-update-source-register.prompt.md` + 新增资料  
**输出**：更新后的 `context-source-register.md`

**触发时机**：
- 新增源材料文件时
- 补充了缺失资料时
- 资料版本更新时

**操作**：
1. 添加新资料条目到注册表
2. 更新已有资料的版本/日期信息
3. 将"待补充"状态改为实际文件路径
4. 同步更新缺口清单

---

## 步骤 4：人工审核

**执行者**：人工  
**输入**：更新后的注册表和缺口清单  
**输出**：审核通过或修改意见

**审核重点**：
- 资料分类是否准确
- 权威级别是否合理
- 使用范围和禁止用途是否明确
- 缺失资料是否完整识别

---

## 文件命名规范

### 提示词文件
- `00-generate-source-register.prompt.md` - 生成注册表的提示词
- `01-generate-gap-list.prompt.md` - 生成缺口清单的提示词
- `02-update-source-register.prompt.md` - 更新注册表的提示词

### 输出文件
- `context-source-register.md` - 上下文源注册表
- `context-source-gap-list.md` - 上下文源缺口清单

### 说明文件
- `README.md` - 本文件，管理流程说明

---

## 维护规则

### 新增资料时
1. 扫描新增的文件
2. 更新 `context-source-register.md`
3. 检查是否填补了缺口，相应更新 `context-source-gap-list.md`

### 资料版本更新时
1. 更新注册表中的版本/日期字段
2. 如有重大变更，在备注中说明

### 定期检查
- 每次迭代开始前检查资料完整性
- 确认缺失资料的补充进度
- 更新缺口清单状态

---

## 当前状态

- ✅ 步骤1：已完成（`context-source-register.md` 已生成，包含18项资料）
- ✅ 步骤2：已完成（`context-source-gap-list.md` 已生成）
- ⏳ 步骤3：待资料补充时执行
- ⏳ 步骤4：待人工审核

---

## 资料补充进度

### 高优先级（P0）- 待开发补充
- [ ] API接口文档（SRC-013）
- [ ] 数据库设计文档（SRC-014）

### 中优先级（P1）- 已完成
- [x] 业务模块文档（SRC-017）- 已生成

### 低优先级（P2）- 可选
- [ ] 测试环境配置文档
- [ ] 部署架构图
- [ ] 第三方依赖说明

---

**更新日期**：2026-06-10
