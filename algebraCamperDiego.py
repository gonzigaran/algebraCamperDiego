from folpy.semantics.algebras import Algebra
from folpy.syntax.types import AlgebraicType
from folpy.semantics.modelfunctions import Operation_decorator

tipo = AlgebraicType({"top": 0, "bottom": 0, "d": 3, "f": 3})

universe = list(range(5))

@Operation_decorator(universe)
def top():
    return 1
@Operation_decorator(universe)
def bottom():
    return 0

@Operation_decorator(universe)
def disc(x,y,z):
    if x == y:
        return z
    else:
        return x

@Operation_decorator(universe)
def f(x,y,z):
    if x == 2 and y == 3 and z == 4:
        return top()
    else:
        return bottom()

alg = Algebra(tipo, universe, {"top": top, "bottom": bottom, "d": disc, "f": f})

alg.to_file("algebraCamperDiego.model")

