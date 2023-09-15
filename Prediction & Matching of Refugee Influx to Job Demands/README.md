# Prediction & Matching of Refugee Influx to Job Demands with the Purpose of Providing Settlement and Employment.

Refugees are in need of acceptance into asylum countries to which refugees could settle down, and employment opportunity.

There are multiple countries that provide asylum. If all refugees focus on going to one country, they will quickly exhaust the resources available from that country that was allocated for the refugees.

What we want to do to solve this problem is predict how many refugees will flow into a country and job demand in those countries. Then matching the number of refugees with job demand. If there is a gap, then providing guidance for increasing intake and job opportunities in those countries.


## Objective 

The research aims to provide
* a prediction on refugee influx each year​
* a prediction of demand for employment the asylum countries to which refugees can fulfill


## Datasets (Under Dataset Branch in GitHub)

1. https://microdata.unhcr.org/index.php/catalog/681/study-description#metadata-data_collection (Refugee information in the US)
2. https://www.bls.gov/charts/job-openings-and-labor-turnover/opening-hire-seps-level.htm (Job Openings in the US)

### Additional statistics collected after analysing original dataset

* https://www.macrotrends.net/countries/DEU/germany/refugee-statistics
* https://www.macrotrends.net/countries/USA/united-states/refugee-statistics
* https://www.macrotrends.net/countries/FRA/france/refugee-statistics
* https://www.macrotrends.net/countries/CAN/canada/refugee-statistics
* https://data.bls.gov/PDQWeb/ln (LabourForceParticipationRate Dataset)


## Results interpretation

We can see that throughout the years about **0.36% to 0.51%** of the available jobs (job openings) in a year could be filled be the refugees that need jobs. The calculation is by dividing Jobs Needed against Predicted Average of Job Openings to compare apple to apple

Note: Future Research: <br>
We will have to obtain more information especially when it comes to education level, skill sets, and experience to match it with the job openings to have a more accurate predictions. This prediction done is based on the assumption that Refugees are not picky, have the relevant skillset the employers are looking for, and the employers are hiring based on the skill set that matches the job. 

Limitation: Racism, Ethnocentrism and Sexism from employers are variables we are unable to predict and fit into models to predict whether or not they'll employ the refugees to fulfill their job openings. 
