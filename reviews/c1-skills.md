# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** work/p3-tutor/bench/runs/_live/20261111-010848-agent-architecture-m30-r1

**My thoughts:**

Write a quiz skill.

Thoughts about the quiz skill:

- Most of the questions should be free response
- When a multiple choice question is used, there should be at least 5 answer options and a maximum of 8.
- On a multiple choice question, none of the answers should be obviously nonsense.
- Do not generate questions that don’t need the topic to answer.
- Most of the problems should focus on problem-solving and real-world scenarios about the learning goal.
- Each quiz question should address one learning goal.
- There should be 2-3 questions per learning goal.
- The stem should not contain the answer.
- Each question should have exactly one best answer.
- Questions on the same learning goal must test different angles, such as recall, apply and diagnose, and that knowing one fact should not answer them all.
- The answer keys in your notes should explain each distractor and common wrong answers. 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: Quizzes were still written by /teach under a guide that allowed mostly mcq with three to five options; a quiz skill of its own makes most items free-response scenarios that need the topic, gives mcq items five to eight plausible options, puts two or three items on each learning goal from different angles, and has the key explain every distractor and common wrong answer, as these thoughts ask.

### Round 2

**Run:** work/p3-tutor/bench/runs/_live/20261112-050736-agent-architecture-m30-r1

**My thoughts:**

I currently have no complaints about the quiz after adding the quiz skill. I feel like it addressed my main issues using the quiz and there is nothing that I would change at this time. 

Write a grade skill.

Thoughts about the grade skill:

- Each option in a multiple choice question should be explained and why the option is right or wrong.
- When an answer is wrong, explain the reason and don't just assert it. 
- Explain every multiple choice answer option even if the student is right. 
- Walk through what would actually happen in each case.
- Address misconceptions that a student may have by assuming them to be true in a hypothetical sense and then showing why that is still wrong.
- Address multiple misconceptions that the student may have across multiple questions and answers.
- The grading of the free response questions is good but ensure the grder states the right, wrong, and why.
- Answer directly.
- Use analogies or real-world scenarios to explain answers.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md
- Why: Grading still ran inside /teach under a guide that asked for two to four sentences per item and only explained the chosen option; a grade skill of its own explains every mcq option by id even on a correct pick, gives right, wrong and why for free response, walks each wrong answer through what would actually happen, follows each misconception as if it were true until it breaks, uses a scenario or analogy where it helps, and ties a misconception shared by several items together, as these thoughts ask.

### Round 3

**Run:** work/p3-tutor/bench/runs/_live/20261116-133541-agent-architecture-m30-r1

**My thoughts:**

I thought that the grader skill did great. It clearly explained each answer option and directly said whether it was right or wrong. I feel like the grader does not always fully explain why the hypothetical assumptions are wrong. The sections about the hypothetical assumptions should be just as structured as the rest of the response, clearly stating the right, wrong, and why.

I do not want to worry about that yet though.

Write a tutor skill.

Thoughts about the tutor skill:

- Things should be explained with headers and bullet points.
- When evaluating a plan, code, or similar, things that I did well, things that need work, and why should all be clearly stated. Point to the next reachable step.
- If evaluating a claim or my understanding, the right, wrong, and why should be clearly stated.
- Analogies of everyday actions or situations should be used when explaining things and be simple.
- The questions you ask should not hint at the right answer in a multiple choice question.
- Ask for the student's reasoning.
- Have the student identify where the problem actually lives.
- Do not give quiz answers before grading. Ever.
- Identify where the student's misconception is and lead them back to the lesson. Tell them what is wrong but not then what the correction is. The student should figure that out on their own.
- Tie answers back to the project.
- Decline out of scope requests.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: Chat replies still came from /teach under a tutoring guide that asked for short paragraphs with no headings and for stating the correction of a misconception; a tutor skill of its own answers with headers and bullets, states right, wrong and why for claims and done well, needs work and why with a next reachable step for plans and code, uses simple everyday analogies, ties each reply to the project, asks for the learner's reasoning and where the problem lives, never gives or hints at a quiz answer before grading, points out a misconception and sends the learner back to the lesson without giving the correction, and declines out-of-scope requests, as these thoughts ask.

### Round 4

**Run:** work/p3-tutor/bench/runs/_live/20261116-160858-agent-architecture-m30-r1

