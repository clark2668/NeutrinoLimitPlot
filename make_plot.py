# -*- coding: utf-8 -*-
import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib
import matplotlib.mlab as mlab
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

def main():

	plt.rc('text',usetex=True) #plot with Latex
	plt.rc('font',family='serif') #Used a serif font
	plt.rc('font', weight='bold') #Make the text bold
	
	xlow =  1.00e14 #the lower x limit
	xup = 1.5e21 #the uppper x limit
	ylow = 0.5e-19 #the lower y limit
	yup = 0.5e-10 #the upper y limit
	fig = plt.figure(figsize=(8,8)) #make a figure object
	ax1 = fig.add_subplot(1,1,1) #make a subplot
	
	#the colors for all of the limits
	anita2color='slategray'
	icecube2016color='saddlebrown'
	auger2015color='green'
	hra3color='purple'
	ara2color='red'
	icecube2015color='black'
	icecube2015fitcolor='black'
	ahlers100color='navy'
	ahlers10color='blue'
	ahlser1color='mediumslateblue'
	
	#call the functions that actually do the plotting
	anita2(ax1,anita2color)
	icecube2016(ax1,icecube2016color)
	auger2015(ax1,auger2015color)
	hra3(ax1,hra3color)
	ara2stationanalysis(ax1,ara2color)
	icecube2015(ax1,icecube2015color)
	icecube2015fit(ax1,icecube2015fitcolor)
	ahlers100pctproton(ax1, ahlers100color)
	ahlers10pctproton(ax1, ahlers10color)
	ahlers1pctproton(ax1, ahlser1color)
	
	#add words to the plot that mark what each line is
	ax1.text(0.05,0.77,r'IceCube `15 ',transform=ax1.transAxes,color=icecube2015color,size=15,fontweight='heavy')
	ax1.text(0.22,0.40,r'IceCube `16 ',transform=ax1.transAxes,color=icecube2016color,size=15)
	ax1.text(0.36,0.30,r'Auger `15 ',transform=ax1.transAxes,color=auger2015color,size=15)
	ax1.text(0.68,0.12,r'ANITA-II `10 ',transform=ax1.transAxes,color=anita2color,size=15)
	ax1.text(0.32,0.88,r'ARA2 `16 ',transform=ax1.transAxes,color=ara2color,size=15)
	ax1.text(0.68, 0.56,r'HRA3 `15 ',transform=ax1.transAxes,color=hra3color,size=15)
	ax1.text(0.04, 0.1, r'100\% p @ 100EeV (Ahlers `12)', verticalalignment='bottom', horizontalalignment='left', transform=ax1.transAxes, color=ahlers100color, fontsize=15)
	ax1.text(0.04, 0.06, r'10\% p', verticalalignment='bottom', horizontalalignment='left', transform=ax1.transAxes, color=ahlers10color, fontsize=15)
	ax1.text(0.04, 0.02, r'1\% p', verticalalignment='bottom', horizontalalignment='left', transform=ax1.transAxes, color=ahlser1color, fontsize=15)

	ax1.text(0.80,0.93,r'Clark 2017',transform=ax1.transAxes,color='black',size=15,fontweight='heavy')

	#prepare the axis labels and save the figure
	sizer=15
	ax1.set_xlabel(r'Energy [eV]',size=sizer, fontweight='bold') #give it a title
	ax1.set_ylabel(r'E F(E) [$\textrm{cm}^{-2} \textrm{s}^{-1} \textrm{sr}^{-1}$]',size=sizer, fontweight='bold')
	ax1.set_yscale('log')
	ax1.set_xscale('log')
	ax1.tick_params(labelsize=sizer)
	ax1.set_xlim([xlow,xup]) #set the x limits of the plot
	ax1.set_ylim([ylow,yup]) #set the y limits of the plot
	
	fig.savefig('leading_limits_plot.pdf',edgecolor='none',bbox_inches="tight") #save the figure
	

