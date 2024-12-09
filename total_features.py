climate_feats = [
    "env_wea_avgtemp_summer_noaa",  # average summer temperature - June, July, August
    "env_wea_precip_annual_noaa",  # total annual precipitation
    "env_wea_avgtemp_noaa",        # average January temperature
    "env_wea_precip_noaa",         # total January precipitation
    "d_env_wea_avgtemp_noaa",      # 4-year change in env_wea_avgtemp_noaa values (2017 and 2013)
    "d_env_wea_avgtemp_summer_noaa",  # 4-year change in env_wea_avgtemp_summer_noaa values (2017 and 2013)
    "d_env_wea_precip_noaa",       # 4-year change in env_wea_precip_noaa values (2017 and 2013)
    "d_env_wea_precip_annual_noaa" # 4-year change in env_wea_precip_annual_noaa values (2017 and 2013)
]

demographic_feats = [
    "dem_pop_pop_census",  # total population, intercensal estimate
    "dem_pop_male_census",  # total male population, intercensal estimate
    "dem_pop_female_census",  # total female population, intercensal estimate
    "dem_pop_child_census",  # total population ages 0-19, intercensal estimate
    "dem_pop_adult_census",  # total population ages 20-64, intercensal estimate
    "dem_pop_senior_census",  # total population ages 65 or older, intercensal estimate
    "dem_soc_white_census",  # total white alone (non-hispanic) population, intercensal estimate
    "dem_soc_black_census",  # total black alone (non-hispanic) population, intercensal estimate
    "dem_soc_native_census",  # total native alone (non-hispanic) population, intercensal estimate
    "dem_soc_asian_census",  # total asian alone (non-hispanic) population, intercensal estimate
    "dem_soc_pacific_census",  # total pacific islander alone (non-hispanic) population, intercensal estimate
    "dem_soc_racetwo_census",  # total population of two or more races (non-hispanic), intercensal estimate
    "dem_soc_hispanic_census",  # total latino/hispanic (all races) population, intercensal estimate
    "dem_age_boom_census",  # portion of baby boomers to total population in 2010, intercensal estimate
    "dem_soc_ed_bach_acs5yr",  # education share-bachelors or higher to total population for ages 25-64
    "dem_soc_ed_hsgrad_acs5yr",  # education share-high school grad to total population for ages 25-64
    "dem_soc_ed_lesshs_acs5yr",  # education share-less than high school grad to total population for ages 25-64
    "dem_soc_ed_somecoll_acs5yr",  # education share-some college to total population for ages 25-64
    "dem_soc_vet_acs5yr",  # share of the civilian population 25 and older with veteran status
    "dem_soc_singparent_acs5yr",  # share of under 18 population living with single parent
    "dem_health_ins_acs5yr",  # share of civil noninstitutionalized population with health insurance
    "dem_soc_singadult_acs5yr",  # proportion of 1-person households to all households
    "dem_pop_density_census",  # total population estimate divided by square miles
    "dem_pop_mig_census",  # net migration from year-1 to year, intercensal estimate
    "dem_health_alcoholdeath_IMHE",  # 2014 mortality rate of alcohol use disorders, per 100,000 population, from IMHE
    "dem_mort_lifeexp_IMHE",  # 2014 life expectancy, from IMHE
    "dem_health_mentalhlth_chr",  # number of mental health providers, from county health rankings
    "dem_health_excesdrink_chr",  # percentage of adults that report excessive drinking, from county health rankings
    "dem_health_cost_dart",  # total medicare reimbursements per enrollee (parts a&b), dartmouth
    "dem_pop_adult_census_share",  # adult population (ages 20-64) to total population
    "dem_pop_child_census_share",  # child population (ages 0-19) to total population
    "dem_pop_female_census_share",  # female population to total population
    "dem_pop_male_census_share",  # male population to total population
    "dem_pop_mig_census_share",  # yearly increase in population to total population
    "dem_pop_senior_census_share",  # senior population (ages 65 and older) to total population
    "dem_age_boom_census_2011",  # 2010 share of baby boomers to total population
    "dem_soc_asian_census_share",  # asian (non-hispanic) population to total population
    "dem_soc_black_census_share",  # black (non-hispanic) population to total population
    "dem_soc_hispanic_census_share",  # hispanic/latino population (all races) to total population
    "dem_soc_native_census_share",  # native (non-hispanic) population to total population
    "dem_soc_pacific_census_share",  # pacific islander (non-hispanic) population to total population
    "dem_soc_racetwo_census_share",  # two or more races to total population
    "dem_soc_white_census_share",  # white (non-hispanic) population to total population
    "dem_soc_other_census_share",  # sum of native, pacific islander, and two or more race shares
    "dem_health_mentalhlth_chr_share",  # mental health care providers to total population
    "dem_health_mhlth_chr_share_2017",  # 2016 share of mental health care providers to total population
    "dem_health_excesdrink_chr_2017",  # 2016 share of excess drinkers
    "dem_health_alcdeath_IMHE_2015",  # 2014 alcohol mortality rate
    "dem_mort_lifeexp_IMHE_2015",  # 2014 life expectancy, from IMHE
    "dem_health_ins_acs5yr_2012",  # 2011 share of the population with health insurance
    "dem_health_ins_acs5yr_2017",  # 2016 share of the population with health insurance
    "dem_soc_ed_bach_acs5yr_2012",  # 2011 share of the population with bachelors or higher
    "dem_soc_ed_bach_acs5yr_2017",  # 2016 share of the population with bachelors or higher
    "dem_soc_ed_bach_acs5yr_diff",  # change in dem_soc_ed_bach_acs5yr values (2016 and 2011)
    "dem_soc_ed_somecoll_acs5yr_2012",  # 2011 share of the population with some college
    "dem_soc_ed_somecoll_acs5yr_2017",  # 2016 share of the population with some college
    "dem_soc_ed_hsgrad_acs5yr_2012",  # 2011 high school graduate share of the population
    "dem_soc_ed_hsgrad_acs5yr_2017",  # 2016 high school graduate share of the population
    "dem_soc_ed_lesshs_acs5yr_2012",  # 2011 share of the population without high school diploma
    "dem_soc_ed_lesshs_acs5yr_2017",  # 2016 share of the population without high school diploma
    "dem_soc_ed_lesshs_acs5yr_diff",  # change in dem_soc_ed_lesshs_acs5yr values (2016 and 2011)
    "dem_soc_singparent_acs5yr_2012",  # 2011 percentage of children living with a single parent
    "dem_soc_singparent_acs5yr_2017",  # 2016 percentage of children living with a single parent
    "dem_soc_singparent_acs5yr_diff",  # change in dem_soc_singparent_acs5yr values (2016 and 2011)
    "dem_soc_singadult_acs5yr_2012",  # 2011 proportion of one-person households
    "dem_soc_singadult_acs5yr_2017",  # 2016 proportion of one-person households
    "dem_soc_singadult_acs5yr_diff",  # change in dem_soc_singadult_acs5yr values (2016 and 2011)
    "dem_soc_vet_acs5yr_2012",  # 2011 percentage of veterans
    "dem_soc_vet_acs5yr_2017",  # 2016 percentage of veterans
    "dem_soc_vet_acs5yr_diff",  # change in dem_soc_vet_acs5yr values (2016 and 2011)
    "dem_soc_ed_bach_xt",  # education share-bachelors or higher to total population for ages 25-64
    "dem_soc_ed_somecoll_xt",  # education share-some college to total population for ages 25-64
    "dem_soc_ed_hsgrad_xt",  # education share-high school grad to total population for ages 25-64
    "dem_soc_ed_lesshs_xt",  # education share-less than high school grad to total population for ages 25-64
    "dem_health_ins_xt",  # share of civil noninstitutionalized population with health insurance
    "dem_soc_singadult_xt",  # proportion of one-person households to all households
    "dem_soc_singparent_xt",  # share of under 18 population living with single parent
    "dem_soc_vet_xt",  # share of the civilian population 25 and older with veteran status
    "d_dem_soc_white_census_share",  # 4-year change in dem_soc_white_census_share values (2017 and 2013)
    "d_dem_soc_black_census_share",  # 4-year change in dem_soc_black_census_share values (2017 and 2013)
    "d_dem_soc_hispanic_census_share",  # 4-year change in dem_soc_hispanic_census_share values (2017 and 2013)
    "d_dem_soc_asian_census_share",  # 4-year change in dem_soc_asian_census_share values (2017 and 2013)
    "d_dem_pop_child_census_share",  # 4-year change in dem_pop_child_census_share values (2017 and 2013)
    "d_dem_pop_adult_census_share",  # 4-year change in dem_pop_adult_census_share values (2017 and 2013)
    "d_dem_pop_senior_census_share",  # 4-year change in dem_pop_senior_census_share values (2017 and 2013)
    "d_dem_pop_female_census_share",  # 4-year change in dem_pop_female_census_share values (2017 and 2013)
    "d_dem_pop_mig_census_share",  # 4-year change in dem_pop_mig_census_share values (2017 and 2013)
    "d_dem_soc_ed_bach_xt",  # 4-year change in dem_soc_ed_bach_xt values (2017 and 2013)
    "d_dem_health_cost_dart",  # 4-year change in dem_health_cost_dart values (2017 and 2013)
    "d_dem_soc_singadult_xt",  # 4-year change in dem_soc_singadult_xt values (2017 and 2013)
    "d_dem_soc_singparent_xt",  # 4-year change in dem_soc_singparent_xt values (2017 and 2013)
    "d_dem_soc_vet_xt",  # 4-year change in dem_soc_vet_xt values (2017 and 2013)
    "dem_soc_ed_lessbach_xt"  # share of the population without a bachelors degree
]

