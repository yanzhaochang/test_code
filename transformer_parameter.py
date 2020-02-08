# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:34:45 2020

@author: 常延朝
"""


def transformer2_parameter_calculation(Pk,Uk,P0,I0,SN,UN):#归算到UN侧
    RT = Pk*UN**2/(1000*SN**2)  #SN单位是MVA
    XT = Uk*UN**2/(100*SN)
    GT = P0/(1000*UN**2)
    BT = I0*SN/(100*UN**2)
    return RT,XT,GT,BT
#下面为三绕组计算
def transformer3_R_calculation(Pk1,Pk2,Pk3,SN,UN):
    RT1 = Pk1*UN**2/(1000*SN**2)
    RT2 = Pk2*UN**2/(1000*SN**2)
    RT3 = Pk3*UN**2/(1000*SN**2)
    return RT1,RT2,RT3
def transformer3_X_calculation(Uk1,Uk2,Uk3,SN,UN):
    XT1 = Uk1*UN**2/(100*SN)
    XT2 = Uk2*UN**2/(100*SN)
    XT3 = Uk3*UN**2/(100*SN)
    return XT1,XT2,XT3
def transformer3_G_B_calculation(P0,I0,SN,UN):
    GT = P0/(1000*UN**2)
    BT = I0*SN/(100*UN**2)
    return GT,BT
def short_circuit_loss_reduction(Pk1_2,Pk1_3,Pk2_3,capacity_ralation):
    if capacity_ralation ==2:  #100/100/50
        Pk1_2 = Pk1_2
        Pk1_3 = 4*Pk1_3
        Pk2_3 = 4*Pk2_3
    if capacity_ralation == 3: #100/50/100
        Pk1_2 = 4*Pk1_2
        Pk1_3 = Pk1_3
        Pk2_3 = 4*Pk2_3
    Pk1 = 0.5*(Pk1_2+Pk1_3-Pk2_3) 
    Pk2 = 0.5*(Pk1_2+Pk2_3-Pk1_3)
    Pk3 = 0.5*(Pk2_3+Pk1_3-Pk1_2)
    return Pk1,Pk2,Pk3
def short_circuit_voltage_reduction(Uk1_2,Uk1_3,Uk2_3):
    Uk1 = 0.5*(Uk1_2+Uk1_3-Uk2_3)
    Uk2 = 0.5*(Uk1_2+Uk2_3-Uk1_3)
    Uk3 = 0.5*(Uk1_3+Uk2_3-Uk1_2)
    return Uk1,Uk2,Uk3
    
    
    
    
    
    