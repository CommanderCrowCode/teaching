# AI Workshop Transformation: Agent Instructions

## Project Overview
Transform a full-day workshop on "Enhancing Research with AI Tools" into a comprehensive half-day format with complete materials and resources.

## Directory Structure
```
workshop-ai-tools-halfday/
├── 01-rescoped-schedule/
│   └── halfday-schedule.md
├── 02-detailed-content/
│   └── workshop-content.md
├── 03-presentation-materials/
│   ├── presentation-slides.md
│   └── speakers-notes.md
├── 04-slide-deck/
│   └── slides.ev
├── 05-resources/
│   ├── datasets/
│   ├── exercises/
│   └── solutions/
└── project-status.md
```

---

## Agent 1: Workshop Rescoping Agent

### Objective
Condense the 8-hour workshop into a 3-hour format (9:00 AM - 12:00 PM) while maintaining maximum educational value.

### Instructions
1. **Core Priorities:**
   - Focus on hands-on skills that provide immediate value
   - Prioritize tools with lowest barrier to entry
   - Maintain balance between theory and practice
   - Ensure each module has a clear takeaway

2. **Rescoping Guidelines:**
   - Eliminate redundancies and merge similar content
   - Reduce tool coverage to essentials: ChatGPT/Claude + one literature tool + one data tool
   - Compress theoretical content, expand practical exercises
   - Include one 10-minute break at the midpoint

3. **Time Allocation Framework:**
   - Welcome & Setup: 15 minutes
   - Module 1 (AI Fundamentals): 30 minutes
   - Module 2 (Literature Review): 45 minutes
   - Break: 10 minutes
   - Module 3 (Writing & Analysis): 45 minutes
   - Module 4 (Workflow & Wrap-up): 45 minutes

4. **Output Requirements:**
   - Create `halfday-schedule.md` with:
     - Clear time blocks
     - Learning objectives per module
     - Tool focus for each segment
     - Hands-on activity descriptions

---

## Agent 2: Content Development Agent

### Objective
Expand the rescoped schedule into comprehensive, actionable content with precise timing.

### Instructions
1. **Content Structure Per Module:**
   - **Lecture Component (40%)**: Key concepts, demonstrations
   - **Example Component (30%)**: Real-world applications
   - **Hands-on Exercise (30%)**: Participant activities

2. **Detailed Breakdown Requirements:**
   - Minute-by-minute timing (e.g., 9:00-9:03, 9:03-9:08)
   - Specific talking points for each time block
   - Clear transitions between segments
   - Equipment/tool checks at strategic points

3. **Interactive Elements:**
   - Poll questions with timing
   - Breakout room activities with clear instructions
   - Share-screen moments marked explicitly
   - Participant engagement checkpoints

4. **Example Development:**
   - Create 2-3 concrete examples per tool
   - Show before/after comparisons
   - Include common mistakes and solutions
   - Real research scenarios from multiple disciplines

5. **Output Requirements:**
   - Create `workshop-content.md` with:
     - Complete script-like content
     - Visual cue markers
     - Interaction prompts
     - Technical setup notes

---

## Agent 3: Presentation Materials Agent

### Objective
Separate content into screen-visible presentation materials and detailed speaker notes.

### Instructions
1. **Presentation Slides Requirements:**
   - **Slide Density**: Maximum 5 bullet points per slide
   - **Visual Elements**: Indicate where screenshots, diagrams needed
   - **Font Hierarchy**: Title, subtitle, body text specifications
   - **Animations**: Mark entrance/exit animations
   - **Color Coding**: Different modules = different accent colors

2. **Speaker Notes Requirements:**
   - **Verbatim Scripts**: What to say for each slide
   - **Timing Markers**: Duration per slide
   - **Interaction Cues**: When to pause, ask questions
   - **Technical Notes**: Demo steps, fallback options
   - **Energy Markers**: High/medium/low energy delivery points

3. **Time Synchronization:**
   - Each slide numbered with timestamp
   - Speaker notes reference slide numbers
   - Include "buffer time" notes for Q&A
   - Mark "can skip if behind" content

4. **Output Requirements:**
   - `presentation-slides.md`: Slide-by-slide content
   - `speakers-notes.md`: Synchronized speaker script

---

## Agent 4: Slide Design Agent

### Objective
Transform presentation content into visually appealing slide.ev format.

