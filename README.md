# JV-Plotting Program
 This program plots the raw data from the University of Toledo's PV Measurements, Inc.'s solar simulator for solar cell characterization. Given the current density and voltage readings, the program will plot each curve and display the sample's power conversion efficiency (PCE), fill factor (FF), short circuit current density (Jsc), and open circuit voltage (Voc). 

 ![](/JV_TD_batch3_11_3.png)


## How to Build
1. Clone the repository
2. Open the project folder using your personal Python IDE
3. Run the following command in the terminal:
```
pip install matplotlib
```

## How to Use
1. Specify the directory where your data is stored in the 'directory' variable.
2. Change the 'sample_ID' variables to correspond with your personal file naming convention.
3. Run the program.

## Result
- A new folder will be created within the specified directory named 'Plots'
- Each file in the directory will have a JV plot within the new folder
- Displayed will be the sample's PCE, FF, Jsc, and Voc

## References
