import pandas as pd
import matplotlib.pyplot as plt

# For reading in csvs and cutting off useless cells
def csv_extractor(state):
    path = 'Demographics/' + state + '_demog.csv'
    df = pd.read_csv(path, encoding='Latin-1')
    df = df.iloc[ : , 0 : 8]
    df = df.loc[df['YEAR'] > 2, : ]
    return df

# Easy peasy csv readie
al_df = csv_extractor('Alabama')
ak_df = csv_extractor('Alaska')
az_df = csv_extractor('Arizona')
ar_df = csv_extractor('Arkansas')
ca_df = csv_extractor('California')
co_df = csv_extractor('Colorado')
ct_df = csv_extractor('Connecticut')
de_df = csv_extractor('Delaware')
dc_df = csv_extractor('DC')
fl_df = csv_extractor('Florida')
ga_df = csv_extractor('Georgia')
hi_df = csv_extractor('Hawaii')
id_df = csv_extractor('Idaho')
il_df = csv_extractor('Illinois')
in_df = csv_extractor('Indiana')
ia_df = csv_extractor('Iowa')
ks_df = csv_extractor('Kansas')
ky_df = csv_extractor('Kentucky')
la_df = csv_extractor('Louisiana')
me_df = csv_extractor('Maine')
mt_df = csv_extractor('Montana')
ne_df = csv_extractor('Nebraska')
nv_df = csv_extractor('Nevada')
nh_df = csv_extractor('New Hampshire')
nj_df = csv_extractor('New Jersey')
nm_df = csv_extractor('New Mexico')
ny_df = csv_extractor('New York')
nc_df = csv_extractor('North Carolina')
nd_df = csv_extractor('North Dakota')
oh_df = csv_extractor('Ohio')
ok_df = csv_extractor('Oklahoma')
or_df = csv_extractor('Oregon')
md_df = csv_extractor('Maryland')
ma_df = csv_extractor('Massachusetts')
mi_df = csv_extractor('Michigan')
mn_df = csv_extractor('Minnesota')
ms_df = csv_extractor('Mississippi')
mo_df = csv_extractor('Missouri')
pa_df = csv_extractor('Pennsylvania')
ri_df = csv_extractor('Rhode Island')
sc_df = csv_extractor('South Carolina')
sd_df = csv_extractor('South Dakota')
tn_df = csv_extractor('Tennessee')
tx_df = csv_extractor('Texas')
ut_df = csv_extractor('Utah')
vt_df = csv_extractor('Vermont')
va_df = csv_extractor('Virginia')
wa_df = csv_extractor('Washington')
wv_df = csv_extractor('West Virginia')
wi_df = csv_extractor('Wisconsin')
wy_df = csv_extractor('Wyoming')

state_dict1 = {'Alabama' : al_df,
              'Arizona' : az_df,
              'Arkansas' : ar_df,
              'Connecticut' : ct_df,
              'Delaware' : de_df,
              'Florida' : fl_df,
              'Georgia' : ga_df,
              'Hawaii' : hi_df,
              'Idaho' : id_df,
              'Illinois' : il_df,
              'Indiana' : in_df,
              'Iowa' : ia_df,
              'Kansas' : ks_df,
              'Kentucky' : ky_df,
              'Louisiana' : la_df}

state_dict2 = {'Montana' : mt_df,
              'Nebraska' : ne_df,
              'New Hampshire' : nh_df,
              'New Jersey' : nj_df,
              'New Mexico' : nm_df,
              'New York' : ny_df,
              'North Carolina' : nc_df,
              'North Dakota' : nd_df,
              'Ohio' : oh_df,
              'Oklahoma' : ok_df,
              'Maryland' : md_df,
              'Michigan' : mi_df}

state_dict3 = {'Minnesota' : mn_df,
              'Mississippi' : ms_df,
              'Missouri' : mo_df,
              'Pennsylvania' : pa_df,
              'Rhode Island' : ri_df,
              'South Carolina' : sc_df,
              'South Dakota' : sd_df,
              'Tennessee' : tn_df,
              'Texas' : tx_df,
              'Utah' : ut_df,
              'Vermont' : vt_df,
              'Virginia' : va_df,
              'West Virginia' : wv_df,
              'Wisconsin' : wi_df,
              'Wyoming' : wy_df}

