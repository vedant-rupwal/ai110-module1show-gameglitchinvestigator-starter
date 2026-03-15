# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 
 
- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- The game is a number guessing game built with the Streamlit application framework. The game aloows a user to find a number within a given range. The range of the numbers and the number of attempts depend of the difficulty level by the user. The game also offers hints telling them if closer to the number. The score is determined by the number of attempts it takes to find the number.
- [ ] Detail which bugs you found.
- When trying to start a new game, the attempts reset, but the game did not actually let the player start guessing again. The hints feature did not give the correct directional hints and sometimes telling the player to go higher or lower incorrectly. The counter for attempts did not reach zero causing the game to end prematurely and rob the player of a guess. The game also accepts numerical values that were outside the allowed bounds of the current difficulty levels.
- [ ] Explain what fixes you applied.
- I updated the new_game button logic to explicitly reset st.session_state.status = "playing", along with resetting the score and history. This ensures Streamlit knows the game is active again rather than stuck in a "won" or "lost" state. Then added a type-checking guard in the check_guess function to convert the secret into an integer if it was passed as a string. This stopped Python from doing alphabetical string comparisons and fixed the backward hints. Changed the initialization of st.session_state.attempts to start at 0. Previously, it was initializing at 1, which triggered the game-over condition one turn too early. And finally updated the parse_guess function to include a boundary check. It now verifies that the guess is not less than the low limit or greater than the high limit, returning a helpful error message if it is.

## 📸 Demo

- [ ] [!alt text](image.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
