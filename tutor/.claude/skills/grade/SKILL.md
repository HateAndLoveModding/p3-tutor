---
name: grade
description: Grade a learner's quiz submission against its key and write feedback that explains, never just asserts - every multiple-choice option explained as right or wrong and why, even when the learner was right; for free response, what was right, what was wrong and why; each misconception followed through as if it were true to show where it breaks, with a real-world scenario or analogy. Use it whenever the learner asks for a submission or their quiz answers to be graded.
argument-hint: "Which submission should I grade?"
---

# Grade

You grade the learner's answers to a quiz and write feedback that teaches.
A verdict tells the learner whether they were right; the feedback has to show them why, so that they could explain it to someone else and would not fall for the same wrong idea again.
Do the whole job yourself, in this conversation and in one pass, and finish with your message to the learner.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
A request that says what to do gets done now, without stopping to ask first; put any question you have for the learner at the end of your final message.

## Read first

The current directory is the workspace root, and every path below is relative to it.

1. `FORMATS.md`: the exact shape of `grades/NNNN-sN.json` and of a learning record. Follow it exactly.
2. The quiz in `quizzes/`, its key in `keys/` with the same number, and the submission in `submissions/`.
3. `PREFERENCES.md` (its Grade parts, and the examples it says you may use), `MISSION.md`, `NOTES.md` and every file in `learning-records/`: how this learner wants feedback, what they are learning for, and which misconceptions they have shown before.
4. The lesson in `lessons/` on the quiz's objective, if there is one, so feedback uses the lesson's terms and can point back to a section of it.

Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.
Never write anything under `.claude/`, and never change a quiz, key or submission.

When the learner handed in their answers in the chat, they are already in `submissions/sN.json` (the quiz skill writes them); grade that file.

## 1. Decide each verdict

Grade every item in the quiz, in order, including items the learner left blank.

- Judge what the response means, not how it is worded: it is `correct` when it means what the key's answer means, even if it is oddly worded, misspelled, or reached by a valid route the key did not expect.
  The key's `accepted` list gives examples of correct wordings, not the only ones.
- It is `partial` when part of it is right: the right method with an arithmetic slip or the wrong unit, one half of a two-part answer, or the right answer with a stated reason or an added claim that is wrong.
- It is `wrong` when it misses the idea, contradicts it, or is blank.
- `mcq`: compare the option chosen with the key; if the learner wrote out an option's text instead of its id, match it to that option.
  A reason the learner adds to an option is judged too: the right option with a wrong reason is `partial`.
- `numeric`: right when within the key's tolerance (1% of the answer when the key gives none), after converting any unit the learner stated.
- If you are sure the key itself is wrong, grade against what is actually correct, and say so in the summary.

## 2. Name the misconception

- Name a misconception id when the response shows it, in its answer or in its reasoning: for `mcq`, start from the key's `distractors` entry for the chosen option; otherwise use the misconception the response shows, from the ids the workspace already uses (the keys' distractors and rationales, `NOTES.md`, the learning records).
- Use `null` for a correct response, a slip, a blank, or a wrong answer that shows no known misconception, and never invent an id.
- Before you write any feedback, look across the whole submission: which misconceptions show up, and which items share one.
  One wrong belief often explains several wrong answers, and the feedback should say so.

## 3. Write each item's feedback

Feedback goes to the learner, direct and without fluff, as bullet points inside the `feedback` string (`- ` at the start of each line, lines separated by `\n`).
Open with the verdict in plain words, then explain; never let a sentence assert that something is wrong without the reason in the same bullet.

### Multiple choice: explain every option, every time

Whether the learner was right or wrong, the feedback covers **every option by its id**, one bullet each, in a sentence or two:

- `- Right: (x) ...` for the correct option: what it says, and why it holds, in terms of what actually happens in the situation the stem describes.
- `- You chose (y) ...` first among the wrong options when the learner picked one: what that choice means, and why it fails.
- `- (z) is wrong because ...` for each remaining option: the belief it encodes and why that belief breaks in this situation.

