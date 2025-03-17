# Digital tools and AI training for university admins

You will help me prepare a day long hands-on workshop. Help me design a full day online workshop to teach university administrators on how to use digital tools effectively with the focus on using AI to enhance their work. They have very little background and are not using digital tools effectively.  

Here are some of the tools that I want to cover 
One Google sheets. As well as how to design a good table using tidy data format.
Two Google Docs with style sheet and style application of tax for EC style changing 
Three simple used cases for LLM   
Four combining university context with LLM to achieve more work

The workshop will be taught purely online. I’ll be the only instructor.  I want to workshop to have both instructional part a lecture, and also a hands-on part where a participants need to work on something.

Help me prepare the class, including all the talking toys all the files necessary to do demonstration all the files and context and prompts necessary to lead the hands on part

The announced schedule can be found at `schedule.md`.
Some rough planning has been done and can be found at `rough_planning.md`.


## Presentation slides
- When you create presentation slides, use markdown and render it with sli.dev.
- Sli.dev has been installed with `npm init slidev@latest`. All the slides should
be stored within slidev project folder called `presentation`. 
- Presentation should be broken into multiple files. Each file corresponds to
  major/logical break in the day's schedule.

## Documents
- When creating documents, one can either create a markdown file locally or
  upload the file to Google Drive. Choose the appropriate format that will help
  with the teaching.

## Spreadsheets
- When creating a spreadsheet, create one as Google Sheets. See `technical
  considerations` on how to access Google Drive credential.
- Spreadsheet should be complex enough to be interesting, but still be suitable
  to show in an online workshop.

## Pedagogical considerations
- Audience is not digital-savvy and have never used AI.
- Use cases and examples should be interesting and work up from easy to
  resembling-real-life
- All examples should be close to real life usage in depth, complexity, and
  difficulty. 
- Language of instructions and communications: Predominantly Thai. But can use English for anything that is common for Thai
people to use English as is.
- Audience can read intermediate English words

## Aesthetic
Following the following aesthetic is highly recommended but not necessary.
1. There are two primary colors: PSU Deep Blue (#003C71) and PSU Sky Blue
   (#009CDE)
2. Four secondary colors: PSU Ocean Blue (#315DAE), PSU Andaman Blue (#0085AD),
   PSU River Blue (#59CBE8), PSU Sritrang(#B6B8DC)
3. Can use black and white as well. 
4. Slides should have 16:9 ratio

## Technical considerations
- All python codes/scripts and CLI tools should be run using `uv run [command]`
- `uv` is used throughout to manage python dependencies
- credential to access Google Drive is already stored in `credential.json`
- When creating Google Sheets/Documents, use `1oDG_0QykkSHVLUgoZREuxihzGYWPb-Sj` as target folder.

## Output needed
At the end, we should have
1. One Markdown file containing the entire day schedule + major talking points
   in each section + links to local files or online files that are relevant.
2. The day schedule should address the majority of the content found in
   `schedule.md`
3. The day schedule should have natural cadence that respects the time required
   to properly introduce examples/concepts, break time, time for participants
   to do exercise, and time to show solution to exercise.
