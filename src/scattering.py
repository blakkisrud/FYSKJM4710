import numpy as np
import matplotlib.pyplot as plt

# Define some constants
h = 6.62607004e-34 # Units of m^2kg/s
c = 299792458 # Units of m/s
m_e = 9.109e-31 # Units of kg
r_0 = 2.81794e-15 # Units of m

def convert_from_MeV_to_j(energy_in_MeV):

    return energy_in_MeV*1.6021e-13

def convert_from_j_to_MeV(energy_in_j):

    return energy_in_j*6.2415091e12

def compton_scatter(photon_wave_len, scatter_angle_theta):

    # Simplifies the scatter equation to
    # hv' = alpha/(1 + beta) where 
    # alpha = hv and beta = (hv/m_c^2)*(1-cos(theta))

    global h
    global c
    global m_e
    
    photon_k = c/photon_wave_len

    photon_energy_j = photon_k*h

    #print 'Incoming photon energy:' + str(convert_from_j_to_MeV(photon_energy_j))

    alpha = photon_energy_j
    beta = (photon_energy_j/(m_e*c*c))*(1-np.cos(scatter_angle_theta))

    scattered_photon_energy_j = alpha/(1+beta)

    #print 'Scattered photon energy: ' + str(convert_from_j_to_MeV(scattered_photon_energy_j))

    return convert_from_j_to_MeV(scattered_photon_energy_j)

def klein_nishina_fractional_cross_section_energy(incoming_photon_energy_j, outgoing_photon_energy_j):

    # Simplifies the fractional cross section to
    # alpha*(beta + delta^2)

    global c
    global h
    global m_e
    global r_0

    print incoming_photon_energy_j

    alpha = (np.pi*r_0*r_0*m_e*c*c)/(incoming_photon_energy_j*incoming_photon_energy_j)
    beta = (outgoing_photon_energy_j/incoming_photon_energy_j) + (incoming_photon_energy_j/outgoing_photon_energy_j) - 1
    delta = 1-((incoming_photon_energy_j/outgoing_photon_energy_j)-1)*(m_e*c*c/incoming_photon_energy_j)

    print alpha
    print beta
    print delta

    return alpha*(beta + delta*delta)

def photon_wave_len_to_meV(photon_wave_len):

    global c
    global h

    return convert_from_j_to_MeV((c/photon_wave_len)*h)

print klein_nishina_fractional_cross_section_energy(convert_from_MeV_to_j(2), convert_from_MeV_to_j(np.arange(0.1,1.5,0.1)))

#wave_len_vec = np.arange(1e-13, 50e-13, 1e-13)
#
#incoming_e = photon_wave_len_to_meV(wave_len_vec)
#
#fig = plt.figure()
#
#angle_theta_vec = np.arange(0,2*np.pi/2,np.pi/8)
#
#for i in range(len(angle_theta_vec)):
#
#    angle_theta = angle_theta_vec[i]
#    outgoing_e = compton_scatter(wave_len_vec, angle_theta)
#    plt.plot(incoming_e, outgoing_e)
#
#plt.show()

outgoing_energy_vec = np.arange(0.1,0.2,0.01)
outgoing_energy_vec_j = convert_from_MeV_to_j(outgoing_energy_vec)
#
#
foo = klein_nishina_fractional_cross_section_energy(convert_from_MeV_to_j(0.2), outgoing_energy_vec_j)

#
#foo = klein_nishina_fractional_cross_section_energy(convert_from_MeV_to_j(0.5), outgoing_energy_vec_j)
#
plt.figure()
plt.plot(outgoing_energy_vec, foo)
plt.show()



