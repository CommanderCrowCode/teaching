# Design Notes: Slidev Presentation

## Slidev Configuration

### Theme and Styling
- **Theme**: Default theme for maximum compatibility
- **Transitions**: slide-left for smooth progression
- **Highlighter**: Shiki for code syntax highlighting
- **Layout variety**: Using intro, center, two-cols, section layouts

### Visual Design Principles

#### Color Palette
- **Primary**: Blue gradient (#2B90B6 to #146b8c)
- **Accent colors**:
  - Green (#10B981) for success/positive
  - Yellow (#F59E0B) for warnings/tips
  - Red (#EF4444) for errors/wrong examples
  - Purple (#8B5CF6) for special highlights

#### Typography
- Clean sans-serif fonts
- Large text for readability (minimum 18px)
- Clear hierarchy with size and weight
- Emoji usage for visual interest and quick recognition

#### Layout Patterns
1. **Title slides**: Centered, large text, gradient effects
2. **Content slides**: Clear sections, bullet points, visual breaks
3. **Exercise slides**: Prominent timers, clear instructions, example boxes
4. **Comparison slides**: Side-by-side layouts, visual differentiation

## Slide Structure Decisions

### Opening Sequence (Slides 1-6)
- Builds excitement and sets expectations
- Interactive poll early for engagement
- Visual framework introduction

### Module Structure
Each module follows a pattern:
1. Section opener (builds anticipation)
2. Concept introduction (visual + text)
3. Demo/example slide
4. Exercise instructions (clear, timed)
5. Recap or transition

### Progressive Disclosure
- Heavy use of `v-clicks` for step-by-step reveals
- Prevents cognitive overload
- Maintains attention and pacing

### Visual Elements

#### Icons and Emojis
Strategic use for:
- Quick visual recognition (✍️ for writing, 🔍 for search, 📊 for data)
- Emotional connection
- Breaking up text-heavy content
- Status indicators (✅ ❌ 💡)

#### Code Blocks and Examples
- Highlighted syntax where appropriate
- Real examples, not generic
- Contrast backgrounds for visibility

#### Interactive Elements
- Polls and live feedback
- QR codes for resources
- Clear CTAs for exercises

## Speaker Support Features

### Speaker Notes
- Embedded in HTML comments
- Key talking points
- Timing reminders
- Energy level cues

### Navigation Aids
- Progress indicators implied through module numbers
- Clear section breaks
- Visual callbacks to earlier content

## Accessibility Considerations

1. **High contrast** between text and backgrounds
2. **Large fonts** throughout (minimum 24pt equivalent)
3. **Clear headings** for screen reader navigation
4. **Alt text** placeholders for images
5. **Logical flow** without relying solely on visuals

## Technical Implementation

### Slidev Features Used
- **Layouts**: default, intro, center, two-cols, section, end
- **Components**: v-clicks for animations
- **Styling**: Inline Tailwind CSS classes
- **Icons**: Carbon icon set integration

### File Organization
- Single presentation.md file for easy maintenance
- External images referenced (to be created)
- Consistent naming conventions

## Animation and Transitions

### Purposeful Animation
- Slide transitions: Consistent left-to-right
- Content reveals: Top-to-bottom with v-clicks
- No distracting animations
- Focus on content, not effects

### Pacing Controls
- Speaker controls narrative flow
- Animations support, not distract
- Quick transitions between slides

## Responsive Design Notes

### Screen Adaptability
- Flexible grid layouts
- Relative sizing where possible
- Core content visible at various resolutions
- Optimized for screen sharing

## Image Placeholders Required

The following images need to be created:
1. `/chatgpt-claude-comparison.png` - Side-by-side interface
2. `/connected-papers-interface.png` - Annotated screenshot
3. `/julius-interface.png` - Interface overview
4. QR codes for surveys and resources

## Maintenance and Updates

### Easy Updates
- Content in markdown for simple edits
- Modular slide structure
- Clear comments for customization
- Template patterns for consistency

### Version Control Friendly
- Plain text format
- Logical section breaks
- Clear commit points

## Performance Optimization

- Minimal external dependencies
- Efficient use of Slidev features
- Fast load times
- Smooth presentation delivery

## Future Enhancements

Potential additions:
1. Live coding demonstrations
2. Embedded videos for tool demos
3. Real-time collaboration features
4. Automated progress tracking
5. Integration with workshop platform

## Summary

This Slidev presentation balances:
- **Visual appeal** with **functionality**
- **Information density** with **clarity**
- **Interactivity** with **smooth delivery**
- **Modern design** with **accessibility**

The design supports both presenter needs and participant engagement throughout the 3-hour workshop.