from do_photometry import view_image
import os
from glob import glob
from astropy.io import fits
import astroalign as aa

image_path='/mnt/eac99553-b108-449e-bf41-0716c975df8b/TRT-data/NGC 5947/band_wise/R_band/aligned'
calibration_path='/mnt/eac99553-b108-449e-bf41-0716c975df8b/TRT-data/calibration/'
filename='*fits'

s=sorted(glob(os.path.join(image_path,filename)))
#print(len(s))
ref=s[1]

view_image(s[72],10) #46,47,48,49 do again
#image=fits.open(ref)
#reference_image=image[0].data
'''
for i in range(50,len(s)):
    image_data=fits.open(s[i])
    source_image=image_data[0].data
    header=image_data[0].header
    image_aligned,footprint=aa.register(source_image,reference_image)

    aligned_file=s[i].replace('.fits','')
    fits.writeto(aligned_file+'_aligned'+'.fits',image_aligned,header,overwrite=True)

    print('No. %i done'%i)
'''