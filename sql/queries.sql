-- Top 5 Funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV Per Month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- Transactions By State
SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state;

-- Funds With Expense Ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Top Performing Funds
SELECT *
FROM fact_performance
ORDER BY return_3y DESC
LIMIT 5;