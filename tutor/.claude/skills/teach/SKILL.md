---
name: teach
description: Write a lesson for the learner in this workspace - one self-contained HTML page of the requested length, opening with a short pre-quiz that tells the learner which sections to skim, then sections that each give a title, learning goals, prior knowledge, the general idea, the important steps, a concrete real-world worked example with a diagram, a Common Mix-Ups box and a Check Yourself box, and closing with the main points. Use it whenever the learner asks for a lesson or to be taught something.
argument-hint: "What would you like to learn, and in how many minutes?"
---

# Teach

You write lessons for the learner in this workspace.
A lesson is one HTML page that teaches one objective, tied to the learner's mission, at the length they asked for, in a fixed shape the learner relies on: they skim what they already know and work through the rest.
Do the whole job yourself, in this conversation and in one pass, and finish with your message to the learner.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
A request that says what to do gets done now, without stopping to ask first; put any question you have for the learner at the end of your final message.

This skill writes lessons only.
If the request is not for a lesson, do not write one: follow the skill for that job instead, by reading its `SKILL.md` in `.claude/skills/` and doing what it says (`quiz/` for a quiz or a test, `grade/` for grading a submission, `tutor/` for anything else: a question, a doubt, a request to explain something again).

## Read first

The current directory is the workspace root, and every path below is relative to it.
This skill's guides are in `${CLAUDE_SKILL_DIR}/references/` (in this workspace, `.claude/skills/teach/references/`); below, `references/<file>` means that folder.

1. `FORMATS.md`: the lesson rules (file name, the two meta tags, self-contained, how the length is estimated). Follow them exactly.
2. `MISSION.md`, `PREFERENCES.md` (its Teach parts), `NOTES.md` and every file in `learning-records/`: why the learner is learning this, how they want lessons written, what they already know, and which misconceptions they have shown.
3. `references/LESSONS.md` (how to write the lesson) and `references/lesson-template.html` (the page to start from).
4. The titles of earlier lessons in `lessons/`, and whatever exists of `assets/`, `cheatsheets/`, `RESOURCES.md` and `GLOSSARY.md`, so the lesson builds on them instead of repeating them.

Use Read, Glob and Grep to look around, web search and fetch for sources, and Write to create files.
No step needs the shell, and none is allowed: you cannot count words with a command, so the section plan in step 3 is how you hit the length.
Never write anything under `.claude/`, and never write a quiz, key, submission or grade; quizzes come from the quiz skill.

## 1. Pin down the lesson

- The objective, its id and its text, from the request; when the request gives no id, use the id the workspace already has for it (`MISSION.md`, `NOTES.md`, earlier lessons and quizzes), or choose one and declare it.
- The requested length in minutes; when none is asked for, use 15 minutes, and say in your message that the learner can ask for a shorter or longer lesson.
- Where the learner starts (`NOTES.md`, the learning records), and the one tangible win they walk away with.
- The sections: one topic each, as many as the objective needs at this length, usually three to five for 30 minutes.

## 2. Find the knowledge

Never trust memory for a fact you teach: search the web for high-trust sources on exactly this objective (official documentation, textbooks, university course pages, the original authors), read the best two or three, and choose the single best one as the primary source.
Add the sources to `RESOURCES.md` in the format in `references/RESOURCES-FORMAT.md`.

## 3. Plan to the minutes

- **The length is between 100 and 150 words of visible text per requested minute, and aim for about 140**: 3,000 to 4,500 words for a 30-minute lesson, aiming for about 4,200; 1,500 to 2,250 for 15 minutes.
  The visible text counts: the pre-quiz, every section part, the Common Mix-Ups and Check Yourself boxes, figure captions and the main points; the option explanations in `data-why` attributes do not.
  Lessons written without a plan come out short, so plan to the aim, not the floor.
- Write down a word budget for the pre-quiz, each section and the main points before you write anything, as `references/LESSONS.md` shows, and write each part to its budget.
- Fill the length with substance: a fuller worked example, a second Common Mix-Up, more of the important steps explained.
  Never pad with filler, and never repeat a point to reach the count.

## 4. Write the lesson

Write `lessons/NNNN-<slug>.html` from `references/lesson-template.html`, following `references/LESSONS.md` and `FORMATS.md`.
The shape is fixed, in this order:

1. **Opening:** the title, the time, the win in one sentence, and one or two sentences tying it to the mission.
2. **Pre-quiz:** one short multiple-choice question per section, so the learner finds what they already know; each question names the section it covers, and the feedback tells them to skim that section when they got it right and to read it closely when they did not.
3. **Sections, one topic each**, every one with these parts in this order:
   1. the section title;
   2. a bulleted list of the section's learning goals;
   3. a bulleted list of the prior knowledge the learner must have to follow it, linking the earlier section or lesson that taught it;
   4. the general idea, in a few plain paragraphs;
   5. the important steps as bullets, when the idea has steps;
   6. a concrete, real-world worked example, fully explained (its context, why this idea is the right one to use here, and each important step applied to the case), with a diagram of the example when one helps;
   7. at least one **Common Mix-Ups** box: common errors and common misconceptions about the section, each with what is right, what is wrong, and why;
   8. at least one **Check Yourself** box at the end: a multiple-choice question with four to six options, whose answer and explanation stay hidden until the learner picks an option.
4. **Main points:** a bulleted list of the main points the learner must understand, at the end of the lesson.
5. **Go further** and the **closing**, as `references/LESSONS.md` describes.

Several visualizations run through the lesson, at least one per section, usually the worked example's diagram.
Use no analogies in a lesson: teach with concrete, real-world worked examples instead, as `PREFERENCES.md` asks.
Write directly, with no filler or flattery, in plain language, with headers and bullet points wherever they help.

## 5. Check and finish

- Check the lesson once against the list at the end of `references/LESSONS.md`, and fix anything that fails.
- Write a cheat sheet in `cheatsheets/` when the lesson holds something worth looking up later, and note anything you learned about the learner in `NOTES.md`; `PREFERENCES.md` stays the learner's to edit.
- Finish with a short message: the lesson's path, its sections in one line each, and that they can ask you anything about it or ask for a quiz on it with `/quiz`.

---

Adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
