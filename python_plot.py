import matplotlib as plt
import numpy as np
import cmath

arr1d = []
c = 0
import matplotlib.pyplot as plt
import numpy as np

# cnums = np.arange(5) + 1j * np.arange(6,11)
# X = [x.real for x in cnums]
# Y = [x.imag for x in cnums]
# plt.scatter(X,Y, color='red')
# plt.show()
# import matplotlib as plt
# import numpy as np
#
# x = np.linspace(-0.5,0.5,100)
# y = np.linspace(-3,0,100)
# X, Y = np.meshgrid(x,y)
#
# def f(x, y):
#     return 1./(1+1j*(x+1j*y))
#
# import pylab
# pylab.imshow(np.abs(f(X,Y)))
# pylab.show()
a = []
d = complex(0.1,0.1)
z = complex(1.0,1.0)
for b in range(20):
    d = z ** 2 + d
    a.append(d)
    print(d)

import matplotlib.pyplot as plt
# plt.plot(a)
# plt.ylabel('some numbers')
# plt.show()
# # a = cmath.phase(complex(-1.0, 0.1))
# print(a)

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()