def ara2stationanalysis(axis,color):
	#this is the limit from Thomas' PRD for the analysis level, 2 stations after 7.5 month of livetime
	energy_paper_anaLevel_2Station = [9.80923E+15,3.11547E+16,9.79329E+16,3.1057E+17,9.75635E+17,3.0924E+18,9.80103E+18,3.07732E+19,9.75028E+19] #energy in eV
	limit_paper_anaLevel_2Station = [0.000166106,1.24595E-05,4.06271E-06,2.04351E-06,1.48811E-06,1.42649E-06,1.50393E-06,2.10936E-06,3.25384E-06] #limit is E^2F(E) plot in GeV/cm^2/s/sr
	i=0
	while i < len(energy_paper_anaLevel_2Station):
		limit_paper_anaLevel_2Station[i]/=(energy_paper_anaLevel_2Station[i]/1e9) #divide by GeV to convert to E^-1
		i+=1
	axis.plot(energy_paper_anaLevel_2Station, limit_paper_anaLevel_2Station,'-', linewidth=2.0,color=color) #label="ARA2, 7.5 Months, Analysis Level (2016)",
	
def ara3year(axis,color):
	#this is an estimate, by Ming-Yuan Lu, for the ARA3 sensitivity projection
	oneYearScaling = 12./7.5
	oneStationScaling = 1./2.
	Aeff_paper= [1.2121e-1, 1.6452e1, 3.2073e2, 2.5147e3, 1.0463e4]
	Aeff_MYSigCalib= [0.112720, 11.068038, 269.388260, 2715.722577, 13109.019000]
	AeffScaling_MYSigCalib = [0.112720, 11.068038, 269.388260, 2715.722577, 13109.019000]
	i=0
	while i < len(Aeff_paper):
		AeffScaling_MYSigCalib[i] = Aeff_MYSigCalib[i] / Aeff_paper[i]
		i+=1

	#this comes from the trigger level
	energy_paper=[1.01518E+16,1.01357E+17,1.01748E+18,1.0234E+19,1.03113E+20]
	limit_paper=[3.29175E-05,1.65897E-06,8.73E-07,1.06368E-06,2.71842E-06]
	limit_2Stations_2013To2015_trigger = [3.29175E-05,1.65897E-06,8.73E-07,1.06368E-06,2.71842E-06]
	i=0
	while i < len(limit_paper):
		limit_2Stations_2013To2015_trigger[i] = limit_paper[i] / (oneYearScaling * oneStationScaling * ((7.52 + 9.71 + 10.95)/12.) * AeffScaling_MYSigCalib[i] + oneYearScaling * oneStationScaling * ((7.58 + 11.66 + 7.92)/12.) * AeffScaling_MYSigCalib[i] );
		limit_2Stations_2013To2015_trigger[i]/=(energy_paper[i]/1e9)
		i+=1
	
	axis.plot(energy_paper, limit_2Stations_2013To2015_trigger,'s--',color=color, linewidth=2.0) #label="ARA3, 3 years, Trigger Level (2017 ICRC)",

	
def ara37projection(axis,color):
	#this is the limit from Thomas' PRD for the trigger level, 37 stations, 3 years
	energy_paper_trigLevel_37Station=[1.00427E+16,3.33698E+16,1.02968E+17,3.64401E+17,1.12379E+18,3.40242E+18,9.48561E+18,2.89745E+19,9.69788E+19] #energy in eV
	limit_paper_trigLevel_37Station = [2.36E-07,3.84E-08,1.68E-08,1.03E-08,9.21E-09,9.51E-09,1.10E-08,1.65E-08,2.85E-08] #limit is E^2F(3) plot in GeV/cm^2/s/sr
	i=0
	while i < len(energy_paper_trigLevel_37Station):
		limit_paper_trigLevel_37Station[i]/=(energy_paper_trigLevel_37Station[i]/1e9) #divide by GeV to convert to E^-1
		i+=1
	axis.plot(energy_paper_trigLevel_37Station,limit_paper_trigLevel_37Station,'s--',color=color, linewidth=2.0) #label="ARA37 Proj, 3 years, Trigger Level (2017 ICRC)",
	
