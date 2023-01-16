
import os
def main():
   
    folder = "../data/train4/"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Image{str(count)}.tif"
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{dst}"
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
    main()