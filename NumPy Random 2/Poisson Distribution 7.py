# Poisson Distribution:

# Poisson Distribution
  # Poisson Distribution is a Discrete Distribution.
  # It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
  # It has two parameters:
      # lam - rate or known number of occurrences e.g. 2 for above problem.
      # size - The shape of the returned array.

  # Example:
      # Generate a random 1x10 distribution for occurrence 2:

from numpy import random

d = random.poisson(lam = 2, size = 10)
print(d)

# Visualization of Poisson Distribution
  # Example

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam = 2, size = 1000), kde = False)
plt.show()

# Difference Between Normal and Poisson Distribution
  # Normal distribution is continuous whereas poisson is discrete.
  # But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.
  # Example:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc = 50, scale = 7, size = 1000), hist = False, label = "Normal")
sns.distplot(random.poisson(lam = 50, size = 1000), hist = False, label = "Poisson")

plt.show()

# Difference Between Binomial and Poisson Distribution
   # Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.
   # But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.
   # Example:

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n= 1000, p = 0.01, size = 1000), hist = False , label = "Binomial")
sns.distplot(random.poisson(lam= 10,size = 1000), hist = False , label = "Pousson")

plt.show()

# Own notes: In normal - parameters are loc, scale and size. 'Size' is default. So her 'loc' is mean (the centre value), scale means how many axis values you want i.e Standard deviation known as sigma. 
           # In Binomial, parameters are n, p & size only. N is the number of trails and p is the probability of occurance. 
           # In Poisson - parameters are lam and size. Here lam is n*p. 'lam' means the rate or know number of occurance. 

           # In last example you see that lam is 10 (the answer of n and p. That is 1000*0.01)
           # In the second last example. loc is 50, so mean (the center value is 50 with the scale 7, so it would be 20,30,40,50,60,70,80)




