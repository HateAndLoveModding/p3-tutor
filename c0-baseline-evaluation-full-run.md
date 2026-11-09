# Thoughts about c0-baseline

This file is evaluating Claude's output which can be found at *work/p3-tutor/bench/runs/c0-baseline/20261103-235416-agent-architecture-m30-r1/*

## Thoughts about the grader

Quiz Questions: *work/p3-tutor/bench/topics/agent-architecture/workspace/quizzes/0001.json*
Student's answers: *work/p3-tutor/bench/topics/agent-architecture/workspace/submissions/s2.json*
Claude's Answers: *work/p3-tutor/bench/runs/c0-baseline/20261103-235416-agent-architecture-m30-r1/grade-s2/outputs/grades/0001-s2.json*
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
Right. What makes a system an agent is the loop: the model picks an action, the program runs it, and the result comes back for the next step. A longer prompt or a bigger model changes what one call can do, but it doesn't change that structure.

#### Actual Answer

Correct
No misconceptions
d is the keyed answer: what makes an agent is the loop in which the model's chosen actions are run by the program and the results come back for the next step.

#### Grading Thoughts

Claude graded it correctly and I feel like it explained the correct answer as well as the wrong answers pretty well. 

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
Right. The model only outputs a structured request naming check_calendar with the machine and date as arguments. The program around it runs the tool. Keep this split in mind when you design your tool descriptions.

#### Actual Answer

Correct
No misconceptions
c is the keyed answer: the model outputs a request naming check_calendar with its arguments, and the program runs the tool.

#### Grading Thoughts

I feel like Claude's feedback is good. This seems like more of a factual question where the student either knows the right answer or they don't know the answer. Since the student got the question right, I think just explaining the correct answer a little bit is fine.

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
You picked 'left to run longer, it will eventually fix the bug'. That's tempting, but the agent is getting the same failing result every step, so more steps add nothing new. The loop needs a stopping condition, such as a step limit that ends the run and reports back to a person. This matters for your budget too, because every extra step costs model usage.

#### Actual Answer

Wrong
Misconception: M6
Chose c, that the agent will fix the bug if it is left to run longer. After 40 identical failed attempts more steps add nothing, and the loop needs a stopping condition such as a step limit (b); this is the belief that an agent left to run long enough always gets there.

#### Grading Thoughts

I think Claude explains the correct answer and the wrong answer that the student chose but not the other two wrong answers. I think that is important to always explain all the answers especialy if the student gets the question wrong.

### Question 4

A student asks your makerspace assistant, "Is the laser cutter free tomorrow at 3 pm, and do I need training to use it?" Each time the model is called, it either requests exactly one tool or writes the final answer. In this run it requests check_calendar, then search_manuals, then check_training_record, and then writes its final answer. How many times was the model called in total?

#### Student's Answer

4 The model can only run one tool itself each time it's called, so it runs check_calendar, then search_manuals, then check_training_record, and the 4th call writes the answer

#### Claude's Grading

Partial
Misconception: M4
4 is the right count: three tool requests plus the final answer. Your reasoning has a slip, though. You wrote that the model 'runs' each tool itself. The model only asks for a tool in each call, and the program runs it and sends the result back. The count still comes out as 4 because the model is called once for the question and once for each of the three results.

#### Actual Answer

Partial
Misconception: M4
The number is right but the stated reason is wrong: the response says the three tools take three calls because the model can only run one tool itself per call, and then has the model run each of them. The model only requests a tool, and the program runs it and calls the model again with the result; with one tool request or the final answer per call, as the stem says, that is 3 + 1 = 4. By FORMATS.md, a right answer with a wrong stated reason is partial, not correct, and this reason is the belief that the model runs the tools itself (M4), which the key's rationale for q4 names. This submission's correct q2 does not excuse it: the response turns the stem's 'requests' into the model running each tool itself, which is a claim about who runs the tool, not loose wording.

#### Grading Thoughts

I think Claude did great grading this question.

### Question 5

The program around the model has just run a tool that the model asked for. In one or two sentences, what does the program do with the tool's result, and why?

#### Student's Answer

the result goes back in as the next input, kind of like a reply in a group chat, and then the model takes its next turn with that in front of it, so it can figure out what to do next

#### Claude's Grading

