import numpy as np
import matplotlib.pyplot as plt

#Parameters
def beta(t): #Exposure rate / Rate of being Susceptible => Exposed
    return 1.8
def gamma(t): #Recovery rate / Rate of being Infected => Recovered
    return 0.1
def birth(t): #Birth rate
    L = 0.005
    x0 = 0
    k = 0.00002
    #return 0.001 #Birth rate is constant
    return (L/(1+np.e**(-k*(t-x0)))) #Logistic growth function
def death(t): #Death rate
    return 0.001
def increased_death(t): #Increased likelihood of death from infection
    return 0.004
def quarantine(t, I, N): #Likelihood of being quarantined
    if (t > 150):
        return 0.25
    else:
        return 0
    #Societal Response Hanlder, Becomes messy if enabled
    #returnvar = 0
    #permanent_quarantine_enabled = True
    #permanent_quarantine = False
    #quarantine_value = 0.2
    #if I > (0.2*N):
    #    returnvar = quarantine_value
    #    if permanent_quarantine_enabled:
    #        permanent_quarantine = True
    #    return returnvar
    #else:
    #    if permanent_quarantine:
    #        returnvar = quarantine_value
    #        return returnvar
    #    else:
    #        returnvar = 0
    #        return returnvar
def alpha(t): #Likelihood of being infected / Rate of being Exposed => Infected
    return 0.1
def carrier(t): #Likelihood of becoming a carrier
    return 0.0
def carrier_exit(t): #Likelihood of no longer being a carrier
    return 0.0
def mutation(t): #Losing immunity
    return 0.1
graph_deceased = True

#Initial Values
E = 1
I = 0
R = 0
Q = 0
C = 0
D = 0
N = 100000
S = N - E - I - R - Q - C

#Lists
Susceptible = []
Exposed = []
Infected = []
Recovered = []
Carriers = []
Quarantined = []
Population = []
Deceased = []
Reproduction = []

def Infection_SEIRQCD(S, E, I, R, Q, C, D, N, T=100):
    t = 0
    repro = 0
    while (t < T):
        N = S+E+I+R+Q+C
        S, E, I, R, Q, C, D = S + mutation(t)*R - (beta(t)*(I+C)*S)/N + (birth(t)*N) - (death(t)*S), E + (beta(t)*(I+C)*S)/N - alpha(t)*E - (death(t)*E), I + alpha(t)*E - quarantine(t, I, N)*I - gamma(t)*I - carrier(t)*I + carrier_exit(t)*C - ((death(t)+increased_death(t))*I), R + gamma(t)*(I+Q) - mutation(t)*R, Q + quarantine(t, I, N)*I - gamma(t)*Q - (death(t)+increased_death(t))*Q, C + carrier(t)*I - carrier_exit(t)*C, D + increased_death(t)*(I+Q) + death(t)*N
        repro = (beta(t)/gamma(t))*(S/N)
        
        Susceptible.append(S)
        Exposed.append(E)
        Infected.append(I)
        Recovered.append(R)
        Carriers.append(C)
        Deceased.append(D)
        Quarantined.append(Q)
        Population.append(N)
        Reproduction.append(repro)
        t = t + 1
Infection_SEIRQCD(S, E, I, R, Q, C, D, N, T=350)

figure = plt.figure()
plt.title("The Progression of a Fictitious Disease (SEIRQCD)", loc="right", fontdict={'fontsize': 10})

Infected_line, = plt.plot(Infected, label='Infected')

Exposed_line, = plt.plot(Exposed, label='Exposed')

Susceptible_line, = plt.plot(Susceptible, label='Susceptible')

Recovered_line, = plt.plot(Recovered, label='Recovered')

Carriers_line, = plt.plot(Carriers, label='Carriers')

Quarantined_line, = plt.plot(Quarantined, label='Quarantined')

if graph_deceased == True:
    Deceased_line, = plt.plot(Deceased, label='Deceased')

Population_line, = plt.plot(Population, label='Population')

if graph_deceased == False:
    plt.legend(handles=[Infected_line, Susceptible_line, Exposed_line, Carriers_line, Quarantined_line, Recovered_line, Population_line])
else:
    plt.legend(handles=[Infected_line, Susceptible_line, Exposed_line, Carriers_line, Quarantined_line, Recovered_line, Deceased_line, Population_line])

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.xlabel('Time (Days)')
plt.ylabel('People in container at time t')

plt.show()



figure2 = plt.figure()
plt.title("Progression of the Effective Reproduction Number, Rt", loc="right", fontdict={'fontsize': 10})
Reproduction_line = plt.plot(Reproduction, label='Reproduction')
plt.ticklabel_format(style='plain', axis='y', scilimits=(0,0))
plt.xlabel('Time (Days)')
plt.ylabel('Effective Reproduction Number')
plt.show()

print("Graphs have been completed.")
t = 0
print("The Basic Reproduction Number, also known as R-Naught or R0: " + str((beta(t))/gamma(t)))
print("Amount of Infected at the end: " + str(Infected[int((len(Infected)))-1]))