economic_feats = [
    "econ_labor_topskilled_acs5yr",  # employment rate-bachelors degree or higher for ages 25-64
    "econ_labor_midskilled_acs5yr",  # employment rate-high school grad or some college for ages 25-64
    "econ_labor_unskilled_acs5yr",  # employment rate-less than high school grad for ages 25-64
    "econ_labor_incineq_acs5yr",  # gini index of income inequality by households
    "econ_labor_medinc_acs5yr",  # median household income
    "econ_labor_pov_acs5yr",  # population in poverty to total population with poverty status determined
    "econ_labor_force_pop_BLS",  # total population in the labor force
    "econ_labor_emp_pop_BLS",  # total employed population
    "econ_labor_unemp_pop_BLS",  # total unemployed population
    "econ_labor_unemp_rate_BLS",  # unemployment rate, from BLS LAUS
    "econ_labor_pov_pop_census",  # count of all ages in poverty, from SAIPE
    "econ_labor_medinc_census",  # median household income, from SAIPE
    "cpi_2017",  # consumer price index
    "econ_labor_incineq_acs5yr_2012",  # 2011 gini coefficient
    "econ_labor_incineq_acs5yr_2017",  # 2016 gini coefficient
    "econ_labor_incineq_acs5yr_diff",  # change in econ_labor_incineq_acs5yr values (2016 and 2011)
    "econ_labor_topskill_acs5yr_2012",  # 2011 employment rate for high-skilled workers
    "econ_labor_topskill_acs5yr_2017",  # 2016 employment rate for high-skilled workers
    "econ_labor_topskill_acs5yr_diff",  # change in econ_labor_topskilled_acs5yr values (2016 and 2011)
    "econ_labor_midskill_acs5yr_2012",  # 2011 employment rate for middle-skilled workers
    "econ_labor_midskill_acs5yr_2017",  # 2016 employment rate for middle-skilled workers
    "econ_labor_midskill_acs5yr_diff",  # change in econ_labor_midskilled_acs5yr values (2016 and 2011)
    "econ_labor_unskill_acs5yr_2012",  # 2011 employment rate for low-skilled workers
    "econ_labor_unskill_acs5yr_2017",  # 2016 employment rate for low-skilled workers
    "econ_labor_unskill_acs5yr_diff",  # change in econ_labor_unskilled_acs5yr values (2016 and 2011)
    "econ_labor_medinc_acs5yr_2012",  # 2011 median income
    "econ_labor_medinc_acs5yr_2017",  # 2016 median income
    "econ_labor_pov_pop_census_share",  # poverty rate, number of persons in poverty to total population
    "econ_labor_midskill_xt",  # employment rate-high school grad or some college for ages 25-64
    "econ_labor_incineq_xt",  # gini index of income inequality by households
    "ln_econ_labor_medinc_census",  # log of median income
    "d_econ_labor_medinc_census",  # 4-year change in econ_labor_medinc_census values (2017 and 2013)
    "d_econ_labor_unemp_rate_BLS",  # 4-year change in econ_labor_unemp_rate_BLS values (2017 and 2013)
    "d_econ_labor_incineq_xt"  # 4-year change in econ_labor_incineq_xt values (2017 and 2013)
]

