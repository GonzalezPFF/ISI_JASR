# ISI_JASR
Ionospheric Spectral Imager, simulations of quiet conditions and ML algorithms

FOR THE SIMULATIONS,

First extract the output-30.dat ... output-45.dat datafiles created from LFSM LWA1 model (Dowell et al., 2017) from the following link

https://drive.google.com/drive/folders/12iOMVQonEKwAM1kxTg91WnBbR4jcktms?usp=drive_link

Then, execute the .py files 

lectura2.py -> lectura4.py (optional) -> lectura4_dbmcorr.py -> lectura5_imagenes.py (optional) -> lectura5_imagenes_dbmcorr.py -> lectura6_imagenes_3x3.py (optional) -> lectura6_imagenes_7x7.py -> lectura6_imagenes_7x7_dbmcorr_TEST38.2.py -> lectura6_imagenes_7x7_LITE.py (optional) -> lectura7_database_creation_PNRANDOM.py (optional) -> lectura7_database_creation_PNREAL.py -> lectura8_new_image_display_from_database.py (optional) -> lectura9_absorption_database_creation.py -> lectura10_abs_coef_image_display_from_database.py (optional) -> lectura11_abs_event_image_display_direct.py (optional) 

to create the simulated databases based on the LFSM (Dowell et al., 2017) outputs, which are necessary to reproduce the final results of the paper.

As an alternative, you can also download dataset_real.csv and dataset_images_as_columns.csv to explore and/or reproduce the Jupyter notebooks (.ipynb) attached in the main Google Drive folder.

FOR TRELEW'S ANALYSIS,

Download the images1103_TRW.csv and/or explore the notebook "newfigs_REMAKE_OG_FINAL_1103_V6DISPLAY_ML_TO_ISI_OUTPUT.ipynb". You will find this in the main Google Drive folder.

You are free to download and modify the code and/or databases to improve its efficiency or for any other purpose you see fit.

Feel free to contact me at pegonzalez2018@udec.cl for further details or assistance with using these resources.

Best of luck and regards!
