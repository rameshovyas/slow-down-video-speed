# Ramesh Vyas
# Script to slow down video speed
# Slow down all videos in a particular folder
import os
import subprocess
rootdir = os.getcwd()
count=0
print ("started slowing down the videos " + " in directory : " + rootdir)
for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    if filename.endswith(".mp4"):    
        try:    
            outfile=os.path.splitext(filename)[0] +"_slow.mp4"             
            sou=os.path.join(subdir, filename)      
            des=os.path.join(subdir, outfile)
            print (sou)
            subprocess.call(['ffmpeg ' + ' -i ' + sou + " -vf setpts=4*PTS " + des],shell=True)
            count=count+1            
        except:          
            continue      
    else:
        continue
print("total " + str(count) + " conversions done, thank you for using tool")



