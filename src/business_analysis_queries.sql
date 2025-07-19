
-- CTE: Join opportunities with metadata
WITH opp_details AS (
  SELECT
    o.id,
    o.status,
    o.stage,
    o.deal_value_usd,
    o.probability_pct,
    o.expected_close_date,
    o.actual_close_date,
    p.product_name,
    ow.owner_name,
    c.country_name
  FROM opportunities o
  JOIN products p ON o.product_id = p.product_id
  JOIN owners ow ON o.owner_id = ow.owner_id
  JOIN countries c ON o.country_id = c.country_id
),

-- CTE: Total count of opportunities
total_ops AS (
  SELECT COUNT(*) AS total FROM opp_details
)

-- 1. Status Breakdown with Inline Subquery for % Calc
SELECT
  status,
  COUNT(*) AS status_count,
  ROUND(100.0 * COUNT(*) / (SELECT total FROM total_ops), 1) AS status_pct
FROM opp_details
GROUP BY status
ORDER BY status_count DESC;

-- 2. Active Opportunities by Stage (includes scalar subquery for %)
SELECT
  stage,
  COUNT(*) AS stage_count,
  ROUND(
    100.0 * COUNT(*) /
    (SELECT COUNT(*) FROM opp_details WHERE status = 'Opportunity'),
    1
  ) AS pct_of_active
FROM opp_details
WHERE status = 'Opportunity' AND stage IS NOT NULL
GROUP BY stage
ORDER BY stage_count DESC;

-- 3. Forecasted Weighted Revenue by Month
SELECT
  DATE_TRUNC('month', expected_close_date::date) AS forecast_month,
  SUM(deal_value_usd * probability_pct / 100.0) AS weighted_revenue
FROM opp_details
WHERE status IN ('New','Qualified','Opportunity','Sales Accepted')
  AND expected_close_date IS NOT NULL
GROUP BY 1
ORDER BY forecast_month;

-- 4. Global Win Rate Using Subquery in SELECT
SELECT
  (SELECT COUNT(*) FROM opp_details WHERE status = 'Customer') AS wins,
  (SELECT COUNT(*) FROM opp_details) AS total,
  ROUND(
    100.0 * 
    (SELECT COUNT(*) FROM opp_details WHERE status = 'Customer')::decimal / 
    (SELECT COUNT(*) FROM opp_details), 2
  ) AS global_win_rate
;

-- 5. Win Rate by Country with Correlated Subquery for Country Total
SELECT
  country_name,
  COUNT(*) AS total_ops,
  SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) AS wins,
  ROUND(
    100.0 * SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END)::decimal / COUNT(*), 1
  ) AS win_rate_pct,
  (
    SELECT ROUND(
      100.0 * COUNT(*)::decimal / (SELECT COUNT(*) FROM opp_details WHERE status = 'Customer'),
      1
    )
    FROM opp_details o2
    WHERE o2.country_name = o1.country_name AND o2.status = 'Customer'
  ) AS pct_of_global_wins
FROM opp_details o1
GROUP BY country_name
ORDER BY win_rate_pct DESC;

-- 6. Win Rate by Product and Country
SELECT
  country_name,
  product_name,
  COUNT(*) AS total_ops,
  SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END) AS wins,
  ROUND(100.0 * SUM(CASE WHEN status = 'Customer' THEN 1 ELSE 0 END)::decimal / COUNT(*), 1) AS win_rate_pct
FROM opp_details
GROUP BY country_name, product_name
ORDER BY country_name, win_rate_pct DESC;