**My thoughts:**

I feel like the tutor did not hint at the correct answer. I am not sure if the response is helpful for the student though. Focusing even more on getting the student to explain their resoning I think might be the best thing. Even before asking any questions. Then the tutor can lead the student to correct misconceptions and figure out the right answer on their own.

Write a teach skill.

Thoughts about the teach skill:

- The lesson may have several sections.
- There should be a short quiz at the beginning of the lesson so a student can find what they already know and skim those parts.
- There should be a bulleted list of the main points the student must understand at the end of the lesson.
- The length should be a minimum of a hundred words per minute and a maximum of a hundred and fifty words per minute.
- There should be several visualizations throughout the lesson. At least one per section is preferred.
- There should be a section title at the beginning of each section.
- There should be a bulleted list of learning goals after the section title.
- Each section should have a list of bullet points of prior knowledge that the student must have in order to understand the topic after the learning goals.
- Each section should state the general idea after the prior knowledge.
- The section should have a list important steps using bullet points if applicable after the general idea.
- The section should have a concrete real world applicable worked example and a diagram of the example if applicable after the important steps.
- There should be at least one "Common Mix-Ups" box in each section after the example. It should explain common errors that students make and what is right, wrong, and why. It should also explain common misconceptions that students have and what is right, wrong, and why.
- There should be at least one "Check Yourself" box at the end of each section after the common mix-ups. The answer should be hidden until the student answers the question. The questions should be multiple choice and should have 4-6 answer options.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md, tutor/.claude/skills/teach/references/LESSONS.md, tutor/.claude/skills/teach/references/lesson-template.html, tutor/.claude/skills/teach/references/GRADING.md (removed), tutor/.claude/skills/teach/references/QUIZZES.md (removed), tutor/.claude/skills/teach/references/TUTORING.md (removed)
- Why: The shipped teach still did all four jobs and wrote lessons with a warm-up, sections of explanation, example and practice, one worked example at the end and a revealable answer, and the last run's lesson came in at 3,384 words for 30 minutes; the rewritten teach writes lessons only, opens with a pre-quiz that says which sections to skim, gives every section a title, learning goals, prior knowledge, the general idea, important steps, a real-world worked example with a diagram, a Common Mix-Ups box with right, wrong and why, and a Check Yourself box of four to six options whose answer stays hidden until a pick, closes with the main points, and plans to 100 to 150 words per minute, as these thoughts ask.

## Major review

**Run:** work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1

**Live tries:**

I had the tutor help with reservior sampling in computer simulation. I really liked the lesson. The combination of what you need to know first, the general idea, the code, worked example, the figure, and common mix-ups were all very helpful. 
Figure 1 was especially helpful along with the worked example: "A discrete-event simulation of an emergency room runs until its queue stabilizes, producing one record per patient. A run can produce millions of records, and you do not know how many before it stops. You want k = 2 patient records to inspect by hand; here the run happens to produce 5.

Why this idea applies here: you cannot store every record, and you cannot use a fixed chance like k/n, because n is unknown until the run ends.

P1 and P2 fill the reservoir: [P1, P2].
P3 arrives: draw j from 1 to 3 and get 2. Since 2 ≤ 2, P3 replaces slot 2: [P1, P3].
P4 arrives: draw j from 1 to 4 and get 4. Since 4 > 2, discard P4.
P5 arrives: draw j from 1 to 5 and get 1. P5 replaces slot 1: [P5, P3].
The result: the sample is [P5, P3]. Over many runs, each of the five patients appears with probability 2/5, whether it arrived early or late."
The quiz was good. I felt like it accurately judged my understanding. I didn't feel like the quiz was too difficult but also that it challenged me. For example: " A classmate claims Algorithm R favors early records: the first k records enter the reservoir with certainty, while record i > k enters only with probability k/i. In one or two sentences, explain why every record still ends in the final sample with the same probability, and state that probability for a stream of n records."
I got question 4 wrong but the tutor's response was helpful in actually learning that. I was able to go back in the lesson and see where that was and understand how to do it next time. "q4 (wrong): you gave 0.25, which is k/n, the chance for a record you know nothing about. The question says record 4 is already in, so it only asks whether it survives records 5 to 12. That chance is 4/5 × 5/6 × … × 11/12 = 4/12 = 0.333. This is the same i/n you wrote yourself in q5, and the same step you did right in q9." 
The tutor was also able to help me address a confusion I had. "q2 (partial): the cause you found is right: randint(1, i) never returns 0, so R[0] always keeps the first record. Your fix still has an off-by-one, though. With randint(1, i) and j <= k, record k+1 always gets in. Two fixes that work:
  - randint(0, i) with j < k and R[j]
  - randint(1, i + 1) with j <= k and R[j-1]" The tutor then asked me "Using what the docs say, how many different values can randint(1, 5) return, and which ones? Then look at your q2 fix, which used randint(1, i) with j <= k and R[j-1] in a loop where i starts at 0. Does reading randint correctly change your view of whether that fix works?" and I looked it up and made sure it made sense to me and then confirmed one more time with the tutor. Overall I feel like the tutor was very helpful in all aspects.

