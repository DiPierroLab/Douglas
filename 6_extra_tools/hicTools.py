#inputs a multi hi-C map. Outputs its top left quarter square matrix
def block11(squareMatrixText = "matrix.txt",outputFileName = "matrix11"):#inputs are strings
    from numpy import zeros, loadtxt, savetxt
    M = loadtxt(squareMatrixText)
    N = round(M.shape[0]/2)
    block = zeros((N,N))
    for i in range(N):
        for j in range(N):
            block[i][j] = M[i][j]
    savetxt(outputFileName+".txt",block)
    return block

def block12(squareMatrixText = "matrix.txt",outputFileName = "matrix12"):#inputs are strings
    from numpy import zeros, loadtxt, savetxt
    M = loadtxt(squareMatrixText)
    N = round(M.shape[0]/2)
    block = zeros((N,N))
    for i in range(N):
        for j in range(N):
            block[i][j] = M[i+N][j]
    savetxt(outputFileName+".txt",block)
    return block

def block22(squareMatrixText = "matrix.txt",outputFileName = "matrix22"):#inputs are strings
    from numpy import zeros, loadtxt, savetxt
    M = loadtxt(squareMatrixText)
    N = round(M.shape[0]/2)
    block = zeros((N,N))
    for i in range(N):
        for j in range(N):
            block[i][j] = M[i+N][j+N]
    savetxt(outputFileName+".txt",block)
    return block

#normalizes by dividing each entry by its expected value at its corresponding genomic distance.
#You can input a matrix that has different maps on the upper and lower triangles and it will still work.
def observedOverExpected(squareMatrixText = "matrix.txt",outputFileName = "observedOverExpected"):
    from numpy import zeros, loadtxt, savetxt
    M = loadtxt(squareMatrixText)
    N = M.shape[0]
    average = zeros((N,N))
    for d in range(N):
        sum_d = 0.0
        for i in range(d,N):
            sum_d += M[i][i-d]
        avg = sum_d/(N-d)
        for i in range(d,N):
            average[i][i-d] = avg 
            average[i-d][i] = avg
    obsOverExp = M/average
    savetxt(outputFileName+".txt",obsOverExp)
    return obsOverExp

#normalizes by dividing each entry by its expected value at its corresponding genomic distance.
#You can input a matrix that has different maps on the upper and lower triangles and it will still work.
def normalize(squareMatrixText = "matrix.txt", outputFileName = "normalized"):
    from numpy import zeros, loadtxt, savetxt
    M = loadtxt(squareMatrixText)
    N = M.shape[0]
    average = zeros((N,N))
    for i in range(N):
        total = 0
        for j in range(N):
            total += M[i][j]
        for j in range(N):
            M[i][j] /= total
    savetxt(outputFileName+".txt",M)
    return M

#This method does not work when the lowerLeft and upperRight triangles are not from the same Hi-C map.
def pearson(squareMatrixText = "matrix.txt",outputFileName = "pearsonMatrix"):
    from numpy import corrcoef, loadtxt, savetxt
    M = loadtxt(squareMatrixText)
    pearson = corrcoef(M)
    savetxt(outputFileName+".txt",pearson)
    return pearson

# Takes two square matrices and creates a new one sharing the lower left triangle with the first input and the upper right triangle with the second input. Inputs are expected as numpy arrays
# the output matrix has zeros along the diagonal.
#do this step last since the other methods require a symmetric matrix
def combine(lowerLeft,upperRight,filename ="combined"):#For example, you could input ".\matrix1.txt" for the first entry
    from numpy import zeros, loadtxt, savetxt
    lowerLeft = loadtxt(lowerLeft)
    upperRight = loadtxt(upperRight)
    N = upperRight.shape[0]
    combined = zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i>j:
                combined[i][j] = lowerLeft[i][j]
            elif i<j:
                combined[i][j] = upperRight[i][j]
    savetxt(filename+".txt",combined)
    return combined

def makeHiC(MatrixTxt,outputFileName="HiC",vMin = .001, vMax = 1.0):
    import numpy
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    M = numpy.loadtxt(MatrixTxt)
    plt.matshow(M, norm=mpl.colors.LogNorm(vmin=vMin, vmax=vMax),cmap="Reds")
    plt.colorbar()
    plt.savefig(outputFileName+".png")
   