def anita2(axis,color):
	#anita2 sensitivity
	#from https://arxiv.org/abs/1003.2961
	energy_ANITA = [1.01559E+18,3.15274E+18,9.98235E+18,3.16399E+19,1.00334E+20,3.18361E+20,1.01E+21]
	limit_ANITA = [37472.95562,349.356824,19.35793264,2.789412999,0.623550734,0.239777094,0.099631676]
	i=0
	while i< len(limit_ANITA):
		limit_ANITA[i]/=(1e5 * 1e5 * 31557600 );
		i+=1
	axis.plot(energy_ANITA,limit_ANITA,'-',linewidth=2.0,color=color) #label="ANITA-II (2010)"
	
def icecube2016(axis,color):
	#icecube2016
	#from https://arxiv.org/abs/1607.05886
	#energies are in GeV
	energy_icecube=[5319813,12462854,31420359,79214517,195360452,496155180,1250867057,3153586740,7834727653,19897787152,49433789552,98542936103]
	#limit is E*Flux in 1/cm^2/s/sr
	limit_icecube = [2.813727358155058e-15, 1.4171053250274781e-15,  8.113359681118772e-16, 4.3567243967621647e-16, 2.1524270035680275e-16, 1.0102419139990222e-16, 5.637522471378329e-17, 2.9130242450321316e-17, 1.2823359239088069e-17,  8.134730973182811e-18, 5.644942449591301e-18, 5.328490567756232e-18]
	i=0
	while i< len(energy_icecube):
		revised = energy_icecube[i]* 1e9 #turn the energy to GeV
		energy_icecube[i]=revised
		i+=1
	axis.plot(energy_icecube,limit_icecube,'-',color=color, linewidth=2.0) #label="IceCube (2016)",
	
def auger2015(axis,color):
	#auger2015
	#from https://arxiv.org/abs/1504.05397v2
	
#energies are in eV
	energy_auger = [20868803142207580, 51285493451265340, 165163359618139600, 521964099644067900, 1670432977351871700, 5413510372466059000, 17001026730254017000, 54067068586441160000, 175219623037815460000]
	#limit is E^2Flux in GeV/cm^2/s/sr
	limit_auger = [0.000002240769454276632, 1.4953996737237063e-7, 3.634619552207654e-8, 2.142790439010042e-8, 2.6256749039406124e-8, 4.6763058987069e-8, 1.028860692719856e-7, 2.51597365945131e-7, 6.728070848306684e-7]
	
	i=0
	while i< len(energy_auger):
		limit_auger[i]  = limit_auger[i] / energy_auger[i] * 1e9 #divide by the energy in GeV
		i+=1
	axis.plot(energy_auger,limit_auger,'-',color=color, label="Auger (2015)",linewidth=2.0)
	

def hra3(axis,color):
	#hra3
	#from https://arxiv.org/abs/1410.7352
	energy_hra3 = [105423789.65423203, 164106994.72984993, 311968218.853512, 636930072.5228734, 991471473.3516375, 1780184322.801447, 4904994917.286609, 16270740385.211306, 72839718361.54079, 166704254305.77405, 307985796303.4945]
	limit_hra3 = [0.00003744782282999763, 0.00002941246805744629 , 0.000021486606589958947 , 0.000020473345297940047 , 0.00001904233844452056 , 0.000020973857918781288, 0.000026066571698682204 , 0.00003836331112351675 , 0.00006686130134652767 , 0.00009605444843114641 , 0.00012229609429093995]
	i=0
	while i< len(energy_hra3):
		energy_hra3[i]*=1e9
		limit_hra3[i]/=(energy_hra3[i]/1e9)
		i+=1
	axis.plot(energy_hra3,limit_hra3,'-',color=color, linewidth=2.0) #label="HRA3, 170 days (2015)",
	
