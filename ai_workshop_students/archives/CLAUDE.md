# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains an educational content transformation project that converts an 8-hour AI workshop into a 3-hour format using a system of 6 AI agents. The workshop teaches researchers how to use AI tools (ChatGPT, Claude, Connected Papers, Semantic Scholar, Julius AI, and Zotero) to accelerate their research.

## Agent System Architecture

The project uses a sequential 6-agent system, where each agent has specific responsibilities:

1. **Agent 1 (Schedule Optimizer)**: Creates a 3-hour schedule from the 8-hour content
2. **Agent 2 (Content Developer)**: Expands the condensed schedule into detailed workshop content
3. **Agent 3 (Presentation Creator)**: Creates comprehensive slides and speaker notes
4. **Agent 4 (Visual Designer)**: Transforms content into visual presentations (.ev format)
5. **Agent 5 (Resource Developer)**: Creates exercises, datasets, and participant resources
6. **Agent 6 (Quality Supervisor)**: Validates and ensures consistency across all outputs

## Key Commands

Execute transformation for all agents:
```bash
claude-code execute workshop-transformation --agents all
```

Execute transformation for a specific agent:
```bash
claude-code execute workshop-transformation --agent [1-6]
```

Check transformation status:
```bash
claude-code status workshop-transformation
```

Package final workshop materials:
```bash
claude-code package workshop-transformation --output workshop-ready.zip
```

## Directory Structure and Outputs

- `00-source-materials/`: Original 8-hour workshop content
- `01-rescoped-schedule/`: Agent 1 outputs - `schedule.md`, `module_breakdown.md`, `timing_rationale.md`
- `02-detailed-content/`: Agent 2 outputs - `workshop_content.md`, `learning_objectives.md`, `content_notes.md`
- `03-presentation-materials/`: Agent 3 outputs - `slides_outline.md`, `speaker_notes.md`, `presentation_checklist.md`
- `04-slide-deck/`: Agent 4 outputs - `presentation.ev`, `visual_assets/`, `design_notes.md`
- `05-resources/`: Agent 5 outputs - `exercises/`, `datasets/`, `quick_reference.pdf`, `setup_instructions.md`

## Agent Workflow Rules

1. Agents must work sequentially - each agent depends on the previous agent's output
2. All outputs must be saved in the designated directories
3. Each agent must complete all required outputs before the next agent can proceed
4. Agent 6 reviews all outputs and can request revisions from any previous agent

## Content Focus Areas

The workshop covers six main AI tools:
- ChatGPT: General research assistance and writing
- Claude: Advanced analysis and reasoning
- Connected Papers: Literature discovery and mapping
- Semantic Scholar: AI-powered literature search
- Julius AI: Data analysis and visualization
- Zotero: Reference management with AI plugins

## Quality Validation

Agent 6 uses specific checklists to validate:
- Schedule feasibility and timing
- Content completeness and learning objectives
- Presentation clarity and visual design
- Exercise practicality and resource quality
- Overall workshop coherence and flow

## Development Guidelines

1. Always check `project-status.md` to understand current progress
2. Refer to `agent_instructions.md` for detailed requirements for each agent
3. Maintain the 3-hour constraint while preserving educational value
4. Focus on hands-on practice - at least 50% of time should be interactive
5. Ensure all materials are beginner-friendly for researchers new to AI tools