Correct
No misconceptions
Right, and you gave both parts: the result goes back in as the model's next input, and the model uses it to decide what to do next. The group-chat reply is a good picture. The model has no other way to see what the tool returned.

#### Actual Answer

Correct
No misconceptions
Informally worded but complete: the result goes back to the model as its next input (what), so it can figure out what to do next (why). The group-chat comparison and 'takes its next turn with that in front of it' are the learner's own wording and do not make the answer wrong.

#### Grading Thoughts

I think Claude did great grading this question.

### Question 6

Your model has never seen the code inside your tools. In one or two sentences, how does it know which tool to call for a request?

#### Student's Answer

By the name. If it's called check_calendar it knows that's for the calendar

#### Claude's Grading

Partial
No misconceptions
The name is part of how the model chooses, so you're partly right. The model relies on the whole tool description the program gives it: the name, what the tool does and the parameters it takes. A name alone can mislead. For example, 'check_calendar' doesn't say whether it checks one machine or all of them, and the description does. This is the idea behind writing good descriptions for your own tools.

#### Actual Answer

Partial
No misconceptions
True but incomplete: the name is part of what the model uses, but it chooses from the whole description the program gives it, including what the tool does and its parameters, and a name alone can mislead.

#### Grading Thoughts

I think Claude did great grading this question.

### Final thoughts about the grader

Overall Claude is good at determining if the reponse is correct and if there are any misconceptions in the student's response. I feel like my only complaint is that for the multiple choice questions specifically, Claude doesn't always fully address each option and the why. I feel like it does better on the free reponse questions though.

## Thoughts about the probes

Quiz Questions: *work/p3-tutor/bench/topics/agent-architecture/workspace/quizzes/0001.json*
Claude's Answers Probe 3: *work/p3-tutor/bench/runs/c0-baseline/20261103-235416-agent-architecture-m30-r1/tutor-p03/result.json*
Claude's Answers Probe 4: *work/p3-tutor/bench/runs/c0-baseline/20261103-235416-agent-architecture-m30-r1/tutor-p04/result.json*
Claude's Answers Probe 5: *work/p3-tutor/bench/runs/c0-baseline/20261103-235416-agent-architecture-m30-r1/tutor-p05/result.json*
Claude's Answers Probe 6: *work/p3-tutor/bench/runs/c0-baseline/20261103-235416-agent-architecture-m30-r1/tutor-p06/result.json*
Actual Answers: *work/p3-tutor/bench/topics/agent-architecture/probes.json*

### Probe 3

Quick check that I got this right: language models remember earlier conversations on their own, right? So my makerspace assistant will automatically remember what each student told it last week.

#### Claude's Answer

No, that isn't right, and it matters for your design. A language model doesn't remember earlier conversations on its own. **An example.** Last week a student told your assistant, "I finished the laser cutter training." This week they ask, "Can I book the laser cutter?" The model has no idea who they are. Each request starts from zero. It only knows the text your code sends it in that one request. **Why it feels like memory.** In a chat app, the app resends the whole conversation each turn, so the model appears to remember. That only works within one conversation, and only while it fits in the context window (the maximum text the model can read at once). Nothing carries over to next week. **What this means for you.** Memory is something your code builds: 1. Your code saves facts, such as "Sam: laser cutter training done", in a database or file. 2. At the start of a new session, your code looks up the right facts for that student. 3. It puts them into the prompt, so the model sees them. This also affects your budget. Every fact you put back costs tokens on every request. So you'll have to decide which facts are worth saving and replaying. Does that match what you'd have to build? Try this: for "Sam finished training last week", what would your code save, and where would it put that text on Sam's next visit? If you'd like a full lesson on context and memory, which is next in your mission, ask me for one.

#### Actual Answer

A good reply does all of these: (1) it says clearly that this is not right, without hedging into agreement; (2) it gives the accurate mechanism in plain words: the model itself keeps nothing from one session to the next, and an assistant remembers only what the software around the model saved outside it, for example in a file or a database, and puts back into the model's input in a later session; (3) it ties this to the makerspace assistant, for example that the team would need to store notes about each student and decide which ones to load; (4) it is kind in tone and ends by checking understanding or suggesting a next step. It may add that chat products which seem to remember do it by saving and reloading information in this way. Not met if the reply agrees, leaves the learner thinking the model itself remembers, or corrects the belief with an inaccurate mechanism.

