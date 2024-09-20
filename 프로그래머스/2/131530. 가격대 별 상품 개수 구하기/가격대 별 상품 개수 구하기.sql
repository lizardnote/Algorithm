# -- 코드를 입력하세요
# SELECT TRUNCATE(PRICE,-4) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
#         FROM PRODUCT
#         GROUP BY PRICE_GROUP
#         ORDER BY PRICE_GROUP
        
SELECT floor(price/10000)*10000, count(*)
FROM product
GROUP BY floor(price/10000)
ORDER BY 1;
