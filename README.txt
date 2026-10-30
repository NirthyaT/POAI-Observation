PRINCIPLES OF AI PRACTICAL - FULL CODE

This folder contains 11 standalone experiment programs:
01-05 and 07-11 are Python 3 programs (.py).
06_likes_facts_rules.pl is the Prolog program.

RUN PYTHON PROGRAMS:
1. Install Python 3.
2. Open Command Prompt or terminal in this folder.
3. Run a program, for example:
   python 01_eight_queens.py

RUN THE PROLOG PROGRAM:
1. Open the file in SWI-Prolog.
2. Consult it:
   ?- consult('06_likes_facts_rules.pl').
3. Try queries such as:
   ?- likes(mary, food).
   ?- likes(john, food).

NOTES:
- The programs follow the supplied Principles of AI Practical Exam Guide.
- Small execution/indentation issues have been cleaned up.
- Experiment 7 is a simple teaching implementation, not a full theorem prover.
- Experiment 10 demonstrates the simple pickup/stack plan described in the guide.
