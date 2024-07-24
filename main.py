from matplotlib import pyplot as plt
import numpy as np
import os


def main():
    directory = 'C:/Users/khoaw/OneDrive/Personal Documents/UT - REU/Data/JV Data/07122024'  # TO CHANGE

    # Create folder to store the plots
    if not os.path.exists(directory + '/Plots'):
        os.makedirs(directory + '/Plots')

    for files in os.listdir(directory):
        if files.endswith('.csv') and not files.startswith('summary'):
            # Unpack PV Measurement Inc. file data
            volt_list, curr_dens_list = np.loadtxt(os.path.join(directory, files), delimiter=',',
                                                   skiprows=4, unpack=True, usecols=(1, 2))

            # Get useful parameters
            Jmin, Jmax, Jsc, Voc, FF, PCE = run_calculations(volt_list, curr_dens_list)

            # Plot all the data
            create_plot(volt_list, curr_dens_list, files, Jmin, Jmax, Jsc, Voc, FF, PCE)

            # Save the plot
            index = [i for i, n in enumerate(files) if n == '_'][0] + 1
            plt.savefig(directory+'/Plots/'+files[index:len(files) - 4]+'.png', bbox_inches='tight')

            # Clear the plot
            plt.clf()


def run_calculations(volts, curr_dens):
    # Variable Initializations
    Jsc = 1
    Voc1 = [0, 999]
    Voc2 = [1, -999]
    Pmp = -999
    Jmin = 999
    Jmax = -999

    # Find specific parameters
    for volt, curr in zip(volts, curr_dens):
        if volt == 0:
            Jsc = curr
        if Voc1[1] > curr > 0:
            Voc1 = volt, curr
        if 0 > curr > Voc2[1]:
            Voc2 = volt, curr
        if (volt * curr) > Pmp:
            Pmp = volt * curr
        if curr < Jmin:
            Jmin = curr
        if curr > Jmax:
            Jmax = curr

    # Calculations
    m = (Voc2[1] - Voc1[1]) / (Voc2[0] - Voc1[0])
    Voc = (m * Voc1[0] - Voc1[1]) / m
    FF = (Pmp * 0.075) / (Voc * Jsc * 0.075)
    PCE = (Voc * (Jsc * 0.075) / 1000 * FF) / 0.0075

    return Jmin, Jmax, Jsc, Voc, FF, PCE


def create_plot(volts, curr_dens, files, Jmin, Jmax, Jsc, Voc, FF, PCE):
    # Plot the data
    plt.plot(volts, curr_dens, color='r', linestyle='-', marker='.')

    # Get sample ID from file name (MAY HAVE TO CHANGE)
    file_name = files.split('_')
    sample_name = file_name[4]
    cell_name = file_name[5][:len(file_name[5]) - 4]

    # Add labels to the plot
    plt.title('JV of Sample ' + sample_name + ' Cell ' + cell_name)
    plt.xlabel('Voltage, V [V]')
    plt.ylabel('Current Density, J [mA/cm{}]'.format(get_super('2')))

    # Add text to the plot
    space = np.linspace((Jmin + Jmax) / 2, Jmin, num=4)
    plt.text(0, space[0], 'PCE = {:.2f} %'.format(PCE * 100), fontsize=10)
    plt.text(0, space[1], 'FF = {:.2f} %'.format(FF * 100), fontsize=10)
    plt.text(0, space[2], 'Jsc = {:.2f} mA/cm{}'.format(Jsc, get_super('2')), fontsize=10)
    plt.text(0, space[3], 'Voc = {:.2f} V'.format(Voc), fontsize=10)


# Returns superscript character
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


if __name__ == "__main__":
    main()
