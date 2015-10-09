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

    (b) Set $U=X+Y$ and $V=X-Y$. Then $X=\frac{U+V}{2}$ and $Y=\frac{U-V}{2}$. Then it follows that
        $$
        |J_{x,y}|=
        \begin{vmatrix}
        1 & 1 \\
        1 & -1 \\
        \end{vmatrix} = 2 \\
        f_{U,V} (u, v) = f_X(x=(u+v)/2)f_Y(y=(u−v)/2)
        $$

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
    (a) **Let 
        $Y_1 = \left[\begin{matrix}x_{1}\\x_{2}\end{matrix}\right]$, and $Y_2 = x_3$. Then $E Y_1 = \mu \text{ and } E Y_2 = \left[\begin{matrix}\mu\\\mu\end{matrix}\right]$
        Additionally,
        $$
        \Sigma_{11} = \left[\begin{matrix}3 & 0\\0 & 1\end{matrix}\right]
        \Sigma_{12} = \left[\begin{matrix}1\\1\end{matrix}\right]
        \Sigma_{21} = \left[\begin{matrix}1 & 1\end{matrix}\right]
        \Sigma_{22} = \left[\begin{matrix}2\end{matrix}\right]
        $$
        Then $\mu_2^{*} = E Y_1 | Y_2 = \mu + \left[\begin{matrix}- \frac{4 \mu}{3} + \frac{x_{1}}{3} + x_{2}\end{matrix}\right]$ and 
        $\Sigma_{22}^{*} = Cov Y_1 | Y_2 = \left[\begin{matrix}\frac{2}{3}\end{matrix}\right]$
        So the conditional distribution is 
        $$
        \boxed{\text{MVN}(\mu_2^{*}, \Sigma_{22}^*)}
        $$
        **
    (b) Let
        $Y_1 = x_1$ and $Y_2 = \left[\begin{matrix}x_{2}\\x_{3}\end{matrix}\right]$ Then $E Y_1 = \mu \text{ and } E Y_2 = \left[\begin{matrix}\mu\\\mu\end{matrix}\right]$
        Additionally,
        $$
        \Sigma_{11} = \left[\begin{matrix}3\end{matrix}\right]
        \Sigma_{12} = \left[\begin{matrix}0\\1\end{matrix}\right]
        \Sigma_{21} = \left[\begin{matrix}0 & 1\end{matrix}\right]
        \Sigma_{22} = \left[\begin{matrix}1 & 1\\1 & 2\end{matrix}\right]
        $$

        Then $\mu_2^* = \left[\begin{matrix}\mu\\\frac{2 \mu}{3} + \frac{x_{1}}{3}\end{matrix}\right]$ and
        $\Sigma_22^*=\left[\begin{matrix}1 & 1\\1 & \frac{5}{3}\end{matrix}\right]$

        So the conditional distribution is 
        $$
        \boxed{\text{MVN}(\mu_2^{*}, \Sigma_{22}^*)}
        $$

