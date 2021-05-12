import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def transition_emission(A, niveau):
    if A > 1:
        A = A - 1
    else:
        A = niveau

    return A

def level_emissions(n_atoms, n_photons, niveau):
   
    A = np.ones(n_atoms, dtype=np.int8)
    N_1 = np.zeros(n_photons)                
    N_2 = np.zeros(n_photons)   
    N_3 = np.zeros(n_photons)   
    N_4 = np.zeros(n_photons)   
    N_high = np.zeros(n_photons)   

    for i in np.arange(n_photons):
        atom_no = np.random.randint(0, n_atoms)#bestimme Atome für Übergang
        A[atom_no] = transition_emission(A[atom_no], niveau)   # Übergang, falls A_i 
        N_1[i] = (A == 1).sum()
        N_2[i] = (A == 2).sum()
        N_3[i] = (A == 3).sum() 
        N_4[i] = (A == 4).sum()
        N_high[i]  = (A > 1).sum()
        
    phothons = np.arange(n_photons)
    plt.clf()
    plt.plot(phothons, N_1, label="$N_1(t)$")
    plt.plot(phothons, N_high, label="$N_{high}(t)$")
    plt.xlabel("Photonen")
    plt.ylabel("Besetzungsdichte $N$ /w.E.")
    plt.legend()
    plt.grid()

    buff = BytesIO()
    plt.savefig(buff, format='png')
    buff.seek(0)
    img_png = buff.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')
    buff.close()

    data = {
        'chart': graph, 
        'x': phothons.tolist(),
    }
    
    return data
    
