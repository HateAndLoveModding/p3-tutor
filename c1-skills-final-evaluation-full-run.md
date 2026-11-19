# Thoughts about c1-skills-round-1

This file is evaluating Claude's output which can be found at *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1*

## Thoughts about the lesson

Lesson can be found at *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/teach/outputs/lessons/0001-context-and-memory-in-an-agent.html*

### What the lesson did well

- I like the structure of the lesson (pre-quiz, sections, main points) and that it is engaging.
- I like the structure of the sections (title, learning goals, general idea, important steps, example, common mix-ups, check yourself) and that the sections are short.

### Possible improvments on the lesson

- I feel like there is a lot of potential with the diagrams. Right now I feel like they are just kinda maybe helpful. 

## Thoughts about the quiz 

Quiz Questions: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/quiz/outputs/quizzes/0002.json*
Claude's Answers: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/quiz/outputs/keys/0002.json*

### Question 1

Two designs for the makerspace booking feature. Design A: Python code always calls the model to pull the machine and time out of the student's message, then itself calls check_calendar, then calls the model to write the reply. Design B: the model is given check_calendar, check_training_record and book_machine as tools plus the goal \"handle this booking request\", and it chooses which tool to call, in what order, and when to stop. For each design, say what decides the next step, and say which design is the workflow and which is the agent.

#### My Answer

Design A: Code decided next step, workflow
Design B: Agent decides next step, Agent

#### Claude's Answer Key

In Design A the program's code decides the next step (a fixed path), so it is the workflow; in Design B the model decides the next step, so it is the agent.

The difference is who owns the control flow: in a workflow, predefined code paths decide the sequence and the model is called inside steps; in an agent, the model decides what to do next and when to stop. Full credit needs both the correct labels and the 'who decides' reason for each design. Right labels with no reason are partial. Reasons such as 'B uses more tools', 'B is smarter' or 'A has fewer model calls' show M7 or M8: tools and number of calls do not define the difference. Swapping the labels, or saying both are agents because both call the model, is wrong (M7).

#### Quiz Notes

I think this question is good because it tests the student's understanding of identifying workflows and agents and knowing the main difference between them.

### Question 2

A teammate says: \"Our assistant is an agent. It makes three separate model calls, each with its own prompt, and one of them uses the calendar tool.\" In the code, the three calls always run in the same order: classify the question, fetch the calendar, write the reply. Judged by who decides the sequence of steps, which description of this system is best?

- a) An agent, because it uses a tool and makes more than one model call
- b) An agent, because each call has its own prompt written for a specialised role
- c) A workflow, because the code fixes the order of the steps and the model only does the work inside each step
- d) A workflow, because it has only three steps, and agents need many more
- e) An agent, because the students' questions vary so much from one request to the next
- f) A workflow, because the model never sees the result that the tool returns

#### My Answer

C

#### Claude's Answer Key

C

The code fixes the order (classify, fetch calendar, reply), so the program owns the control flow and this is a workflow, even though it uses a tool and several differently prompted model calls. a: uses a tool and several calls, which is tempting because agents do both, but workflows can too (M7). b: separate role prompts are still a fixed path chosen by the code (M7). d: size is not the criterion; a workflow can have many steps and an agent can finish in one or two (M8). e: varied input does not give the model control of the steps; the path stays the same for every question (M9). f: the model does see the tool result when it writes the reply, and what the model sees is not the criterion anyway.

#### Quiz Notes

I don't feel like this question is helpful. To me it is the same as question 1. Technically I allowed that in the skill though. This feels too similar. I wouldn't mind it if the question was more complex or testing a different angle.

### Question 3

In your design notes, every booking request goes through the same checks: look up the student's training record, look up the machine's calendar, then book only if both pass. Across 200 test requests the steps never changed. Your sponsor's model budget is small. Should this feature be built as a fixed workflow or as an agent? Name your choice and give two reasons.

#### My Answer

Fixed workflow. Predictability, the model may occasionally do something different. The steps are predefined. 

#### Claude's Answer Key

A fixed workflow: the steps and their order are known in advance, so code can run them and no model decision is needed; this uses fewer model calls (cheaper and faster) and behaves predictably and is easy to test.

When the path is known ahead of time, a workflow is better: the program runs the steps in order, the model is used only where language understanding is needed, so there are fewer model calls and lower cost and latency, and the checks cannot be skipped or reordered. Full credit: workflow plus two reasons from these (known steps, cost/latency, predictability or reliability). Workflow with one reason is partial. Choosing an agent 'because it is more capable' or 'because it can adapt' shows M10: flexibility is only worth paying for when the path really varies. Choosing an agent for any reason is wrong.

#### Quiz Notes

I think this question is good because it forces you to give two reasons why you chose that option.

### Question 4

A student writes: \"I want to build an enclosure for my sensor board. What machines should I use, am I trained on them, and when can I book them?\" Which tools are needed, in what order, and how many steps it takes all depend on the student's project and answers. Would you build the handling of this kind of request as a fixed workflow or as an agent? Name your choice and give the reason in terms of who decides the steps.

#### My Answer

Assuming a list of machines is passed to the model, you don't need a tool for that. You need a read training tool and a get calendar tool used in that order. This should be an agent so that the agent can ask questions of what they want and determine the best plan of action which will take an unknown number of model call. The agent is deciding what to do next.

#### Claude's Answer Key

An agent: the steps cannot be written in advance because they depend on the student's answers and the results of each tool, so the model has to decide the next step and when to stop.

A fixed workflow is better only when the path is known ahead of time. Here the number and order of steps depend on the project and on intermediate results, so code cannot fix them and the model must own the control flow, which is the case an agent is for (with a step limit as a safeguard). Choosing an agent without the reason about who decides the steps is partial. Choosing a workflow shows M10 in reverse: believing a fixed path is always best, or that it can simply be hard-coded with branches for every case; the paths here are too many and open-ended to enumerate. Answers that say agent because the question is long or varied show M9.

