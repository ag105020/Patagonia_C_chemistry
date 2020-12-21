'''
Created on Sep 21, 2020

@author: keiin
'''

from pylab import *
from FigSetting2 import *
from sf import sf

def Cchem(T,DIC,S,rho):  
    T = T + 273.15 
    DIC = DIC #(umol/kg)
    rho = rho/1000 #(kg*1000/m3)(kg/L) Water Density (http://www.csgnetwork.com/h2odenscalc.html)
    pH = arange(0,15.001,0.1)
    H = 1/(10**pH) #(mol/L)
    H = H/rho #(mol/kg)
    
    pK1 = 3633.86/T - 61.2173 + 9.6777*log(T) - 0.011555*S + 0.0001152*S**2 #(Emerson book, pp. 131)
    pK2 = 471.78/T + 25.9290 - 3.16967*log(T) - 0.01781*S + 0.0001122*S**2  #(Emerson book, pp. 131)
    
    K1 = 1/(10**(pK1)) #(mol/kg)
    K2 = 1/(10**(pK2)) #(mol/kg)
    
    CO2 = DIC/(1 + K1/H + K1*K2/H**2) #(umol/kg)
    HCO3 = DIC/(H/K1 + 1 + K2/H)  #(umol/kg)
    CO3 = DIC/(1 + H**2/(K1*K2) + H/K2) #(umol/kg)
    
    return pH,CO2,HCO3,CO3

def fig(pH,CO2,HCO3,CO3):
    figure(1)
    plot(pH,CO2,label='CO$_{2}$',color="#660033")
    plot(pH,HCO3,label='HCO$_{3}^{-}$',color="#CC0000")
    plot(pH,CO3,label='CO$_{3}^{2-}$',color="#FFCC00")
    yscale('log')
    xticks(arange(0,15+1e-10,3))
    ylim(bottom=10e-2,top=10e5)
    xlabel('pH')
    ylabel('Concentration ($\mu$mol kg$^{-1}$)')
    legend(loc=1,edgecolor='k')

#PM and IE
pH,CO2,HCO3,CO3 = Cchem(14,2191,34,1025.442)
fig(pH,CO2,HCO3,CO3)
sf("","Cchem",300)
# 
# #PU-short
# pH,CO2,HCO3,CO3 = Cchem(13.8,2191,33,1024.711)
# fig(pH,CO2,HCO3,CO3)
# 
# #PU-long
# pH,CO2,HCO3,CO3 = Cchem(13.5,2191,33,1024.772)
# fig(pH,CO2,HCO3,CO3)

show()