def hra1296(axis,color):
	
	energy_hra1296 =[ 3237996.684414255, 5283133.271435962, 8288911.819763258, 17106768.016228348, 31391406.33305966, 54317498.24945811, 93987207.3514816, 175879879.23742318, 304330265.78145313, 516380133.1350471, 859190167.5307561, 1516082698.33195, 2378640695.264278, 4628981779.196366, 9186428611.890398, 17877357746.79667, 36895532051.4327, 77651317834.427, 157150103161.25165, 394485626229.0343, 583610795527.0767, 999999999999.9918]
	limit_hra1296 = [6.841712731578685e-8 , 4.284184167086895e-8 , 2.6156667852726875e-8 , 1.6587472649501155e-8 , 1.1639493066120233e-8 , 9.75014308321885e-9 , 8.376776400682992e-9 , 6.504094059042228e-9 , 5.3122037646255635e-9 , 4.923882631706832e-9 , 4.5639477032622285e-9 , 4.923882631706792e-9 , 5.3122037646255635e-9 , 6.341584770237488e-9 , 7.570435770161551e-9 , 9.506529014324001e-9 , 1.2557439628235892e-8 , 1.744850578429644e-8 , 2.5503125414431675e-8 , 4.021569739810773e-8 , 5.1794746792312653e-8 , 6.928820980810343e-8]
	i=0
	while i< len(energy_hra1296):
		energy_hra1296[i]*=1e9
		limit_hra1296[i]/=(energy_hra1296[i]/1e9)
		i+=1
	axis.plot(energy_hra1296,limit_hra1296,'*--',color=color, linewidth=2.0) #label="ARIANNA1296, 5 years (2017 ICRC)",

def icecube2015(axis,color):
	#icecube2015
	#from https://arxiv.org/abs/1507.03991
	
	#energy in GeV
	energy_icecube = [1.4681e4, 3.1640e4, 6.8191e4, 1.4697e5, 3.1675e5, 1.4713e6]
	#lower error bar on energy
	lowerenergy = [1.0033e4, 2.1552e4, 4.6450e4, 9.9781e4, 2.1576e5, 1.0022e6]
	#upper error bar on energy
	upperenergy = [2.1482e4, 4.6298e4, 9.9455e4, 2.1435e5, 4.6348e5, 2.1599e6]
	#E^2F in 1/GeV/cm^2/s/sr
	flux_icecube = [ 9.0685e-8, 2.250e-7, 5.6283e-8, 3.1947e-8, 4.2459e-8, 6.8292e-8]
	#lower error bar on flux
	lowerflux = [1.7401e-8, 1.6991e-7, 2.4415e-8, 7.9622e-9, 1.9759e-8, 4.4804e-8]
	#upper error bar on flux
	upperflux = [1.7266e-7, 2.8331e-7, 9.1316e-8, 5.8956e-8, 6.9698e-8, 9.7031e-8]
	
	limit_energy = [ 6.8042e5, 3.1709e6]
	limit_lowerenergy = [4.6348e5, 2.1599e6]
	limit_upperenergy = [1.0022e6, 4.8263e6]
	#limit_flux = [1.4510e-8,  1.4726e-8]
	limit_flux = [0.4510e-8,  0.4726e-8]
	limit_upperflux = [1.4510e-8,  1.4726e-8]
	limit_lowerflux = [1e-19, 1e-19]
	
	i=0
	while i<len(energy_icecube):
		flux_icecube[i]/=energy_icecube[i] #divide out the energy in GeV
		upperflux[i]/=energy_icecube[i] #divide out the energy in GeV
		lowerflux[i]/=energy_icecube[i] #divide out the energy in GeV
		upperflux[i]=upperflux[i]-flux_icecube[i]
		lowerflux[i]=flux_icecube[i]-lowerflux[i]
		#if i!=5 or i!=7:
			#upperflux[i]=abs(flux_icecube[i]-upperflux[i])
			#lowerflux[i]=abs(flux_icecube[i]-lowerflux[i])
		upperenergy[i]*=1e9 #convert GeV to eV
		lowerenergy[i]*=1e9 #convert GeV to eV
		energy_icecube[i]*=1e9 #convert GeV to eV
		upperenergy[i]=abs(energy_icecube[i]-upperenergy[i])
		lowerenergy[i]=abs(energy_icecube[i]-lowerenergy[i])
		i+=1
	
	i=0
	while i<len(limit_energy): 
		limit_flux[i]/=limit_energy[i]
		limit_upperflux[i]/=limit_energy[i]
		limit_lowerflux[i]/=limit_energy[i]
		limit_energy[i]*=1e9
		limit_lowerenergy[i]*=1e9
		limit_upperenergy[i]*=1e9
		limit_lowerenergy[i]=abs(limit_energy[i]-limit_lowerenergy[i])
		limit_upperenergy[i]=abs(limit_energy[i]-limit_upperenergy[i])
		i+=1
		
	#lowerflux[5]=1e-19
	#lowerflux[7 ]=1e-19
	#mask for upper limits
	#uplims = np.array([0,0,0,0,0,1,0,1], dtype=bool)
	uplims = np.array([1,1], dtype=bool)
	
	#axis.errorbar(energy_icecube, flux_icecube, yerr=[lowerflux, upperflux], xerr=[lowerenergy, upperenergy], uplims=uplims, fmt='o', color=color, capsize=5)
	axis.errorbar(energy_icecube, flux_icecube, yerr=[lowerflux, upperflux], xerr=[lowerenergy, upperenergy], fmt='o', color=color, capsize=5, linewidth=2)
	axis.errorbar(limit_energy, limit_flux, yerr=[5e-15, 1e-15], xerr=[limit_lowerenergy, limit_upperenergy],fmt='.', uplims=True, color=color, capsize=5, linewidth=2)

