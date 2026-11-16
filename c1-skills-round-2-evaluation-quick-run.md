# Thoughts about c1-skills-round-1

This file is evaluating Claude's output which can be found at *work/p3-tutor/bench/runs/_live/20261112-050736-agent-architecture-m30-r1*

## Thoughts about the quiz 

I answered the questions before looking at the answer key.

Quiz Questions: *work/p3-tutor/bench/runs/_live/20261112-050736-agent-architecture-m30-r1/quiz/outputs/quizzes/0002.json*
Claude's Answers: *work/p3-tutor/bench/runs/_live/20261112-050736-agent-architecture-m30-r1/quiz/outputs/keys/0002.json*

### Question 1

In one or two sentences, explain the difference between a workflow and an agent in how the order of steps gets decided when a request runs.

#### My Answer

When using an agent, the agent decided the order of steps which also means that the order of steps can change between different runs. When using a workflow, the program that you write determines the order of steps which also means that the order of steps never changes between different runs. 

#### Claude's Answer Key

In a workflow, the developer's code fixes the steps and their order in advance; in an agent, the model decides at run time which step or tool comes next and when to stop.

Full credit needs both sides: the code or developer fixes the path in a workflow, and the model chooses the next step in an agent. Naming only one side is partial. Answers that say an agent is more complex, uses tools, makes more model calls or is smarter, while a workflow is simple, show M10: the difference is who owns the control flow, not complexity or capability. Answers that say a workflow uses no model show M8; a workflow can call the model many times, but the code sets the order.

#### Quiz Notes

I like this question. I feel like it ensures that the student understands the differences between workflows and agents.

### Question 2

Your team prototypes a request handler. Step 1: Python code calls the model once to label a student's message as 'manual question', 'booking' or 'other'. Step 2: Python code uses an if/elif on that label to run either a manual-search prompt or a booking prompt, and returns that reply. The code never calls the model again after step 2. How should this design be described?

- a) An agent, because a model call decides which branch of the program runs
- b) An agent, because it makes more than one call to the language model
- c) A workflow, because the code fixes the possible paths and their order, and the model only produces the label
- d) An agent, because it handles two kinds of request, which takes flexible decision-making
- e) A workflow, but only because it is small; adding more branches would turn it into an agent
- f) A workflow, because it has no tool calls and a design needs tools to be an agent

#### My Answer

C

#### Claude's Answer Key

C

The developer's code fixes both the possible paths and their order; the model only produces output (a label) that the code then reads. Control flow stays with the code, so this is a workflow (the pattern is called routing). a: tempting because the model's output picks the branch, but the branches and order are still written in advance and the model never chooses actions or loops (M9). b: the number of model calls does not decide it; a workflow can chain many calls (M9). d: handling several kinds of request is done here with a fixed if/elif, not model-chosen steps (M10). e: size is not the criterion; a large workflow with many branches is still a workflow as long as code fixes the paths (M10). f: right label, wrong reason; tools are not what separates the two, since workflows can call tools too and an agent is defined by the model choosing the steps (M8).

#### Quiz Notes

I like this question as well. I feel like it covers most of the options a student might think of and ensure that they know not just the difference between a workflow and an agent but also the why.

### Question 3

The makerspace assistant's booking path always does the same thing: read the machine and date from the student's message, check the calendar for that slot, book it if it is free, and otherwise report that the slot is taken. Should this path be built as an agent or as a fixed workflow? Name your choice and give the reason.

#### My Answer

Fixed workflow because the steps depend on each other. You need the machine and date to check the calendar. You need the calandar in order to book the machine. Since they depend on each other and the assistant should always do the same thing, the order should be fixed. You can achieve that with a workflow.

#### Claude's Answer Key

A fixed workflow, because the steps and their order are known in advance and the same every time, so code can run them directly without the model deciding what to do next.

The right choice is a workflow, and the reason must be that the steps and their order are known ahead of time. Mentioning that this is cheaper (fewer model calls) or more predictable is a good addition. Workflow with no reason, or with a reason that is not about the steps being predictable, is partial. Choosing an agent because it is more capable or flexible shows M7: more capability only pays when the path cannot be known in advance. Choosing an agent because the booking path touches several tools shows M8/M10: the number of tools does not matter, the predictability of the path does.

#### Quiz Notes

I think this question is good. It asks about workflow vs agent but also the reason why.

### Question 4

