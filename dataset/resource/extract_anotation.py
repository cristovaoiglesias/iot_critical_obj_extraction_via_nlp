# Python program to
# demonstrate reading files
# using for loop


#("The sensor preferably is either an anisotopic magnetoresistive element or a spin valve element less than 0.6 m wide.", {"entities": [(4, 10, "Device")]})


import glob
filesname=glob.glob("*.txt")

entity='Resource'
for file in filesname:
    instance=file.split('.')[0]
    instance=instance.replace('_',' ')
    file = open(file, 'r')
    count = 0
    for line in file:
        count += 1
        if "Show More S" in str(line.strip()) or "Examples from Classical" in str(line.strip()) :
            continue
        idx1=str(line.strip()).find(instance)
        idx2=idx1+len(instance)
        sentence=str(line.strip()).replace('"',"'")
        print("(\""+sentence+"\",{\"entities\": [("+str(idx1)+","+str(idx2)+",\""+entity+"\")]}),")
    # Closing files
    file.close()

# import random
#
# train=[('My materials included an BeagleBone Uno, an BeagleBone Ethernet shield, a bunch of 10mm diffused white LEDs and a box kindly donated by National Journal graphic artist Libby Isenstein.',{'entities': [(25,35,'Device')]}),
# ('These guys hooked up an air freshener to a Twitter account via an BeagleBone controller.',{'entities': [(66,76,'Device')]}),
# ('With an BeagleBone uno, 4 AA batteries and 128 LEDs. I always wanted a playable Tshirt, well now I made one myself.',{'entities': [(8,18,'Device')]}),
# ('With a simple BeagleBone board, heart or respiratory rate can be tracked in a player.',{'entities': [(14,24,'Device')]})]
#
# random.shuffle(train)
# testdtsize=round(len(train)*0.35)
#
# test=[]
# for i in train:
#     sentence=i[0]
#     enty=i[1]['entities']
#     test.append((sentence,enty))
#     print((sentence,enty))
# ("The temperature of the water bath is controlled by a microprocessor and a temperature sensor.", [(74, 92, "Device")])
