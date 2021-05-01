from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import math
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Doppelspalt
def doppelspalt(response):
    return render(response, 'main/experiments/doppelspalt/index.html')

# Return the data
def doppelspalt_api(response, lam, b, d, angle):
    
        # ------------------------->  EINGABE: Spaltbreite in mm
    b_mm = b
    # Spaltbreite in m: b
    b = b_mm / 1000
    # ------------------------->  EINGABE: Spaltabstand in mm
    d_mm = d
    # Spaltabstand in m: d
    d = d_mm / 1000
    # ------------------------->  EINGABE: Wellenlänge in Mikrometer 
    lambd_micro = lam/1000
    # Wellenlänge in Meter: lambd
    lambd = lambd_micro / 1000000
    # ------------------------->  EINGABE: Winkelabstand zwischen den Doppelstern-
    #                                      komponenten A und B in Bogensekunden 
    rho_sek = 2 
    # Winkelabstand in Grad: rho
    rho = rho_sek / 3600 * np.pi / 180
    # ------------------------->  EINGABE: Intensitätsverhältnis I_B / I_A) der 
    #                                      Doppelsternkomponenten (w, 0 ...1)
    w = 1.0
    # ------------------------->  EINGABE: Winkelbereich der ausgegebenen 
    #                                      Intensitätsverteilung in Bogensekunden  
    a_limit = angle
    #Erzeugung der Ausgabewinkelliste
    a_list = np.linspace(-a_limit, a_limit, 2000) 
    a_list_deg = a_list / 3600 * np.pi / 180
        #--------------------------------------------------------------------------
    # Berechnung der Intensität für Doppelsternkomponente A (die hellere Komponent)
    argb_A = math.pi * b * np.sin(a_list_deg) / lambd
    argd_A = math.pi * d * np.sin(a_list_deg) / lambd
    I_list_A = np.cos(argd_A)**2 * (np.sin(argb_A) / argb_A)**2
    # Berechnung der Intensität für Doppelsternkomponente B 
    # (die i.d.R. um den Winkel roho verschobene schwächere Komponente)
    argb_B = math.pi * b * np.sin(a_list_deg + rho) / lambd
    argd_B = math.pi * d * np.sin(a_list_deg + rho) / lambd
    I_list_B = np.cos(argd_B)**2 * (np.sin(argb_B) / argb_B)**2
    # Inkohärente Summe der Intensitäten der Doppelsternkomponenten A+B 
    I_list = I_list_A + I_list_B
    #return(I_list_A, I_list_B, I_list)
    #--------------------------------------------------------------------------

    #I_list_A, I_list_B, I_list = Doppelsterninterferogramm(b,d,rho,lambd,w,a_list_deg) 
    plt.clf()
    plt.plot(a_list, I_list_A, label="Intensität Spalt A")  
    plt.plot(a_list, I_list_B, label="Intensität Spalt B")  
    plt.plot(a_list, I_list, label="gesamt Intensität")  
    plt.xlabel("Winkel in Grad")
    plt.ylabel("Intensität in %")
    plt.legend()
 
    buff = BytesIO()
    plt.savefig(buff, format='png')
    buff.seek(0)
    img_png = buff.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')
    buff.close()
    
    
    chart, dataA, dataB, dataAll = [graph, I_list_A, I_list_B, I_list]
    data = {
        'chart': chart, 
        'x': a_list.tolist(),
        'dataA': dataA.tolist(),
        'dataB': dataB.tolist(),
        'dataAll': dataAll.tolist()
    }
    return JsonResponse(data, safe=False)