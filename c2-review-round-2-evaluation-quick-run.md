# Thoughts about c2-review-round-1

This file is evaluating Claude's output which can be found at *work/p3-tutor/bench/runs/_live/20261126-131617-agent-architecture-m30-r1*

## Thoughts about the quiz

I answered the questions before looking at the answer key.

Quiz Questions: *work/p3-tutor/bench/runs/_live/_live/20261126-131617-agent-architecture-m30-r1/quiz/outputs/quizzes/0002.json*
Claude's Answers: *work/p3-tutor/bench/runs/_live/_live/20261126-131617-agent-architecture-m30-r1/quiz/outputs/keys/0002.json*

### Question 1

Your makerspace assistant's booking feature is built as a short script: every request calls check_training_record, then check_calendar, then book_slot, always in that exact order, regardless of what the student typed. Is this piece a workflow or an agent? In one or two sentences, say which it is and name who decides what step runs next.

#### My Answer

It is a workflow because the code in the program decides what step runs next.

#### Claude's Answer Key

It's a workflow: the developer fixed the order of the three calls in the script in advance, so the program decides what runs next, not the model.

A workflow is orchestrated through a predefined code path: the developer wrote the order down once, and the program simply follows it every time, so the program (not the model) owns the control flow. Calling it an agent because it calls three tools shows M7, the common error of judging by how many tools run rather than by who picked the order. Saying 'workflow' with no reason, or naming the model as the decider, is only partial credit.

#### Quiz Notes

Question about identifying workflow vs agent. I like that it asks about who decides what step runs next.

### Question 2

A different part of the assistant answers free-form student questions. Each time it runs, it reads the student's question and chooses one of three tools - search_manuals, check_calendar, or check_training_record - then looks at what came back and chooses again, stopping on its own once it has enough to answer. Which statement best explains whether this is a workflow or an agent, and why?

- a) It's an agent, because it calls more than one tool during a single request.
- b) It's an agent, because at each step the model, not a hardcoded order, decides the next tool and when to stop.
- c) It's a workflow, because the three tools it can choose from were fixed by the developer in advance.
- d) It's an agent, because running it costs more per request than a single model call would.
- e) It's a workflow, because the loop always ends after a bounded number of tool calls.
- f) It's a workflow, because each tool's result is handed back to the program before the next step happens.

#### My Answer

B

#### Claude's Answer Key

B

What makes a system an agent is that the model itself chooses the next action and when to stop, based on what came back from the previous step, rather than following a path a developer wrote in advance. Here the model picks among three tools and decides when it has enough, so it owns the control flow. Option a shows M7: it counts the number of tool calls instead of asking who chose them - a fixed workflow can call several tools too. Option c shows M9: it mistakes a fixed, known-in-advance set of available tools for a fixed, known-in-advance order of calling them; the model can still choose which of those three tools to call and when. Option d shows M8: it treats cost as the test itself, when cost is a consequence of letting the model decide, not the definition of an agent. Option e shows M10: an agent's loop can also end after a small, bounded number of steps, so boundedness does not mark a workflow. Option f shows M11: returning a tool's result to the program before the next step happens is true of both workflows and agents, so it cannot be what tells them apart.

#### Quiz Notes

Another question about identifying a workflow vs an agent. I kinda just don't really like this question but it's fine and I don't hate it either.

### Question 3

The booking feature always needs exactly the same three steps, in the same order, for every student: verify training, check the calendar, then write the booking. Your sponsor also wants each booking request to use as few model calls as possible, to stay inside the model budget. For this part of the assistant, is a fixed workflow or an agent calling those three tools the better choice? Name your choice and give one reason tied to the budget and to the task's structure.

#### My Answer

It should be a fixed workflow because the steps are known beforehand. It is also cheaper that way because the model doesn't have to reason about what to do next.

#### Claude's Answer Key

A fixed workflow, because the three steps and their order never change between requests, so hardcoding them skips paying for the model to re-decide a path that is already known, which keeps the per-request model-call count (and cost) down.

When a task's steps and their order are already known and never vary, a workflow gets the same result as an agent for a fraction of the model calls, because there is no real decision left for the model to make. A common wrong answer is 'agent, because it calls multiple tools' (M7), which mistakes tool count for the reason a workflow or an agent is chosen; the right criterion is whether the path is already known, not how many tools are involved. An answer of 'workflow' with no reason tied to cost or to the fixed structure is partial.

#### Quiz Notes

I kinda don't like this question either because again it is primarily asking about identifying workflows vs agents. It does ask the student to give a reason tied to the budget and the task's structure and while that is good, I feel like the question could overall be better by focusing on something else like not just identifying workflow vs agents.

### Question 4

Sometimes a student's question is clear enough for the assistant to search the manuals right away. Other times the assistant first needs to ask a clarifying question, such as which machine the student means, and it cannot know in advance whether a given question will need zero, one, or more clarifying rounds before it can search. For this part of the assistant, would a fixed workflow or an agent fit better? Name your choice and give one reason tied to the task's structure.

#### My Answer