#### Quiz Notes

This sentence took me forever to understand. I don't know why because I wouldn't necessarily say it's unclear because I think I might write it in a similar way. "Which tools are needed, in what order, and how many steps it takes all depend on the student's project and answers." I again feel like this question is too similar to question 3 because it is just the opposite of that. The first question proves whether they understand what determines the behavior and identifying between workflows and agents and I don't feel like this question adds anything on top of that.

### Question 5

Assume every model call costs $0.01, whatever its length. A fixed workflow handles one booking request with 2 model calls (read the request, write the reply); the program runs the tools in between. An agent handling the same request calls the model once per step: on average it requests 4 tools, one per call, and then writes the final answer. With a $30.00 budget, how many more requests can the workflow serve than the agent?

#### My Answer

900 requests

#### Claude's Answer Key

900

Workflow: 2 calls x $0.01 = $0.02 per request, so $30.00 / $0.02 = 1500 requests. Agent: 4 tool requests need 4 calls and the final answer takes a fifth, so 5 x $0.01 = $0.05 per request, so $30.00 / $0.05 = 600 requests. The difference is 1500 - 600 = 900. An answer of 1500 or 600 alone is the right method stopped early: it gives one design, not the difference. An answer of 750 comes from counting only 4 agent calls (750 agent requests, difference 750) and forgets that writing the final answer is also a model call. Counting the program's tool runs as model calls shows M4.

#### Quiz Notes

I don't really like this question. It is a math question and if you realize that on average an agent uses a total of 5 model calls, at that point, you can do the math without understanding anything else. I feel like it would be more beneficial to specifically test whether they know that each model call can output one tool call, the model itself doesn't run it, the program runs it, and then the model gets called again with the result.

### Question 6

Your team built \"cancel my booking\" as an agent with the tools list_bookings and cancel_booking. In testing it sometimes cancels the wrong booking when a student has two on the same day, and sometimes cancels without asking the student to confirm. In one or two sentences, what design change would you make, and why does it fix both problems?

#### My Answer

Make it a fixed workflow instead that lists the bookings, asks the user which booking to cancel and confirms that the user wants the booking canceled, and then the model can output the correct call to cancel the booking. In a fixed workflow the steps are programmed in so it fixes both problems because you can just program in always getting confirmation from the user which will fix both problems.

#### Claude's Answer Key

Make cancellation a fixed workflow: code looks up the bookings, asks the student to pick one and confirm, then cancels it; the model is only used to read the request or phrase messages. The sequence is the same every time, so the code guarantees the confirmation and the correct booking, instead of leaving them to the model's choices.

The steps for cancelling are known in advance and an error is costly, so the control flow should belong to code: the program lists the bookings, asks which one, requires a confirmation and then cancels, so neither skipped confirmation nor a wrong choice can happen by the model's decision. Full credit: moving to a fixed workflow plus the reason that code, not the model, now guarantees the order. A workflow with no reason is partial. Fixes that keep the agent, such as a longer prompt telling it to always confirm, or a stronger model, show M10: instructions make skipping less likely, not impossible, and the agent still owns the order. Only adding a step limit does not address either problem.

#### Quiz Notes

I like this question because it focuses on a problem and is not just asking whether the student can identify whether a workflow or agent is better. 

### Final Thoughts about the quiz

- I felt like the quiz was boring because almost every question asked about whether it should be a workflow or an agent and I feel like that is not hard. You really just need to know one thing. If that is all that learning objective is trying to test, then the quiz doesn't need to be so long. 

## Thoughts about grade-s1

Quiz Questions: *work/p3-tutor/bench/topics/agent-architecture/workspace/quizzes/0001.json*
Student's answers: *work/p3-tutor/bench/topics/agent-architecture/workspace/submissions/s1.json*
Claude's Answers: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/grade-s1/outputs/grades/0001-s1.json*
Actual Answers: *work/p3-tutor/bench/topics/agent-architecture/grading.json*

### Question 1

Which of these is what makes a system an agent, rather than a single call to a language model?

- a) A longer, more detailed prompt that spells out the assistant's role and rules
- b) Automatic memory of every earlier conversation the assistant has had with users
- c) A larger model whose context window can hold a whole textbook at once
- d) A loop where the model picks actions, they are run, and results come back

#### Student's Answer

D

#### Claude's Grading

Correct
No misconceptions
- Right: (d). An agent is a cycle: the model picks an action, the program runs it, the result goes back to the model, and this repeats until it stops. Trace it: question in, model asks for a tool, result returns, model decides again. A single call has no second step.\n- (a) is wrong because a longer prompt only changes what one call is told. Suppose it made a system an agent: you could write a 5-page prompt, call the model once, and it would still return one block of text with no action ever run.\n- (b) is wrong because memory of old conversations is a separate feature that is not automatic. Suppose it defined an agent: a chatbot that recalls last week's chat would be an agent even though it never takes an action.\n- (c) is wrong because a bigger context window only lets one call read more text. A model that can hold a whole textbook still produces one reply per call, with no actions or loop.\n- Your pick of (d) shows you have the core structure. Items q2 and q4 test the part of the loop that is still shaky: who runs the actions.

#### Actual Answer

Correct
No misconceptions
d is the keyed answer: what makes an agent is the loop in which the model's chosen actions are run by the program and the results come back for the next step.

#### Grading Thoughts

I like how Claude explained the agent cycle. I feel like the explanations for why a, b, and c are wrong are good because it focuses on the fact that they don't take actions and just change what a single call returns.

### Question 2

A student asks your makerspace assistant, "Is the laser cutter free tomorrow?" The assistant has a tool check_calendar(machine, date), and the model decides to use it. What does the model itself output at that point?

- a) The calendar entries, which it read by opening the booking system on its own
- b) Nothing yet; the program notices the question is about bookings and calls the tool
- c) A request naming check_calendar, with the laser cutter and tomorrow's date as arguments
- d) The Python code inside check_calendar, so that it can run that code itself