state_dict_2012 = {'Colorado' : co_df,
                    'Washington' : wa_df}

state_dict_2014 = {'Alaska' : ak_df,
                   'District of Columbia' : dc_df,
                   'Oregon' : or_df}

state_dict_2016 = {'California' : ca_df,
                   'Maine' : me_df,
                   'Nevada' : nv_df,
                   'Massachusetts' : ma_df}
                   
state_dict_2018 = {'New Jersey' : nj_df,
                   'Oklahoma' : ok_df,
                   'Michigan' : mi_df,
                   'Missouri' : mo_df,
                   'Utah' : ut_df,
                   'Vermont' : vt_df,
                   'Virginia' : va_df}

# CSV containing urban/rural info by county
urban_path = 'Demographics/PctUrbanRural_County.txt'
urban_df = pd.read_csv(urban_path, encoding='Latin-1')

# Function returning only counties within a given range of urban percentages
def urban_slice(df, target_state, high, low):
    
    try:
        # The urban_df covers the whole US, need to specify
        state_urban_df = urban_df.loc[urban_df['STATENAME'] == target_state, : ]

        # Get number of entries per county
        unique_counties = df['CTYNAME'].value_counts()[0]

        county_list = []

        # Build list of urban percentages for main state dataframe
        for i, j in state_urban_df.iterrows():
            county = j[7]
            for k in range(unique_counties):
                county_list.append(county)

        # Add urban percentages to main state df, slice by passed boundaries
        df['urban_percent'] = county_list
        df_urban_percent = df.loc[df['urban_percent'] < high, :]
        df_urban_percent = df_urban_percent.loc[df['urban_percent'] > low, :]

        return df_urban_percent
    
    except:
        print(f'ValueError in {target_state}')
        
# Graph of total population change over 2010-2016 for passed df
def total_graph(df, area):
    
    try:
        # AGEGRP 0 is total
        tot = df.loc[df['AGEGRP'] == 0, ]

        tot_group_year = tot.groupby('YEAR')
        tot_group_year = tot_group_year.sum()
        tot_group_year.reset_index(inplace=True)

        tot_group_year.plot('YEAR', 'TOT_POP', figsize=(18,9))
    

        plt.title(f'Total population of {area}')
    except:
        return f'TypeError for {area}!'
    
# Plot of population of passed df sorted by age group
def age_graph(df, area, threshold):
    
    # Age groups as provided by the census bureau
    legend_dict = {0 :'Age 0 to 4 years',
            1 : 'Age 5 to 9 years',
            2 : 'Age 10 to 14 years',
            3 : 'Age 15 to 19 years',
            4 : 'Age 20 to 24 years',
            5 : 'Age 25 to 29 years',
            6 : 'Age 30 to 34 years',
            7 : 'Age 35 to 39 years',
            8 : 'Age 40 to 44 years',
            9 : 'Age 45 to 49 years',
            10 : 'Age 50 to 54 years',
            11 : 'Age 55 to 59 years',
            12 : 'Age 60 to 64 years',
            13 : 'Age 65 to 69 years',
            14 : 'Age 70 to 74 years',
            15 : 'Age 75 to 79 years',
            16 : 'Age 80 to 84 years',
            17 : 'Age 85 years or older'}
    
    # Build list of dataframes, each entry in list is a different age group
    index = [x + 1 for x in range(18)]
    age_list = []
    
    for i in index:
        age = df.loc[df['AGEGRP'] == i].groupby('YEAR').sum()
        age.reset_index(inplace=True)
        age_list.append(age)
    
    # Init plot
    fig, ax = plt.subplots(figsize=(18,9))
    
    for age in range(len(age_list)):
        
        # Find pop at beginning and end of 2010-2016 for each age group
        begin_pop = age_list[age].get_value(0, 'TOT_POP')
        end_pop = age_list[age].get_value(6, 'TOT_POP')
        
        # Find change in pop for each age group
        diff = abs(end_pop - begin_pop) * 100
        threshcheck = diff / begin_pop
        
        # Compare change in pop to passed threshold, drop age groups that did not change enough to be of interest
        if threshold == None:
            ax.plot(age_list[age]['YEAR'], age_list[age]['TOT_POP'], label=legend_dict[age])
            
        elif threshcheck > threshold:
            ax.plot(age_list[age]['YEAR'], age_list[age]['TOT_POP'], label=legend_dict[age])  
            
    # Plot
    plt.title(f'Population by age in {area}')
    plt.grid()
    plt.legend()

