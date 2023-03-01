# Python program to
# demonstrate reading files
# using for loop


#("The sensor preferably is either an anisotopic magnetoresistive element or a spin valve element less than 0.6 m wide.", {"entities": [(4, 10, "Device")]})


import glob
filesname=glob.glob("*.txt")

# ft='QR_code.txt'

entity='Device'
for file in filesname:
    # file='QR_code.txt'
    instance=file.split('.')[0]
    # print("\n",instance)
    instance=instance.replace('_',' ')
    # print("\n",instance)
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




# # Opening file
# file = open('notebook.txt', 'r')
# count = 0
# device="notebook"
# for line in file:
#     count += 1
#     idx1=str(line.strip()).find(device)
#     idx2=idx1+len(device)
#
#     print("('"+str(line.strip())+"',{'entities': [("+str(idx1)+","+str(idx2)+",'Device')]})")
# # Closing files
# file.close()

# ('In the notebook were pretty drawings, simple little doodles of simple little joys.',{'entities': [(7,15,'Device')]})
