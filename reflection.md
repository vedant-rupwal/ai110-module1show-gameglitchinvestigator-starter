# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - When you try to start a new game reguardless if you won or not it resets the number of attemts but does not let you start guessing again. 
  - The show hint feature does not give the right hints and sometimes does not show when I click out of it and then click on it again.
  - The counter for attemts does not reach zero and ends the game prematurely.
  - The game accepts values outside the bounds of the values that can be guessed.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - AI perfectly sought out the problems and gave me the righ answers to the bugs that were present. It also pointed out more bugs that exisited that I didnt know.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - I didnt get one.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Both by running the test cases and playing the game specfically for the change and enduse the bug.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - I ran the code and played the game for checking if the hints were right. The test passed and when I played the game the hints were right and directed me to the right number.
- Did AI help you design or understand any tests? How?
  - Yes it did. It expained to me what it was doing step by step and why the test cases were desinged the way they were.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Reruns are like starting all over again from the start. You wipe clean all memory and start from the first line of code. A session state is like a notebook with information that does not wipe clean. This saves important information that would have otherwise been wiped out.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - The step by step process of solving a problem and asking the AI for clarifing questions.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would ask AI for more explainations
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  -I think that AI is a great tool that can help guide me with the challenges. 
