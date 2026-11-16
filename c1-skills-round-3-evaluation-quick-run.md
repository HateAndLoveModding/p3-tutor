# Thoughts about c1-skills-round-1

This file is evaluating Claude's output which can be found at *work/p3-tutor/bench/runs/_live/20261112-050736-agent-architecture-m30-r1*

## Thoughts about the grader

Quiz Questions: *work/p3-tutor/bench/topics/agent-architecture/workspace/quizzes/0001.json*
Student's answers: *work/p3-tutor/bench/topics/agent-architecture/workspace/submissions/s1.json*
Claude's Answers: *work/p3-tutor/bench/runs/_live/20261116-133541-agent-architecture-m30-r1/grade-s1/outputs/grades/0001-s1.json*
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
- Right: (d). An agent is a cycle: the model picks an action, the program runs it, the result goes back to the model, and this repeats until a stop. That structure is what separates it from one call, which can only answer from what it was given.\n- (a) is wrong because a longer prompt changes what one call is told, not how the system is built. Suppose it were true that a detailed prompt makes an agent: you could write a huge prompt, call the model once, and get one block of text with nothing ever run and nothing fed back. That is still a single call.\n- (b) is wrong because memory of earlier conversations is not automatic, and it is not what defines an agent. A single call with a saved transcript pasted in still makes no choices and runs no actions.\n- (c) is wrong because a bigger context window only lets one call read more text. A model that holds a whole textbook but never acts or gets results back is still one call.\n- Note: keep (d) in mind for q2 and q4, where the loop is traced step by step.

#### Actual Answer

Correct
No misconceptions
d is the keyed answer: what makes an agent is the loop in which the model's chosen actions are run by the program and the results come back for the next step.

#### Grading Thoughts

I like the grading. Claude explained each answer using bullet points. One bullet point for each answer option. I also like that it used hypothetical assumptions to explain answer choices. 

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
- You chose (a): that the model opens the booking system and reads the entries itself. That is wrong. The model only produces text, so it cannot open anything. Suppose it could: then a model with no network access or credentials could still read your calendar, and nothing would need to be programmed to connect the tool. In practice the tool is a Python function that your program runs.\n- Right: (c). The model outputs a structured request naming check_calendar, with the laser cutter and tomorrow's date as arguments. The program then runs the function and sends the calendar entries back as the next input.\n- (b) is wrong because the model, not the program, decides to call the tool. The stem says so: 'the model decides to use it'. The program only sees the model's request and acts on it.\n- (d) is wrong because the model never sees or runs the tool's code. It only has the tool's description, so it cannot output the function body for itself to run.\n- This is the same belief as in q4: that the model runs the tools itself. The fix is that the model asks and the program does.

#### Actual Answer

Wrong
Misconception: M4
Chose a, the distractor in which the model opens the booking system and reads the calendar itself. The model only outputs a request naming the tool and its arguments (c) and the program runs the tool, so this answer shows the belief that the model runs tools itself.

#### Grading Thoughts

I like how it also used hypotheticals here but I don't feel like it explained why the answer was still wrong with the assumption. I also like how it explained q4 and the misconception that the model runs the tools itself.

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
- Right: (b). The agent repeats the same edit and gets the same failing test, so more steps add nothing. A step limit ends the loop after a set number of steps and reports what happened, so a person can take over and the budget is not burned.\n- (a) is wrong because all 40 steps already fit in the context. The agent can see everything it needs and is still stuck, so a larger window gives it nothing new.\n- (c) is wrong because it assumes an agent needs no stopping condition. Walk through it: each new step produces the same edit and the same failure, so step 41 looks like step 40. Nothing changes, so waiting does not help, and every step costs money, which matters with your small budget.\n- (d) is wrong because a longer prompt tells the model to try harder but does not stop the loop. The model is already trying and keeps getting the same result. A stopping condition is enforced by the program, not requested of the model.

#### Actual Answer

Correct
No misconceptions
b is the keyed answer: a step limit is the safeguard that ends a loop that keeps repeating the same failed attempt.

#### Grading Thoughts

I think that Claude's answer is great. It explained the options well I think. No complaints.

### Question 4

