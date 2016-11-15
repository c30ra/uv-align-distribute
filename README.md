# [Blender Add-on] uv-align-distribute
This add-on help align and distribute uv island in the uv space

**Warning in order to use this, you need to install networkx python package**:  
To install networkx you need to install pip on your Blender python distribution:
- First download get-pip.py [from here](https://pip.pypa.io/en/stable/installing/)
- Then locate your Blender installation folder. On Windows should be:

on 32bit machine
> C:\Programs(x86)/Blender Foundation/Blender

on 64bit machine
> C:\Programs\Blender Foundation/Blender

- then go to 2.78(this may change depending on your Blender version)\python
- right click on "bin" folder while holding shift, and on context menu click Copy as path.
- Open a terminal as administrator and type
 > cd (paste the path here)  
 > python.exe "location_to_get-pip"/get-pip.py

 i.e: python.exe C:\get-pip.py
- wait until it finish
- then run

 > python.exe -m pip install --upgrade pip  
 > python.exe -m pip install networkx


Now you should ready to go and follow the next step:

  * download the zip file(using the github green button)  
  * In blender user preference go to Add-ons page  
  * click on install from file  
