---
title: "Homework 1"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
output: pdf_document
---

1. Prove that $A \cap B = B \cap A$  
    Let $c \in A \cap B$. Then $c \in A$ and $c \in B$. Thus $c \in B \cap A$. The reverse follows similarly. \qedsymbol
 
2. Prove that $A \cup (B \cup C)=(A \cup B) \cup C$  
    Let $d \in A \cup (B \cup C)$. Then
    $$
    \begin{aligned}
    d \in A \cup (B \cup C) &\iff d \in A \lor d \in B \cup C \\
    &\iff d \in (A \cup B) \lor d \in C \\
    \end{aligned}
    $$
    Thus $A \cup (B \cup C)=(A \cup B) \cup C$. \qedsymbol 

3. Equality of ordered pairs is defined as $(a,b)=(c,d)$ if and only if $a=c$ and $b=d$. Show that this is equivalent to the  definition  by sets i.e. 
    $$
    \{\{a\},\{a,b\}\} = \{\{c\},\{c,d\}\}
    $$

4. Let $A$ and $B$ be events with probabilities $\mathbb{P}(A)=\frac{3}{4}$ and $\mathbb{P}(B)=\frac{1}{3}$. Show that
    $$
    \frac{1}{12} \leq \mathbb{P}(A \cap B) \leq \frac{1}{3}
    $$
    
    Show that these bounds hold (are sharp) when
    $$
    \Omega=\{1,2,\ldots,12\}\mbox{ with }\mathbb{P}(\{i\})=\frac{1}{12}\;\;,\;\;i=1,2,\ldots,12
    $$
    
    and $A=\{1,2,\ldots,9\}$, $B=\{9,10,11,12\}$ for the lower bound and $A=\{1,2,\ldots,9\}$, $B=\{1,2,3,4\}$ for the upper bound.
    
    Repeat, finding upper and lower bounds for  $A \cup B$, the same $A$ and $B$ work for the sharp statement.

5. You flip three coins. At least two are alike. Since it is an even chance that the remaining coin is a head or tail the probability that all three are alike is $\frac{1}{2}$. Is this reasoning correct?  
    Consider $A$ to be the number of total alike coins of the three coins flipped. Then we are interested in 
    $$
    \mathbb{P}(A=3|A \geq 2) = \frac{\mathbb{P}(A=3 \cap A \geq 2)}{\mathbb{P}(A \geq 2)}
    $$
    It follows that $\mathbb{P}(A=3 \cap A \geq 2)=\mathbb{P}(A=3)$, since $A\geq 2 \subset A=3$. Additionally, in three flips, at least two must be either tails or heads, so $\mathbb{P}(A \geq 2)=1$. Finally, $A=3$ occurs in two out of four possible outcomes, so $\mathbb{P}(A=3)=\frac{1}{2}$. Thus,
    $$
    \mathbb{P}(A=3|A\geq2) = \frac{\frac{1}{2}}{1}=\frac{1}{2}
    $$
    and so the reasoning is correct. \qedsymbol


6. Show that the probability of exactly one of the events $A$ and $B$ occurs is $\mathbb{P}(A)+\mathbb{P}(B)-2\mathbb{P}(A \cap B)$.

