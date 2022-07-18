## _Quadratic equation_

This program can decide quadratic equations, such as `a * x ** 2 + b * x + c = 0` 
by using discriminant (`d`), if `a != 0`. If `a == 0` - equation isn't quadratic.

`d = b ** 2 - 4 * a * c`

If `d > 0` - equation has 2 roots
  
Roots are calculated using the formula 
`(-b ± math.sqrt(d)) / (2 * a)`

If `d == 0` - equation has 1 root

Root is calculated using the formula `-b / 2 * a`

If `d < 0` - equation hasn't roots


![python](https://img.shields.io/pypi/pyversions/Django?color=green&style=flat-square)
![issues](https://img.shields.io/github/issues/Lily-Simon/Quadratic_equation?color=green)