def convertHiC_cooler_to_txt(coolerFilePath,outputFileName="HiC"):# converts a .cool file to a full dense numpy array written to a .txt file.
    import cooler
    import numpy as np
    c = cooler.Cooler(coolerFilePath)
    A = c.matrix(balance=False)[:,:]#balance=False prevents from beautifying the data in some way.
    np.savetxt(outputFileName+".txt",A)
    return A

def firstPC(MatrixTxt,filename = "firstPrincComp"):
    import numpy as np
    A = np.loadtxt(MatrixTxt)
    U, D, VT = np.linalg.svd(A)
    sigma1 =D[0]
    firstPrincipleComponent = sigma1*U[:,0]#first column of U is proportional to the first eigenvector in the original basis.
    #Maybe I don't need the sigma1 multiplication
    np.savetxt(filename+".txt",firstPrincipleComponent)
    return firstPrincipleComponent

def makeHistogram(MatrixTxt,outputFileName="HiC",vMin = .001, vMax = 1.0):
    import numpy
    import matplotlib.pyplot as plt
    M = numpy.loadtxt(MatrixTxt)
    plt.hist(M, bins='auto')
    _ = plt.hist(M, bins='auto')
    plt.savefig(outputFileName+".png")

def PvsGenomic(squareMatrixText = "matrix.txt",outputFileName = "PvsGenomic"):
    from numpy import zeros, loadtxt, savetxt, log
    import matplotlib.pyplot as plt
    M = loadtxt(squareMatrixText)
    N = M.shape[0]
    average = zeros(N)
    for d in range(N):
        sum_d = 0.0
        for i in range(d,N):
            sum_d += M[i][i-d]
        avg = sum_d/(N-d)
        average[d] = avg
    plt.plot(log(average))
    plt.ylabel('log average contact probability')
    plt.xlabel('trans genomic distance from trans diagonal')
    savetxt(outputFileName+".txt",average)
    return average

def PAAvsGenomic(squareMatrixText, types1, types2, outputFileName = "PAAvsGenomic"):
    from numpy import zeros, loadtxt, savetxt, log
    import matplotlib.pyplot as plt
    M = loadtxt(squareMatrixText)
    N = M.shape[0]
    types1array = loadtxt(types1,"str")
    types2array = loadtxt(types2,"str")
    average = zeros(N)
    for d in range(N):
        sum_d = 0.0
        counter = 0.0
        for i in range(d,N):
            if types1array[i,1]=="A1" and types2array[i-d,1]=="A1":
                sum_d += M[i][i-d]
                counter += 1.0
            if counter != 0:
                avg = sum_d/counter
                average[d] = avg
    plt.plot(log(average))
    savetxt(outputFileName+".txt",average)

def PBBvsGenomic(squareMatrixText, types1, types2, outputFileName = "PBBvsGenomic"):
    from numpy import zeros, loadtxt, savetxt, log
    import matplotlib.pyplot as plt
    M = loadtxt(squareMatrixText)
    N = M.shape[0]
    types1array = loadtxt(types1,"str")
    types2array = loadtxt(types2,"str")
    average = zeros(N)
    for d in range(N):
        sum_d = 0.0
        counter = 0.0
        for i in range(d,N):
            if types1array[i,1]=="B1" and types2array[i-d,1]=="B1":
                sum_d += M[i][i-d]
                counter += 1.0
            if counter != 0:
                avg = sum_d/counter
                average[d] = avg
    plt.plot(log(average))
    savetxt(outputFileName+".txt",average)

def PABvsGenomic(squareMatrixText, types1, types2, outputFileName = "PABvsGenomic"):
    from numpy import zeros, loadtxt, savetxt, log
    import matplotlib.pyplot as plt
    M = loadtxt(squareMatrixText)
    N = M.shape[0]
    types1array = loadtxt(types1,"str")
    types2array = loadtxt(types2,"str")
    average = zeros(N)
    for d in range(N):
        sum_d = 0.0
        counter = 0.0
        for i in range(d,N):
            if (types1array[i,1]=="A1" and types2array[i-d,1]=="B1") or (types1array[i,1]=="B1" and types2array[i-d,1]=="A1"):
                sum_d += M[i][i-d]
                counter += 1.0
            if counter != 0:
                avg = sum_d/counter
                average[d] = avg
    plt.plot(log(average))
    savetxt(outputFileName+".txt",average)
