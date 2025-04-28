-- Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
-- Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age.
-- Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power.
-- If more than one wand has same power, sort the result in order of descending age.

SELECT W.ID, WP.AGE, W.COINS_NEEDED, W.POWER
FROM WANDS W 
JOIN WANDS_PROPERTY WP
ON (W.CODE = WP.CODE)
WHERE WP.IS_EVIL = 0
AND (WP.AGE, W.POWER, W.COINS_NEEDED) IN
    (SELECT WP.AGE, W.POWER, MIN(W.COINS_NEEDED)
    FROM WANDS W
    JOIN WANDS_PROPERTY WP ON W.CODE = WP.CODE
    GROUP BY W.POWER, WP.AGE)
ORDER BY W.POWER DESC, WP.AGE DESC;