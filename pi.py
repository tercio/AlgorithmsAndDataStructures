import random
import sys

n_run = 50000000

dentro = 0.0
fora   = 0.0

print ("running: (%d) " % (n_run),end="")

while n_run:

    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    if x*x + y*y <= 1.0:
        dentro += 1.0
    else:
        fora += 1.0

    #if n_run % 10000 == 0:
    #    print (".",end="")
    #    sys.stdout.flush()

    n_run -= 1

print ("\nPI = %.10f" % (4.0*dentro/(fora+dentro)) )