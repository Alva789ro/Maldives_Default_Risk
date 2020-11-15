# Maldives_Default_Risk

This is an analysis of a dataset from the International Mutual Fund Database about the Maldives since 2000 to 2021 (future dates are estimates) with additional statistical values that I personally came up to achieve better insights. 
This project was inspired by the article “Maldives at high risk of debt distress from China: World Bank” from The Edition, written by Mariyam Malsa, June 27th. 2020.
The database includes the following tables and headings, respectively:
•	RealGPD
o	Year
o	YTYchange: represents the percentage (in decimal values) change of the Real GDP in a yearly basis of the Maldives.
•	NominalGPD
o	Year
o	NominalGDP: shows the Nominal GDP per year.
o	YTYchange: represents the percentage (in decimal values) change of the Nominal GDP in a yearly basis of the Maldives.
•	GDPperCapita
o	Year
o	Change YTY: represents the percentage (in decimals) change of the GDP per Capita in a yearly basis of the Maldives.
•	 Inflation
o	Year
o	YTYchange: represents the percentage (in decimals) change of the inflation in a yearly basis of the Maldives.
•	LendingBorrowingNet
o	Year
o	Net: shows the borrowing/lending net value of the Maldives in a yearly basis.
o	YTYchange: represents the percentage (in decimals) change of the Lending/Borrowing in a yearly basis of the Maldives. 
•	AccountBalance
o	Year
o	Balance: shows the Account Balance of Maldives in a yearly basis.
o	YTYchange: represents the percentage (in decimals) change in a yearly basis. 
All the values in the database that are not representing a percentage are in billions of dollars.
The database stores values of each column in each table per year since 2000 to 2021, having 22 entries in total. 
The values of 2020 and 2021 are estimates, and therefore, any statistical value from amounts of these years are also estimates.
Findings
I ran queries on the most important data from the tables to compare and visualize them through the years. Here are the queries and some select columns from them:
SELECT realgdp.year, realgdp.YTYchange AS realgpd, nominalgdp.YTYchange AS nominalgdp, gdppercapita.YTYchange AS gdppercapita, inflation.YTYchange AS inflation, lendingborrowingnet.YTYchange AS LBnet, accountbalance.YTYchange AS accountbalance
FROM realgdp, nominalgdp, gdppercapita, inflation, lendingborrowingnet, accountbalance
WHERE realgdp.year = nominalgdp.year
AND realgdp.year = gdppercapita.year
AND realgdp.year = inflation.year
AND realgdp.year = lendingborrowingnet.year
AND realgdp.year = accountbalance.year
ORDER BY realgdp.year DESC
LIMIT 7;
This query selects the YTY change from all the tables (realgdp, nominalgdp, gdppercapita, inflation, lendingborrowingnet, and accountbalance) in desceding order since 2015. Here are some results:
(‘2021’, ‘0.132 ‘, ‘0.154’, ‘0.113’, ‘0.015’, ‘0.381’, ‘0.4’, ‘09’)
(‘2020’, ‘-0.081’, ’-0.075’, ‘-0.096’, ‘0.015’, ‘-0.987’, ‘0.1’, ‘81’)
(‘2019’, ‘0.057’, ‘0.075’, ‘0.039’, ‘0.013’, ‘-0.146’, ‘-0.0’, ‘64’)
(‘2018’, ‘0.069’, ‘0.095’, ‘0.051’, ‘0.014’, ‘0.097’, ‘-0.3’, ‘32’)
(‘2017’, ’0.068’, ‘0.088’, ‘0.050’, ‘0.023’, ‘0.215’, ‘0.0’, ‘01’)
(‘2016’, ‘0.063’, ‘0.074’, ‘0.046’, ‘0.008’, ‘-0.392’, ‘-2.3’, ‘92’)
(2015, ‘0.029’, ‘0.040’, ‘0.012‘, ‘0.019’, ‘0.004’, ‘-1.1’, ’29’)
This help us compare the change in each of the economic metrics, represented by the tables, over the years.
SELECT realgdp.year, nominalgdp.NominalGDP AS NominalGDP, realgdp.YTYchange AS Change_in_real_GDP, accountbalance.balance AS accountbalance
FROM realgdp, nominalgdp, accountbalance
WHERE realgdp.year = nominalgdp.year
AND realgdp.year = accountbalance.year
AND realgdp.YTYchange > 0
ORDER BY realgdp.year DESC
LIMIT 6;
This query returns the nominal GDP amount, the real GDP change, and the account balance if the Real GDP change of the year was positive. Here are the results.
(‘2021’, ‘9.047’, ‘0.132’, ‘-1.072)
(‘2019’, ‘8.474’, ‘0.057’, ‘-2.214)
(‘2018’, ‘7.883’, ‘0.069’, ‘-2.081)
(‘2017’, ‘7.199’, ‘0.068’, ‘-1.562 )
(‘2016’, ‘6.616’, ‘0.063’, ‘-1.564’)
(‘2015’, ‘6.158’, ‘0.029’, ‘-0.461’)

In a query without the ‘LIMIT 6’ command, we would have noticed that instead of 22 results (which are all the entries in the database) we would receive only 19. This is because the years 2005, 2009 and 2020 we had a negative Real GDP change.
Also, this query reveals that even if the Real GDP change is positive and the Nominal GDP maintains a stable rate, the Account Balance of the Maldives is always negative. This will be better showcased in the following query:
SELECT year, balance, YTYchange
FROM accountbalance
WHERE balance > 0;
Here we will get all of the years where the Account Balance of the Maldives was positive. Unfortunately, as expected, the only result we got from these was an “empty set”. Therefore we conclude that Maldives has not had any positive Account balance since the year 2000.
We can also verify what has been the net value of the Lending and Borrowing of the Maldives and compare it to their Account Balance using this query:
SELECT lendingborrowingnet.year, lendingborrowingnet.net AS NetBorrow, accountbalance.balance AS AccountBalance
FROM lendingborrowingnet
LEFT JOIN accountbalance
ON lendingborrowingnet.year = accountbalance.year
ORDER BY lendingborrowingnet.year DESC;
Some of the results are:
(‘2021’, ‘-0.581’, ‘-1.072’) 
(‘2020’, ‘-0.940’, ‘-1.814’)
(‘2019’, ‘-0.473’, ‘-2.214’)
(‘2018’, ‘-0.412’, ‘-2.081’)
(‘2017’, ‘-0.457’, ‘-1.562’)
(‘2016’, ‘-0.582’, ‘-1.564’)
(‘2015’, ‘-0.418’, ‘-0.461’)



Article link:
https://edition.mv/news/17487 

github link for data extracted from the International Mutual Fund:
https://raw.githubusercontent.com/fivethirtyeight/data/master/state-of-the-state/words.csv (Links to an external site.)

github repository:
https://github.com/fivethirtyeight/data/tree/master/state-of-the-state (Links to an external site.)
