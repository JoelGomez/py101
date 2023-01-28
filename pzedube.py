"""_summary_
    Evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresandolo en horas y minutos. las horas van de 0 a 23 hrs y los minutos de 0 a 59. el resultado debe ser mostrado en la consola

    Ej. si el evento inicia a las 12:17 y dura 59 minutos terminará a las 13:16
    input:23:58 642 output: 10:40
"""

def hr_fin(hr_ini: int, min_ini: int, duracion: int):
    
    min_tot = min_ini + duracion
    hrs = min_tot // 60
    hr_fin = hr_ini + hrs

    if hr_fin >= 24:
        hr_fin = hr_fin % 24

    min_fin = min_tot % 60
     
    return(hr_fin, min_fin)
    

print(hr_fin(12,17,59))
print(hr_fin(23,58,642))