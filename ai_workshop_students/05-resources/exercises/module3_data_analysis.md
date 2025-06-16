# Module 3: Data Analysis Made Simple - Julius AI Exercises

## Dataset Overview: research_productivity.csv

### Variables in Your Dataset
- **researcher_id**: Unique identifier (1-100)
- **publications**: Number of published papers
- **citations**: Total citations received
- **years_experience**: Years in research (1-22)
- **funding_thousands**: Research funding in $1000s
- **collaboration_score**: Collaboration index (1-10)

### Sample Size: 100 researchers
### Context: Academic research productivity metrics

---

## Exercise 1: Data Exploration (10 minutes)

### Natural Language Commands to Try

Copy and paste these commands into Julius AI:

#### Basic Exploration
1. **"Show me summary statistics for all variables"**
   - Expected: Mean, median, SD, min, max for each variable

2. **"What's the distribution of publications?"**
   - Expected: Histogram showing publication counts

3. **"Are there any outliers I should know about?"**
   - Expected: Box plots or outlier identification

4. **"Show me the correlation matrix"**
   - Expected: Correlation table with all variables

5. **"Which variables are most strongly related?"**
   - Expected: Sorted correlation pairs

### Your Exploration Notes

**Interesting Finding 1:**
_________________________________

**Interesting Finding 2:**
_________________________________

**Surprising Pattern:**
_________________________________

### Follow-Up Questions to Ask
- "Why might [variable] have this distribution?"
- "Show me researchers with unusual patterns"
- "What percentile is [X publications]?"
- "Create a scatter plot matrix"

---

## Exercise 2: Statistical Analysis (10 minutes)

### Guided Analysis Sequence

Follow these steps exactly:

#### Step 1: Test Correlation
**Command:** "Test the correlation between years_experience and publications. Include significance test."

**Record Results:**
- Correlation coefficient (r): _____
- P-value: _____
- Interpretation: _____

#### Step 2: Run Regression
**Command:** "Run a multiple regression with publications as the outcome variable and years_experience, funding_thousands, and collaboration_score as predictors. Show me the full results."

**Record Results:**
- R-squared: _____
- Significant predictors: _____
- Largest coefficient: _____

#### Step 3: Check Assumptions
**Command:** "Check the regression assumptions including normality of residuals, homoscedasticity, and multicollinearity."

**Record Results:**
- Assumptions met? _____
- Any concerns? _____

#### Step 4: Plain English Interpretation
**Command:** "Explain these regression results in plain English that a non-statistician could understand. What's the practical meaning?"

**Key Takeaway:**
_________________________________
_________________________________

### Additional Analyses to Try
- "Test if funding differs by experience level"
- "Do a mediation analysis with collaboration as mediator"
- "What's the optimal funding level for publications?"
- "Identify the most 'efficient' researchers"

---

## Exercise 3: Publication-Ready Visualization (15 minutes)

### Main Visualization Task

#### Step 1: Create Base Plot
**Command:** 
```
Create a scatter plot with:
- X-axis: years_experience 
- Y-axis: publications
- Add a trend line with confidence interval
- Add point colors based on funding_thousands
- Make it publication quality
```

#### Step 2: Customize for Journal
**Sequential Commands:**
1. "Make the font size larger for all text"
2. "Change to APA style formatting"
3. "Use grayscale colors suitable for print"
4. "Add a proper figure caption"
5. "Export as 300 DPI PNG"

### Alternative Visualizations to Create

#### Option A: Grouped Comparison
```
Create a box plot showing publications 
grouped by experience level (0-5, 6-10, 
11-15, 16+ years). Add significance 
indicators between groups.
```

#### Option B: Multi-Panel Figure
```
Create a 2x2 panel figure showing:
1. Publications vs experience scatter
2. Citations vs publications scatter  
3. Funding distribution histogram
4. Collaboration score by experience
```

#### Option C: Advanced Visualization
```
Create a bubble chart where:
- X = years_experience
- Y = citations
- Bubble size = publications
- Color = collaboration_score
Add quadrant lines at medians
```

### Customization Commands

#### For APA Style:
- "Format according to APA 7th edition"
- "Use Times New Roman or Arial font"
- "Remove gridlines, keep axes only"
- "Add tick marks facing outward"

#### For Nature/Science Style:
- "Use Helvetica or Arial font"
- "Make lines thicker (2pt)"
- "Use high contrast colors"
- "Minimize non-data ink"

#### For Accessibility:
- "Use colorblind-friendly palette"
- "Add patterns in addition to colors"
- "Increase contrast between elements"
- "Make all text at least 8pt"

### Export Specifications

**Command Template:**
```
Export this figure as:
- Format: PNG
- Resolution: 300 DPI  
- Size: 6.5 inches wide
- Background: white
- File name: figure1_publications_analysis
```

---

## Advanced Julius AI Commands

### Statistical Testing
```
Perform a one-way ANOVA testing if 
publications differ by experience groups 
(0-5, 6-10, 11-15, 16+ years). Include 
post-hoc tests if significant.
```

### Predictive Modeling
```
Build a model to predict citations based 
on all other variables. Compare linear 
regression, polynomial, and random forest. 
Which performs best?
```

### Custom Calculations
```
Calculate the "impact factor" for each 
researcher as citations/publications. 
Who are the top 10 researchers by this 
metric? What characteristics do they share?
```

### Publication Metrics
```
Create a new variable for "productivity" 
as publications/years_experience. How does 
productivity change over career stages? 
Show me the trend.
```

---

## Interpreting Your Results

### Questions to Consider
1. What factors most strongly predict publication success?
2. Is more funding always better for productivity?
3. How important is collaboration?
4. Are there diminishing returns with experience?

### Connecting to Your Research
- How do these patterns compare to your field?
- What additional variables would you include?
- Which findings challenge your assumptions?
- How could you apply this analysis approach?

### Common Pitfalls to Avoid
- ❌ Over-interpreting small correlations
- ❌ Assuming causation from correlation
- ❌ Ignoring assumption violations
- ❌ P-hacking by testing everything
- ❌ Not considering practical significance

---

## Julius AI Pro Tips

### Getting Better Results
1. **Be specific** about what you want
2. **Use proper variable names** exactly
3. **Ask for explanations** of methods used
4. **Request step-by-step** for complex analyses
5. **Iterate on visualizations** until perfect

### Time-Saving Shortcuts
- "Do the same analysis but with [different variable]"
- "Repeat this for all variables"
- "Save all results to a summary table"
- "Create a methods section describing this analysis"

### Quality Checks
- Always verify calculations on key results
- Ask Julius to show its work/formulas
- Request confidence intervals, not just point estimates
- Cross-check unusual findings

### Export Formats
- **PNG**: Best for presentations, documents
- **SVG**: Best for editing later
- **PDF**: Best for print quality
- **CSV**: For data/results tables

---

## Your Analysis Summary

### Key Findings
1. _________________________________
2. _________________________________
3. _________________________________

### Most Interesting Visualization
_________________________________

### How You'll Use Julius in Your Research
_________________________________
_________________________________

### Next Steps
- [ ] Try with your own data
- [ ] Explore advanced analyses
- [ ] Create publication figures
- [ ] Set up regular analysis workflow