def icecube2015fit(axis,color):
	#icecube2015
	#from https://arxiv.org/abs/1507.03991

	energy = [24934.595401615374, 45849.7750546467,107281.10937121414,242758.48506146987,636471.6586212207, 1571161.8678611445, 2812729.104110674, 2822158.4616679763, 2803331.2517949035,1565912.3231479314,587347.8033287398, 231646.41394427684, 106565.41463295571, 43751.039099091824,24851.284269805557,24851.284269805557]
	limit = [1.8339323676544484e-7, 1.301878819358863e-7, 8.200479604541022e-8, 5.4615616189087235e-8, 3.551288229247809e-8, 2.4415779805067885e-8, 1.9070020008818375e-8, 1.2308450388738867e-8,7.66479681253502e-9, 1.0970366443856528e-8, 1.939355983856261e-8, 3.216796861533313e-8, 4.6599206880848976e-8, 6.724086325790956e-8, 8.405758199818991e-8, 1.2615223723752815e-7]

	i=0
	while i<len(energy):
		limit[i]/=energy[i]
		energy[i]*=1e9
		i+=1

	axis.fill(energy, limit, color=color, alpha=0.4) #, edgecolor=color
	
	
def ahlers100pctproton(axis, color):
	#ahlers 2012, from https://arxiv.org/abs/1208.4181
	#sensitivity for 100% proton
	energy_Ahlers_protonFraction1= [299675.0342,764280.5686,928525.5975,1396135.391,3729568.732,8277027.462,13909682.93,23812861.95,37157655.95,69791144.78,106901920.5,165270924.8,239456733.1,313309984.5,421501099.4,556636471.7,735096924,1007443298,1305996548,1661926896,2114860879,2641801370,3424692464,4650202011,6084417428,8035112255,10037147491,12772625930,19204979531,29967503423,48527770397,64086017645,87018887470,3.01346E+11]
	flux_Ahlers_protonFraction1 = [8.00E-13,3.81E-12,5.21E-12,9.46E-12,3.02E-11,6.38E-11,1.13E-10,2.26E-10,4.19E-10,1.03E-09,1.79E-09,2.90E-09,4.07E-09,5.04E-09,6.03E-09,6.83E-09,7.40E-09,7.67E-09,7.67E-09,7.40E-09,6.95E-09,6.53E-09,5.76E-09,4.95E-09,4.14E-09,3.29E-09,2.65E-09,1.99E-09,1.10E-09,5.14E-10,1.88E-10,9.96E-11,4.59E-11,1.27E-12]
	i=0
	while i< len(flux_Ahlers_protonFraction1):
		energy_Ahlers_protonFraction1[i]*=1e9 #convert to eV
		flux_Ahlers_protonFraction1[i]/=(energy_Ahlers_protonFraction1[i]/1e9)
		i+=1
	axis.plot(energy_Ahlers_protonFraction1,flux_Ahlers_protonFraction1,'--',color=color,linewidth=2.0) #Ahlers 100% protons
	
