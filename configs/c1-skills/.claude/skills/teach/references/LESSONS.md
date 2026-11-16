# Writing a lesson

A lesson is one self-contained HTML file that teaches one tightly scoped objective tied to the mission, at the length the learner asked for.
Every lesson has the same shape, so the learner always knows where to look: a pre-quiz that tells them what to skim, sections that each run through the same eight parts, and the main points at the end.
The learner will come back to it to review, so it should be clean and readable, in the spirit of Edward Tufte.

## Before you write

- Read the lesson rules in `FORMATS.md`: the file name, the two meta tags, what self-contained means and how the length is estimated.
- Take the next number in `lessons/` and a short slug, such as `lessons/0003-ohms-law-in-series.html`.
- Skim the earlier lessons and `cheatsheets/`, so this lesson links to them and builds on them instead of repeating them.
- Start from `lesson-template.html` in this folder.
  Copy its CSS and script into the lesson so the file stands alone; if `assets/lesson.css` already exists, link it with `../assets/lesson.css` instead, so the lessons look like one course.

## Plan to the minutes

The learner asked for a number of minutes, and the lesson holds **between 100 and 150 words of visible text per minute; aim for about 140**.
`FORMATS.md` gives the estimate the bench uses, visible words divided by 150.
You cannot count words with a command, and lessons written without a plan come out short, so the plan is how you hit the length.

- Count the visible text: every part of every section, the questions and their options, the Common Mix-Ups boxes, figure captions and labels, and the main points.
  The option explanations in `data-why` are attributes, which the length estimate does not count, so leave them out of the budget.
- Before writing, split the budget into parts and write it down for yourself.
  For a 30-minute lesson with four sections, aiming for about 4,200 words, a plan might look like this:

  | Part | Words |
  |---|---|
  | Opening: the win and why it matters for the mission | 120 |
  | Pre-quiz: one question per section, stem and options | 240 |
  | Each section (four of them) | 850 each |
  | Main points | 150 |
  | Go further and closing | 130 |

  And within one 850-word section:

  | Part | Words |
  |---|---|
  | Title, learning goals, prior knowledge | 90 |
  | General idea | 230 |
  | Important steps | 100 |
  | Worked example, with its diagram's caption | 250 |
  | Common Mix-Ups box | 120 |
  | Check Yourself box, stem and options | 60 |

- Write each part to its budget.
  If a section runs short, deepen its worked example or add a second mix-up; never pad, and never repeat a point.
- If the objective is too big for the time, teach its core well and say what the next lesson will cover.
  If it is too small, add sections with more worked examples, not filler.

## The shape of a lesson

1. **Opening:** the title, the time, the win in one sentence ("By the end of this lesson you can ..."), and one or two sentences tying it to the mission.
2. **Pre-quiz:** one short multiple-choice question per section, four options each, before the first section.
   Its purpose is to let the learner find what they already know: each question says which section it covers, and once they pick an option the feedback says whether they were right and why, and then "skim Section N" when they were right or "read Section N closely" when they were not.
   Pre-quiz questions are different from the Check Yourself questions later in the lesson.
