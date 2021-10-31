# Modelling Task

### Data Folder:

Contains data used for modelling/predicitons

- unified_homelessness_data.csv contains umemployment, poverty, home value index, median house hold income (MHHI) combined with homelessness data from Jan-2007 to Jan-2020 on monthly basis.

- homelessness_forecast.csv contains forecasted values for homelessness number from period of Jan-2020 to Sept-2021.


### Scripts/Notebooks:

- 00_homelessness_data_collection.ipynb contains scripts used to scrape data from census, zillow, bls.gov, rentdata.org, etc.

- 01_poverty_rate_forecast.ipynb contains code to forecast povery rate data from 2019 - 2021. This data is further used in the forecast of homelessness counts in the next nextbook.

- 02_homelessness_forecast.ipynb contains code to forecast homelessness people during Jan-2020 to Sept-2021. Along with previous years homelessness data, unemployment rate, average home value index, & poverty_rate are used as features in forecasting homelessness. (Years - 2020, 2021 are affected by special event - covid, for which forecasts are not adjsuted.)


