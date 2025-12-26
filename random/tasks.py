def lucky_bilet(bilet):
    bilet = str(bilet)
    if len(bilet) % 2 != 0:
        center = len(bilet) // 2
        pervi_srez = bilet[:center]
        vtoroi_srez = bilet[center + 1:]
        shet = 0
        for i in pervi_srez:
            shet += int(i)

        shet2 = 0
        for i in vtoroi_srez:
            shet2 += int(i)

        if shet == shet2:
            return "Вы счастливчик!"
        
print(lucky_bilet(131))