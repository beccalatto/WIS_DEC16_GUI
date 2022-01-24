# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:12:28 2022

@author: becca
"""
from pathlib import Path
import PySimpleGUI as sg
import os.path
from PIL import Image, ImageTk
import cv2


#print(sg.Window.get_screen_size())
w, h = sg.Window.get_screen_size()
font_heading = ("Arial", 15)
font_subheading = ("Arial", 13)
font_subtext = ("Arial", 11)
        

images_data_folder = Path(str(Path.cwd()) + "/images/")
dayplot_data_folder = Path(str(Path.cwd()) + "/DAYPLOTS/")

# Resize PNG file to size
size = (int(w/3+w/3), int(0.67*h))
im_b = Image.open(images_data_folder / 'background.png')
im_b = im_b.resize(size, resample=Image.BICUBIC)

# First the window layout in 2 columns
dayplot_viewer = [
#    [
#        sg.Text("Dayplot viewer", key='-text-', font=font_heading)
#    ],
    [sg.Text(" ", key='-STATION_UPDATE_r1-', font=font_subtext)],
    [sg.Text(" ", key='-STATION_UPDATE_r2-', font=font_subtext)],
    [
         sg.Image(size=(w/3+w/3,int(0.67*h)), pad = (int(0.01*w),int(0.04*h)), key='-IMAGE_L-')
    ],
    [sg.Text("Change vertical axes by:", key='-text-', font=font_subheading)],
    [sg.Radio('50%', "ZOOM",key='-ZOOMOUT-', font=font_subtext),\
    sg.Radio('100%', "ZOOM",key='-NOZOOM-', default=True, font=font_subtext),\
    sg.Radio('250%', "ZOOM",key='-ZOOMIN_1-', font=font_subtext),\
    sg.Radio('500%', "ZOOM",key='-ZOOMIN_2-', font=font_subtext),\
    sg.Button('Click to update', key='-ZOOM-', font=font_subheading,enable_events=True)],\
    [sg.Text('_'*30,pad=(int(0.02*w),int(0.04*h)))], 
    #[sg.Image(key="-IMAGE-")],
]
size = (int(w/3.5), int(h/3))
im_w = Image.open(images_data_folder / 'BB_RESET.png')
im_w = im_w.resize(size, resample=Image.BICUBIC)
# For now will only show the name of the file that was chosen
dayplot_choices = [
    [sg.Text("Whillans Ice Stream", key='-text-', font=font_heading)],
    [sg.Text("2010 - 2011 deployment", key='-text-', font=font_subheading)],
    [sg.Image(size=(w/4,h/3), pad = (0,int(0.01*h)), key='-IMAGE_TR-')],
    [sg.Text('_'*30)], 
    [sg.Text("Pick which station(s) to plot:", key='-text-', font=font_subheading)],
    [sg.Checkbox('BB01', key='-BB01-', font=font_subtext), \
     sg.Checkbox('BB03', key='-BB03-', font=font_subtext),sg.Checkbox('BB04', key='-BB04-', font=font_subtext), sg.Checkbox('BB06', key='-BB06-', font=font_subtext),\
     sg.Checkbox('BB07', key='-BB07-', font=font_subtext)], 
    [sg.Checkbox('BB08', key='-BB08-', font=font_subtext),\
     sg.Checkbox('BB10', key='-BB10-', font=font_subtext), sg.Checkbox('BB11', key='-BB11-', font=font_subtext),\
     sg.Checkbox('BB12', key='-BB12-', font=font_subtext), sg.Checkbox('BB13', key='-BB13-', font=font_subtext)],\
     [sg.Checkbox('BB14', key='-BB14-', font=font_subtext), sg.Checkbox('BB15', key='-BB15-', font=font_subtext),\
     sg.Checkbox('BB16', key='-BB16-', font=font_subtext), sg.Checkbox('BB17', key='-BB17-', font=font_subtext)],
     [sg.Button('Reset', key='-RESET-', font=font_subheading,enable_events=True),sg.Button('Select all', key='-ALL-', font=font_subheading,enable_events=True)],    
    [sg.Text("Pick a component:", key='-text-', font=font_subheading)],
    [sg.Radio('HHZ', "COMPONENT",key='-HHZ-', default=True, font=font_subtext),
    sg.Radio('HHE', "COMPONENT",key='-HHE-', font=font_subtext),sg.Radio('HHN', "COMPONENT",key='-HHN-', font=font_subtext)],
    [sg.Text("Pick a filter:", key='-text-', font=font_subheading)],
    [sg.Radio('No filter', "FILTER",key='-NOFILTER-', default=True, font=font_subtext),
    sg.Radio('Lowpass 1 Hz', "FILTER",key='-LOWPASS-', font=font_subtext),sg.Radio('Highpass 1 Hz', "FILTER",key='-HIGHPASS-', font=font_subtext)],
    [sg.Text("Pre-processing:", key='-text-', font=font_subheading)],
    [sg.Radio('Detrended', "PREP",key='-DETREND-', default=True, font=font_subtext),
    sg.Radio('Detrended, frequency normalised', "PREP",key='-NORM-', font=font_subtext)],
    [sg.Button('Load', key='-LOAD-', font=font_subheading,enable_events=True)],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(dayplot_viewer,size=(w/3+w/3,h)),
        sg.VSeperator(pad=int(0.0075*w)),
        sg.Column(dayplot_choices,size=(w/3,h)),
    ]
]

window = sg.Window('Dayplot Viewer', layout, location=(0,0), size=(w,h), finalize=True)

# Convert im to ImageTk.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im_b)
window['-IMAGE_L-'].update(data=image)
image = ImageTk.PhotoImage(image=im_w)
window['-IMAGE_TR-'].update(data=image)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-ALL-":  # RESET checkboxes
        #print(event)
        #print(values)
        #print(type(values))
        count = 0
        for key in values:
            count = count + 1
            #print(count)
            if count > 4 and count <= 18:
                window[key].update(True)
    elif event == "-RESET-":  # RESET checkboxes
        #print(event)
        #print(values)
        #print(type(values))
        count = 0
        for key in values:
            count = count + 1
            #print(count)
            if count > 4 and count <= 18:
                window[key].update(False)
                
    elif event == "-LOAD-" or event == "-ZOOM-":  # 
        #print(event)
        #print(values)
        #print(type(values))
        # Station picks:
        stations = []
        count = 0
        for key in values:
            count = count + 1
            #print(count)
            if count > 4 and count <= 18:
                print(values[key])
                if values[key] == True:
                    stations.append(key.replace("-", ""))
        # Component picks:
        if values["-HHZ-"] == True:
            comp = 'HHZ'
        elif values["-HHN-"] == True:
            comp = 'HHN'
        elif values["-HHE-"] == True:
            comp = 'HHE' 
        # Pre-processing choice:
        if values["-DETREND-"] == True:
            prep = 'Detrended'
        elif values["-NORM-"] == True:
            prep = 'FrequencyNormalised'
        # Filter choice:
        if values["-NOFILTER-"] == True:
            filt = 'NoFilter'
        elif values["-LOWPASS-"] == True:
            filt = 'LPFilter'
        elif values["-HIGHPASS-"] == True:
            filt = 'HPFilter'
        # Adjust zoom:
        if values["-NOZOOM-"] == True:
            zoom = ''
        elif values["-ZOOMOUT-"] == True:
            zoom = '50'
        elif values["-ZOOMIN_1-"] == True:
            zoom = '250'
        elif values["-ZOOMIN_2-"] == True:
            zoom = '500'
        elif values["-ZOOMIN_3-"] == True:
            zoom = '1000'
        if len(stations) == 1:
            try:
                #print(('DAYPLOT_DATE_20101216_STATION_%s_COMPONENT_%s_FILTER_%s_%s.PNG' %(stations[0],comp,filt,prep))
                fn = dayplot_data_folder / ('DAYPLOT_DATE_20101216_STATION_%s_COMPONENT_%s_FILTER_%s_%s%s.PNG' %(stations[0],comp,filt,prep,zoom))
                img = Image.open(fn).convert("RGBA")
                size = (int(w/3+w/3)-int(0.02*w), int(0.67*h)-int(0.04*h))
                img = img.resize(size, resample=Image.BICUBIC)
                img.save(images_data_folder / 'temp.png','PNG')
                window["-IMAGE_L-"].update(images_data_folder / 'temp.png')
                
                fn = images_data_folder / '%s.PNG' %(stations[0])
                size = (int(w/3.5), int(h/3)-int(0.01*h))
                img_w = Image.open(fn).convert("RGBA")
                img_w = img_w.resize(size, resample=Image.BICUBIC)
                img_w.save(images_data_folder / 'temp.png','PNG')
                window["-IMAGE_TR-"].update(images_data_folder / 'temp.png')
                window["-STATION_UPDATE_r1-"].update(' ')
                window["-STATION_UPDATE_r2-"].update(' ')

            except:
                pass   
        elif len(stations) > 1:
            try:
                fn = dayplot_data_folder / ('DAYPLOT_DATE_20101216_STATION_%s_COMPONENT_%s_FILTER_%s_%s%s.PNG' %(stations[0],comp,filt,prep,zoom))
                #bg_img = Image.open(fn).convert("RGBA")
                bg_img = cv2.imread(fn)
                for ii in range(1,len(stations)):
                    #print(('DAYPLOT_DATE_20101216_STATION_%s_COMPONENT_%s_FILTER_%s_%s.PNG' %(stations[ii],comp,filt,prep))
                    fn = dayplot_data_folder / ('DAYPLOT_DATE_20101216_STATION_%s_COMPONENT_%s_FILTER_%s_%s%s.PNG' %(stations[ii],comp,filt,prep,zoom))
                    #fg_img = Image.open(fn).convert("RGBA")
                    fg_img = cv2.imread(fn)
                    if ii == 1:
                        new_img = cv2.addWeighted(bg_img, 0.7, fg_img, 0.3, 0)
                        continue
                    else:
                        new_img = cv2.addWeighted(new_img, 0.7, fg_img, 0.3, 0)
         
                    #if ii == 1:
                    #    new_img = Image.blend(bg_img, fg_img, 0.5)
                    #else:
                    #    new_img = Image.blend(new_img, fg_img, 0.5)
                cv2.imwrite(dayplot_data_folder / 'temp.png',new_img)
                new_img = Image.open(dayplot_data_folder / 'temp.png').convert("RGBA")
                size = (int(w/3+w/3)-int(0.01*w), int(0.67*h)-int(0.04*h))
                new_img = new_img.resize(size, resample=Image.BICUBIC)
                new_img.save(dayplot_data_folder / 'temp.png','PNG')
                #src = cv2.imread('D:\\Seagate Dashboard\\UTAS 2019-2021\\1_Masters_2020\\Winberry station plots\\ALL_BB_STATIONS\\DAYPLOT_REPOSITORY\\DAYPLOTS\\temp.png')
                #grayImage = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
                #(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
                #cv2.imwrite('D:\\Seagate Dashboard\\UTAS 2019-2021\\1_Masters_2020\\Winberry station plots\\ALL_BB_STATIONS\\DAYPLOT_REPOSITORY\\DAYPLOTS\\temp.png',blackAndWhiteImage)                
                window["-IMAGE_L-"].update(dayplot_data_folder / 'temp.png')
                if len(stations) < 5:
                    window["-STATION_UPDATE_r1-"].update('Ignore station label. Now plotting a composite of: ' + ' , '.join(stations))
                    window["-STATION_UPDATE_r2-"].update(' ')
                else:
                    window["-STATION_UPDATE_r1-"].update('Ignore station label. Now plotting a composite of: ' + ' , '.join(stations[0:6]))
                    window["-STATION_UPDATE_r2-"].update(' , '.join(stations[6:len(stations)]))
                
                size = (int(w/3.5), int(h/3))
                img_w = Image.open(images_data_folder / 'BB_RESET.png')
                img_w = img_w.resize(size, resample=Image.BICUBIC)
                img_w.save(images_data_folder / 'temp.png','PNG')
                window["-IMAGE_TR-"].update(images_data_folder / 'temp.png')
            except:
                pass        
        
        
window.close()