geograph_feats = [
    "state_abr",  # state abbreviation
    "state",  # numerical state ID, based on state_abr
    "census_region",  # census region
    "census_division"  # census region
]

housing_feats = [
    "hou_mkt_rentshare_acs5yr_2012",  # 2011 share of renters
    "hou_mkt_rentshare_acs5yr_2017",  # 2016 share of renters
    "hou_mkt_rentshare_acs5yr_diff",  # change in hou_mkt_rentshare_acs5yr values (2016 and 2011)
    "hou_mkt_rentvacancy_acs5yr_2012",  # 2011 rental vacancy rate
    "hou_mkt_rentvacancy_acs5yr_2017",  # 2016 rental vacancy rate
    "hou_mkt_rentvacancy_acs5yr_diff",  # change in hou_mkt_rentvacancy_acs5yr values (2016 and 2011)
    "hou_mkt_ovrcrowd_acs5yr_2012",  # 2011 share of overcrowded housing units
    "hou_mkt_ovrcrowd_acs5yr_2017",  # 2016 share of overcrowded housing units
    "hou_mkt_ovrcrowd_acs5yr_diff",  # change in hou_mkt_ovrcrowd_acs5yr values (2016 and 2011)
    "hou_mkt_homeage_acs5yr_2012",  # 2011 median housing unit age
    "hou_mkt_homeage_acs5yr_2017",  # 2016 median housing unit age
    "hou_mkt_homeage_acs5yr_diff",  # change in hou_mkt_homeage_acs5yr values (2016 and 2011)
    "hou_mkt_homeval_acs5yr_2012",  # 2011 median home value
    "hou_mkt_homeval_acs5yr_2017",  # 2016 median home value
    "hou_mkt_homeval_acs5yr_diff",  # change in hou_mkt_homeval_acs5yr values (2016 and 2011)
    "hou_mkt_medrent_acs5yr_2012",  # 2011 median rent
    "hou_mkt_medrent_acs5yr_2017",  # 2016 median rent
    "hou_mkt_medrent_acs5yr_diff",  # change in hou_mkt_medrent_acs5yr values (2016 and 2011)
    "hou_mkt_utility_acs5yr_2012",  # 2011 utility costs
    "hou_mkt_utility_acs5yr_2017",  # 2016 utility costs
    "hou_mkt_utility_acs5yr_diff",  # change in hou_mkt_utility_acs5yr values (2016 and 2011)
    "hou_mkt_burden_own_acs5yr_2012",  # 2011 percentage of home owners with cost burden
    "hou_mkt_burden_own_acs5yr_2017",  # 2016 percentage of home owners with cost burden
    "hou_mkt_burden_own_acs5yr_diff",  # change in hou_mkt_burden_own_acs5yr values (2016 and 2011)
    "hou_mkt_burden_sev_own_acs_2012",  # 2011 percentage of home owners with severe cost burden
    "hou_mkt_burden_sev_own_acs_2017",  # 2016 percentage of home owners with severe cost burden
    "hou_mkt_burden_sev_own_acs_diff",  # change in hou_mkt_burden_sev_own_acs5yr values (2016 and 2011)
    "hou_mkt_burden_rent_acs5yr_2012",  # 2011 percentage of renters with cost burden
    "hou_mkt_burden_rent_acs5yr_2017",  # 2016 percentage of renters with cost burden
    "hou_mkt_burden_rent_acs5yr_diff",  # change in hou_mkt_burden_rent_acs5yr values (2016 and 2011)
    "hou_mkt_burden_sev_rent_acs_2012",  # 2011 percentage of renters with severe cost burden
    "hou_mkt_burden_sev_rent_acs_2017",  # 2016 percentage of renters with severe cost burden
    "hou_mkt_burden_sev_rent_acs_diff",  # change in hou_mkt_burden_sev_rent_acs5yr values (2016 and 2011)
    "hou_mkt_pmt_unit_census_share",  # share of new housing permits to total housing units
    "evict_file_flag",  # flag for missing eviction filing rate value
    "evict_flag",  # flag for missing eviction rate value
    "hou_mkt_density_dummy",  # indicator for high housing density CoC (>= 75th percentile)
    "hou_mkt_homeval_xt",  # median housing unit value of owner-occupied housing units
    "hou_mkt_burden_own_xt",  # share of owned housing units with 30+% monthly owner costs to income
    "hou_mkt_burden_sev_own_xt",  # share of owned housing units with 50+% monthly owner costs to income
    "hou_mkt_burden_rent_xt",  # share of rented housing units with 30+% monthly owner costs to income
    "hou_mkt_burden_sev_rent_xt",  # share of rented housing units with 50+% monthly owner costs to income
    "hou_mkt_homeage_xt",  # median age of housing structure
    "hou_mkt_medrent_xt",  # median contract rent for renter-occupied housing units
    "hou_mkt_utility_xt",  # utility costs as the difference of median gross and contract rent
    "hou_mkt_rentshare_xt",  # share of renter-occupied housing units to all occupied housing units
    "hou_mkt_rentvacancy_xt",  # rental vacancy rate-share of vacant units for rent to total rental units
    "hou_mkt_ovrcrowd_xt",  # share of occupied housing units with occupants per room exceeding 1.5
    "ln_hou_mkt_homeval_xt",  # log of median housing unit value
    "ln_hou_mkt_medrent_xt",  # log of median rent
    "d_hou_mkt_homeval_xt",  # 4-year change in hou_mkt_homeval_xt values (2017 and 2013)
    "d_hou_mkt_burden_sev_rent_xt",  # 4-year change in hou_mkt_burden_sev_rent_xt values (2017 and 2013)
    "d_hou_mkt_burden_own_xt",  # 4-year change in hou_mkt_burden_own_xt values (2017 and 2013)
    "d_hou_mkt_burden_sev_own_xt",  # 4-year change in hou_mkt_burden_sev_own_xt values (2017 and 2013)
    "d_hou_mkt_burden_rent_xt",  # 4-year change in hou_mkt_burden_rent_xt values (2017 and 2013)
    "d_hou_mkt_medrent_xt",  # 4-year change in hou_mkt_medrent_xt values (2017 and 2013)
    "d_hou_mkt_utility_xt",  # 4-year change in hou_mkt_utility_xt values (2017 and 2013)
    "d_fhfa_hpi_2009",  # 4-year change in fhfa_hpi_2009 values (2017 and 2013)
    "d_hou_mkt_rentshare_xt",  # 4-year change in hou_mkt_rentshare_xt values (2017 and 2013)
    "d_hou_mkt_rentvacancy_xt",  # 4-year change in hou_mkt_rentvacancy_xt values (2017 and 2013)
    "d_hou_mkt_ovrcrowd_xt",  # 4-year change in hou_mkt_ovrcrowd_xt values (2017 and 2013)
    "d_hou_mkt_evict_rate"  # 4-year change in hou_mkt_evict_rate values (2017 and 2013)
]

