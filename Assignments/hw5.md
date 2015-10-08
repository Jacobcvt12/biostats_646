---
title: "Homework 5"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
    - \usepackage{mathtools}
output: pdf_document
---

1. 
    $$
    \begin{aligned}
    {n \choose r} &= \frac{n!}{r!(n-r)!} \\
    &= \frac{[r+(n-r)](n-1)!}{r!(n-r)!} \\
    &= \frac{(n-1)!r+(n-1)!(n-r)}{r!(n-r)!} \\
    &= \frac{(n-1)!r}{r!(n-r)!} + \frac{(n-r)(n-1)!}{r!(n-r)!} \\
    &= \boxed{{n-1 \choose r-1} + {n-1 \choose r}}
    \end{aligned}
    $$

2.
    (a) 
        $$
        \begin{aligned}
        F_Z(z)=P(\{(x, y) : \frac{x}{y} \leq z\}) &= 
        P(\{(x, y):x\leq yz, y > 0\}) + P(\{(x, y):x\geq yz, y < 0\}) \\
        &= \int_0^{\infty} \int_{-\infty}^{yz} f_{XY} dx dy +
        \int_{-\infty}^0 \int_{yz}^{\infty} f_{XY} dx dy \\
        f_Z &= \int_0^{\infty} (y f_{XY}(yz, y) - 0 \times f_{XY}(yz, y) +
        \int_{-\infty}^{yz} \frac{\partial}{\partial z} f_{XY} dx) dy + \\
        & \phantom{=} \int^0_{-\infty} (0 \times f_{XY}(\infty, y) - y f_{XY}(yz, y) +
        \int^{\infty}_{yz} \frac{\partial}{\partial z} f_{XY} dx) dy \\
        &= \int_0^{\infty} y f_{XY}(yz, y) dy + 
        \int_{-\infty}^0 (-y) f_{XY} (yz, y) dy \\
        &= \int_{-\infty}^{\infty} |y| f_{XY} (yz, y) dy \\
        &= \int_{-\infty}^{\infty} \frac{1}{2\pi} |y| \exp
        \Big\{-\frac{y^2}{2}(z^2+1)\Big\} dy \\
        &= \int_0^{\infty} \frac{y}{\pi}e^{-y^2\frac{z^2+1}{2}}dy \\
        &= \boxed{\frac{1}{\pi}\frac{1}{z^2+1}}
        \end{aligned}
        $$

    (b)

3.
    (a) $f_X = \int_0^{1-x} 2 dy = 2(1-x)$ **Not uniform**
    (b) $f_{Y|X} = \frac{2}{2(1-x)}=\frac{1}{1-x}$
    (c) $f_Y = \int_0^{1-y} 2 dx = 2(1-y)$ **Not independent**
4.
    $$
    \begin{aligned}
    P(X_1=x_1, ..., X_k=x_k|S=X_1+...+X_k=s)  &=
    \frac{P(X_1=x_1, ..., X_k=x_k,s=X_1+...+X_k)}{P(S=\sum X_i=s)} \\
    &= \frac{P(X_1=x_1) \dotsm P(X_k=s-\sum_{i=1}^{k-1}x_i)}{P(S=s)} \\
    &= \frac{\lambda_1^{x_1} e^{-\lambda_1}}{x_1!} \dotsm
    \frac{\lambda_k^{s-\sum x_i} e^{-\lambda_k}}{(s-\sum x_i)!}
    \frac{s!}{(\lambda_1 + ... + \lambda_k)^s e^{-(\lambda_1+...+\lambda_k)}} \\
    &= \frac{\lambda_1^{x_1} \dotsm \lambda_k^{x_k} s!}{x_1! \dotsm x_k!
    (\lambda_1+...+\lambda_k)^s} \\
    &= \frac{\lambda_1^{x_1} \dotsm \lambda_k^{x_k} s!}{x_1! \dotsm x_k!
    (\lambda_1+...+\lambda_k)^{x_1+...x_k}} \\
    &= \frac{s!}{x_1! \dotsm x_k!}\frac{\lambda_1}{\sum \lambda_i}^{x_1}
    \dotsm \frac{\lambda_k}{\sum \lambda_i}^{x_k} \\
    &= \boxed{\text{Mult}(n, \mathbf{\pi})} \\
    \text{where } \pi_i = \frac{\lambda_i}{\sum \lambda_j}^{x_i}
    \end{aligned}
    $$

5.

