# 01-04

## Challenge 04 - Vector 2D

![](https://mathinsight.org/media/image/image/vector_2d_add.png?auto=format&fit=crop&w=1350&q=80)

## Objectives
Special methods

## Guidelines
2d-vectors are described by a pair of real numbers (a,b). There are mathematical rules for operations on vectors:

$$ (a,b)+(c,d) = (a+c, b+d) $$

$$ {(a,b)−(c,d) = (a−c, b−d)} $$

$$ {{(a,b)}.{(c,d)} = ac + bd} $$

$$ {||(a,b)||= \sqrt{{(a,b)}.{(a,b)}}} $$

Moreover, two vectors $ {(a,b)} $ and $ {(c,d)} $ are equal if ${a=c}$ and ${b=d}$.

Build a class `Vector2D` where the above mathematical operations are implemented by special methods. The class must contain two data attributes `x` and `y`, one for each component of the vector. It must include special methods for addition, subtraction, the scalar product (multiplication), the absolute value (length), comparison of two vectors (== and !=), as well as a method for printing out a vector and the number of dimensions (in that case, it is always 2).

Your program must be written in `src/vector2d.py`. You should be able to instanciate circles and play with them directly from your iPython console.
