#!/usr/bin/python (EASTER EGG: added just because shbang sounds lit)

from PIL import Image 
import sys

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m' 


def menu(): 
    choice = int(input("Choose (1) to Encode or (2) to Decode > ")) 
    if (choice == 1): 
        encode() 
        
    elif (choice == 2): 
        print("Decoded String > " + decode())
        

    else: 
        print (colors.RED + ("Incorrect input") + colors.STOP)
        print (colors.RED + ('Exiting the code...') + colors.STOP)
        sys.exit() 

def bitconv(data): 
        
         
        newd = [] 
        
        for i in data: 
            newd.append(format(ord(i), '08b')) 
        return newd 
        
 
def pixeller(pixel, data): 
    
    datalist = bitconv(data) 
    lendata = len(datalist) 
    imdata = iter(pixel) 

    for i in range(lendata):  
        pixel = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]] 
                                     
        for j in range(0, 8): 
            if (datalist[i][j]=='0') and (pixel[j]% 2 != 0): 
                
                if (pixel[j]% 2 != 0): 
                    pixel[j] -= 1
                    
            elif (datalist[i][j] == '1') and (pixel[j] % 2 == 0): 
                pixel[j] -= 1
                
 
        if (i == lendata - 1): 
            if (pixel[-1] % 2 == 0): 
                pixel[-1] -= 1
        else: 
            if (pixel[-1] % 2 != 0): 
                pixel[-1] -= 1

        pixel = tuple(pixel) 
        yield pixel[0:3] 
        yield pixel[3:6] 
        yield pixel[6:9] 

def encode_enc(out_img, data): 
    w = out_img.size[0] 
    (x, y) = (0, 0) 
    
    for pixel in pixeller(out_img.getdata(), data): 
        out_img.putpixel((x, y), pixel) 
        if (x == w - 1): 
            x = 0
            y += 1
        else: 
            x += 1
            
def encode(): 
    img = input("Enter image name > ")+".png" 
    image = Image.open(img, 'r') 
    
    data = input("Enter data to be encoded > ") 
    if (len(data) == 0): 
        print ('No message entered')
        print ('Exiting the code...')
        sys.exit() 
        
    out_img = image.copy() 
    encode_enc(out_img, data) 
    
    new_img_name = input("Enter the name of new image > ") +".png"
    out_img.save(new_img_name, str(new_img_name.split(".")[1].upper())) 


def decode(): 
    img = input("Enter image name > ")+".png" 
    image = Image.open(img, 'r') 
    
    data = '' 
    imgdata = iter(image.getdata()) 
    
    while (True): 
        pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]] 
        binstr = '' 
        for i in pixels[:8]: 
            if (i % 2 == 0): 
                binstr += '0'
            else: 
                binstr += '1'
        data += chr(int(binstr, 2)) 
        if (pixels[-1] % 2 != 0): 
            output = open("decoded.txt","w")
            output.write(data)
            output.close()
            return data
            

            

menu()