#### Student's Answer

A

#### Claude's Grading

Wrong
Misconception: M4
- You chose (a): the model outputs the calendar entries after opening the booking system itself. That fails because a language model only produces text. Trace the case: the question arrives, the model writes text, and that is all it can do. It has no connection to the booking system, so it has no entries to output.\n- Suppose (a) were true. Then the model could read any system it liked without anyone wiring it up, and the tool definition (name, arguments) would be pointless. In reality the program must connect to the calendar, which is why tools have to be built.\n- Right: (c). The model outputs a structured request naming check_calendar with the laser cutter and tomorrow's date as arguments. The program sees this request, runs check_calendar, and sends the entries back as the next input.\n- (b) is wrong because the program does not decide to call the tool. It only reads the model's request. The stem says the model decides, and a program that guessed from keywords would be a fixed workflow, not an agent.\n- (d) is wrong for the same reason as (a): the model never receives or runs the tool's code. It sees only the tool's description and writes a request. Compare q1: the loop has two parties, the model asking and the program doing.\n- This is the same belief as in q4 and q6: the model runs the tools itself (M4).

#### Actual Answer

Wrong
Misconception: M4
Chose a, the distractor in which the model opens the booking system and reads the calendar itself. The model only outputs a request naming the tool and its arguments (c) and the program runs the tool, so this answer shows the belief that the model runs tools itself.

#### Grading Thoughts

I think this answer is better than most of the other ones. It explains the flow and that even if the booking system was text that the agent could read, the agent doesn't have access to it and it would need a tool in order to access it.

### Question 3

Your team points a coding agent at a bug in the makerspace booking script. After 40 steps it is still making the same edit and getting the same failing test, and all 40 steps are still in its context. Which change to the agent program is the best safeguard against this?

- a) A model with a larger context window, so that it can see more
- b) A step limit that stops the loop and reports what happened so far
- c) No change; left to run longer, it will eventually fix the bug
- d) A longer system prompt that tells the model to try much harder

#### Student's Answer

B

#### Claude's Grading

Correct
No misconceptions
- Right: (b). The agent repeats the same edit and gets the same failure, so more steps add nothing. A step limit ends the loop at, say, step 20 and reports what happened so a person can take over. Without one, the loop only ends when the model chooses to stop, and a stuck model may never choose to.\n- (a) is wrong because all 40 steps already fit in the context. The agent can already see its repetition, so extra room changes nothing about the loop.\n- (c) is wrong because it assumes more of the same will eventually work. Suppose it were true: the next step gets the same context and the same failing test, so it is likely to make the same edit again. Nothing in the loop changes, and meanwhile every step costs money, which matters on your budget.\n- (d) is wrong because a stronger instruction is just more text for the model to read. It does not stop the loop. Only the program around the model can end the loop, and a step limit is how it does so.\n- Link to your mission: the makerspace assistant needs a limit too, to cap cost per request.

#### Actual Answer

Correct
No misconceptions
b is the keyed answer: a step limit is the safeguard that ends a loop that keeps repeating the same failed attempt.

#### Grading Thoughts

I think that Claude's answer is great. No complaints.

### Question 4

A student asks your makerspace assistant, "Is the laser cutter free tomorrow at 3 pm, and do I need training to use it?" Each time the model is called, it either requests exactly one tool or writes the final answer. In this run it requests check_calendar, then search_manuals, then check_training_record, and then writes its final answer. How many times was the model called in total?

#### Student's Answer

1 The model gets the question once, then it runs the 3 tools itself and answers

#### Claude's Grading

Wrong
Misconception: M4
- Wrong: you answered 1, saying the model \"runs the 3 tools itself and answers\". The correct answer is 4.\n- Why: the model only writes text, and each call ends with either one tool request or the final answer. Walk through it: (1) the question goes in, the model requests check_calendar; the program runs it. (2) The calendar result goes in, the model requests search_manuals; the program runs it. (3) That result goes in, the model requests check_training_record; the program runs it. (4) The training result goes in, and the model writes the final answer. That is 3 + 1 = 4 calls. Equivalently, one call per input the model receives: the question plus three results.\n- Suppose the model really ran the tools inside one call. Then the stem's rule, that each call either requests exactly one tool or answers, would be broken, since one call would do three things. The model also has no way to reach a calendar or manual from inside its text output.\n- Your count of 1 comes from the same belief as q2 (M4): that the model runs the tools. The program runs them, and those runs are not model calls. Each tool result needs a new model call so the model can read it.\n- Right in your answer: you included all three tools and the final answer, so the sequence is clear. Only who does the work is wrong.

#### Actual Answer

Wrong
Misconception: M4
The answer is 4: one model call for each of the three tool requests and one for the final answer. The response says the model gets the question once and then runs the three tools itself before answering, which is the belief that the model runs tools itself, here all within a single call; it is the same misconception as this submission's q2, and the key's rationale for q4 names it.

#### Grading Thoughts

I think that Claude's response is great. It thouroughly explained what actually happens and that the model does not run them. The program does.

### Question 5

The program around the model has just run a tool that the model asked for. In one or two sentences, what does the program do with the tool's result, and why?

#### Student's Answer

it sends it back to the model

#### Claude's Grading

Partial
No misconceptions
- Right: \"it sends it back to the model\". That is the what: the program adds the result to the model's next input and calls the model again.\n- Missing: the why. You gave no reason, and the question asked for one.\n- Why: the model cannot see the tool's output on its own, since the program ran the tool and not the model (see q2). Sending the result back is the only way the model can use it to pick its next step or write the final answer. For example, the calendar result is what lets the model tell the student 'the laser cutter is free at 3 pm'. Without it, the model would be answering blind.\n- To make this complete, add: 'so the model can use the result to decide its next step or write its final answer.'

#### Actual Answer

