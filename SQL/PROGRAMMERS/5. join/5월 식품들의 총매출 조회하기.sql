SELECT
    PRODUCT_ID,
    PRODUCT_NAME,
    SUM(PRICE * AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT
JOIN (
    SELECT
        PRODUCT_ID,
        AMOUNT
    FROM FOOD_ORDER
    WHERE PRODUCE_DATE LIKE ('2022-05%')
) DATE USING(PRODUCT_ID)
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC;