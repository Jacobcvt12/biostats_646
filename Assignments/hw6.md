---
title: "Homework 6"
author: "Jacob Carey"
date: \today
header-includes:
    - \usepackage{amsthm}
    - \usepackage{mathtools}
output: pdf_document
---

1. 
    (a) The number of possible combinations is
        $$
        \begin{aligned}
        {2n \choose 2} \times {2n-2 \choose 2} \times \dotsm \times {2n - (2n-2) \choose 2} &= \frac{(2n)!}{2!(2n-2)!} \times \dotsm \times 
        \frac{(2n-(2n-2))!}{2!(2n-(2n-2)-2)!} \\
        &= \frac{2n(2n-1)}{2!} \times \dotsm \times \frac{2\times 1}{2!} \\
        &= \frac{(2n)!}{2^n}
        \end{aligned}
        $$
        At step 1, we have $n$ options for choosing a matching long and short pair, at step 2, we have $n-1$ options for choosing a matching pair, etc. Thus the probability that the parts will be joined in the original order is
        $$
        \boxed{n! \times \frac{2^n}{(2n)!}}
        $$

    (b) The number of possible combinations is the same as part (a). However, at step 1, we have $n^2$ possibilities for choices, step 2 we have $(n-1)^2$, etc. Across all $n$ pairs, we have $(n!)^2$.

        Thus, our probability of matching all long parts to short parts is 
        $$
        \frac{2^n(n!)^2}{(2n)!} = \boxed{\frac{2^n}{{2n \choose n}}}
        $$

2. 
    $$ 
    \begin{aligned}
    \int_{x^2 > 0} x^2 f(x) dx &= \int_0^{\infty} x^2 f(x) dx \\
    &= \int_0^{\infty}\{\int_0^{x^2}du\}f_X(x) dx \text{ where $u=x^2$} \\
    &= \int_0^{\infty} \{\int_u^{\infty} f_X(x)dx\}du \\
    &= \int_0^{\infty} 1 - F_X(u) du \\
    &= \boxed{\int_0^{\infty} 2x [1-F_X(x)] dx}
    \end{aligned}
    $$
