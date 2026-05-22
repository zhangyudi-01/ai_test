## ADDED Requirements

### Requirement: Baseline and iteration modes are separated
The business baseline SHALL define separate working modes for initial full baseline construction and later iteration diff analysis.

#### Scenario: Initial baseline mode is full-scope
- **WHEN** the first baseline is created from a complete PRD
- **THEN** all mandatory asset categories are populated from the source set

#### Scenario: Later diff mode is incremental
- **WHEN** a subsequent requirement change is analyzed
- **THEN** the analysis references an existing baseline version and impacted asset IDs instead of rebuilding the entire baseline

### Requirement: Diff entries compare old and new behavior
Iteration diff analysis SHALL record the baseline version, impacted asset IDs, old behavior, new behavior, source of change, change type, and baseline update decision for each diff item.

#### Scenario: Reviewers can compare behaviors
- **WHEN** a diff item is reviewed
- **THEN** the original baseline behavior and changed behavior are visible in the same record

### Requirement: Baseline update governance
The baseline SHALL only be rewritten directly after the relevant diff items are confirmed and incorporated.

#### Scenario: Diff and baseline do not drift silently
- **WHEN** a change is still under analysis or not yet frozen
- **THEN** the change is tracked in diff artifacts without silently overwriting baseline assets
