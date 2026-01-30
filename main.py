import os
import sys
import cv2
import easygui
import imageio
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import *


def landscape():
    top_1 = tk.Tk()
    top_1.geometry('1000x500')
    top_1.title('Image Cartoonification ( Landscape )')
    top_1.configure(background='#1cb8a1')
    label_1 = Label(top_1, background='#CDCDCD', font=('Times New Roman', 10, 'bold'))

    def upload_landscape():

        image_path = easygui.fileopenbox()
        cartoonify_landscape(image_path)

    def cartoonify_landscape(image_path):

        original_image = cv2.imread(image_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

        if original_image is None:
            print("Cannot find any image ! Choose an appropriate file !")
            sys.exit()

        resized_1 = cv2.resize(original_image, (1290, 960))
        fig_1 = plt.imshow(resized_1, cmap='gray')
        print("\n", fig_1)

        gray_scale = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        resized_2 = cv2.resize(gray_scale, (1290, 960))
        fig_2 = plt.imshow(resized_2, cmap='gray')
        print("\n", fig_2)

        smooth_gray_scale = cv2.medianBlur(gray_scale, 5)
        resized_3 = cv2.resize(smooth_gray_scale, (1290, 960))
        fig_3 = plt.imshow(resized_3, cmap='gray')
        print("\n", fig_3)

        get_edge = cv2.adaptiveThreshold(smooth_gray_scale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        resized_4 = cv2.resize(get_edge, (1290, 960))
        fig_4 = plt.imshow(resized_4, cmap='gray')
        print("\n", fig_4)

        color_image = cv2.bilateralFilter(original_image, 9, 300, 300)
        resized_5 = cv2.resize(color_image, (1290, 960))
        fig_5 = plt.imshow(resized_5, cmap='gray')
        print("\n", fig_5)

        cartoon_image = cv2.bitwise_and(color_image, color_image, mask=get_edge)
        resized_6 = cv2.resize(cartoon_image, (1290, 960))
        fig_6 = plt.imshow(resized_6, cmap='gray')
        print("\n", fig_6)

        images = [resized_1, resized_2, resized_3, resized_4, resized_5, resized_6]

        fig, axes = plt.subplots(3, 2, figsize=(10, 10), subplot_kw={'xticks': [], 'yticks': []},
                                 gridspec_kw=dict(hspace=0.1, wspace=0.1))
        for i, axis in enumerate(axes.flat):
            axis.imshow(images[i], cmap='gray')

        save_image_landscape = Button(top_1, text="Save Cartoon Image", command=lambda: save(resized_6, image_path),
                                      padx=30, pady=5)
        save_image_landscape.configure(background='#080000', foreground='white', font=('Times New Roman', 10, 'bold'))
        save_image_landscape.pack(side=TOP, pady=50)

        plt.show()

    def save(resized_image, image_path):

        new_name = "Cartoonified Image"
        file_path = os.path.dirname(image_path)
        extension = os.path.splitext(image_path)[1]
        path = os.path.join(file_path, new_name + extension)
        cv2.imwrite(path, cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR))
        I = "Image saved as " + new_name + " at " + path
        tk.messagebox.showinfo(title=None, message=I)

    upload_landscape = Button(top_1, text="Cartoonify An Image", command=upload_landscape, padx=10, pady=5)
    upload_landscape.configure(background='#080000', foreground='white', font=('Times New Roman', 10, 'bold'))
    upload_landscape.pack(side=TOP, pady=50)

    top_1.mainloop()


def portrait():
    top_2 = tk.Tk()
    top_2.geometry('1000x500')
    top_2.title('Image Cartoonification ( Portrait )')
    top_2.configure(background='#1cb8a1')
    label_2 = Label(top_2, background='#CDCDCD', font=('Times New Roman', 10, 'bold'))

    def upload_portrait():

        image_path = easygui.fileopenbox()
        cartoonify_portrait(image_path)

    def cartoonify_portrait(image_path):

        original_image = cv2.imread(image_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

        if original_image is None:
            print("Cannot find any image ! Choose an appropriate file !")
            sys.exit()

        resized_1 = cv2.resize(original_image, (960, 1290))
        fig_1 = plt.imshow(resized_1, cmap='gray')
        print("\n", fig_1)

        gray_scale = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        resized_2 = cv2.resize(gray_scale, (960, 1290))
        fig_2 = plt.imshow(resized_2, cmap='gray')
        print("\n", fig_2)

        smooth_gray_scale = cv2.medianBlur(gray_scale, 5)
        resized_3 = cv2.resize(smooth_gray_scale, (960, 1290))
        fig_3 = plt.imshow(resized_3, cmap='gray')
        print("\n", fig_3)

        get_edge = cv2.adaptiveThreshold(smooth_gray_scale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        resized_4 = cv2.resize(get_edge, (960, 1290))
        fig_4 = plt.imshow(resized_4, cmap='gray')
        print("\n", fig_4)

        color_image = cv2.bilateralFilter(original_image, 9, 300, 300)
        resized_5 = cv2.resize(color_image, (960, 1290))
        fig_5 = plt.imshow(resized_5, cmap='gray')
        print("\n", fig_5)

        cartoon_image = cv2.bitwise_and(color_image, color_image, mask=get_edge)
        resized_6 = cv2.resize(cartoon_image, (960, 1290))
        fig_6 = plt.imshow(resized_6, cmap='gray')
        print("\n", fig_6)

        images = [resized_1, resized_2, resized_3, resized_4, resized_5, resized_6]

        fig, axes = plt.subplots(3, 2, figsize=(10, 10), subplot_kw={'xticks': [], 'yticks': []},
                                 gridspec_kw=dict(hspace=0.1, wspace=0.1))
        for i, axis in enumerate(axes.flat):
            axis.imshow(images[i], cmap='gray')

        save_image_portrait = Button(top_2, text="Save Cartoon Image", command=lambda: save(resized_6, image_path),
                                     padx=30, pady=5)
        save_image_portrait.configure(background='#080000', foreground='white', font=('Times New Roman', 10, 'bold'))
        save_image_portrait.pack(side=TOP, pady=50)

        plt.show()

    def save(resized_image, image_path):

        new_name = "Cartoonified Image"
        file_path = os.path.dirname(image_path)
        extension = os.path.splitext(image_path)[1]
        path = os.path.join(file_path, new_name + extension)
        cv2.imwrite(path, cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR))
        I = "Image saved as " + new_name + " at " + path
        tk.messagebox.showinfo(title=None, message=I)

    upload_portrait = Button(top_2, text="Cartoonify An Image", command=upload_portrait, padx=10, pady=5)
    upload_portrait.configure(background='#080000', foreground='white', font=('Times New Roman', 10, 'bold'))
    upload_portrait.pack(side=TOP, pady=50)

    top_2.mainloop()


while True:
    print("\n\nWELCOME TO IMAGE CARTOONIFICATION\n")
    print("\n1) Landscape Image")
    print("\n2) Portrait Image")
    print("\n3) Exit")
    choice = int(input("\nEnter your choice ( 1 to 3 ) : "))
    if choice == 1:
        landscape()
    elif choice == 2:
        portrait()
    elif choice == 3:
        print("\nThank You !\n")
        break
    else:
        print("\nEnter the correct choice !\n")
