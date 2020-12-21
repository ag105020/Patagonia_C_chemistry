'''
Created on Sep 21, 2020
Kh tested in p003 00
@author: keiin
'''

from pylab import *
from FigSetting2 import *
from sf import sf
from st import st

def Cchem(T,DIC,S,rho,pH):  
    T = T + 273.15 
    DIC = DIC #(umol/kg)
    rho = rho/1000 #(kg*1000/m3)(kg/L) Water Density (http://www.csgnetwork.com/h2odenscalc.html)
    pH = pH
    H = 1/(10**pH) #(mol/L)
    H = H/rho #(mol/kg)
    
    pK1 = 3633.86/T - 61.2173 + 9.6777*log(T) - 0.011555*S + 0.0001152*S**2 #(Emerson book, pp. 131)
    pK2 = 471.78/T + 25.9290 - 3.16967*log(T) - 0.01781*S + 0.0001122*S**2  #(Emerson book, pp. 131)
    
    K1 = 1/(10**(pK1)) #(mol/kg)
    K2 = 1/(10**(pK2)) #(mol/kg)
    
    CO2 = DIC/(1 + K1/H + K1*K2/H**2) #(umol/kg)
    HCO3 = DIC/(H/K1 + 1 + K2/H)  #(umol/kg)
    CO3 = DIC/(1 + H**2/(K1*K2) + H/K2) #(umol/kg)

    lnKh = 9345.17/T - 60.2409 + 23.3585*log(T/100)\
      + S*(0.023517 - 0.00023656*T + 0.0047036*(T/100)**2)
    Kh = exp(lnKh) #(umol kg-1 uatm-1)
    pCO2 = CO2/Kh
    
    #Unit conversion
    
    return pH,CO2,HCO3,CO3,pCO2

def fig(pH,CO2,HCO3,CO3):
    figure(1)
    plot(pH,CO2,label='CO$_{2}$',color="#660033")
    plot(pH,HCO3,label='HCO$_{3}^{-}$',color="#CC0000")
    plot(pH,CO3,label='CO$_{3}^{2-}$',color="#FFCC00")
    yscale('log')
    xticks(arange(0,15+1e-10,3))
    ylim(bottom=10e-2,top=10e5)
    xlabel('pH')
    ylabel('Concentration ($\mu$M)')
    legend(loc=1,edgecolor='k')

#PM and IE
pH,CO2_PM,HCO3_PM,CO3_PM,pCO2_PM = Cchem(14,2191,34,1025.442,8.102)
pH,CO2_IE,HCO3_IE,CO3_IE,pCO2_IE = Cchem(14,2191,34,1025.442,8.34)
pH,CO2_PU_s,HCO3_PU_s,CO3_PU_s,pCO2_PU_s = Cchem(13.8,2191,33,1024.711,8.07)
pH,CO2_PU_l,HCO3_PU_l,CO3_PU_l,pCO2_PU_l = Cchem(13.5,2191,33,1024.772,8.28)

st([["CO2 (umol/kg)",CO2_PM,CO2_IE,CO2_PU_s,CO2_PU_l],\
    ["HCO3 (umol/kg)",HCO3_PM,HCO3_IE,HCO3_PU_s,HCO3_PU_l],\
    ["CO3 (umol/kg)",CO3_PM,CO3_IE,CO3_PU_s,CO3_PU_l],\
    ["pCO2 (uatm)",pCO2_PM,pCO2_IE,pCO2_PU_s,pCO2_PU_l]],"","Output")

pHred = 0.4
pH,CO2_PM_a,HCO3_PM_a,CO3_PM_a,pCO2_PM_a = Cchem(14,2191,34,1025.442,8.102-pHred)
pH,CO2_IE_a,HCO3_IE_a,CO3_IE_a,pCO2_IE_a = Cchem(14,2191,34,1025.442,8.34-pHred)
pH,CO2_PU_s_a,HCO3_PU_s_a,CO3_PU_s_a,pCO2_PU_s_a = Cchem(13.8,2191,33,1024.711,8.07-pHred)
pH,CO2_PU_l_a,HCO3_PU_l_a,CO3_PU_l_a,pCO2_PU_l_a = Cchem(13.5,2191,33,1024.772,8.28-pHred)

st([["CO2 (umol/kg)",CO2_PM_a,CO2_IE_a,CO2_PU_s_a,CO2_PU_l_a],\
    ["HCO3 (umol/kg)",HCO3_PM_a,HCO3_IE_a,HCO3_PU_s_a,HCO3_PU_l_a],\
    ["CO3 (umol/kg)",CO3_PM_a,CO3_IE,CO3_PU_s_a,CO3_PU_l_a],\
    ["pCO2 (uatm",pCO2_PM_a,pCO2_IE_a,pCO2_PU_s_a,pCO2_PU_l_a]],"","Output_low_pH")


def doublebar(ylable,IE,PU_s,PU_l,IE_a,PU_s_a,PU_l_a):
    w=0.4
    x = ['IE','PU (S)','PU (L)']
    bar1 = arange(len(x))
    bar2 = [i+w for i in bar1] 
    Before = [IE,PU_s,PU_l]
    After = [IE_a,PU_s_a,PU_l_a]
    bar(bar1,Before,w,label='Before')
    bar(bar2,After,w,label='After')
    xticks(bar1+w/2.03,x)
    ylabel(str(ylable) + ' ($\mu$mol kg$^{-1}$)')

rcParams.update({'font.size': 27})
figure(1,figsize=(24,6.5))
subplot(1,3,1)
doublebar('[CO$_{2}$]',CO2_IE,CO2_PU_s,CO2_PU_l,CO2_IE_a,CO2_PU_s_a,CO2_PU_l_a)
legend(loc=2,edgecolor='k')

subplot(1,3,2)
doublebar('[HCO$_{3}^{-}$]',HCO3_IE,HCO3_PU_s,HCO3_PU_l,HCO3_IE_a,HCO3_PU_s_a,HCO3_PU_l_a)

subplot(1,3,3)
doublebar('[CO$_{3}^{2-}$]',CO3_IE,CO3_PU_s,CO3_PU_l,CO3_IE_a,CO3_PU_s_a,CO3_PU_l_a)

sf('','C shift',300)

show()





