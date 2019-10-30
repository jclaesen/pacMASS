""" preprocess.py
    This module implements the functions to handle the different sources of input for the pacMASS package
    It also converts the masses to their neutral mass
"""

import pandas as pd
import numpy as np
import os

def calculateMonoMass(inputDF):
    """
    Function that calculates the neutral monoisotopic mass
    
    Parameters
    ----------
        inputDF: numpy array
            measured masses and charges
        
    Returns
    -------
        monoMass: list
            Neutral monoisotopic masses
    """
    monoMass = list()

    for row in inputDF.iterrows():   # row[1][0]=charge, row[1][1]=m/z
        monoMass.append(row[1][1] * row[1][0] - row[1][0] * 1.009794)

    return monoMass

def filterMonoMass(monoMass, lowerLimit, upperLimit):
    """
    Function that filters (array of) monoisotopic mass

    Parameters
    ----------
    
        monoMass: float or numpy array
        lowerLimit: float
        upperLimit: float
        
    Returns
    -------
        monoMassFiltered: list 
            Filtered monoisotopic masses
    """
    
    if isinstance(monoMass, float):
        if((monoMass >= lowerLimit) & (monoMass <= upperLimit)):
            return([monoMass])
    elif isinstance(monoMass, np.ndarray):

        down = monoMass >= lowerLimit
        up = monoMass <= upperLimit
        
        index = np.where(down & up)
        monoMassFiltered = list(monoMass[index])

        return monoMassFiltered

def handleInput(monoMassInput, columns):
    """
    Parameters
    ----------
    
        monoMassInput: float, list or string
            A single monoisotopic mass (neutral), list of monoisotopic masses (neutral), file containing measured masses (with charge) 
    
    Returns
    -------
    
        monoMassOut: list
            Neutral monoisotopic mass(es)

    """
    
    if not isinstance(monoMassInput, str) and not isinstance(monoMassInput, float) and not isinstance(monoMassInput, list):
        print("Argument 'monoMassInput' should be a list, float or a string")
        return
    
    if not isinstance(columns, list) or not len(columns)==2:
        print("Argument 'columns' should be a list of length 2")
        return
 
    
    if isinstance(monoMassInput, str):
        if os.path.isfile(monoMassInput):
            print("importing mass input file...")

            # reading given columns from inputfile (.txt)
            if monoMassInput.endswith(".txt"):
                try:
                    mz = pd.read_csv(monoMassInput, delimiter="\t", usecols=[columns[0], columns[1]], dtype={columns[0]: float, columns[1]: float})
                except ValueError:
                    print("Given column names don't match file")
        
            # reading given columns from inputfile (.csv)
            elif monoMassInput.endswith(".csv"):
                try:
                    mz = pd.read_csv(monoMassInput, delimiter=",", usecols=[columns[0], columns[1]], dtype={columns[0]: float, columns[1]: float})
                except ValueError:
                    print("Given column names don't match file")
        
            else: print("Error: File can not be opened : \"{}\"".format(monoMassInput))

        monoMassOut = calculateMonoMass(mz)


    # If input is one monomass
    if isinstance(monoMassInput, float):

        monoMassOut = filterMonoMass(monoMassInput, 0, 4000)
                
    # If input in a list of monomasses
    elif isinstance(monoMassInput, list):

        monoMassArray = np.array(monoMassInput)
        # Filtering input
        monoMassOut = filterMonoMass(monoMassArray, 0, 4000)
        
    return(monoMassOut)
