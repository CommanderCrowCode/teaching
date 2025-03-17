# Diagram Enhancement Plan for AI for Admins Workshop

This document outlines the plan to enhance the workshop presentation with mermaid diagrams for improved clarity and visual appeal.

## Diagram Opportunities

### 1. Tidy Data Transformation Flow (`04_tidy_data.md`)
**Purpose:** Visualize the process of transforming untidy data to tidy data format  
**Description:** A flowchart showing the step-by-step transformation process  
**Benefits:** Helps participants understand the practical steps in data cleaning  

```mermaid
flowchart LR
    A[Untidy Data] --> B[Identify Issues]
    B --> C[Separate Mixed Columns]
    C --> D[Fix Merged Cells]
    D --> E[Normalize Multiple Values]
    E --> F[Tidy Data]
    
    style A fill:#f9f9f9,stroke:#cccccc
    style F fill:#e6f7ff,stroke:#009CDE
```

### 2. AI Prompt Engineering Techniques (`05_ai_tools.md`)
**Purpose:** Show different prompt engineering approaches and their relationships  
**Description:** A hierarchical diagram showing prompt techniques and use cases  
**Benefits:** Creates a visual reference for different prompting strategies  

```mermaid
mindmap
    root((AI Prompt<br>Techniques))
        Basic Prompts
            Clear Instructions
            Context Setting
            Format Specification
        Advanced Techniques
            Role-based Prompting
            Chain of Thought
            Few-shot Learning
            Self-reflection
```

### 3. Digital Tools Workflow Integration (`08_integration.md`)
**Purpose:** Illustrate how different tools connect and data flows between them  
**Description:** A flowchart showing the integration of Google Workspace and AI tools  
**Benefits:** Demonstrates the end-to-end process visually  

```mermaid
flowchart TD
    A[Google Forms] -->|Data Collection| B[Google Sheets]
    B -->|Data Organization| C{Data Analysis}
    C -->|Manual Analysis| D[Google Sheets<br>Functions & Pivot Tables]
    C -->|AI-assisted Analysis| E[AI Analysis<br>Trends & Insights]
    D --> F[Google Docs<br>Report Creation]
    E --> F
    F -->|Collaboration| G[Team Review<br>& Feedback]
    G -->|Final Version| H[Publication<br>& Distribution]
    
    style A fill:#fbbc04,stroke:#ea8600
    style B fill:#0f9d58,stroke:#0b8043
    style F fill:#4285f4,stroke:#185abc
    style E fill:#b2a3ff,stroke:#673ab7
```

### 4. Before/After Process Comparison (`07_ai_case_studies.md`)
**Purpose:** Compare traditional workflows with AI-enhanced workflows  
**Description:** A side-by-side comparison diagram showing process improvements  
**Benefits:** Clearly illustrates time and effort savings  

```mermaid
flowchart TB
    subgraph Before ["Traditional Process"]
        direction TB
        A1[Manual Data<br>Collection] --> B1[Manual Data<br>Entry]
        B1 --> C1[Manual Analysis]
        C1 --> D1[Report Creation]
        D1 --> E1[Review & Revisions]
        E1 --> F1[Final Document]
    end
    
    subgraph After ["AI-Enhanced Process"]
        direction TB
        A2[Digital Data<br>Collection] --> B2[Automated<br>Organization]
        B2 --> C2[AI-assisted<br>Analysis]
        C2 --> D2[AI-assisted<br>Report Creation]
        D2 --> E2[Review]
        E2 --> F2[Final Document]
    end
    
    style Before fill:#fff0f0,stroke:#ffcccc
    style After fill:#f0fff0,stroke:#ccffcc
```

### 5. AI Conceptual Model (`03_ai_intro.md`)
**Purpose:** Simplify the concept of how AI works  
**Description:** A basic flow diagram showing AI processing  
**Benefits:** Demystifies AI for non-technical administrators  

```mermaid
flowchart LR
    A[User Input<br>Prompt] --> B[AI Processing]
    B --> C[Generated<br>Output]
    
    subgraph AI Processing
    D[Pattern<br>Recognition] --> E[Context<br>Understanding]
    E --> F[Response<br>Generation]
    end
    
    style B fill:#e6f7ff,stroke:#009CDE
```

## Aesthetic Considerations

### Color Scheme
- Use Prince of Songkla University's official colors:
  - PSU Blue: #003C71 (primary color)
  - PSU Light Blue: #009CDE (secondary color)
  - Complementary accent colors for highlights
- Maintain consistent color usage across all diagrams
- Use light backgrounds with darker outlines for readability

### Typography
- Keep text concise and readable
- Use hierarchical text sizing for diagram labels
- Ensure text contrasts well with background colors
- Keep consistent terminology with the rest of the presentation

### Layout
- Maintain left-to-right or top-to-bottom flow for process diagrams
- Use appropriate spacing between elements
- Limit diagram complexity - focus on key concepts
- Balance text and visual elements
- Ensure diagrams are responsive and visible on different screen sizes

### Cultural Considerations
- Include Thai terms alongside English where appropriate
- Design with consideration for Thai aesthetic preferences
- Ensure examples relate to university administrative contexts

## Implementation Plan

1. Prioritize diagrams in this order:
   - Digital Tools Workflow Integration (highest impact)
   - Before/After Process Comparison
   - Tidy Data Transformation Flow
   - AI Prompt Engineering Techniques
   - AI Conceptual Model

2. Create one diagram at a time, integrate into slides, and test

3. Gather feedback and refine diagrams as needed

4. Ensure all diagrams work properly with the slidev presentation framework

5. Finalize documentation including diagram source code