def ahlers10pctproton(axis, color):
	#ahlers 2012, from https://arxiv.org/abs/1208.4181
	#sensitivity for 10% proton
	
	energy_Ahlers_protonFraction1in10= [319764.9939,422283.2591,573395.2703,800537.4298,1087005.857,1345316.524,1826731.502,2574115.438,3799357.365,5660020.907,7902155.502,11555850.97,15260714.91,20530491.94,30869742.82,85578988.64,129875301.9,162235139.9,224412321.7,313309984.5,429388334.6,567052394.1,762864956.1,1045499120,1432846536,2000447758,3239417983,4522666091,6800301691,12307706571,25128179782,45478903357,76428056860,1E+11]
	flux_Ahlers_protonFraction1in10 = [5.08E-13,8.07E-13,1.31E-12,2.15E-12,3.33E-12,4.43E-12,6.39E-12,9.21E-12,1.35E-11,1.97E-11,2.78E-11,4.35E-11,6.21E-11,9.62E-11,1.70E-10,6.26E-10,9.60E-10,1.19E-09,1.46E-09,1.74E-09,1.89E-09,1.96E-09,1.92E-09,1.74E-09,1.50E-09,1.17E-09,7.54E-10,5.23E-10,3.12E-10,1.23E-10,2.76E-11,5.95E-12,1.26E-12,5.08E-13]
	i=0
	while i< len(flux_Ahlers_protonFraction1in10):
		energy_Ahlers_protonFraction1in10[i]*=1e9 #convert to eV
		flux_Ahlers_protonFraction1in10[i]/=(energy_Ahlers_protonFraction1in10[i]/1e9)
		i+=1
	axis.plot(energy_Ahlers_protonFraction1in10,flux_Ahlers_protonFraction1in10,'--',color=color,linewidth=2.0) #ahlers 10% protons
	
def ahlers1pctproton(axis, color):
	#ahlers 2012, from https://arxiv.org/abs/1208.4181
	#sensitivity for 1% proton
	energy_Ahlers_protonFraction1in100= [319764.9939,463299.161,671262.0726,937172.736,1489731.121,2346228.848,3275653.13,4834816.908,7269653.105,9962989.992,17375431.07,25645886.35,40017912.32,66015471.99,59065863.03,95648095.83,126313356.4,166810053.7,224412321.7,313309984.5,406158598.8,507357412.3,682556310.6,893070344.4,1223944358,1616347075,2056858941,7600415922,12422325321,17667779260,26812751604,34437929850]
	flux_Ahlers_protonFraction1in100 = [5.08E-13,9.31E-13,1.68E-12,2.72E-12,4.89E-12,8.06E-12,1.09E-11,1.56E-11,2.57E-11,3.61E-11,7.49E-11,1.26E-10,2.30E-10,4.62E-10,3.93E-10,6.72E-10,8.47E-10,1.03E-09,1.17E-09,1.28E-09,1.28E-09,1.23E-09,1.09E-09,9.26E-10,6.96E-10,5.14E-10,3.60E-10,3.13E-11,1.02E-11,3.95E-12,1.13E-12,5.08E-13]
	i=0
	while i< len(flux_Ahlers_protonFraction1in100):
		energy_Ahlers_protonFraction1in100[i]*=1e9 #convert to eV
		flux_Ahlers_protonFraction1in100[i]/=(energy_Ahlers_protonFraction1in100[i]/1e9)
		i+=1
	axis.plot(energy_Ahlers_protonFraction1in100,flux_Ahlers_protonFraction1in100,'--',color=color,linewidth=2.0) #ahlers 1% protons


#actually execute the main function
main()