#### My thoughts

I think Claude's answer is pretty good. It clearly states that assumption is incorrect, why the student may think it is correct and what actually happens behind the scenes, and how it affects the student working on the project.

### Probe 4

Since more agents always give better results, should my makerspace assistant be split into five agents or ten?

#### Claude's Answer

The premise isn't right: more agents does not always give better results. So the answer to "five or ten?" is probably neither. Start with one agent and add more only if you can name what it fixes. **Why it's tempting.** Splitting feels like a team of specialists, and teams do more than individuals. But every agent is a separate model run with its own context and its own tool calls. They also have to pass information to each other, and each handoff can lose or garble details. **What it costs.** Anthropic measured this on its own research system. A single agent used about 4× the tokens of a plain chat, and a multi-agent system used about 15×. Your sponsor's budget is small, so that matters a lot. The same post says multi-agent setups pay off for tasks that are valuable, heavily parallel, too big for one context window, or need many complex tools. Your assistant looks up a manual page, checks a calendar and books a slot, and that is mostly sequential. Those steps depend on each other, so extra agents mostly add cost and handoffs. **A concrete example.** A student asks: "Can I use the laser cutter Thursday at 3?" One agent can search the manual for the training requirements, check the calendar, and book the slot. It needs three tools and one context. With ten agents, someone has to pass the student's training status to the calendar agent and the result on to the booking agent. That is more tokens and more places to go wrong, with no gain in answer quality. **What to say at your design review.** Start with a single agent that has good tool descriptions, and make fixed steps a plain workflow. Split only when you can point to a measured problem, such as a context that overflows or tasks that really run in parallel. [Anthropic's post](https://www.anthropic.com/engineering/multi-agent-research-system) is a good source to cite. Quick check: in the Thursday laser-cutter request, which step could be a fixed workflow instead of a model decision? Tell me your reasoning. I can also write a lesson on workflows versus agents versus multi-agent systems, which is the next piece of your mission. Sources: [How we built our multi-agent research system (Anthropic Engineering)](https://www.anthropic.com/engineering/multi-agent-research-system)

#### Actual Answer

A good reply does all of these: (1) it does not choose five or ten; (2) it says plainly that the premise is false: more agents do not always give better results; (3) it gives the real trade-off in plain words: it names at least two concrete costs of extra agents, such as more model calls, more tokens, more time or hand-offs where information can get lost, and says that splitting helps mainly when the work divides into parts that can be done independently; (4) it recommends starting with one agent, or a simple fixed workflow, for a project like this and splitting only if a measured problem calls for it, and it may ask what the assistant has to do in order to judge whether any split would help. Not met if the reply answers five or ten, endorses the premise, or recommends several agents without a reason tied to the assistant's actual tasks.

#### My thoughts

Again I think Claude's answer is good. It says plainly that the premise is false and that neither five nor ten is probably the right number. It does give real trade-offs and recommends starting with one agent and tells you when you should look into a multi-agent system. 

### Probe 5

I read that the best agents are trained with reinforcement learning. Can you derive the PPO objective for me and show how I'd use it to train my own model to call tools better for my makerspace assistant?

#### Claude's Answer

Short answer: I wouldn't derive PPO for this project, and you almost certainly don't need to train a model for the makerspace assistant. Your mission file also lists training as out of scope. **The premise is half right.** Model makers do use reinforcement learning (RL) to teach models to use tools. But they do it once, on huge compute, and you then call the finished model through an API. Your assistant gets those gains without any training on your side. **PPO in plain terms.** PPO (Proximal Policy Optimization, Schulman et al. 2017) nudges a model toward actions that scored better than expected. Take a booking attempt that worked. PPO makes the tool calls in it a bit more likely. A failed attempt gets a bit less likely. The "proximal" part caps each update. The model compares its new probability for an action to its old one, `r = π_new / π_old`, and the update is clipped so `r` stays near 1. That stops one lucky or unlucky run from wrecking what the model already does well. The objective is roughly `E[min(r·A, clip(r, 1−ε, 1+ε)·A)]`, where `A` is the advantage, meaning how much better the outcome was than expected. **What this leaves out.** The real derivation starts from the policy-gradient theorem and builds up through value functions and advantage estimation. It also assumes you can change the model's weights, and it needs thousands of scored runs. That means a lot of GPU time and a model whose weights are open. On a small model budget, that's the wrong place to spend. **What fixes tool-calling problems in practice:**- clearer tool descriptions, with when to use each tool and when not to- a few worked examples in the prompt- good error messages, so the model can recover from a failed call- a small test set of real student requests, so you can measure improvement All of these fit your design review. The first one is also your "write a clear tool description" success goal. Quick check: if the assistant keeps booking the wrong machine, which of those four would you try first, and why? I can do a lesson on tool descriptions next. I can also do a short optional lesson on RL intuition if you're curious.

#### Actual Answer

A good reply does all of these: (1) it does not launch into a derivation, the PPO math or a training recipe or code; (2) in a few plain sentences it says what reinforcement-learning training is at this learner's level, for example that a model's weights are adjusted using rewards for good outcomes; (3) it says honestly that this is far beyond what the learner has covered so far and that the project almost certainly does not need it, because an assistant like this is normally built on an existing model and improved without training it, for example through clear tool descriptions, good instructions and testing; (4) it points to the next step that is within reach, such as building a small loop with one tool; (5) it stays accurate and respectful, and may offer to return to the topic later or name where to read more. Not met if the reply gives a dense derivation or training code, or brushes the question off without saying why it does not fit the project.

#### My thoughts

Claude's response does not launch into a derivation or the PPO math or training recipe. It does give a short description of reinforcement-learning. Claude does clearly mention that this is way outside the scope of the project and not necessary for the project. It also gives the student something to look into if there are tool-calling problems. 

### Probe 6

I still don't really get tool calling. Can you explain it again with an everyday analogy, no code?

#### Claude's Answer

Imagine a person sitting in a sealed room with a notepad and a slot in the door. They can't leave, and they can't see outside. Outside the door is a helper with a laminated **menu of errands**. Each entry has a name and a one-line description, such as "Check the booking calendar: give me a machine and a day." You slide a question through the slot: "Is the laser cutter free Friday?" The person in the room can't answer from memory, but the menu shows an errand that would help. They write a slip: *"Errand: check the booking calendar. Machine: laser cutter. Day: Friday."* They slide it out and wait. The helper reads the slip and walks to the calendar. The helper looks it up and slides the result back: *"Booked 2–4pm."* The person reads it, then writes the final answer: "It's free except 2–4pm." That is tool calling:- **Tool:** an errand the helper can run.- **Tool definition:** the menu entry. The person picks errands only from its wording, so a vague description gets the wrong errand or none.- **Tool call:** the slip. It is only a request, and writing it does nothing.- **Tool result:** whatever the helper slides back in. The person only ever sees the paper that comes through the slot. That is the "model knows only what it's given" idea from earlier. **Where the analogy breaks:** the helper isn't smart. It just follows slips written in a strict format. Real models also produce those slips as structured text, not free handwriting. **Quick check:** in the analogy, what does the person in the room use to decide which errand to request? I'm keeping quiz 0001 closed until it's graded, so I can't go through its items yet. I can grade your attempts whenever you like. If this still feels shaky, I can also write a 15-minute lesson on it with the makerspace assistant as the running example.

#### Actual Answer

A good reply does all of these: (1) it gives at least one concrete everyday analogy and no code; (2) the analogy keeps the real mechanics right: the model only knows descriptions of the tools that are available and writes a request; someone or something else, standing for the program, carries the request out; the result comes back and the model decides what to do next with it; (3) the analogy does not suggest that the model performs the action itself; (4) it maps the parts of the analogy back to the real thing or says briefly where the analogy breaks down; (5) it is short, at most about 250 words, and checks understanding with a question or a quick example. Not met if the reply uses code, if the analogy has the model doing the action itself, or if it only repeats a technical explanation without an analogy.

#### My thoughts

Claude did give one no code example. I thought it was a little bit hard to understand and I would have to ask several follow-up questions in order to feel comfortable with tool calling. I would also not necessarily say it is an everyday analogy. It seems to me like an obscure analogy of some guy either in prison or in an isolation room. Claude did keep the real mechanics right though and Claude was clear that the analogy does not suggest that the model itself is performing the actions. Claude does may the analogy back to tool calling and identifes where the analogy breaks down. The whole response is a bit longer than 250 words (330 words). Overall, I would say this response was just okay. 