identifiers = [
    "year",  # year
    "cocnumber",  # continuum of care number
    "coctag",  # tag(cocnumber)
    "panelvar"  # CoC number used to set panel
]

local_policies_feats = [
    "hou_pol_hlessconduct_food",  # count of food sharing laws
    "hou_pol_hlessconduct_total",  # total count of prohibited conduct laws
    "hou_pol_hlessconduct_sleep",  # count of sleeping, camping, lying/sitting, and vehicle restriction laws
    "hou_pol_hlessconduct_loiter",  # count of loitering and vagrancy laws
    "hou_pol_hlessconduct_beg"  # count of begging laws
]

safety_net_feats = [
    "hou_pol_fedfundcoc",  # CoC federal funding - HUD
    "hou_pol_fund_project",  # count of federal funded projects - HUD
    "hou_pol_bed_es_hic_hud",  # total year-round beds, emergency shelter
    "hou_pol_bed_oph_hic_hud",  # total year-round beds, other permanent housing
    "hou_pol_bed_psh_hic_hud",  # total year-round beds, permanent supportive housing
    "hou_pol_bed_rrh_hic_hud",  # total year-round beds, rapid re-housing
    "hou_pol_bed_sh_hic_hud",  # total year-round beds, safe haven
    "hou_pol_bed_th_hic_hud",  # total year-round beds, transitional housing
    "hou_pol_perm_bed_hic_hud",  # permanent beds; sum of permanent supportive, rapid rehousing, & other permanent
    "hou_pol_temp_bed_hic_hud",  # temporary beds; sum of emergency shelter, transitional housing, & safe haven
    "econ_sn_cashasst_acs5yr",  # share of households with public assistance income to all households
    "hou_mkt_homeage1940_acs5yr",  # proportion of housing structures built before 1940 to total housing structures
    "hou_pol_hudunit_psh_hud",  # number of HUD-assisted units
    "hou_pol_occhudunit_psh_hud",  # HUD unit occupancy rate
    "hou_mkt_pplunit_psh_hud",  # people per unit - average household size
    "hou_pol_eli_psh_hud",  # % of HUD households with income below 30% of local median family income
    "hou_mkt_pctoverhouse_psh_hud",  # pct overhoused (households with more bedrooms than people)
    "econ_sn_ssdi_SSA",  # total number of disabled workers receiving benefits
    "econ_sn_ssdi_part_rate_SSA",  # SSDI participation rate (ssdi participants/census population)
    "econ_sn_ssi_part_SSA",  # total number of SSI recipients
    "econ_sn_ssi_pay_SSA",  # amount of payments in thousands of dollars
    "econ_sn_ssi_part_rate_SSA",  # SSI participation rate (ssi participants/census population)
    "econ_sn_eitc_irs",  # number of income tax returns (households) with earned income credit (EITC)
    "econ_sn_returns_irs",  # number of returns (households)
    "econ_sn_eitc_irs_share",  # share of returns (households) with earned income tax credit (EITC)
    "econ_sn_cashasst_acs5yr_2012",  # 2011 share of households with public assistance income
    "econ_sn_cashasst_acs5yr_2017",  # 2016 share of households with public assistance income
    "econ_sn_cashasst_acs5yr_diff",  # change in econ_sn_cashasst_acs5yr values (2016 and 2011)
    "hou_mkt_homeage1940_acs5yr_2012",  # 2011 percentage of housing units built before 1940
    "hou_mkt_homeage1940_acs5yr_2017",  # 2016 percentage of housing units built before 1940
    "hou_mkt_homeage1940_acs5yr_diff",  # change in hou_mkt_homeage1940_acs5yr values (2016 and 2011)
    "hou_pol_hudunit_psh_hud_share",  # share of HUD-subsidized housing units to total housing units
    "fedfundcoc_flag",  # flag for missing funding value
    "hou_mkt_homeage1940_xt",  # share of housing structures built before 1940 to total housing structures
    "econ_sn_cashasst_xt",  # share of households with public assistance income to all households
    "d_hou_mkt_homeage1940_xt",  # 4-year change in hou_mkt_homeage1940_xt values (2017 and 2013)
    "d_hou_mkt_pctoverhouse_psh_hud",  # 4-year change in hou_mkt_pctoverhouse_psh_hud values (2017 and 2013)
    "d_hou_pol_eli_psh_hud",  # 4-year change in hou_pol_eli_psh_hud values (2017 and 2013)
    "d_hou_pol_hudunit_psh_hud_share",  # 4-year change in hou_pol_hudunit_psh_hud_share values (2017 and 2013)
    "d_hou_pol_occhudunit_psh_hud",  # 4-year change in hou_pol_occhudunit_psh_hud values (2017 and 2013)
    "d_hou_pol_fedfundcoc",  # 4-year change in hou_pol_fedfundcoc values (2017 and 2013)
    "d_econ_sn_cashasst_xt",  # 4-year change in econ_sn_cashasst_xt values (2017 and 2013)
    "d_econ_sn_eitc_irs_share",  # 4-year change in econ_sn_eitc_irs_share values (2017 and 2013)
    "d_econ_sn_ssdi_part_rate_SSA",  # 4-year change in econ_sn_ssdi_part_rate_SSA values (2017 and 2013)
    "d_econ_sn_ssi_part_rate_SSA"  # 4-year change in econ_sn_ssi_part_rate_SSA values (2017 and 2013)
]

