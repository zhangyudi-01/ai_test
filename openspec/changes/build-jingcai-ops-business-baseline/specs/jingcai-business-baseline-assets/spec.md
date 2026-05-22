## ADDED Requirements

### Requirement: Business baseline asset library
The change SHALL produce a business baseline asset library for the竞猜赛事运营系统 that covers modules, pages/functions, roles/permissions, business objects/fields, rules, states/flows, external dependencies/file flows, API/action mappings, and open questions derived from the full PRD.

#### Scenario: Mandatory asset set exists
- **WHEN** the change directory is reviewed
- **THEN** it contains a README plus one document for each mandatory business baseline asset category

#### Scenario: Business-only scope is enforced
- **WHEN** the asset library is inspected
- **THEN** it contains no test plans, test cases, automation scripts, or test reports

### Requirement: Full-PRD baseline coverage
The baseline SHALL be built from the full PRD source and SHALL preserve any unreadable or unresolved details explicitly rather than omitting them silently.

#### Scenario: PRD content is represented
- **WHEN** a reviewer samples a module, page, or rule from the PRD
- **THEN** the sampled item can be located in the corresponding baseline document or in the open questions register

#### Scenario: External gaps are not inferred
- **WHEN** a required detail depends on images, prototypes, or external attachments that cannot be reliably read in the workspace
- **THEN** the baseline marks the detail as `依赖外部原型补充`

### Requirement: Verifiable coverage contract
The baseline SHALL define verifiable output requirements for each asset category so completeness can be checked without reinterpreting the author’s intent.

#### Scenario: Coverage can be reviewed deterministically
- **WHEN** the baseline README or governance sections are reviewed
- **THEN** they state what each asset must contain and what qualifies as complete coverage
