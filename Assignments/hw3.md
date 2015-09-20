---
title: "Homework 3"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
    - \usepackage{mathtools}
output: pdf_document
---

1. A set of 8 cards contains one joker. $A$ and $B$ are two players and $A$ chooses 5 cards at random, $B$ takes the remaining three cards. What is the probability that $A$ has the joker?  If $A$ discards four cards and $B$ discards two cards and it is known that the joker has not been discarded what is the probability that $A$ has the joker?

2. 
    (a) An urn contains  10 black balls and 10 white balls, identical except for color. You choose "black" or "white". One ball is drawn at random, and if its color matches your choice, you get \$10, otherwise nothing. Write down the maximum amount you are willy to pay to play the game. The game will be played just once.

    (b) A friend of yours has available many black and white balls , and he puts black and white balls into the urn to suit himself. You choose "black" or "white". A ball is drawn randomly from this urn. Write down the maximum amount you are willing to pay to play this game again assuming you will get \$10 if you guess right. The game will be played just once.

    (c) Do your answers differ, if so why? If not why?

3. Let a sequence of events be defined as
    $$
    E_n = \left\{\begin{array}{cl}
    A & \mbox{$n$ is odd} \\
    B & \mbox{$n$ is even}\end{array}\right.
    $$
    (a) Find $\liminf E_n$
    (b) Find $\limsup E_n$

4. If $E_n=\{x\::\;0 < x \leq \frac{1}{n}\}$ find $\lim E_n$, repeat if $F_n=\{x\::\;0 \leq x \leq  \frac{1}{n}\}$

5. Explain why the probability of a bridge hand which consists of 13 cards of the same suit is given by either of the expressions 
    $$
    \frac{52 \times 12!}{(52)_{13}}\;\;\mbox{or}\;\;\frac{4\times 13! \times 39!}{52!}
    $$
    depending on whether you consider samples as ordered or not.

6. What $c$ makes the following  probability density functions
    (a) $cx^3\;\;0 \leq x \leq 1$
    (b) $c/x\;\;1 \leq x \leq 2$
    (c) $c/(1-x)\;\;0 \leq x \leq 1/2$

7. Consider the following 4 dice which have sides numbered as indicated.
    $$
    \begin{tabular}{cc}
    A & (4,4,4,4,0,0) \\
    B & (3,3,3,3,3,3) \\
    C & (6,6,2,2,2,2) \\
    D & (5,5,5,1,1,1)
    \end{tabular}
    $$
    In a game played with these dice, one player picks a dice and the other player picks one of the remaining three. The dice chosen are tossed and the player with the highest number wins. Show that you can guarantee that the game is favorable to you if you let your opponent choose the dice! Specifically show that
    $$
    \mathbb{P}(A > B) = \mathbb{P}(B > C) =\mathbb{P}(C > D)=\mathbb{P}(D > A) = \frac{2}{3}
    $$
    What simple change will make the game fair?

8. Find the distribution function for the Cauchy density function i.e.
    $$
    f(x) = \frac{1}{\pi(1+x^2)}\;\;,\;\;-\infty < x < +\infty
    $$
    Hint: If $y=\tan^{-1}(x)$ then $\frac{dy}{dx}=\frac{1}{1+x^2}$
