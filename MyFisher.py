def MyFisher(observed_ref,observed_alt, population_ref, population_alt):
    import scipy.stats
    import numpy as np
    cntrl = np.array([population_alt,population_ref]) #control
    cond = np.array([observed_alt,observed_ref]) #condition
    Fish = scipy.stats.fisher_exact([cntrl,cond])
    return Fish[1]