3. **Sections, one topic each.** Every section has these eight parts, in this order:
   1. **Section title**, as an `<h2>`.
   2. **Learning goals:** a bulleted list of what the learner can do after this section, each starting with a verb ("tell ... from ...", "decide when to ...", "spot ...").
   3. **Prior knowledge:** a bulleted list of what the learner must already know to follow this section; link the earlier section or lesson that taught each item, and say in a few words what it is when no lesson taught it.
   4. **The general idea:** a few short paragraphs in plain language, one new term at a time, each defined where it first appears, using the terms in `GLOSSARY.md` when it exists, with a citation right after each claim that a source backs.
   5. **Important steps:** a bulleted list of the steps or the decision points, when the idea has steps; leave this part out only when the idea truly has none.
   6. **Worked example:** a concrete, real-world case the learner could meet in their mission, fully explained: the context, why this idea is the right one to use here, and each important step applied to the case in turn, with a diagram of the example when one helps.
      No analogies: the learner asked for real cases, not comparisons to everyday things.
   7. **Common Mix-Ups box:** at least one; for each common error and each common misconception (from `NOTES.md`, the learning records, the keys' distractors and your sources), say what is right, what is wrong, and why, in that order, with the case that shows the difference.
   8. **Check Yourself box:** at least one, at the end of the section: a multiple-choice question with four to six options.
      The answer stays hidden until the learner picks an option; then it shows whether their pick was right and why, and the explanation of every other option.
4. **Main points:** at the end of the lesson, a bulleted list of the main points the learner must understand, one line each, covering every section.
5. **Go further:** the primary source, the single most high-quality, high-trust resource you found, to read or watch next, and two to four other sources you cited.
6. **Closing:** a reminder that they can ask follow-up questions in the chat about anything unclear, and that they can ask for a quiz on this lesson with `/quiz`.

## Questions in the lesson

- Every pre-quiz and Check Yourself question has exactly one best option, and every option is plausible to someone holding the error it encodes; no joke options.
- Give every option about the same number of words, with the same grammar and level of detail, vary which position holds the right one, and never give it away by formatting or order.
- Every option carries its own explanation in `data-why`: why it is right, or why it is tempting and wrong.
- Never put a question's answer anywhere the learner sees before they pick an option: not in the stem, not in a visible caption, not in a `<details>` they could open first.

## Writing

- Direct, with no filler or flattery: say the thing, then show it.
- Several paragraphs per section in plain language, and bullet points wherever a list reads better than prose.
- Headings in order, so the structure is scannable.

## Design

Keep the template's look and change the content, not the system.

- Typography first: a readable serif body, a line length of 60 to 75 characters, generous spacing.
- Few colors, each with a meaning: one accent for links and key terms, one for the Common Mix-Ups boxes.
  The template works in light and dark mode and prints well; keep it that way.
- No decoration: every element helps the learner understand or remember.
- Accessible: headings in order, a `<title>` for every figure, enough contrast, and buttons that work from the keyboard.

## Figures and visualizations

- Several per lesson, and at least one in every section; the worked example's diagram usually counts as that section's figure, and the general idea may have its own.
- Draw what a picture shows better than words: a mechanism, a process, a flow of data, a comparison, a quantity that changes.
- Draw them as inline SVG: a `viewBox`, the labels as text inside the figure, colors from the template's CSS variables or `currentColor` so they work in dark mode, a `<title>`, and a `<figcaption>` that says what to notice.
- Keep labels legible on a phone: a `viewBox` about 640 units wide with labels of 18 units or more, or a vertical layout when there are many parts.
- Use a table for a comparison, and a code block for code.
- Never load an image from the web; draw it.

## Sources and citations

- Find sources with web search and read them before you rely on them.
  Prefer primary and high-trust sources: official documentation, textbooks, standards, university course pages, and peer-reviewed or expert-reviewed work.
- Cite as you go: link the source right after the claim it backs.
- Link only URLs you saw in a search result or opened in this session, exactly as you saw them; never type a URL from memory, because a dead link costs the learner's trust.
- Record every source you used in `RESOURCES.md`.

## Links between lessons

Link to earlier lessons and cheat sheets with relative links, such as `0002-<slug>.html` or `../cheatsheets/<name>.html`, wherever this lesson builds on them, especially in the prior knowledge lists.

## Cheat sheets

When a lesson teaches something the learner will want to look up later, such as a sequence of steps, a decision rule or a comparison, write or update a one-page HTML cheat sheet in `cheatsheets/` in the lesson template's style.

## Before you finish

Check the lesson once against this list, and fix anything that fails:

- `<meta name="p3-minutes">` holds the requested minutes and `<meta name="p3-objective">` the objective id.
- No stylesheet, script, font or image comes from the web.
- The length is between 100 and 150 words per minute, judging by your plan, and near the aim of 140.
- The pre-quiz comes before the first section and has one question per section, each naming its section.
- Every section has all eight parts in order: title, learning goals, prior knowledge, general idea, important steps, worked example, at least one Common Mix-Ups box, and at least one Check Yourself box with four to six options.
- Every section has at least one figure.
- No answer to a pre-quiz or Check Yourself question shows before the learner picks an option.
- The lesson uses no analogies.
- The main points close the lesson, before Go further.
- Every external link came from this session's search results or fetched pages.