### Instructions
1. **Design Principles:**
   - **Theme**: Modern, academic, professional
   - **Color Palette**: 
     - Primary: Deep blue (#1E3A8A)
     - Secondary: Teal (#0891B2)
     - Accent: Orange (#F97316)
     - Background: Off-white (#FAFAFA)
   - **Typography**:
     - Headers: Inter or Helvetica Bold
     - Body: Open Sans or Arial
     - Code: Fira Code or Consolas

2. **Slide Types:**
   - Title slides (module breaks)
   - Content slides (bullet points)
   - Demo slides (screenshot placeholders)
   - Exercise slides (instructions)
   - Progress slides (timeline indicators)

3. **Visual Elements:**
   - Icons for each AI tool
   - Progress bar showing workshop timeline
   - Consistent header/footer design
   - QR codes for resource links

4. **Interactive Features:**
   - Clickable menu for navigation
   - Embedded timers for exercises
   - Live poll integration markers

5. **Output Requirements:**
   - Create `slides.ev` with complete deck
   - Include slide notes in metadata
   - Export backup as PDF markers

---

## Agent 5: Resources Creation Agent

### Objective
Generate all datasets, exercises, and solutions needed for the workshop.

### Instructions
1. **Dataset Requirements:**
   - **Literature Dataset**: 
     - CSV with 50 paper entries (title, author, year, abstract, keywords)
     - Mix of disciplines (biology, psychology, engineering)
   - **Research Data**:
     - Numerical dataset (100 rows, 5 variables)
     - Include missing values for cleaning exercise
     - Time series component for visualization

2. **Exercise Materials:**
   - **Exercise 1**: AI Prompt Templates
     - 5 research scenarios
     - Starter prompts to improve
     - Evaluation criteria
   - **Exercise 2**: Literature Mapping
     - Seed paper information
     - Expected discovery goals
     - Search strategy worksheet
   - **Exercise 3**: Data Analysis
     - Research questions
     - Analysis steps
     - Visualization requirements

3. **Solution Sets:**
   - Complete solutions with explanations
   - Common variations accepted
   - Troubleshooting guides
   - "If you're stuck" hints

4. **Output Requirements:**
   - `/datasets/`: All CSV and data files
   - `/exercises/`: Exercise PDFs/markdown
   - `/solutions/`: Complete answer keys

---

## Agent 6: Claude Code Supervisor Agent

### Objective
Oversee and coordinate the entire workshop transformation process.

### Instructions
```python
# Claude Code Supervision Instructions

## Initial Setup
1. Create directory structure as specified
2. Verify all agents have completed their tasks
3. Run quality checks on outputs

## Execution Sequence
```
workflow = {
    "phase_1": {
        "agent": "Agent 1 - Rescoping",
        "input": "Full-day workshop plan",
        "output": "halfday-schedule.md",
        "validation": ["3-hour total", "4 modules", "clear objectives"]
    },
    "phase_2": {
        "agent": "Agent 2 - Content",
        "input": "halfday-schedule.md",
        "output": "workshop-content.md",
        "validation": ["minute-by-minute", "examples included", "exercises defined"]
    },
    "phase_3": {
        "agent": "Agent 3 - Materials",
        "input": "workshop-content.md",
        "output": ["presentation-slides.md", "speakers-notes.md"],
        "validation": ["time-synced", "slide numbers", "speaker cues"]
    },
    "phase_4": {
        "agent": "Agent 4 - Design",
        "input": "presentation-slides.md",
        "output": "slides.ev",
        "validation": ["consistent design", "all slides created", "navigation works"]
    },
    "phase_5": {
        "agent": "Agent 5 - Resources",
        "input": "workshop-content.md",
        "output": ["datasets/*", "exercises/*", "solutions/*"],
        "validation": ["all files present", "data validates", "solutions complete"]
    }
}
```

## Quality Assurance Checklist
- [ ] Total duration exactly 3 hours
- [ ] All transitions smooth and logical
- [ ] No missing dependencies between modules
- [ ] All exercises have data/resources
- [ ] Speaker notes align with slides
- [ ] Technical requirements clearly stated
- [ ] Backup plans for technical issues
- [ ] Resource links all functional

## Progress Tracking
Update `project-status.md` after each phase:
```markdown
# Workshop Transformation Status

## Phase Completion
- [x] Agent 1: Rescoping - COMPLETE
- [ ] Agent 2: Content Development - IN PROGRESS
- [ ] Agent 3: Materials Separation
- [ ] Agent 4: Slide Design
- [ ] Agent 5: Resource Creation
- [ ] Agent 6: Final Review

## Issues Log
- None

## Next Steps
- Begin Agent 2 execution
```

## Final Deliverables Checklist
1. **Core Materials**
   - [ ] Complete slide deck (slides.ev)
   - [ ] Speaker notes document
   - [ ] All datasets generated
   - [ ] Exercise materials created
   - [ ] Solution guides complete

2. **Supporting Documents**
   - [ ] Pre-workshop email template
   - [ ] Technical setup guide
   - [ ] Post-workshop resources list
   - [ ] Feedback form

3. **Quality Metrics**
   - [ ] Timing adds up correctly
   - [ ] All tools demonstrated
   - [ ] Interactive elements every 15 min
   - [ ] Clear learning outcomes
   - [ ] Actionable takeaways

## Error Handling
If any agent fails:
1. Log error in project-status.md
2. Identify dependencies affected
3. Provide fallback content
4. Mark as "needs revision"
5. Continue with next possible agent

## Final Review Protocol
1. Run through entire workshop timeline
2. Check all internal references
3. Verify resource availability
4. Test all interactive elements
5. Generate final summary report
```

---

## Execution Notes for Claude Code

When implementing this system:

1. **Start Command**: 
   ```
   claude-code execute workshop-transformation --agents all
   ```

2. **Individual Agent Execution**:
   ```
   claude-code execute workshop-transformation --agent 1
   ```

3. **Status Check**:
   ```
   claude-code status workshop-transformation
   ```

4. **Final Package**:
   ```
   claude-code package workshop-transformation --output workshop-ready.zip
   ```

The Claude Code supervisor should maintain logs of each agent's execution and ensure smooth handoffs between phases. Any conflicts or ambiguities should be resolved by referring back to the core objective: creating an effective, engaging 3-hour workshop that provides immediate value to research students.