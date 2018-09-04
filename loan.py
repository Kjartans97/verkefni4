lan_int = int(input("Input the cost of the item in $: ")) #læt notenda skrifa inn upphæð láns

man_fjoldi = 0              #núllstilli mánuðina til að geta telja þá síðar
total_vextir = 0            #núllstilli vextina til að geta talið þá síðar

if lan_int > 1000:      #set inn if setningu sem segir að ef lánið er stærra en $1000 eru vextir 2% annars 1,5%
    vextir = 0.02
else:
    vextir = 0.015

while lan_int > 0:          #set while lykkju í gang, á meðan lánið er stærra en 0 keyrir forritið while lykkjuna
    interest = vextir * lan_int
    if lan_int > 50:        #ef lánið er hærri en $50 er greiðslan $50
        payment = 50.0        #greiðslan = $50
        lan_int = lan_int + (interest - payment)    #hér er eftirstaða láns eftir afborgunina
    else:                   #hér er lánið undir $50 og því klárast lánið (síðasta greiðslan er hér)
        payment = lan_int + interest
        lan_int = 0.0
    man_fjoldi = man_fjoldi + 1     #fjöldi mánaðar reiknaður
    total_vextir = total_vextir + interest      #tótal vextirnir reiknaðir

    #hér er svo forritið prentað með round fallinu með 2 aukastöfum
    print('Month: '+str(man_fjoldi)+' Payment: '+str(round(payment,2))+
    ' Interest paid: '+str(round(interest,2))+' Remaining debt: '+str(round(lan_int,2)))

print('')           #hér er bilið sett inn
print('Number of months: ' +str(man_fjoldi))    #hér er prentaður heildarfjöldi mánaðar
print('Total interest paid: ' +str(round(total_vextir,2)))      #hér er prentað heildarvaxtagjöld