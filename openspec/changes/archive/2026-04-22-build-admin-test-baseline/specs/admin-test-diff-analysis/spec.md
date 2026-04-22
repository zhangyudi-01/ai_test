## ADDED Requirements

### Requirement: Iteration diff analysis template captures change impact and source back references
The test baseline SHALL provide an iteration diff analysis template that records change source type, source identifier or back reference, version or sprint identifier, affected modules, affected roles, permission impact, rule impact, interface or data impact, and related risks.

#### Scenario: QA lead analyzes a new version
- **WHEN** a new sprint, release, or hotfix enters test planning
- **THEN** the diff analysis template MUST provide fields to capture what changed, where it came from, and which structural assets are affected

#### Scenario: Reviewer compares multiple change items
- **WHEN** several change requests are bundled into one release
- **THEN** the template MUST allow each change item to be recorded separately with its own source back reference, affected rules, and risk assessment

### Requirement: Iterative diff analysis reuses the existing structural baseline
The test baseline SHALL define iterative diff analysis as a downstream activity that reuses the full baseline structure and records only changed or newly affected assets unless structural changes are explicitly introduced.

#### Scenario: Release changes behavior but not structure
- **WHEN** a release changes logic inside existing modules and rules
- **THEN** the diff analysis MUST reference existing module, permission, and rule identifiers instead of recreating the full structural inventory

#### Scenario: Release changes the structural baseline
- **WHEN** a release introduces a new module, role, permission model, or rule family
- **THEN** the diff analysis MUST mark which baseline assets require structural updates in addition to the release-level coverage work

### Requirement: Diff analysis classifies risk, regression strategy, and coverage state
The test baseline SHALL require each diff item to include change type, business criticality, technical uncertainty, regression breadth, recommended regression strategy, and explicit coverage state.

#### Scenario: Team prioritizes limited test capacity
- **WHEN** test resources cannot cover every changed path equally
- **THEN** the diff analysis MUST surface risk and regression priority data that supports ordering of manual and automated coverage

#### Scenario: Team records an uncovered change item
- **WHEN** an in-scope change item cannot be fully covered
- **THEN** the diff analysis MUST record the uncovered or partially covered status together with the reason and follow-up action

### Requirement: Diff items map to downstream test assets and reporting references
The test baseline SHALL require each diff item to reference relevant modules, rules, planned test themes, existing or new test cases, candidate automation items, and report references where available.

#### Scenario: Tester derives coverage from a diff item
- **WHEN** a tester reads a completed diff record
- **THEN** the tester MUST be able to identify which test areas, case assets, and automation candidates should be updated or re-executed

#### Scenario: Report owner explains release risk
- **WHEN** a release report summarizes residual risk
- **THEN** the report owner MUST be able to cite unresolved or partially covered diff items from the analysis template

### Requirement: Precise coverage is auditable at the diff-item level
The test baseline SHALL define precise coverage so that every in-scope diff item is either linked to a verification path or explicitly excluded with rationale.

#### Scenario: Auditor checks release coverage
- **WHEN** a QA manager audits a release package
- **THEN** the auditor MUST be able to verify for each in-scope diff item whether it is covered by test plan themes, test cases, automation decisions, and report conclusions, or whether it has an approved exclusion reason