Your team's first draft of the manual-answering feature is fixed Python code: it searches the manuals once with the student's question, passes the top three pages to the model, and returns the model's answer. A student asks, "My 3D print keeps warping, what should I try?" The useful page only turns up if the model reads the first results and searches again with a different term, but the code never allows a second search. In one or two sentences, state what in the design causes this failure and what change fixes it.

#### My Answer

The assistant is using a fixed workflow but that may not be the right choice here. If the assistant used an agent instead, the model would be able to use the search feature as many times as it needs to find the information. Though, step limits should always be used when letting an agent loop on its own.

#### Claude's Answer Key

The code, not the model, owns the control flow and fixes a single search; the fix is to let the model decide whether and what to search next, in a loop with a stopping limit, so that part becomes an agent.

Full credit names the cause (the steps are fixed by the code, one search, although this task's steps depend on what each result shows) and the fix (the model chooses the next step, in an agent loop; a step limit is a good addition). Only saying 'use an agent' without saying what failed is partial. Blaming the model, the search quality or the number of pages, or proposing more pages or a bigger model, misses the point that no amount of better output can fix a path the code never lets the model extend. Proposing a longer fixed sequence, such as always searching three times, still fixes the path in advance, and it spends calls on easy questions (M7 in reverse: it keeps the workflow where the steps cannot be predicted).

#### Quiz Notes

I like this question because it is a real world example.

### Question 5

A teammate proposes building the nightly job as an agent: find every student whose safety training expires within 7 days, then email each one the renewal link. The same four steps run every night. The teammate argues, "An agent can do everything a workflow can, so it is the safer choice." Given our small model budget, give two concrete costs of choosing an agent for this job.

#### My Answer

Higher token cost because the model has to reason through things itself and it might do some extra things which it was not required to do or the agent keeps looping on one step which can cause every high token consumption.
Certain steps or checks may be skipped if the agent does not feel that they are needed at that moment. That could result in the wrong people getting the link.

#### Claude's Answer Key

Two of: more model calls and tokens per run, because the model re-reads its growing context to decide steps that are already known; less predictable behaviour, because the model might skip a student, repeat an email or loop, so it needs a step limit and is harder to test.

Two distinct costs are needed, and good ones are: cost (extra model calls or tokens spent on deciding steps that are already known) and reliability (the run varies, so a step could be skipped, repeated or looped; testing is harder). Only one cost is partial. A vague 'it is slower' or 'it is more complex' without a link to the model deciding steps is weak. Agreeing with the teammate shows M7: an agent can do what a workflow does, but at higher cost and lower predictability, and the extra capability buys nothing when the steps never change.

#### Quiz Notes

I love this question because it makes you think and it is a real world example.

### Question 6

The assistant gets three kinds of request: (1) booking a machine for a stated date and time; (2) open troubleshooting questions, such as why a print is warping, where the number of manual searches needed cannot be known in advance; (3) "am I certified for the CNC router?", which needs one training-record lookup. Which design is best if the criterion is the lowest model cost that still handles all three kinds correctly?

- a) One agent loop with all the tools, used for every kind of request
- b) A fixed workflow for all three, with a set number of manual searches for troubleshooting
- c) Agents for booking and certification checks, and a fixed workflow for troubleshooting
- d) Fixed workflows for booking and certification checks, and an agent only for troubleshooting
- e) A fixed workflow for booking only, and an agent for troubleshooting and certification checks

#### My Answer

D

#### Claude's Answer Key

D

Booking and the single certification lookup have steps known in advance, so fixed workflows handle them with the fewest model calls; only troubleshooting needs the model to choose how many searches to run, so only that part earns an agent's extra cost. a: tempting for simplicity and capability, but it pays loop cost on requests whose steps never vary (M7). b: cheapest to run but fails the criterion of handling all three correctly, since a set number of searches cannot suit open questions (M10: assuming a fixed path can always replace model-chosen steps). c: inverts the rule, giving the agent to predictable tasks and fixing the path of the unpredictable one (M7). e: right about booking and troubleshooting but sends the single-lookup certification check through an agent, which costs more and gains nothing; the choice depends on whether the path is predictable, not on which tool is used.

#### Quiz Notes

I think this is a good question. It makes the student think a real world example and determining how to chose agent vs workflow.

### Final Thoughts about the quiz

- I liked that the questions covered more topics like retrieval, how context is saved, and what context is saved.
- I liked that there was only one multiple choice question. I liked this quiz so much better because I felt like I had to think and each question more and it challenged me even though I have seen this content probably like 10 times. 
- I also like that there were more options for the multiple choice question.
- I also felt like the questions focused more on real-world scenarios and the application of the content.
