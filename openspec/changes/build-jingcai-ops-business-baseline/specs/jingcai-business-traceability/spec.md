## ADDED Requirements

### Requirement: Unified identifier model
Every baseline asset item SHALL use a stable identifier from a shared numbering system for modules, pages, roles, permission bundles, objects, fields, rules, states, flows, external dependencies, file rules, actions, questions, and diff items.

#### Scenario: Items are directly addressable
- **WHEN** a reviewer references an entry in any baseline document
- **THEN** the entry has a stable ID that can be reused across other assets and later diffs

### Requirement: Source backreference model
Every traceable baseline item SHALL record its source type and source pointer back to PRD sections, tables, interfaces, or external links where available.

#### Scenario: Rules trace back to source
- **WHEN** a rule entry is inspected
- **THEN** it includes a source type and source pointer that identifies where the rule originated

#### Scenario: Missing source detail is explicit
- **WHEN** the source cannot be fully resolved from the local workspace
- **THEN** the entry records the best available source pointer and marks the gap as `依赖外部原型补充`

### Requirement: Cross-asset trace links
Rules and process entries SHALL link to affected pages, objects, roles, flows, or actions where applicable so impact can be reviewed without re-reading the full PRD.

#### Scenario: Impact chain is navigable
- **WHEN** a reviewer selects a rule or page entry
- **THEN** related upstream or downstream asset IDs can be found from that entry

### Requirement: Rule classification
The business rule library SHALL distinguish通用规则, 模块专属规则, and 跨模块联动规则.

#### Scenario: Rule type is explicit
- **WHEN** a rule entry is inspected
- **THEN** its classification is shown as one of the three rule categories
