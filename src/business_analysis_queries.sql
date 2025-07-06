--------------------------------------------------------------------------------
-- 1. Pipeline Snapshot: Count and percentage by status and stage
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
-- 2. Sales Forecast: Weighted revenue by month
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
-- 3. Opportunity Closure Time: Average and median days to close by country
--------------------------------------------------------------------------------
-- Compute days to close per won deal
WITH won_deals AS (
  SELECT
    country,
    DATEDIFF(day, created_date, actual_close_date) AS days_to_close
  FROM opportunities
  WHERE status = 'Customer'
    AND actual_close_date IS NOT NULL
)
SELECT
  country,
  COUNT(*) AS deals_closed,
  ROUND(AVG(days_to_close), 1) AS avg_days,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY days_to_close) AS median_days
FROM won_deals
GROUP BY country
ORDER BY avg_days;

--------------------------------------------------------------------------------
-- 4. Actual Win Rates: Global and by country
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
-- 5. Win Rates by Product and Region
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