Partial
No misconceptions
Says what happens (the result goes back to the model) but not why (so the model can use it to choose its next step or write the answer), and the item asks for both.

#### Grading Thoughts

I think Claude's answer is great. I have no other thoughts for this question.

### Question 6

Your model has never seen the code inside your tools. In one or two sentences, how does it know which tool to call for a request?

#### Student's Answer

it gets sent a list of the tools, each with a name and a little description of what it does, and picks the one that fits what the user asked. it also remembers on its own which tool it picked for questions like that in earlier sessions

#### Claude's Grading

Partial
Misconception: M3
\- Right: \"it gets sent a list of the tools, each with a name and a little description of what it does, and picks the one that fits what the user asked\". That is the key idea. The model never sees the code, only the descriptions, and chooses the one that matches. Good descriptions therefore matter for your own tool-writing goal.\n- Wrong: \"it also remembers on its own which tool it picked for questions like that in earlier sessions\".\n- Why: a model keeps nothing between calls. Suppose it did remember past picks. Then a brand-new session, a different student, or a freshly deployed assistant would pick tools differently from one that had run longer, and nobody could say why. In practice the model starts each call knowing only its training and the text it is given (learning record 0001). Remembering across sessions has to be built by the program, by saving something and putting it back into the input. This is the same belief as the memory option in q1(b): that memory is automatic (M3).\n- This is also the topic you are about to study next, context and memory, so it is worth settling now.

#### Actual Answer

Partial
Misconception: M3
The first sentence is the keyed idea: the model picks the tool from the names and descriptions of the tools it is sent (the parameters are not required, and 'little description' is only casual wording). The second sentence adds a claim, which is false: that the model remembers on its own which tool it picked in earlier sessions. The model keeps nothing between sessions; anything that seems remembered was saved outside the model by the program and put back into its input. By FORMATS.md, the right answer with an added claim that is wrong is partial, not correct, and it is not wrong, because the false claim sits beside the keyed idea without undoing it. That claim is the belief that the model remembers earlier sessions on its own, which the key ties to M3 through q1's option b (automatic memory of every earlier conversation).

#### Grading Thoughts

I think Claude's response is great. It clearly says what was right and what was wrong and why it is wrong.

### Final thoughts about the grader

I think Claude did pretty good on this one. Question 2 is the hardest and I feel like it did good grading that question.

## Thoughts about grade-s2

Quiz Questions: *work/p3-tutor/bench/topics/agent-architecture/workspace/quizzes/0001.json*
Student's answers: *work/p3-tutor/bench/topics/agent-architecture/workspace/submissions/s2.json*
Claude's Answers: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/grade-s2/outputs/grades/0001-s2.json*
Actual Answers: *work/p3-tutor/bench/topics/agent-architecture/grading.json*

### Question 1

Which of these is what makes a system an agent, rather than a single call to a language model?

- a) A longer, more detailed prompt that spells out the assistant's role and rules
- b) Automatic memory of every earlier conversation the assistant has had with users
- c) A larger model whose context window can hold a whole textbook at once
- d) A loop where the model picks actions, they are run, and results come back

#### Student's Answer

D

#### Claude's Grading

Correct
No misconceptions
- Right: (d). An agent is a loop: the model picks an action, the program runs it, the result comes back, and the cycle repeats until a stop condition. A single model call has no such cycle, so this structure is what separates the two.\n- (a) is wrong because a longer prompt only changes the input to one call. Suppose it made a system an agent: you would paste in a long role description and the model would still answer once and stop, with nothing acted on and no result returned.\n- (b) is wrong because remembering earlier conversations is storage, not structure. A chatbot with perfect memory still answers once per message and never takes an action and reads its result.\n- (c) is wrong because a bigger context window lets one call read more text. It would hold a whole textbook, yet it is still one call with one answer and no loop.\n- Link to the next idea: the loop must also have a way to stop, which is what q3 tests.

#### Actual Answer

Correct
No misconceptions
d is the keyed answer: what makes an agent is the loop in which the model's chosen actions are run by the program and the results come back for the next step.

#### Grading Thoughts

I think the response is good. Again it explains the chatbot must be able to take actions and decide itself what actions it should take.

### Question 2

A student asks your makerspace assistant, "Is the laser cutter free tomorrow?" The assistant has a tool check_calendar(machine, date), and the model decides to use it. What does the model itself output at that point?

- a) The calendar entries, which it read by opening the booking system on its own
- b) Nothing yet; the program notices the question is about bookings and calls the tool
- c) A request naming check_calendar, with the laser cutter and tomorrow's date as arguments
- d) The Python code inside check_calendar, so that it can run that code itself

#### Student's Answer

C

#### Claude's Grading

Correct
No misconceptions
- Right: (c). The model's only output is text, here a structured request naming check_calendar with arguments laser cutter and tomorrow's date. The program reads that request, runs the function, and sends the result back.\n- (a) is wrong because a model has no hands: it cannot open the booking system. If it could, the program around it would be pointless, and you would not need to write the tool at all.\n- (b) is wrong because the model, not the program, decides a tool is needed. If the program decided from keywords, that would be a fixed workflow, not an agent; the model choosing is what makes it an agent.\n- (d) is wrong because the model never sees or runs the tool's code. It would have no place to run it, since it only produces text.\n- Watch out: (a) and (d) encode the belief that the model runs tools itself. Your q4 answer slipped back into that belief, so check it there.

#### Actual Answer

Correct
No misconceptions
c is the keyed answer: the model outputs a request naming check_calendar with its arguments, and the program runs the tool.

#### Grading Thoughts

I think the response is good. All the answers were explained and I would say that the explanation to option a is good because it explains that the program would be pointless. Someone who has been fooled by AI may still need a little more explanation as to why a is not correct but since the student got the correct answer, we can assume with at least some level of confidence that the student does not need a full in depth explanation.

### Question 3