subgroups = [
    "econ_urb_urbanicity",  # urbanicity category
    "urban_cat",  # urbanicity category
    "sub_west_coast",  # indicator for west coast CoC (CA, OR, or WA)
    "sub_low_rent_vacancy",  # indicator for CoCs with rental vacancy rates <= 5 percent
    "sub_high_cost_rent75",  # indicator for CoCs with median rents >= 75th percentile
    "sub_high_cost_homeval75",  # indicator for CoCs with median home value >= 75th percentile
    "sub_high_rent_share75",  # indicator for CoCs with share of renters >= 75th percentile
    "tight_high_cost_rental_mkt",  # sum of the four tight market criteria indicators
    "sub_tight_high_cost_rent",  # indicator for tight, high cost rental market CoCs
    "sub_west_coast_all_urb",  # indicator for suburban or major city/largely urban CoCs in the west region
    "sub_west_census",  # indicator for west region CoCs
    "major_city",  # indicator for major city or largely urban CoC
    "suburban",  # indicator for largely suburban CoC
    "rural"  # indicator for largely rural CoC
]

outcomes = [
    "pit_tot_shelt_pit_hud",  # total sheltered - HUD PIT
    "pit_tot_unshelt_pit_hud",  # total unsheltered - HUD PIT
    "pit_tot_hless_pit_hud",  # total homeless - HUD PIT
    "pit_miss",  # sum of all PIT count values
    "odd_flag",  # odd year of data indicator
    "pit_hless_balance",  # number of non-missing total homeless values across all years
    "pit_shelt_balance",  # number of non-missing sheltered homeless values across all years
    "pit_unshelt_balance",  # number of non-missing unsheltered homeless values across all years
    "unbalance_flag",  # flag for CoCs with less than 5 years of non-missing PIT data
    "pit_shelt_pit_hud_share",  # rate of sheltered homeless per 10,000 people
    "pit_unshelt_pit_hud_share",  # rate of unsheltered homeless per 10,000 people
    "pit_hless_pit_hud_share",  # rate of total homeless per 10,000 people
    "missing",  # number of missing homeless, sheltered, and unsheltered values
    "flag_d_hless",  # flag for missing total homeless share value in 2017 or 2013
    "flag_xt_hless",  # flag for missing total homeless share value in an odd year
    "flag_d_shelt",  # flag for missing sheltered homeless share in 2017 or 2013
    "flag_xt_shelt",  # flag for missing sheltered homeless share value in an odd year
    "flag_d_unshelt",  # flag for missing unsheltered homeless share in 2017 or 2013
    "flag_xt_unshelt",  # flag for missing unsheltered homeless share value in an odd year
    "d_pit_hless_pit_hud_share",  # 4-year change in pit_hless_pit_hud_share values (2017 and 2013)
    "d_pit_shelt_pit_hud_share",  # 4-year change in pit_shelt_pit_hud_share values (2017 and 2013)
    "d_pit_unshelt_pit_hud_share"  # 4-year change in pit_unshelt_pit_hud_share values (2017 and 2013)
]