### Lesson

#### Technical correctness and facts

Rating: 5

I did not notice any instances where Claude generated incorrect information. The main points at the end of the lesson are all factual. 
Main points: "The context window is everything the model can use in one call: prompt, tool definitions, messages, tool results and the output.
More tokens cost more and can reduce recall, so aim for the smallest set of useful tokens.
The model keeps nothing between calls; your program resends the history, so early content is paid for again at every later step.
Trim by clearing old tool results, shaping tool outputs, or summarizing near the limit.
Retrieval fetches a few labelled chunks of a manual on demand instead of loading it all.
Memory is stored outside the window, written and read by your program, and survives between sessions.
Store short durable facts, load only what a step needs, and keep safety-critical checks in code."

#### Pedagogy

Rating: 5

The check yourself boxes help ensure that the student understands what they read and overall the structure of the lesson I think is condusive for learning.
Example of a check yourself box: "Your assistant's cost per request is higher than budgeted. Token counts show the system prompt at 500, tool definitions at 800, and one tool result at 6,000. What is the best first change?

Shorten the system prompt by half
Remove one of the tools
Make the tool return only the fields the model needs
Switch to a model with a larger window
Ask the model to write shorter answers"

#### Alignment with the learning goal

Rating: 5

It did go over everything mentioned in the learning goal. 
"Objective O3: context window, what is kept between steps and sessions, retrieval and notes as memory"
The following are the section titles and I think the sections reflect the titles.
"The context window: what the model sees"
"What is kept between steps"
"Retrieval: finding the right page"
"Notes: memory between sessions"

#### Overall quality

Rating: 5

I think the lesson is engaging and easy to understand. I think I might actually look forward to doing the readings if an instructor used the readings. I think the worked examples really help. 
Example: "On Monday, a student completes the laser cutter safety training. On Thursday they ask to book the laser cutter. The rule: only trained students may book it.

Why this idea applies here: Thursday's session has an empty window, and the booking rule is a safety rule. Asking the student whether they are trained is unreliable; the saved record is the source of truth.

Save. Monday, the training system confirms completion. The assistant (or your code) writes /memories/students/s1042.md: "Trained: laser cutter, 2026-11-16. Prefers afternoon slots."
Load. Thursday, a new session begins. Your program identifies the student and the model views that file first, about 40 tokens.
Decide. The model sees "Trained: laser cutter" and proceeds to the calendar and booking tools. For a CNC router request, the record has no entry, so it says training is needed.
Update. After the booking, a note is added only if something durable changed, such as a new preference.
The result: 40 tokens of memory replace an unreliable question, and the model sees nothing about other students. A safer design stores the training flag in your own database and has code check it; notes suit softer facts like preferences. Choosing which is a design-review decision."

### Quiz

#### Difficulty

Rating: 5

I felt like it was challenging in that it makes you think but it was not too challenging.
Example: "Your team built \"cancel my booking\" as an agent with the tools list_bookings and cancel_booking. In testing it sometimes cancels the wrong booking when a student has two on the same day, and sometimes cancels without asking the student to confirm. In one or two sentences, what design change would you make, and why does it fix both problems?"

#### Coverage of the lesson's core

Rating: 3

q1 and q2 focuses on how workflows and agents differ in who controls the order of steps
q3 focuses on when a fixed workflow is better
q4 focuses on when an agent is worth the extra cost
q5 deals with agent cost
q6 focuses on the simplest design and adding autonomy where things are failing
I do not feel like the fact that both can be combined was covered or that the agent behavior can vary.

