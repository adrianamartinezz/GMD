
from esa import sa
import numpy as np
import matplotlib.pyplot as plt

pysimauto = sa("C:\\Users\\Adriana Martinez\\Desktop\\PowerWorld\\DallasCase")

pysimauto.runScriptCommand("GICClear")
#fieldarray= ["BusNum3W:1", "GICQLosses","GICBlockDevice"]
fieldarray2=["BusNum3W","BusNum3W:1","BusNum3W:2","LineCircuit", "GICBlockDevice"]
fieldarray = ["BusNum3W","BusNum3W:1","BusNum3W:2","LineCircuit", "GICQLosses", "GICBlockDevice"]

#pysimauto.runScriptCommand('LoadAux("C:\\Users\\cklauber\\Documents\\PowerWorld\\texasb3d.aux",NO)')
#What does this line of command do???
#change to uniform field


size=1 #iteration count
ii = np.zeros((size,1))
res = np.zeros((size,861))
for i in range(size):
    pysimauto.runScriptCommand('GICCalculate(3.11,90,"NO")')
    data=pysimauto.getParametersMultipleElement('gicxformer', fieldarray, '')
    ar= np.asarray(data)

    losses=(ar[4,:])
    losses_flt=losses.astype(np.float) #takes the transformer losses
    total_loss=sum(losses_flt)
    print("The total Mvar losses before GIC blocking device placement is:", total_loss)
    xfr_num=(ar[1,:])
    list_losses_ar=np.asarray([])
    values=[]
    #len=length
    for i in range (len(losses_flt)):
        #j=losses[i]
        test=losses_flt[i]
        if (test>50): #looks for transformers that have losses over 50 Mvar
            list_losses_ar=np.append([list_losses_ar],[xfr_num[i]]) #turns into list
            for i in range (len())
            fieldarray_list= [data[0][i], data[1][i], data[2][i], data[3][i], "Yes"]
            values.extend(fieldarray_list)
            simOutput = pysimauto.changeParameters('gicxformer', fieldarray2, fieldarray_list)


    #losses_str = list_losses_ar.astype(np.str) #turns lsit into string
    #print(losses_str)

    #print(simOutput)

    pysimauto.runScriptCommand('GICCalculate(3.11,90,"NO")')
    post_data = pysimauto.getParametersMultipleElement('gicxformer', fieldarray, '')
    ar2 = np.asarray(post_data)
    post_losses = (ar2[4, :])
    losses_flt2 = post_losses.astype(np.float)  # takes the transformer losses
    p_total_loss = sum(losses_flt2)
    print("The total Mvar losses after GIC blocking device placement is:" ,p_total_loss)

    pysimauto.saveCaseAs("C:\\Users\\Adriana Martinez\\Desktop\\PowerWorld\\.pwdDallasCase2")

