# Plot average age over 2010-2016 in passed df
def avg_age_graph(df):
    
    # Drop AGEGRP 0 because that is total pop
    age_df = df.loc[df['AGEGRP'] > 0, : ]
    
    # Create list of dataframes, each df is a year (3-10 is 2010-2017)
    mean_age_list = []
    
    for i in range(3, 10):
        age = age_df.loc[age_df['YEAR'] == i].groupby('AGEGRP').sum()
        mean_age_list.append(age)
        
    # Create list of dataframes to help calculate avg age
    avg_age_list = []

    for year_data in mean_age_list:
        
        # Population x age for our avg age calculation
        year_data['POP*AGE'] = 0

        year_data.reset_index(inplace=True)
        
        for index, row in year_data.iterrows():
            
            # Use index to produce list of avg ages in each age group (0-4 = 2, 5-9 = 7, etc.)
            age = (2 + (row[0] * 5)) - 5
            
            # Find population x age and add to df
            numerator = row[0] * row[5]            
            year_data.set_value(index, 'POP*AGE', numerator)            
        
        # Calculate avg age for current loop's year
        agg_years = year_data['POP*AGE'].sum()
        tot_pop = year_data['TOT_POP'].sum()
        avg_age = agg_years / tot_pop
        
        # Add average age for the year to list 
        avg_age_list.append(avg_age)
    
    # Convert list of average ages to Pandas series and plot
    avg_age_list = pd.Series(avg_age_list)
    avg_age_list.plot.line()
    
    
# Generates plot of average of total pops in ALL states in a given dictionary with a given urban percentage
def avg_pop_from_dict(dictionary, high, low):
    
    # Will be list of lists, where the inner lists are tot pops separated by year
    pop_list = []
    
    # Will be our final list of pops, which will be plotted
    avg_pop = []
    
    for key in dictionary:
        
        try:
            # Get desired slice
            df = urban_slice(dictionary[key], key, high, low)
            
            # Functionally the same as total_graph(), but without the graphing
            # AGEGRP 0 is tot pop
            tot = df.loc[df['AGEGRP'] == 0, ]
            tot_group_year = tot.groupby('YEAR')
            tot_group_year = tot_group_year.sum()
            tot_group_year.reset_index(inplace=True)
            
            tot_year = tot_group_year['TOT_POP'].values.tolist()
            
            # This checks to make sure there was actually data in the urban_slice df
            if len(tot_year) == 7:
                
                # Add the list to our list of lists
                print(key)
                pop_list.append(tot_year)
                
            else:
                print(f'There are no entries in {key} for an urban percentage between {low} and {high}')
            
        except:
             continue   
                
    # First check to make sure there is any data to work with
    if len(pop_list) > 0:    
        
        # This bit is complicated.  
        # I need to iterate over a list of lists, but I need to get the average of all the first items, then average the second items, etc.
        
        # Iterator for each item in each list in our list of lists
        for i in range(len(pop_list[0])):

            # iterator for each list in our list of lists
            for j in range(len(pop_list)):
                
                # loop_list contains the first item of each list, then the second, etc.
                loop_list = []
                loop_list.append(pop_list[j][i])
            
            # Get the average pop for the current loop, add it to our final list
            loop_avg = sum(loop_list) / len(loop_list)
            avg_pop.append(loop_list)


        plt.plot(['2010', '2011', '2012', '2013', '2014', '2015', '2016'], avg_pop)
    
    else:
        print(f'There are no entries in this dictionary for an urban percentage between {low} and {high}')
        
