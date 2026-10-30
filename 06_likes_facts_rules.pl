% Experiment 6: Prolog Facts and Rules (likes/2)

% Facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rule (a): John likes anything Mary likes.
likes(john, X) :-
    likes(mary, X).

% Rule (b): John likes anyone who likes wine.
likes(john, X) :-
    likes(X, wine).

% Rule (c): John likes anyone who likes themselves.
likes(john, X) :-
    likes(X, X).

% Example queries to enter in the Prolog interpreter:
% ?- likes(mary, food).
% ?- likes(john, wine).
% ?- likes(john, food).
% ?- likes(john, mary).
