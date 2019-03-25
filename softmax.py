# softmax range(0,1)
#whatever input it will fixed it in range of (0,1)

#y[2.0,1.0,0.1] = (S(yi)=(e^yi/sum(e^yi))) ==p[0.7,0.2,0.1]




import numpy as np

logits = [2.0, 1.0, 0.1]

exps = [np.exp(i) for i in logits]

sum_of_exps = sum(exps)
softmax = [j/sum_of_exps for j in exps]

print(softmax)
