![boston png](https://cdn.passporthealthusa.com/wp-content/uploads/2017/04/passport-health-downtown-boston-travel-clinic.jpg?x90298)
# Boston AirB&B. Price prediction and objects clustering.

With one small data set available for free we will try to get some insights on the AirB&B market in Boston. 
Is it possible to predict rent price of the bed based on the apartment specification? What are the most common amenities and do they
matter in price prediction? Can we clearly cluster the objects and do those clusters fit into the Boston neighborhood map? 

Data set available here: https://www.kaggle.com/airbnb/boston has a lot of the data we need to clean and change before using in the prediction. We need to decide which fields are not benificial to our prediction and we can drop and wich ones are worth the trouble of cleaning. After cleanup and numeric fields generation I ended up with 2736 rows and 63 columns of clean and usefull data. Base on it our simple linear regression ended up with the following squered error values:
-test: 0.5878648832764807
-train: 0.5840263594330857
Those results are not perfect but acceptable so I am sure that with further data analysis we could achieve better predictions.

During the data preparation phase I decided to split the amenities into separate entities and create new columns with boolean values for each. Top 10 amenities are listed below: \
heating 3382\
kitchen 3272\
wireless internet 3070\
essentials 2994\
smoke detector 2908\
air conditioning 2786\
tv 2607\
dryer 2476\
washer 2475\
carbon monoxide detector 2442\
And the correlation between those amenities and price are:\
Amenities_ tv                          0.226981\
Amenities_air conditioning             0.220434\
Amenities_washer                       0.125687\
Amenities_dryer                        0.105467\
Amenities_kitchen                      0.095146\
Amenities_heating                      0.060418\
Amenities_wireless internet            0.011989\
Amenities_carbon monoxide detector    -0.001271\
Amenities_smoke detector              -0.017888\
In some cases corelation with te price is quite high. 

At the end I tried to see if the price of the stay depends on the neighbourhood. But after comparing the map with all of the objects colored based on the neihbourhood to the map of the objects coloured by the price range we can see that those two don'r relate. After this I attempted to cluster the objectcs with all of the available data but again, cluster didn't match the neighbourhoods. 