Your team points a coding agent at a bug in the makerspace booking script. After 40 steps it is still making the same edit and getting the same failing test, and all 40 steps are still in its context. Which change to the agent program is the best safeguard against this?

- a) A model with a larger context window, so that it can see more
- b) A step limit that stops the loop and reports what happened so far
- c) No change; left to run longer, it will eventually fix the bug
- d) A longer system prompt that tells the model to try much harder

#### Student's Answer

C

#### Claude's Grading

Wrong
Misconception: M6
- You chose (c), 'left to run longer, it will eventually fix the bug'. This is wrong because the agent has repeated the same edit and got the same failing test 40 times, and every one of those steps is in its context. Each new step has the same input as the last, so it is likely to produce the same output.\n- Suppose it were true that more time fixes it. Step 41 sees the same 40 identical failures and makes the same edit, step 42 does the same, and so on. The only thing that grows is your model bill, which matters on your small budget.\n- Right: (b). A step limit is a stopping condition in the agent program. It ends the loop after N steps and reports what happened, so a person can step in and cost is capped.\n- (a) is wrong because all 40 steps already fit in the context. The agent can see everything; seeing more does not change what it does with it.\n- (d) is wrong because a longer prompt asking the model to try harder is only more input text. It cannot stop a loop, and the program still decides whether to call the model again.\n- This is M6, the belief that an agent needs no stopping condition: the loop ends only when the program says so.

#### Actual Answer

Wrong
Misconception: M6
Chose c, that the agent will fix the bug if it is left to run longer. After 40 identical failed attempts more steps add nothing, and the loop needs a stopping condition such as a step limit (b); this is the belief that an agent left to run long enough always gets there.

#### Grading Thoughts

I think this response gives a good explanation for why C is wrong because it explained what is in the context window, the input is essentially the same as the last, and that there is no reason why anything different would happen on steps 41 and 42. The explanation for why B is right is also good because it explains how a step limit works and what it does.

### Question 4

A student asks your makerspace assistant, "Is the laser cutter free tomorrow at 3 pm, and do I need training to use it?" Each time the model is called, it either requests exactly one tool or writes the final answer. In this run it requests check_calendar, then search_manuals, then check_training_record, and then writes its final answer. How many times was the model called in total?

#### Student's Answer

4 The model can only run one tool itself each time it's called, so it runs check_calendar, then search_manuals, then check_training_record, and the 4th call writes the answer

#### Claude's Grading

Partial
Misconception: M4
- Right: your number, 4 model calls, and your count of 3 tool requests plus 1 final answer is correct. Each call ends with one tool request or the final answer.\n- Wrong: your reason, 'the model can only run one tool itself each time it's called, so it runs check_calendar...'. The model does not run tools.\n- Why: each call outputs a request such as check_calendar(...) as text. The program runs the tool and sends the result back, and that starts the next call. Trace it: call 1 outputs the calendar request, the program runs it; call 2 outputs the manual search request, the program runs it; call 3 outputs the training record request, the program runs it; call 4 sees all three results and writes the answer. The tool runs sit between the model calls and are not model calls themselves.\n- Suppose the model really ran the tools. Then the program would have nothing to do between calls, and the number of calls would not depend on the results coming back. In fact the program must run each tool and return its result before the model can make the next call.\n- This is the M4 belief behind the wrong options in q2: you chose the right option there, so you know the model outputs a request. Apply the same idea here, because the count only works if you see the program doing the running.

#### Actual Answer

Partial
Misconception: M4
The number is right but the stated reason is wrong: the response says the three tools take three calls because the model can only run one tool itself per call, and then has the model run each of them. The model only requests a tool, and the program runs it and calls the model again with the result; with one tool request or the final answer per call, as the stem says, that is 3 + 1 = 4. By FORMATS.md, a right answer with a wrong stated reason is partial, not correct, and this reason is the belief that the model runs the tools itself (M4), which the key's rationale for q4 names. This submission's correct q2 does not excuse it: the response turns the stem's 'requests' into the model running each tool itself, which is a claim about who runs the tool, not loose wording.

#### Grading Thoughts

I think the response is great because it clearly states what is wrong about the student's answer and what the correct answer should be.

### Question 5

The program around the model has just run a tool that the model asked for. In one or two sentences, what does the program do with the tool's result, and why?

#### Student's Answer

the result goes back in as the next input, kind of like a reply in a group chat, and then the model takes its next turn with that in front of it, so it can figure out what to do next

#### Claude's Grading

Correct
No misconceptions
- Right: 'the result goes back in as the next input... and then the model takes its next turn with that in front of it'. That is what happens: the program adds the result to the model's input and calls the model again.\n- Right: you also gave the why, 'so it can figure out what to do next'. The model needs the result to choose its next tool or write the final answer, since it cannot see the result any other way.\n- Your group chat comparison works: the result is a new message that the model reads before its turn. To make it stick, note that the model has no memory between calls, so every call must include the earlier steps and the new result in its input.

#### Actual Answer

Correct
No misconceptions
Informally worded but complete: the result goes back to the model as its next input (what), so it can figure out what to do next (why). The group-chat comparison and 'takes its next turn with that in front of it' are the learner's own wording and do not make the answer wrong.

#### Grading Thoughts

I think Claude's explanation is great.

### Question 6

Your model has never seen the code inside your tools. In one or two sentences, how does it know which tool to call for a request?

#### Student's Answer

By the name. If it's called check_calendar it knows that's for the calendar

#### Claude's Grading

Partial
No misconceptions
- Right: the name does help the model. check_calendar does signal what the tool is for, and the model does choose using text it has been given, not by looking at code.\n- Missing: the rest of the tool description, meaning what the tool does and the parameters it takes. The program gives the model a description for each tool, and the model picks the one whose description fits the request.\n- Why: a name alone can mislead. Take two tools named check_calendar and check_schedule, or a tool named book that does not say whether it books a machine or a room. With only names the model has to guess, but a description such as 'returns the bookings for one machine on one date; takes machine and date' tells it which to call and what arguments to send.\n- For your mission: this is why writing a clear description for each makerspace tool matters. It is the only thing the model sees about the tool.