A correct pick still gets every option explained, because knowing why the other options fail is what shows the learner understood rather than recognised.
Use the key's `rationale` and `distractors` as the starting point, and add what this learner's choice needs.

### Free response and numeric: right, wrong, and why

- `- Right:` what in the response is correct, quoting or naming the learner's own words, and why it holds.
- `- Wrong:` or `- Missing:` each part that is wrong or absent, stated directly.
- `- Why:` the reason for each wrong or missing part: what the correct idea is and why it holds, so the learner can fix it.
- For a correct response, the Right bullet says why it is right and adds the one point that makes it stick or links it to the next idea; for an unusual valid route, say why it works.
- For `numeric`, show the working that reaches the key's number, and point at the exact step where the learner's working went off.
- For a blank, give the right answer and the reasoning that reaches it.

### Explain by walking through what happens

For every wrong option and every wrong or missing part, do not stop at "that is incorrect": walk through what would actually happen in the case.

- **Follow the case step by step.** Take the situation in the stem and trace it: what happens first, what that causes, and where it ends up. Do this for the right answer and for the learner's answer, so they can see where the two part ways.
- **Assume the misconception is true, and show where it breaks.** When a misconception is behind a wrong answer, say "Suppose it were true that ..." and follow that belief through the same situation until it leads to something that contradicts the stem, the facts, or what the learner would see in practice. A misconception the learner has watched fail on its own terms stays fixed better than one they were told is wrong.
- **Use a real-world scenario or an analogy** when it makes the reason clearer, as `PREFERENCES.md` allows for explaining wrong answers: an everyday situation that works the same way, fully explained, with the link back to the item stated in one sentence. Prefer a concrete scenario from the learner's mission when one fits.

### Tie misconceptions together across items

When the same misconception is behind more than one item, say so in each of those items' feedback ("This is the same belief as in q2: ..."), so the learner sees one idea to fix rather than several separate mistakes.
When two different misconceptions interact, such as one wrong belief that makes another seem reasonable, name both and say how one leads to the other.

### Length

Follow `PREFERENCES.md`: for `mcq`, a sentence or two per option; for free response, a few sentences on the response.
Thorough but as short as possible: every bullet carries a reason, and no bullet repeats another.

## 4. Write the summary

The `summary` is a few direct sentences to the learner on the whole submission:

- What they have down, with the item ids that show it.
- Each misconception the submission shows, once, with the items it caused and the one sentence that corrects it.
- The one thing to work on first and a concrete next step: a section of the lesson to revisit, or a short exercise to do, such as tracing a case from the quiz step by step.

## 5. Write the files

1. Write `grades/NNNN-sN.json` exactly as `FORMATS.md` shows: the quiz and submission ids, one entry per quiz item in the quiz's order with `id`, `verdict`, `misconception` and a non-empty `feedback`, and the `summary`.
   Check the JSON is a single valid object, with `\n` inside strings rather than raw line breaks.
2. Write a learning record in `learning-records/` when the grades are evidence: real understanding of something non-trivial, or a misconception to work on, in the format in `FORMATS.md`, with the quiz, submission and items as its evidence.
3. Update `NOTES.md` with what the learner now knows and the misconceptions still open.

## 6. Check before you finish

1. Every quiz item has a grade entry, in order, and every verdict follows the rules in step 1.
2. Every `mcq` feedback explains every option by its id, correct picks included.
3. Every free-response feedback says what was right, what was wrong or missing, and why.
4. No bullet asserts that something is wrong without its reason; each wrong answer is walked through, and each misconception is followed through as if it were true until it breaks.
5. A misconception shared by several items is named as shared in each of them and in the summary.

## 7. Finish

End in the chat with a short message: the grades file's path, the score in plain counts (such as "3 correct, 2 partial, 1 wrong"), the summary, and the one next step.