secondary_outcomes = [
    "pit_ind_shelt_pit_hud",  # individuals sheltered - HUD PIT
    "pit_ind_unshelt_pit_hud",  # individuals unsheltered - HUD PIT
    "pit_ind_hless_pit_hud",  # total individuals - HUD PIT
    "pit_perfam_shelt_pit_hud",  # persons in families sheltered - HUD PIT
    "pit_perfam_unshelt_pit_hud",  # persons in families unsheltered - HUD PIT
    "pit_perfam_hless_pit_hud",  # total persons in families - HUD PIT
    "pit_ind_chronic_hless_pit_hud",  # total chronically homeless individuals - HUD PIT
    "pit_perfam_chronic_hless_pit_hud",  # total chronically homeless persons in families - HUD PIT
    "pit_vet_hless_pit_hud",  # total veterans - HUD PIT
    "hou_pol_totalind_hud",  # length of time homeless; ES, SH, and TH universe
    "hou_pol_totalday_hud",  # length of time homeless; ES, SH, and TH total days
    "hou_pol_totalexit_hud",  # total exits: universe
    "hou_pol_numret6mos_hud",  # total exits: return in less than 6 months
    "hou_pol_numret12mos_hud"  # total exits: return in less than 12 months
]

feature_categories = {
    'climate_feats': climate_feats,
    'demographic_feats': demographic_feats,
    'economic_feats':economic_feats,
    'housing_feats':housing_feats,
    'local_policies_feats':local_policies_feats,
    'local_policies_feats':safety_net_feats
}