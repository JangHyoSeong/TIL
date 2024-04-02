-- a
SELECT BillingCountry, SUM(Total) AS TotalSales
FROM invoices
GROUP BY BillingCountry;

-- b
SELECT strftime('%Y', InvoiceDate) AS Year, SUM(total) AS TotalSales
FROM invoices
GROUP BY strftime('%Y', InvoiceDate);

-- c
SELECT
  BillingState,
  SUM(total) AS TotalSales
FROM
  invoices
WHERE
  BillingCountry = 'USA' AND
  InvoiceDate >= '2010-01-01'
GROUP BY
  BillingState;

-- d
SELECT
  BillingCountry,
  MAX(total) AS MaxOrderAmount
FROM
  invoices
WHERE
  BillingCountry = 'Germany' OR
  BillingCountry = 'France'
GROUP BY
  BillingCountry;