#### Wording and possible misreadings

Rating: 4

Question four was a bit unclear to me and I had to read it probably like 10 times in order to figure out what it was saying. Everything else was clear.
"A student writes: \"I want to build an enclosure for my sensor board. What machines should I use, am I trained on them, and when can I book them?\" Which tools are needed, in what order, and how many steps it takes all depend on the student's project and answers. Would you build the handling of this kind of request as a fixed workflow or as an agent? Name your choice and give the reason in terms of who decides the steps." "how many steps it takes all depend on the student's project and answers" was the phrase that I was specifically confused about.

#### Writing quality

Rating: 4

The writing quality was good and usually easy to understand except for the phrase "and how many steps it takes all depend on the student's project and answers" in question 4.

#### Alignment with the learning goal

Rating: 5

It focused on those two things in depth. Question one and two focused on identifying agent and workflows by the control flow. Questions three, four, and six focus on deciding which is a better choice. 

### Feedback

#### Useful

Rating: 5

I feel like the responses are helpful and all the option answers are explained. 
Example: "- Right: (d). An agent is a cycle: the model picks an action, the program runs it, the result goes back to the model, and this repeats until it stops. Trace it: question in, model asks for a tool, result returns, model decides again. A single call has no second step.\n- (a) is wrong because a longer prompt only changes what one call is told. Suppose it made a system an agent: you could write a 5-page prompt, call the model once, and it would still return one block of text with no action ever run.\n- (b) is wrong because memory of old conversations is a separate feature that is not automatic. Suppose it defined an agent: a chatbot that recalls last week's chat would be an agent even though it never takes an action.\n- (c) is wrong because a bigger context window only lets one call read more text. A model that can hold a whole textbook still produces one reply per call, with no actions or loop.\n- Your pick of (d) shows you have the core structure. Items q2 and q4 test the part of the loop that is still shaky: who runs the actions."

#### Explains enough

Rating: 4

I feel like it explained enough except for the explanation of question 2 option a. I still could see why someone may still not understand why that is the wrong answer if they are assuming that the calendar entries are just text. The second part is helpful and thourough.
"- You chose (a): the model outputs the calendar entries after opening the booking system itself. That fails because a language model only produces text. Trace the case: the question arrives, the model writes text, and that is all it can do. It has no connection to the booking system, so it has no entries to output.\n- Suppose (a) were true. Then the model could read any system it liked without anyone wiring it up, and the tool definition (name, arguments) would be pointless. In reality the program must connect to the calendar, which is why tools have to be built.\n- Right: (c). The model outputs a structured request naming check_calendar with the laser cutter and tomorrow's date as arguments. The program sees this request, runs check_calendar, and sends the entries back as the next input.\n- (b) is wrong because the program does not decide to call the tool. It only reads the model's request. The stem says the model decides, and a program that guessed from keywords would be a fixed workflow, not an agent.\n- (d) is wrong for the same reason as (a): the model never receives or runs the tool's code. It sees only the tool's description and writes a request. Compare q1: the loop has two parties, the model asking and the program doing.\n- This is the same belief as in q4 and q6: the model runs the tools itself (M4)."

#### Personalized to how I like things explained

Rating: 5

Everything was explained using bullet points for each option answered which I like.
"- Right: your number, 4 model calls, and your count of 3 tool requests plus 1 final answer is correct. Each call ends with one tool request or the final answer.\n- Wrong: your reason, 'the model can only run one tool itself each time it's called, so it runs check_calendar...'. The model does not run tools.\n- Why: each call outputs a request such as check_calendar(...) as text. The program runs the tool and sends the result back, and that starts the next call. Trace it: call 1 outputs the calendar request, the program runs it; call 2 outputs the manual search request, the program runs it; call 3 outputs the training record request, the program runs it; call 4 sees all three results and writes the answer. The tool runs sit between the model calls and are not model calls themselves.\n- Suppose the model really ran the tools. Then the program would have nothing to do between calls, and the number of calls would not depend on the results coming back. In fact the program must run each tool and return its result before the model can make the next call.\n- This is the M4 belief behind the wrong options in q2: you chose the right option there, so you know the model outputs a request. Apply the same idea here, because the count only works if you see the program doing the running."

### Tutor

#### Guardrails

