SELECT realgdp.year, realgdp.YTYchange AS realgpd, nominalgdp.YTYchange AS nominalgdp, gdppercapita.YTYchange AS gdppercapita, inflation.YTYchange AS inflation, lendingborrowingnet.YTYchange AS LBnet, accountbalance.YTYchange AS accountbalance
FROM realgdp, nominalgdp, gdppercapita, inflation, lendingborrowingnet, accountbalance
WHERE realgdp.year = nominalgdp.year
AND realgdp.year = gdppercapita.year
AND realgdp.year = inflation.year
AND realgdp.year = lendingborrowingnet.year
AND realgdp.year = accountbalance.year
ORDER BY realgdp.year DESC
LIMIT 7;
---Compares all the table's YTY percetange change.


SELECT realgdp.year, nominalgdp.NominalGDP AS NominalGDP, realgdp.YTYchange AS Change_in_real_GDP, accountbalance.balance AS accountbalance
FROM realgdp, nominalgdp, accountbalance
WHERE realgdp.year = nominalgdp.year
AND realgdp.year = accountbalance.year
AND realgdp.YTYchange > 0
ORDER BY realgdp.year DESC
LIMIT 6;
---returns the nominal GDP amount, the real GDP change, and the account balance if the Real GDP change of the year was positive. Here are the results.


SELECT year, balance, YTYchange
FROM accountbalance
WHERE balance > 0;
---get all of the years where the Account Balance of the Maldives was positive (it is going to be empty)


SELECT lendingborrowingnet.year, lendingborrowingnet.net AS NetBorrow, accountbalance.balance AS AccountBalance
FROM lendingborrowingnet
LEFT JOIN accountbalance
ON lendingborrowingnet.year = accountbalance.year
ORDER BY lendingborrowingnet.year DESC;
---net value of the Lending and Borrowing of the Maldives and compare it to their Account Balance
