---
title: "Homework 4"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
    - \usepackage{mathtools}
    - \usepackage{tikz}
output: pdf_document
---

1. 
    $$
    \begin{aligned}
    (\limsup E_n)^C = \{x | x \notin \limsup E_n\} \\
    = \{x | x \notin \cap_{n=0}^{\infty} \cup_{k=n}^{\infty}E_k\} \\
    = \{x | x \in \cup_{n=0}{\infty}(\cap_{k=n}^{\infty}E_k)^C\} \\
    = \{x | x \in \cup_{n=0}{\infty}\cap_{k=n}^{\infty}E_k^C\} \\
    = \boxed{\liminf E_n^C}
    \end{aligned}
    $$
