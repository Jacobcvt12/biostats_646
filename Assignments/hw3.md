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

    **The probability that A has the joker can be written as $P(X=1)$ where the probability follows a hypergeometric distribution, where there is 1 joker, 7 non-jokers, and 5 draws. From R, we have that the probability is 0.625. Given this probability, if A and B discard all cards but one and the joker is still in hand, the probability that A has the joker is still 0.625.**

2. 
    (a) An urn contains  10 black balls and 10 white balls, identical except for color. You choose "black" or "white". One ball is drawn at random, and if its color matches your choice, you get \$10, otherwise nothing. Write down the maximum amount you are willy to pay to play the game. The game will be played just once.  

        **The probability of winning is $\frac{10}{10+10}=\frac{1}{2}$, so the expected value is $\frac{1}{2} \times 10=5$ dollars. Thus, I am willing to bet $5.**

    (b) A friend of yours has available many black and white balls , and he puts black and white balls into the urn to suit himself. You choose "black" or "white". A ball is drawn randomly from this urn. Write down the maximum amount you are willing to pay to play this game again assuming you will get \$10 if you guess right. The game will be played just once.  

        **If you randomly choose "black" or "white", instead of making the choice yourself, you will still be guaranteed a probability $\frac{1}{2}$ of winning. Thus, using this strategy, the expected value is still $5, so I would be willing to bet $5.**

    (c) Do your answers differ, if so why? If not why?  

        **While the methods differ (the first game does not require randomness on the decision), the probability of winning is the same, so my answers are the same.**

3. Let a sequence of events be defined as
    $$
    E_n = \left\{\begin{array}{cl}
    A & \mbox{$n$ is odd} \\
    B & \mbox{$n$ is even}\end{array}\right.
    $$
    (a) Find $\liminf E_n$  
        **If $x \in \liminf E_n$ then $x \in \cap_{n \geq N} E_n \implies \liminf E_n = A \cap B$.**
    (b) Find $\limsup E_n$  
        **If $x \in \limsup E_n$ then $x \in \cup_{n \geq N} E_n \implies \limsup E_n = A \cup B$.**

4. If $E_n=\{x\::\;0 < x \leq \frac{1}{n}\}$ find $\lim E_n$, repeat if $F_n=\{x\::\;0 \leq x \leq  \frac{1}{n}\}$  

    **The first few terms of $E_n$ are 
    $$
    \begin{aligned}
    E_1=(0,1] \\
    E_2=(0,\frac{1}{2}] \\
    E_3=(0,\frac{1}{3}] \\ 
    \end{aligned}
    $$
    Clearly, $E_n$ is monotonic non-increasing and so 
    $$
    \lim_{n\to\infty}E_n = \bigcap_{n=1}^{\infty} E_n = \emptyset
    $$**

    **The first few terms of $F_n$ are 
    $$
    \begin{aligned}
    F_1=[0,1] \\
    F_2=[0,\frac{1}{2}] \\
    F_3=[0,\frac{1}{3}] 
    \end{aligned}
    $$
    Clearly, $F_n$ is monotonic non-increasing and so 
    $$
    \lim_{n\to\infty}F_n = \bigcap_{n=1}^{\infty} F_n = \{0\}
    $$**

5. Explain why the probability of a bridge hand which consists of 13 cards of the same suit is given by either of the expressions 
    $$
    \frac{52 \times 12!}{(52)_{13}}\;\;\mbox{or}\;\;\frac{4\times 13! \times 39!}{52!}
    $$
    depending on whether you consider samples as ordered or not.

6. What $c$ makes the following  probability density functions
    (a) $cx^3\;\;0 \leq x \leq 1$
        $$
        \int_0^1 cx^3 dx = \frac{c}{4} x^4 \Big|_0^1 =\frac{c}{4} \implies \boxed{c=4}
        $$
    (b) $c/x\;\;1 \leq x \leq 2$
        $$
        \int_1^2 \frac{c}{x} = c \log(x) \Big|_1^2 = c \log(2) \implies \boxed{c=\frac{1}{\log(2)}}
        $$
    (c) $c/(1-x)\;\;0 \leq x \leq 1/2$
        $$
        \int_0^{1/2} \frac{c}{1-x} = -c\log(1-x) \Big|_0^{1/2}= -c\log(1/2) \implies \boxed{c=\frac{1}{\log(2)}}
        $$

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
    $$
    F(x) = \int \frac{dx}{\pi(1+x^2)} = \frac{1}{\pi}\tan^{-1}(x) +C
    $$
    **We know that $F(\infty)=1$ and so**
    $$
    \frac{\tan^{-1}(\infty)}{\pi} + C = \frac{\pi/2}{\pi} + C \implies C=\frac{1}{2} \implies \boxed{F(x)=\frac{\tan^{-1}(x)}{\pi} + \frac{1}{2}}
    $$
