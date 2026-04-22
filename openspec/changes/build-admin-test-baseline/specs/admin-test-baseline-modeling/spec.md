## ADDED Requirements

### Requirement: Baseline workflow distinguishes full baseline build from iterative diff analysis
The test baseline SHALL define two operating modes: full baseline build for project initialization, and iterative diff analysis for subsequent releases that reuse the existing structural baseline.

#### Scenario: Team starts the baseline for the first time
- **WHEN** a QA team initializes the baseline for a complex admin project
- **THEN** the baseline package MUST define structural templates, identifier rules, and traceability rules without requiring concrete business test content

#### Scenario: Team analyzes a later release
- **WHEN** a later sprint, release, or hotfix is analyzed
- **THEN** the workflow MUST treat existing module, role, permission, and rule identifiers as inputs and MUST NOT require rebuilding the full baseline unless the structure itself changes

### Requirement: Module map template captures the admin project structure
The test baseline SHALL provide a module map template that records module identifiers, module names, business goals, primary objects, upstream and downstream dependencies, entry points, key workflows, exception paths, and regression risk tags for a complex admin project.

#### Scenario: Analyst initializes a new module landscape
- **WHEN** a tester or QA lead starts building baseline assets for a new admin project
- **THEN** the module map template MUST provide fields that are sufficient to describe the module hierarchy, object boundaries, cross-module interactions, and critical business paths

#### Scenario: Reviewer scopes cross-module regression
- **WHEN** a reviewer inspects a changed module in the baseline
- **THEN** the module map MUST expose dependency and workflow information that helps identify upstream and downstream regression impact

### Requirement: Role-permission matrix models access and control dimensions
The test baseline SHALL provide a role-permission matrix template that maps each role to modules, menu visibility, page access, button or operation permissions, data scope, workflow actions, and constraint notes.

#### Scenario: Analyst evaluates role coverage
- **WHEN** a tester reviews a role in the matrix
- **THEN** the matrix MUST show which modules and permission types are granted, restricted, or conditionally available for that role

#### Scenario: Team checks permission-sensitive behavior
- **WHEN** a change affects a permission-controlled feature
- **THEN** the matrix MUST support tracing from the affected permission entry to the related module and test coverage scope

### Requirement: Module rule library standardizes rule capture and source back references
The test baseline SHALL provide a module rule library template that captures rule identifiers, related modules, source type, source identifier or back reference, trigger conditions, preconditions, validations, calculations, state transitions, asynchronous actions, notifications, audit requirements, exception handling rules, and downstream asset references.

#### Scenario: Analyst records business rules for a module
- **WHEN** a tester documents rule behavior for a module
- **THEN** the rule library template MUST allow the tester to classify the rule and describe the source, trigger, expected result, failure path, and related object or state

#### Scenario: Team traces a failed behavior to a rule source
- **WHEN** a defect, report finding, or automation failure is linked to a broken validation, transition, or calculation
- **THEN** the rule library MUST make it possible to locate the affected rule identifier, its source back reference, and any linked downstream case or automation asset

### Requirement: Structural assets remain traceable across templates
The test baseline SHALL define mandatory references so that modules, roles, permissions, and rules can be referenced consistently from downstream diff analyses, test plans, test cases, automation mappings, and reports.

#### Scenario: Tester writes a traceable case
- **WHEN** a tester creates a test case from the baseline
- **THEN** the tester MUST be able to reference at least one module identifier and, where applicable, a role, permission, or rule identifier from the structural assets

#### Scenario: Manager audits baseline consistency
- **WHEN** a QA manager reviews the baseline package
- **THEN** the manager MUST be able to verify that the same identifiers are reused consistently across all structural templates