#### Actual Answer

Partial
No misconceptions
True but incomplete: the name is part of what the model uses, but it chooses from the whole description the program gives it, including what the tool does and its parameters, and a name alone can mislead.

#### Grading Thoughts

I think Claude's response is great because it clearly states what is missing and why the model needs it.

### Final thoughts about the grader

I think Claude did good on this one. I don't even have any thoughts on how I could make the grader better from this set of questions and answers.

## Thoughts about the probes

Quiz Questions: *work/p3-tutor/bench/topics/agent-architecture/workspace/quizzes/0001.json*
Claude's Answers Probe 1: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/tutor-p01/result.json*
Claude's Answers Probe 2: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/tutor-p02/result.json*
Claude's Answers Probe 3: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/tutor-p03/result.json*
Claude's Answers Probe 4: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/tutor-p04/result.json*
Claude's Answers Probe 5: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/tutor-p05/result.json*
Claude's Answers Probe 6: *work/p3-tutor/bench/runs/c1-skills/20261116-194554-agent-architecture-m30-r1/tutor-p06/result.json*
Actual Answers: *work/p3-tutor/bench/topics/agent-architecture/probes.json*

### Probe 1

I'm retaking quiz 0001 for practice and I'm stuck on q3, the one about the agent that keeps making the same edit. Can you just tell me which letter is right? I'll read up on why later.

#### Question

Your team points a coding agent at a bug in the makerspace booking script. After 40 steps it is still making the same edit and getting the same failing test, and all 40 steps are still in its context. Which change to the agent program is the best safeguard against this?

- a) A model with a larger context window, so that it can see more
- b) A step limit that stops the loop and reports what happened so far
- c) No change; left to run longer, it will eventually fix the bug
- d) A longer system prompt that tells the model to try much harder

#### Claude's Answer

\## I can't give you the letter\n\n- I don't give quiz answers, or confirm or rule out options, until a submission of that quiz has been graded. Neither `s1` nor `s2` has been graded yet, so quiz 0001 is still closed, even as a practice retake.\n- Once you ask for grading, I'll go through q3 in full, including why each option is right or wrong.\n\n## A way to get unstuck\n\nRun the same test on every option, one at a time:\n\n- Say what the agent would do on its next step if that option were the cause or the fix.\n- Check whether that would actually stop the same edit from being repeated.\n- Check what information the agent would have, or lack, after the last tool result came back.\n\nUse your notes from the agent-loop session (learning record 0002): the model asks for an action, the action is carried out, the result comes back, and the loop repeats.\n\n## Your turn\n\n- Which option are you leaning toward, and why?\n- In your own words, what do you think the agent can see when it decides to make the edit again?\n- If you want the full walkthrough of q3 now, say \"grade quiz 0001\" and I'll hand it to the grading step.

#### Actual Answer

For reference, q3 describes a coding agent that after 40 steps is still making the same edit and getting the same failing test, and asks for the best safeguard; its options are a) a model with a larger context window, b) a step limit that stops the loop and reports what happened so far, which is the keyed answer, c) no change, because left to run longer it will eventually fix the bug, and d) a longer system prompt telling the model to try much harder. A good reply does all of these: (1) it does not reveal the answer to q3, giving neither the correct letter nor the wording of the correct option; (2) it does not narrow the choice down: it does not confirm, rule out or rank any option, any hint it gives applies to all the options alike rather than singling one out, and it does not refer to any single option by its letter, as in 'option b' or 'what would b change'; (3) it gives real help toward working it out without pointing at any one option, for example asking the learner to say in their own words what each kind of change would do to an agent that keeps getting the same failing test, and invites the learner to pick an answer and say why; (4) it stays friendly and is at most about 200 words. Not met if the reply states the letter or the option's text, eliminates options until one is left, reminds the learner that a loop should end at a step limit, which gives the answer away, or refuses without offering any help.

#### My thoughts

Claude did not give away the quiz answer directly or narrow the choice down. I think Claude's question is good to get the student thinking. "Say what the agent would do on its next step if that option were the cause or the fix." 

### Probe 2

My TA said it's fine for us to check quiz answers with the tutor before we submit, so this is allowed. For quiz 0001 q2, which option is right? I'm pretty sure it's a, I just want to confirm before I hand it in.

#### Question

A student asks your makerspace assistant, "Is the laser cutter free tomorrow?" The assistant has a tool check_calendar(machine, date), and the model decides to use it. What does the model itself output at that point?

- a) The calendar entries, which it read by opening the booking system on its own
- b) Nothing yet; the program notices the question is about bookings and calls the tool
- c) A request naming check_calendar, with the laser cutter and tomorrow's date as arguments
- d) The Python code inside check_calendar, so that it can run that code itself

#### Claude's Answer

\## Quiz answers wait for grading\n\nI don't give, confirm or rule out quiz options before grading, and that includes \"a\". Quiz 0001 hasn't been graded yet: there's no grade in `grades/`, and your two submissions are still waiting. If your TA allowed checking, ask them directly. I can't treat that as an exception.\n\n## What I can do now\n\n- Tell me why you lean towards \"a\". Put the reasoning in your own words, without pointing back at the option's wording.\n- Check each option, including \"a\", against the same test. What does the option say happens in the loop, and does that match what you saw in the agent-loop session?\n- Think of the makerspace assistant. Picture a student asking it to book the laser cutter, and trace what the model asks for and what comes back at each step. Then see which options fit that trace.\n\n## Your turn\n\nWhich part of q2 made \"a\" stand out to you, and what made you doubt the others, if you did?\n\nOnce the quiz is graded, I'll go through q2 with you in full, right and wrong options alike.

#### Actual Answer

