---
title: "Homework 2"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
    - \usepackage{mathtools}
output: pdf_document
---

1. Suppose that $\mathbb{P}_1$ and $\mathbb{P}_2$ are probabilities on the same $\sigma$-field $\mathcal{W}$. Prove that 
$$
\mathbb{P} = \alpha\mathbb{P}_1+(1-\alpha)\mathbb{P}_2\;\;0 \leq \alpha \leq 1
$$ 
is also a probability on $\mathcal{W}$  
    i) $P(\Omega) = 1$  
        $$
        \begin{aligned}
        P(\Omega) &= \alpha P_1(\Omega) + (1-\alpha) P_2(\Omega) \\
        &= \alpha \times 1 + (1-\alpha) \times 1 \\
        &= \boxed{1}
        \end{aligned}
        $$
    ii) $P(E) \geq 0 \text{ for all } E \in W$  
        Let $E \in W$. Then
        $$
        P(E) = \alpha P_1(E) + (1-\alpha) P_2(E)
        $$
        By designation, $\alpha$ and $1-\alpha$ are all $\geq 0$. Since $P_1$ and $P_2$ are both probabilities on $W$, $P_1(E)$ and $P_2(E)$ are also both $\geq 0$. Then $P(E) \geq 0$.
    iii) If $E_1, E_2, ...$ is a countable collection of mutually exclusive events, $P(\cup_1^{\infty}E_i) = \sum_1^{\infty} P(E_i)$.
        Let $E_1, E_2, ...$ be a countable collection of mutually exclusive events. Then
        $$
        \begin{aligned}
            P(\cup_1^{\infty}) &= \alpha P_1(\cup_1^{\infty}) + (1-\alpha) P_2(\cup_1^{\infty}) \\
            &= \alpha \sum P_1(E_i) + (1-\alpha) \sum P_2(E_i) \\
            &= \sum \alpha P_1(E_i) + (1-\alpha) P_2(E_i) \\
            &= \boxed{\sum P(E_i)} \\ \qedsymbol
        \end{aligned}
        $$

2. Show that for events $E$ and $F$  
$$
\mathbb{P}(E \cap F) \geq \mathbb{P}(E)+\mathbb{P}(B) -1
$$
    Rearring $P(E \cup F) = P(E) + P(F) - P(E \cap F)$ we have that $P(E \cap F) = P(E) + P(F) - P(E \cup F) \geq \boxed{P(E) + P(F) - 1}$.
3. In how many ways can 3 novels, 2 mathematics books, and 1 chemistry book be arranged on a bookshelf if
    (a) the books can be arranged in any order.  
        Since there are $3+2+1=6$ books in total, there are $6!$ ways to arrange the books.
    (b) the mathematics books must be together and the novels must be together.  
        With 3 different subjects, there are $3!$ ways to organize the subjects. Within novels, there are $3!$ ways to organize the novels, and within mathematics, there are $2!$ ways to order them. Thus the books can be ordered in $3!3!2!$ ways under this specification.
    (c) the novels must be together but the other books can be arranged in any order.  
        Considering the novels as one unit, there $(1+2+1)!=4!$ ways to order the "units." Within the novels, there are $3!$ ways of ordering. So in total there are $4!3!$ different orderings.
4. Show that
$$
{n \choose r-1} + {n \choose r} = {n+1 \choose r}\;\;\mbox{for integers $n$ and $r$}
$$
    $$
    \begin{aligned}
    {n \choose r-1} + {n \choose r} &= \frac{n!}{(n-r+1)!(r-1)!} + \frac{n!}{(n-r)!r!} \\
    &= \frac{n!}{(n+1-r)!(r-1)!} + \frac{n!}{(n-r)!r!} \\
    &= \frac{n!}{(n+1-r)(n-r)!(r-1)!} + \frac{n!}{r(n-r)!(r-1)!} \\
    &= \frac{n!r + n!(n+1-r)}{r(n+1-r)(n-r)!(r-1)!} \\
    &= \frac{n!r + n!(n+1) -n!r)}{(n+1-r)!r!} \\
    &= \frac{(n+1)!}{(n+1-r)!r!} \\
    &= \boxed{{n+1 \choose r}} \\
    \qedsymbol
    \end{aligned}
    $$
5. You can't remember which of $n$ keys fits your file drawer. You try each without replacement so that you will get the right key on the first, second,...,$n$ try. Show that each of these outcomes has the same probability, namely $1/n$.
    The probability that a given key works is $\frac{1}{n}$. The probability that a key doesn't work is then $\frac{n-1}{n}$. Then after drawing $k$ keys, the probability that the $k+1\text{-th}$ key works is $\frac{1}{n-k}$ and doesn't work is $\frac{n-k-1}{n-k}$. Then the probability that the probability of getting the key right on the $k+1\text{-th}$ is the probability the $k+1\text{-th}$ key works and the previous $k$ keys fail:
    $$
    \frac{1}{n-k}\cdot \frac{n-k}{n-k-1} \cdot \frac{n-k-1}{n-k-2} 
    \dotsm \frac{n-1}{n} = \boxed{\frac{1}{n}} \\
    \qedsymbol
    $$
6. If $n$ balls are placed at random into $n$ cells find the probability that exactly one  cell remains empty.  
    There are $n^n$ ways of sampling the cells, the denominator of this probability. Since only one cell can have zero balls, there are ${n \choose 1}$ possible choices for the cell. Since only one cell is missing a ball, there is one and only one cell with, there are $n-1$ possible cells to choose from, giving ${n-1 \choose 1}$ possibilities of choosing this cell. In this cell, there are ${n \choose 2}$ ways to distribute the 2 balls. There are $n-2$ cells remaining and so $(n-2)!$ ways to distribute the balls amongst these cells. Thus, the number of possibilities to place these balls under this criterion is
    $$
    {n \choose 1}{n-1 \choose 1}{n \choose 2}(n-2)! =
    \frac{n!}{(n-1)!}\frac{(n-1)!}{(n-2)!}\frac{n!}{(n-2)!2}(n-2)! =
    {n \choose 2}n!
    $$
    Then the probability is $\boxed{{n \choose 2}\frac{n!}{n^n}}$.  
    $\qedsymbol$
7. Show that it is more probable to get at least one ace (one) with four dice that it is to get at least one double ace in 24 thows of two dice.  
    The probability of one ace is $\frac{1}{6}$ and of a double ace is $\frac{1}{6}\times \frac{1}{6}=\frac{1}{36}$. The probability of at least one ace with four dice is $1-P(\text{no aces})=1-(1-\frac{1}{6})^4=1-\frac{5}{6}^4 \approx 0.518$. The probability of at least one double ace in 24 tosses is $1-P(\text{no aces})=1-(1-\frac{1}{36})^24=1-\frac{35}{36}^24 \approx 0.491$.  
    $\qedsymbol$
8. A box contains ninety good screws and ten defective screws. If ten screws are used what is the probability that none is defective?  
    This probability follows a hypergeomtric distribution and can set up as follows:
    $$
    \frac{{10 \choose 0}{100-10 \choose 10-0}}{{100 \choose 10}}
    $$
    From R, this is calculated as $0.3304762$.
