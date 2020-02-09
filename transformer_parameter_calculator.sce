//程序实现双绕组、三绕组变压器参数计算
//双绕组可直接计算参数
//单位：电压kV，容量MVA，功率kW，V0_short_circuit、I0_open_circuit 均为百分数

function RT = transformer_R_calculate(P0_short_circuit,UN,capacity)  //UN是归算侧的额定电压
	RT = P0_short_circuit*UN^2/(1000*capacity^2)
endfunction	
function XT = transformer_X_calculate(V0_short_circuit,UN,capacity)
	XT = V0_short_circuit*UN^2/(100*capacity)
endfunction	
function GT = transformer_G_calculate(P0_open_circuit,UN)
	GT = P0_open_circuit/(1000*UN^2)
endfunction	
function BT = transformer_B_calculate(I0_open_circuit,UN,capacity)	
	BT = I0_open_circuit*capacity/(100*UN^2)
endfunction	
//三绕组先进行归算
function [Pk1,Pk2,Pk3] = short_circuit_loss(Pk1_2,Pk1_3,Pk2_3,capacity_ralation)
	if capacity_ralation == '100/100/50'
        Pk1_2 = Pk1_2
        Pk1_3 = 4*Pk1_3
        Pk2_3 = 4*Pk2_3

	elseif capacity_ralation == '100/50/100'
        Pk1_2 = 4*Pk1_2
        Pk1_3 = Pk1_3
        Pk2_3 = 4*Pk2_3
	else
        Pk1_2 = Pk1_2
        Pk1_3 = Pk1_3
        Pk2_3 = Pk2_3
	end	
    Pk1 = 0.5*(Pk1_2+Pk1_3-Pk2_3) 
    Pk2 = 0.5*(Pk1_2+Pk2_3-Pk1_3)
    Pk3 = 0.5*(Pk2_3+Pk1_3-Pk1_2)	
endfunction		
function [Uk1,Uk2,Uk3] = short_voltage(Uk1_2,Uk1_3,Uk2_3)
    Uk1 = 0.5*(Uk1_2+Uk1_3-Uk2_3)
    Uk2 = 0.5*(Uk1_2+Uk2_3-Uk1_3)
    Uk3 = 0.5*(Uk1_3+Uk2_3-Uk1_2)
endfunction