# Math Adaptive Learning Prototype

An AI-powered **adaptive learning system** that helps children (ages 5–10) practice basic math.  
The difficulty of questions adjusts automatically based on the learner’s performance to keep them in their optimal challenge zone.

---

## Features

✔ Generates random math puzzles (Addition, Subtraction, Multiplication)  
✔ Three difficulty levels → **Easy, Medium, Hard**  
✔ Tracks correctness and response time  
✔ Adaptive engine increases/decreases difficulty based on performance  
✔ Performance summary at the end (accuracy, average time, recommended level)  
✔ Simple, modular Python code (no heavy libraries)

---

## Project Structure
src/
- main.py # Runs the program
- puzzle_generator.py # Creates puzzles
- tracker.py # Tracks performance
- adaptive_engine.py # Adjusts difficulty
css
##  How to Run
```
pip install -r requirements.txt
python src/main.py
```
Future Improvements:
- Add GUI with Streamlit
- Save data to file or database
- Use ML model (Decision Tree, Logistic Regression)


