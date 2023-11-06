from numpy import loadtxt, sum
M10 = loadtxt('Hi-C_directory_10.txt')
M11 = loadtxt('Hi-C_directory_11.txt')

M10avgCisPatContactsPerBead = (sum(M10[0:2500,0:2500])-2500)/(2*2500)
M11avgCisPatContactsPerBead = (sum(M11[0:2500,0:2500])-2500)/(2*2500)
M10avgCisMatContactsPerBead = (sum(M10[2500:5000,2500:5000])-2500)/(2*2500)
M11avgCisMatContactsPerBead = (sum(M11[2500:5000,2500:5000])-2500)/(2*2500)

M10avgCisContactsPerBead = (M10avgCisPatContactsPerBead + M10avgCisMatContactsPerBead)/2
M11avgCisContactsPerBead = (M11avgCisPatContactsPerBead + M11avgCisMatContactsPerBead)/2

print('M10avgCisContactsPerBead =',M10avgCisContactsPerBead)
print('M11avgCisContactsPerBead =',M11avgCisContactsPerBead)
