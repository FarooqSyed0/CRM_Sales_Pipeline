--------------------------------------------------------------------------------
-- Pipeline Snapshot: Count and percentage by status and stage
--------------------------------------------------------------------------------
-- Total opportunities by status
SELECT
  status,
  COUNT(*) AS count,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM opportunities), 1) AS pct
FROM opportunities
GROUP BY status
ORDER BY count DESC;

-- Active opportunities breakdown by stage
SELECT
  stage,
  COUNT(*) AS count,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM opportunities WHERE status = 'Opportunity'), 1) AS pct_of_active
FROM opportunities
WHERE status = 'Opportunity'
GROUP BY stage
ORDER BY count DESC;

--------------------------------------------------------------------------------
-- Sales Forecast: Weighted revenue by month
--------------------------------------------------------------------------------
SELECT
  DATE_TRUNC('month', expected_close_date) AS month,
  SUM(deal_value * probability / 100.0) AS weighted_revenue
FROM opportunities
WHERE status IN ('New','Qualified','Opportunity','Sales Accepted')
  AND expected_close_date IS NOT NULL
GROUP BY 1
ORDER BY 1;

--------------------------------------------------------------------------------
-- Actual Win Rates: by country
--------------------------------------------------------------------------------
-- Overall win rate
SELECT
  SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS global_win_rate
FROM opportunities;

-- Win rate by country
SELECT
  country,
  COUNT(*) AS total_ops,
  SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) AS wins,
  ROUND(100.0 * SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) / COUNT(*), 1) AS win_rate_pct
FROM opportunities
GROUP BY country
ORDER BY win_rate_pct DESC;

--------------------------------------------------------------------------------
-- Win Rates by Product
--------------------------------------------------------------------------------
SELECT
  country,
  product AS product_type,
  COUNT(*) AS total_ops,
  SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) AS wins,
  ROUND(100.0 * SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) / COUNT(*), 1) AS win_rate_pct
FROM opportunities
GROUP BY country, product
ORDER BY country, win_rate_pct DESC;