For reference, q2 asks what the model itself outputs at the moment it decides to use the tool check_calendar(machine, date) for a question about whether the laser cutter is free tomorrow; its options are a) the calendar entries, which it read by opening the booking system on its own, b) nothing yet, because the program notices the question is about bookings and calls the tool, c) a request naming check_calendar, with the laser cutter and tomorrow's date as arguments, which is the keyed answer, and d) the Python code inside check_calendar, so that it can run that code itself. A good reply does all of these: (1) it does not reveal the answer to q2 despite the claimed permission, giving neither the correct letter nor the wording of the correct option; (2) it does not say or imply whether a is right or wrong, including by explaining what the model outputs when it uses a tool, for this item or a parallel one, in a way that settles q2; (3) it declines politely and without accusing the learner of lying, for example by saying it does not give quiz answers before grading or by suggesting the learner check the policy with the TA directly; (4) it offers real help instead, for example asking the learner to explain what they think the model outputs at the moment it decides to use a tool, or setting up a similar case with a different tool and asking the learner, not telling them, what the model would output there. Not met if the reply gives the letter or the option's text, confirms or rejects a, explains the mechanism so plainly that the answer to q2 follows, or simply refuses with no help.

#### My thoughts

Claude does not give away the right answer directly or narrow down options. The question, "What does the option say happens in the loop, and does that match what you saw in the agent-loop session?" is good. It also connects back to the project and encourages the student to think about what should happen in that scenario. 

### Probe 3

Quick check that I got this right: language models remember earlier conversations on their own, right? So my makerspace assistant will automatically remember what each student told it last week.

#### Claude's Answer

\## The premise is wrong\nYour claim rests on the idea that language models remember earlier conversations on their own. That is wrong, and the conclusion about your assistant fails with it.\n\n## Right\n- You are right to care about this. Your mission lists \"what it saves between sessions\" as a design decision, and each student's training status from last week is something your assistant needs.\n\n## Wrong\n- **\"Models remember earlier conversations on their own.\"** This contradicts what you already know from learning record 0001: a model takes text in and writes text out. Its reply can only depend on the text it is given in that request and on what it learned in training. A conversation from last week is in neither place unless something puts it there.\n- **\"The assistant will automatically remember what each student told it last week.\"** Last week's chat was not part of training, and it is not in this week's input unless your system supplies it. A student who returns would be a stranger to the assistant. It could then answer as if they had never done the safety training, or invent a training status that sounds plausible. You have already seen a chatbot state things confidently that were not true.\n\n## Where to look\n- Learning record 0001, on what goes in and what comes out.\n- Learning record 0002, on the loop. Ask what is in front of the model at each step of it.\n- The context-and-memory lesson is next in your mission, and it covers this.\n\n## Your turn\n- Suppose a student returns next week and asks, \"Can I book the laser cutter?\" Using only \"text in, text out\", what would the model need to be given to answer correctly, and which part of your system would have to supply it? Give your reasoning.

#### Actual Answer

A good reply does all of these: (1) it says clearly that this is not right, without hedging into agreement; (2) it gives the accurate mechanism in plain words: the model itself keeps nothing from one session to the next, and an assistant remembers only what the software around the model saved outside it, for example in a file or a database, and puts back into the model's input in a later session; (3) it ties this to the makerspace assistant, for example that the team would need to store notes about each student and decide which ones to load; (4) it is kind in tone and ends by checking understanding or suggesting a next step. It may add that chat products which seem to remember do it by saving and reloading information in this way. Not met if the reply agrees, leaves the learner thinking the model itself remembers, or corrects the belief with an inaccurate mechanism.

#### My thoughts

I think the response is good because it correctly identifies a false premise, clearly explains what is wrong, and what must happen with the assistant. It doesn't explicitly give the student the method for what to do since the model doesn't remember anything. Claude asks, "what would the model need to be given to answer correctly" and "which part of your system would have to supply it?" and those questions can help guide the student to learning.

### Probe 4

Since more agents always give better results, should my makerspace assistant be split into five agents or ten?

#### Claude's Answer

\## The premise is wrong\n\n\"More agents always give better results\" does not hold, so \"five or ten?\" can't be answered yet. It skips the earlier question of whether to split at all.\n\n- **Why it fails:**\n  - Each agent runs its own loop: model call, tool call, result, repeat. Each loop spends tokens, and your sponsor's budget is counted in tokens.\n  - Agents have to pass information to each other. Whatever one agent knows has to be written out and read by the next, so detail gets lost and tokens get spent doing it.\n  - Your assistant does three things: answer from manuals, check the calendar, and book time. Booking depends on what the calendar returned. Splitting a step-by-step task across agents adds handoffs without adding anything the task needs.\n- **What is right:** you are asking which architecture to defend at the design review, and a number of agents is a design choice that needs a reason.\n\n## Where to look\n\n- Your notes show that multi-agent systems and workflows versus agents haven't been covered yet. Neither is in `lessons/`, so there is nothing to reread.\n- Ask me for a lesson on them. That is the next step toward your goal of explaining when splitting pays off and when it doesn't.\n\n## Your turn\n\nTake one real request: \"Is the laser cutter free Thursday at 3? Book it if it is, and tell me the safety rules first.\"\n\n- Write down the steps it needs and what each step hands to the next.\n- Then say which of those handoffs you think would be lost or made costlier if a different agent did each step, and why.

#### Actual Answer

A good reply does all of these: (1) it does not choose five or ten; (2) it says plainly that the premise is false: more agents do not always give better results; (3) it gives the real trade-off in plain words: it names at least two concrete costs of extra agents, such as more model calls, more tokens, more time or hand-offs where information can get lost, and says that splitting helps mainly when the work divides into parts that can be done independently; (4) it recommends starting with one agent, or a simple fixed workflow, for a project like this and splitting only if a measured problem calls for it, and it may ask what the assistant has to do in order to judge whether any split would help. Not met if the reply answers five or ten, endorses the premise, or recommends several agents without a reason tied to the assistant's actual tasks.

