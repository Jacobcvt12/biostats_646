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

3.

4.

5.

