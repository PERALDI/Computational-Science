import numpy as np
import pylab as pl


#question 1

def f(x) :       # fonction a evaluer
    return 1-np.exp(-x)

def coord(n): # tirer des nombres aleatoires
    X=np.random.uniform(0,1,n)
    Y=np.random.uniform(0,1-np.exp(-1),n)
    return X,Y

def rejet(n): # methode du rejet
    [X,Y]=coord(n)
    compt=0
    for i in np.arange(n):
        if Y[i] < f(X[i]) :
            compt=compt+1
    return (compt/float(n))*(1-np.exp(-1))

def generate(n,Nb):
    X=np.zeros(Nb)
    for i in np.arange(Nb):
        X[i]=rejet(n)
    return np.mean(X),np.var(X)

print generate(100,100) 
print np.exp(-1), 'vrai valeur'

N=[20,200,1000,2000,3000,4000,5000]
XX=np.zeros(len(N))
YY=np.zeros(len(N))

# calcul de la moyenne et variance en fonction de N
for i in range(len(N)):
   [XX[i],YY[i]]=generate(N[i],100)
   

   
pl.figure(1)
pl.plot(N,XX)
pl.title(' evolution de la moyenne en fonction de N')
pl.show()


pl.figure(2)
pl.plot(N,YY)
pl.title(' evolution de la variance en fonction de N ')
pl.show()

# question 2

def sample_xs(N): # tire un nombre par rapport a l'axe x
    return (np.sqrt(np.random.rand(N)))

def sample_ys(X,N): # tire un nombre aleatoire par rapport a l'axe y
    return (np.random.uniform(0,X,N))

def sample(N): # on simule un tirage uniformement sur le triangle
    X=sample_xs(N)
    Y=sample_ys(X,N)
    return (X,Y)

N=1000
pl.figure(3)
[X,Y]=sample(N)
pl.plot(X,Y,'ro')
pl.title(' distribution uniforme sur le triangle')
pl.show()


def split(X,Y): # distinction point sous f et au dessus
    inds = Y < f(X)
    X1=X[inds]
    Y1=Y[inds]
    X2=X[~(inds)]
    Y2=Y[~(inds)]
    return (X1,Y1,X2,Y2)


X1,Y1,X2,Y2 = split(X,Y)
print len(X1),len(Y1), len(X2)

pl.figure(4)
pl.scatter(X2,Y2,c='r')
pl.scatter(X1,Y1)
l=np.linspace(0,1,1000)
pl.title( 'representation des fonctions f , g et de la distribution de point')
pl.plot(l,l)
pl.plot(l,f(l))
pl.show()

def moy(N,Nb): # calcul la variance et la moyenne
    M=np.zeros(Nb)
    for i in np.arange(Nb):
        [X,Y]=sample(N)
        X1,Y1,X2,Y2 = split(X,Y)
        M[i]=0.5*len(X1)/float(N)
    return np.mean(M),np.var(M)
        
print moy(100,100)

N=[20,200,1000,2000,3000,4000,5000]
XX=np.zeros(len(N))
YY=np.zeros(len(N))

# calcul de la moyenne et variance en fonction de N
for i in range(len(N)):
   [XX[i],YY[i]]=moy(N[i],100)
   

   
pl.figure(5)
pl.plot(N,XX)
pl.title(' evolution de la moyenne en fonction de N')
pl.show()


pl.figure(6)
pl.plot(N,YY)
pl.title(' evolution de la variance en fonction de N ')
pl.show()

#question 3

def g(x):
    return(1-np.exp(-1))*np.sqrt(x)

def px(x):
    return(3/float(2))*np.sqrt(x)

def samplex3(N):
    return (np.random.uniform(0,1,N))**(2/float(3))


def samplexy3(N):
    X=samplex3(N)
    Y=np.random.uniform(0,g(X),N)
    return X,Y

N=1000
[X,Y]=samplexy3(N)
[X1,Y1,X2,Y2]=split(X,Y)

pl.figure(7)
pl.scatter(X2,Y2,c='r')
pl.scatter(X1,Y1)
l=np.linspace(0,1,1000)
pl.title('representation des fonctions f , g et de la distribution de point')
pl.plot(l,g(l))
pl.plot(l,f(l))
pl.show()

print len(X1)

c=(2/float(3))*(1-np.exp(-1))


def moy(N,Nb):
    M=np.zeros(Nb)
    for i in np.arange(Nb):
        [X,Y]=samplexy3(N)
        X1,Y1,X2,Y2 = split(X,Y)
        M[i]=c*len(X1)/float(N)
    return np.mean(M),np.var(M)
        
print moy(100,100)