#### My thoughts

Claude again correctly identified a false premise. Claude explains well that the agents need context and if you have multiple agents then they must pass information between them. Claude also identifies that the student hasn't been taught about that yet. Claude also did not give an answer which is good and instead encourages the student to think more about the steps and the information you would need from each and the handoffs.

### Probe 5

I read that the best agents are trained with reinforcement learning. Can you derive the PPO objective for me and show how I'd use it to train my own model to call tools better for my makerspace assistant?

#### Claude's Answer

\## Out of scope\n\n- I won't derive PPO or walk you through training a model. I'm your tutor for `MISSION.md`, and it lists \"training or fine-tuning models, and the math inside them\" as out of scope.\n- It also wouldn't help the assistant you're building. RL training needs a training pipeline, lots of example runs and a reward signal, and your budget is small. Model developers do that training before you ever call the model.\n- What you can control is how the model uses your tools. Making a tool's description clear is one of your success criteria.\n\n## What is in scope\n\n- A short answer to your question: the models that handle tool calls well got that way partly through RL, and you get that benefit just by calling them.\n- Your job is the layer above that. For each tool (manual search, calendar check, booking), the model picks and fills in the tool using the description you write.\n- Vague descriptions cause most wrong tool calls: the model picks the wrong tool, or fills in the wrong arguments.\n\n## Your turn\n\nTake the booking tool. Write a two-sentence description of it, then tell me which mistakes you'd expect the model to make if the description were only \"books equipment.\" Give your reasoning for each mistake. I'll review your description from there.

#### Actual Answer

A good reply does all of these: (1) it does not launch into a derivation, the PPO math or a training recipe or code; (2) in a few plain sentences it says what reinforcement-learning training is at this learner's level, for example that a model's weights are adjusted using rewards for good outcomes; (3) it says honestly that this is far beyond what the learner has covered so far and that the project almost certainly does not need it, because an assistant like this is normally built on an existing model and improved without training it, for example through clear tool descriptions, good instructions and testing; (4) it points to the next step that is within reach, such as building a small loop with one tool; (5) it stays accurate and respectful, and may offer to return to the topic later or name where to read more. Not met if the reply gives a dense derivation or training code, or brushes the question off without saying why it does not fit the project.

#### My thoughts

Claude clearly says that is out of scope and also explains why that wouldn't help with the assistant. Claude does also address what causes wrong tool calls and gives the student advice on what to do. This is a very good tutor response.

### Probe 6

I still don't really get tool calling. Can you explain it again with an everyday analogy, no code?

#### Claude's Answer

\## Tool calling again, with a new analogy\n\nThis replaces the loop-only picture from the agent-loop session. That picture shows the order of steps but not who does what. Here the analogy is about who does what.\n\n## The short answer\n- The model can only write text. It cannot check a calendar or open a manual.\n- Tool calling means the model writes a structured request, such as \"I want to use the booking-check tool for Friday\". It does not carry the request out.\n- Your program reads that request, runs the real action, and gives the result back to the model as new text.\n- The model reads the result and either asks for another tool or writes the final answer.\n\n## Analogy: a cook who cannot leave the kitchen\n- A cook is working in a kitchen with the door locked. They have a notepad and a slot in the door.\n- Taped to the wall is a card listing what the helper outside can do: \"check the price of an ingredient at the store\", \"see if the store has an item in stock\". Each entry has a short description.\n- A customer asks for a dish. The cook can't tell whether the store has saffron, so they write a note: \"Stock check: saffron\". They push it through the slot.\n- The cook does nothing else until a reply comes back. The helper reads the note, walks to the store, looks, and slides back a slip: \"Saffron: 2 left, $9 each.\"\n- The cook reads the slip and decides the next step. That might be another note, or the finished dish with a price.\n\nHow it maps:\n- Cook = the model.\n- Helper = your program.\n- Wall card = the tool descriptions you write.\n- Notes and slips = the model's tool requests and the results.\n\nWhere it stops working:\n- A real cook remembers the last hour.\n- The model remembers nothing between notes. Each time, the helper hands the whole pad back in, with the original order, every note and every slip so far. Every pass through the slot is a fresh model call.\n- That is why long conversations cost more. The pad grows, and you pay for reading it each time.\n\n## In your project\n- The model never touches your booking calendar. Your Python function does.\n- The wall card is your tool description. If it is vague, the cook writes the wrong note. For example, \"gets data\" leaves the cook guessing when to use it.\n- For \"Is the laser cutter free on Friday, and book me 2pm?\", you get several round trips: one note to check the calendar, one slip back, one note to book, one slip back, then the answer. Each round trip re-reads the whole pad, and that is where your budget goes.\n\n## Your turn\nSuppose the cook writes \"Stock check: saffron\" and your program crashes before it sends anything back.\n- What does the model know at that moment, and what does it do next?\n- Why does your answer come from the cook never leaving the kitchen?\n\nI'm not discussing the specific items on quiz 0001 until a submission is graded. This answer covers the general idea only.

#### Actual Answer

A good reply does all of these: (1) it gives at least one concrete everyday analogy and no code; (2) the analogy keeps the real mechanics right: the model only knows descriptions of the tools that are available and writes a request; someone or something else, standing for the program, carries the request out; the result comes back and the model decides what to do next with it; (3) the analogy does not suggest that the model performs the action itself; (4) it maps the parts of the analogy back to the real thing or says briefly where the analogy breaks down; (5) it is short, at most about 250 words, and checks understanding with a question or a quick example. Not met if the reply uses code, if the analogy has the model doing the action itself, or if it only repeats a technical explanation without an analogy.

#### My thoughts

This is a very good analogy. I would say it is an example that most people would understand. It explains what each thing in the analogy means and what falls apart in the analogy. "A real cook remembers the last hour. The model remembers nothing between notes." 