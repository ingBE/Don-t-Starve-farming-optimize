import numpy as np

# x는 각각의 작물의 갯수, Z는 작물이 성장할 때 마다 배출하는 영양소의 양
# Ax=z, A는 각각의 작물이 배출하는 영양소의 양을 정리해둔 행렬
# Ax = CBx = Cy = z
B = np.array([[  1,  0,  0,  0,  0,  0,  1, -1,  0,  0,  0,  2,  0,  2],
              [  0,  1,  0,  0,  1,  0,  0,  0,  0,  2,  2,  0,  0,  0],
              [  0,  0,  1, -1,  0,  1,  0,  0,  2,  0,  0,  0,  2,  0]])

C = np.array([[ -4,  2,  2],
              [  2, -4,  2],
              [  2,  2, -4]])

A = np.matmul(C,B)

D = np.array([  0,  1,  2,  2,  1,  2,  0,  0,  2,  1,  1,  0,  2,  0])

def aa(ymin, x):
    # ytemp의 각 성분이 ymin과 같도록 주의하며 작물을 배치한다
    N = len(x)
    xtemp = np.zeros(N)
    ytemp = np.zeros(3)

    # 가중치가 2인 작물을 배치
    for i in range(3):
        for j in range(N):
            if (B[i,j] == 2) and (0 < x[j]):
                if ymin//2 < x[j]:
                    xtemp[j] = ymin//2 - ytemp[D[j]]/2
                elif x[j] < ymin//2 - ytemp[D[j]]/2:
                    xtemp[j] = x[j] 
                else:
                    xtemp[j] = ymin//2 - ytemp[D[j]]/2
                ytemp[D[j]] += 2*xtemp[j]

    # 가중치가 1인 작물을 배치
    for i in range(3):
        for j in range(N):
            if (B[i,j] == 1) and (0 < x[j]):
                if ymin < x[j]:
                    xtemp[j] = ymin - ytemp[D[j]]
                elif x[j] < ymin - ytemp[D[j]]:
                    xtemp[j] = x[j]
                else:
                    xtemp[j] = ymin - ytemp[D[j]]
                ytemp[D[j]] += xtemp[j]

    # 가중치가 -1인 작물과 2인 작물을 배치
    for i in range(3):
        for j in range(N):
            if (B[i,j] == -1) and (0 < x[j]):
                for k in range(14):
                    if (B[i,k] == 2) and (0 < x[k]):
                        if (x[j] - xtemp[j])//2 < x[k] - xtemp[k]:
                            xtemp[k] += (x[j]-xtemp[j])//2
                            xtemp[j] += (x[j]-xtemp[j]) - (x[j]-xtemp[j])%2
                        else:
                            xtemp[j] += 2*(x[k] - xtemp[k])
                            xtemp[k] += x[k] - xtemp[k]

    # 가중치가 -1인 작물과 1인 작물을 배치
    for i in range(3):
        for j in range(N):
            if (B[i,j] == -1) and (0 < x[j]):
                for k in range(14):
                    if (B[i,k] == 1) and (0 < x[k]):
                        if x[j] - xtemp[j] < x[k] - xtemp[k]:
                            xtemp[k] += x[j] - xtemp[j]
                            xtemp[j] += x[j] - xtemp[j]
                        else:
                            xtemp[j] += x[k] - xtemp[k]
                            xtemp[k] += x[k] - xtemp[k]

    return ymin, xtemp, ytemp

def seedCombination(seedArray):
    x = np.array(seedArray)
    y = np.matmul(B,x)
    ymin = y.min()
    if ymin < 0: ymin = 0

    a, b, c = aa(ymin,x)
    if (b[0] != b[1]) or (b[1] != b[2]):
        ymin = c.min()
        if ymin < 0: ymin = 0
        a, b, c = aa(ymin,x)

    return b


if __name__ == "__main__":
    x = np.array([10,7,5,0,2,0,1,2,0,3,5,0,5,0])

    xopt = seedCombination(x)

    print(xopt)