A student asks your makerspace assistant, "Is the laser cutter free tomorrow at 3 pm, and do I need training to use it?" Each time the model is called, it either requests exactly one tool or writes the final answer. In this run it requests check_calendar, then search_manuals, then check_training_record, and then writes its final answer. How many times was the model called in total?

#### Student's Answer

1 The model gets the question once, then it runs the 3 tools itself and answers

#### Claude's Grading

Wrong
Misconception: M4
- Wrong: you answered 1, saying the model 'runs the 3 tools itself and answers' inside a single call. The correct answer is 4.\n- Why: each model call ends with either one tool request or the final answer. The model cannot run tools, so it cannot do three tool runs inside one call. Walk through the run: call 1 (the question) gives a request for check_calendar; the program runs it. Call 2 (the question plus the calendar result) gives a request for search_manuals. Call 3 gives a request for check_training_record. Call 4 (with all three results) gives the final answer. So 3 + 1 = 4.\n- Suppose it were true that the model runs tools itself in one call. Then the model would have to read the booking system and the training records while it was writing text, which it cannot do. The results have to come back as new input, and each new input needs a new call.\n- This is the same belief as in q2: the model runs the tools. The program runs them, and between each pair of tool runs the model is called again.\n- Right: you did see that the question comes in once at the start, and that the loop ends with the model answering.

#### Actual Answer

Wrong
Misconception: M4
The answer is 4: one model call for each of the three tool requests and one for the final answer. The response says the model gets the question once and then runs the three tools itself before answering, which is the belief that the model runs tools itself, here all within a single call; it is the same misconception as this submission's q2, and the key's rationale for q4 names it.

#### Grading Thoughts

I think that Claude's response is great.

### Question 5

The program around the model has just run a tool that the model asked for. In one or two sentences, what does the program do with the tool's result, and why?

#### Student's Answer

it sends it back to the model

#### Claude's Grading

Partial
No misconceptions
- Right: 'it sends it back to the model'. That is the what: the program returns the result as part of the model's next input and calls the model again.\n- Missing: the why. The answer needs both parts.\n- Why: the model has not seen the result, because the program ran the tool, not the model. The model needs it to decide what to do next, such as calling another tool, or to write the final answer. Without the result, the model would be guessing, for example about whether the laser cutter is free.\n- To make it full credit: 'It adds the result to the model's input and calls the model again, so the model can choose its next step or write the answer.'

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
- Right: 'it gets sent a list of the tools, each with a name and a little description of what it does, and picks the one that fits'. The model chooses from the descriptions the program gives it, because it has never seen the code.\n- Wrong: 'it also remembers on its own which tool it picked ... in earlier sessions'. A model keeps nothing between calls. It starts each session knowing only its training and the text it is given. Suppose it did remember on its own: a student who had a bad session could change which tool it picks for the next student, and you could not see or control why. The tool list is sent again each time, and that is how it knows.\n- Why: any memory across sessions has to be built by your program, which saves information and puts it back into the input. This is the same belief as q1's option (b), that memory is automatic. It is the next topic in your mission, context and memory.\n- The extra claim was not needed to answer the question, so it cost you the full verdict.

#### Actual Answer

Partial
Misconception: M3
The first sentence is the keyed idea: the model picks the tool from the names and descriptions of the tools it is sent (the parameters are not required, and 'little description' is only casual wording). The second sentence adds a claim, which is false: that the model remembers on its own which tool it picked in earlier sessions. The model keeps nothing between sessions; anything that seems remembered was saved outside the model by the program and put back into its input. By FORMATS.md, the right answer with an added claim that is wrong is partial, not correct, and it is not wrong, because the false claim sits beside the keyed idea without undoing it. That claim is the belief that the model remembers earlier sessions on its own, which the key ties to M3 through q1's option b (automatic memory of every earlier conversation).

#### Grading Thoughts

I think Claude's response is great. It clearly says what was right and what was wrong and why it is wrong.

### Final thoughts about the grader

Claude still did great at determining correctness and the presence of misconceptions. I think Claude did great at fully addressing each option. The only thing that I didn't like was the response to question 2. Claude should always make sure it clearly respons with the right, wrong, and why even for the hypothetical assumption examples.