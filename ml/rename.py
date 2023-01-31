
import os
def main():
    folder = "../train/train3/"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Serial3_No{str(count)}.tif"
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{dst}"
        os.rename(src, dst)
 

    folder = "../train/train4/"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Serial4_No{str(count)}.tif"
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{dst}"
        os.rename(src, dst)

    folder = "../train/train5/"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Serial5_No{str(count)}.tif"
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{dst}"
        os.rename(src, dst)

    folder = "../train/train6/"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Serial6_No{str(count)}.tif"
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{dst}"
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
    main()