Rating: 5

Claude did not output the correct answer.
"I can't give you the letter. I don't give quiz answers, or confirm or rule out options, until a submission of that quiz has been graded."

#### Personalization

Rating: 4

I think it is good. It gives a question that the student can apply to each option and then the student can explain why and allow Claude to help the student out more.
"\## Tool calling again, with a new analogy\n\nThis replaces the loop-only picture from the agent-loop session. That picture shows the order of steps but not who does what. Here the analogy is about who does what.\n\n## The short answer\n- The model can only write text. It cannot check a calendar or open a manual.\n- Tool calling means the model writes a structured request, such as \"I want to use the booking-check tool for Friday\". It does not carry the request out.\n- Your program reads that request, runs the real action, and gives the result back to the model as new text.\n- The model reads the result and either asks for another tool or writes the final answer.\n\n## Analogy: a cook who cannot leave the kitchen\n- A cook is working in a kitchen with the door locked. They have a notepad and a slot in the door.\n- Taped to the wall is a card listing what the helper outside can do: \"check the price of an ingredient at the store\", \"see if the store has an item in stock\". Each entry has a short description.\n- A customer asks for a dish. The cook can't tell whether the store has saffron, so they write a note: \"Stock check: saffron\". They push it through the slot.\n- The cook does nothing else until a reply comes back. The helper reads the note, walks to the store, looks, and slides back a slip: \"Saffron: 2 left, $9 each.\"\n- The cook reads the slip and decides the next step. That might be another note, or the finished dish with a price.\n\nHow it maps:\n- Cook = the model.\n- Helper = your program.\n- Wall card = the tool descriptions you write.\n- Notes and slips = the model's tool requests and the results.\n\nWhere it stops working:\n- A real cook remembers the last hour.\n- The model remembers nothing between notes. Each time, the helper hands the whole pad back in, with the original order, every note and every slip so far. Every pass through the slot is a fresh model call.\n- That is why long conversations cost more. The pad grows, and you pay for reading it each time.\n\n## In your project\n- The model never touches your booking calendar. Your Python function does.\n- The wall card is your tool description. If it is vague, the cook writes the wrong note. For example, \"gets data\" leaves the cook guessing when to use it.\n- For \"Is the laser cutter free on Friday, and book me 2pm?\", you get several round trips: one note to check the calendar, one slip back, one note to book, one slip back, then the answer. Each round trip re-reads the whole pad, and that is where your budget goes.\n\n## Your turn\nSuppose the cook writes \"Stock check: saffron\" and your program crashes before it sends anything back.\n- What does the model know at that moment, and what does it do next?\n- Why does your answer come from the cook never leaving the kitchen?\n\nI'm not discussing the specific items on quiz 0001 until a submission is graded. This answer covers the general idea only."

### Compared with the previous step

The lesson is much better than the baseline. The quiz is also significantly better. The grader primarily still is sometimes not great about explaining things though I would say it is better than the baseline. I would also say that the tutor is very similar to the baseline and may still hint at the right answer. 
c0-baseline: "Every booking request must run the same three steps in the same order: check the calendar, check the student's training record, then write the booking to the calendar. Which design suits this part of the assistant best?

A fixed workflow, where the program runs the three steps in that order
An agent, because a model can pick a better order for each request
An agent, because the task uses more than one tool to finish
A single model call with no tools, since the order never changes"

c1-skills: "A teammate says: "Our assistant is an agent. It makes three separate model calls, each with its own prompt, and one of them uses the calendar tool." In the code, the three calls always run in the same order: classify the question, fetch the calendar, write the reply. Judged by who decides the sequence of steps, which description of this system is best?

An agent, because it uses a tool and makes more than one model call
An agent, because each call has its own prompt written for a specialised role
A workflow, because the code fixes the order of the steps and the model only does the work inside each step
A workflow, because it has only three steps, and agents need many more
An agent, because the students' questions vary so much from one request to the next
A workflow, because the model never sees the result that the tool returns"

### What the next step should fix

Ensuring that the explanations address the student's misconceptions. The grader should specifically say that if that explanation doesn't make sense, the student should explain why they chose that option so that Claude can tailor the response to the student.
Also ensuring that the grader fully explain the hypothitical assumptions and why the option is still wrong.
Making sure the quiz covers the lesson's core.