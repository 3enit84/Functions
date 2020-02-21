ExAC_alt = 10
ExAC_tot = 100
obs_alt = 1
obs_tot = 50

def MyChisquare(observed_ref,observed_alt, population_ref, population_alt):
    from scipy.stats import chisquare
    chi_obs = np.array([population_alt,population_ref,observed_alt,observed_ref])#observed values
    exp_population_alt = (population_ref+population_alt)*(population_alt+observed_alt)/\
        (population_ref+population_alt+observed_ref+observed_alt)#calculating expected values
    exp_population_ref = (population_ref+population_alt)*(population_ref+observed_ref)/\
        (population_ref+population_alt+(observed_ref+observed_alt))
    exp_observed_alt = (population_alt+obs_alt)*(observed_ref+observed_alt)/\
        (population_ref+population_alt+observed_ref+observed_alt)
    exp_observed_ref = (population_ref+observed_ref)*(observed_ref+observed_alt)/\
        (population_ref+population_alt+observed_ref+observed_alt)
    
    chi_exp = np.array([exp_population_alt,exp_population_ref,exp_observed_alt,exp_observed_ref])
    chi_statistic, p_value = chisquare(chi_obs,chi_exp,2)
    return p_value

print(MyChisquare(obs_tot-obs_alt,obs_alt,ExAC_tot-ExAC_alt,ExAC_alt))