It should be an agent because the steps are never going to be the same and the steps cannot be known beforehand.

#### Claude's Answer Key

An agent, because whether and how many clarifying rounds a question needs can't be known until the assistant sees the question, so the model has to decide at run time whether to ask, and the exact path can't be hardcoded in advance.

A workflow only pays off when the steps and their order are known in advance; here the number of clarifying rounds a question needs varies and cannot be predicted before the question arrives, so the model must be the one deciding, each time, whether to ask. A common partial answer names 'agent' without saying why (the varying, unpredictable number of rounds); naming only speed or simplicity, without the structural reason, is also partial. Answering 'workflow, because clarifying questions can just be hardcoded as a fixed first step' shows M14, confusing the ability to write a fixed clarifying step in the code with being able to predict whether that step is actually needed for a given question.

#### Quiz Notes

Bruh, this is literally the same question. Me no likee.

### Question 5

A teammate builds the booking feature (verify training, check the calendar, write the booking - always these three steps, always in this order, for every student) by giving the model all three tools and a system prompt telling it to use them as it sees fit, letting the model decide the order and when it is done. What is the problem with this design choice for this particular task, and what should the teammate do instead? Answer in one or two sentences.

#### My Answer

That will cost more and the assistant will not always use all three tools or it might use them in a different order each time. It should be a fixed workflow if the same steps are performed in the same order every time. 

#### Claude's Answer Key

Letting the model decide the order and when it's done is wasted model calls and risk for a task that always needs the same three steps in the same order; the teammate should hardcode the three calls as a fixed workflow instead.

Giving an agent a task whose steps and order never vary adds model calls (and the chance of an inconsistent or wrong order) for no benefit, because there is nothing left for the model to decide. The fix is to hardcode the three calls as a workflow. A common wrong answer defends the agent design (e.g., 'it's fine, more flexible is always better,' which overlooks that flexibility is only useful where the path can actually vary) or names a problem unrelated to control flow, such as data privacy; these miss that the task's structure makes the model's freedom to choose pure overhead here. Naming the mismatch without naming the fix, or vice versa, is partial.

#### Quiz Notes

Idk. This question is slightly better but ultimately, it is testing the same thing as the previous four questions. I'm still not a fan of it.

### Question 6

A different teammate builds the question-answering feature as an agent: for each student question, the model itself decides at run time which of the machine manuals to search, how many of them to check, and whether to ask a clarifying question first, stopping once it has enough to answer. A reviewer worries this is more complicated than it needs to be. Is the agent design appropriate here? Which statement best answers that, for the goal of matching the assistant's steps to what each question actually needs?

- a) No: inappropriate, because an agent can never be trusted to stop on its own, so only a hardcoded script has a defined end point.
- b) No: inappropriate, because the three tools available to it were fixed in advance, so nothing about this feature is actually unpredictable.
- c) Yes: appropriate, because the number of lookups and whether clarification is needed varies by question, so the model must decide at run time.
- d) No: inappropriate, because agents always cost more per request than workflows do, regardless of what the task actually requires.
- e) Yes: appropriate, but only because the feature happens to call three different tools instead of just one.
- f) Yes: appropriate, but only because the student can't see how the answer was produced either way.

#### My Answer

Yes an agent is appropriate here because you cannot know the steps beforehand and letting the agent decide is the best plan. 

I didn't see that it was a multiple choice question. Uh C.

#### Claude's Answer Key

C

A fixed workflow only pays off when the steps and their order are known in advance; here the number of manuals to check and whether to ask a clarifying question both depend on the specific question, so letting the model decide at run time is the appropriate choice, not unnecessary complexity. Option a shows M15: an agent's loop ends on a stopping condition (here, 'once it has enough to answer') just as reliably as a script ends after its last line; agents are not inherently unable to stop. Option b shows M9: a fixed, known set of three available tools is not the same as a fixed, known order of calling them - the model can still choose which of the three to call, how many times, and in what order. Option d shows M8: it treats 'agents cost more' as a universal rule rather than a tradeoff that depends on whether the task's path can actually be fixed in advance; here the task's unpredictability is what justifies the extra cost. Option e shows M7: it credits the design for using three tools rather than for the model's run-time choice among them, which is what actually matters. Option f raises a true but unrelated point - how visible the reasoning is to the student doesn't bear on whether a workflow or an agent fits this task's structure.

#### Quiz Notes

Again. I feel like this is just the same question. I do like that the student my recognize that it is appropriate here.

### Final Thoughts about the quiz

I kinda don't like this quiz at all. I feel like all the questions are asking and testing the same thing. It was no where near as engaging or fun or helpful as I thought the one from round 1 was. It did address the one issue I found though. I don't really know how to explain how I feel. I just don't like it as much. The later questions ask about whether a workflow or agent is better suited for the task but I just didn't like them. I feel like you need to know two things to pass the quiz. That code defines what happens next in a workflow and you should use it when the steps are predefined. That the agent defines what happens next in an agent and you should use it when the steps cannot be known in advance. I also don't really feel like it went over that agents and workflows can be combined. 

