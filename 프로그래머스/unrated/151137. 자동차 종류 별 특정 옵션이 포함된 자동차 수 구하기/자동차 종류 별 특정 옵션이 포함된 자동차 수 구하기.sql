-- 코드를 입력하세요
# IN 을 쓸거면 아예 같은 게 있어야 함 안에서 고르는 게 아님
# REGEXP 가 안에 중에서 하나 골라서 맞으면 조건 충족

SELECT
    CAR_TYPE,
    COUNT(CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
# WHERE OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%'
WHERE OPTIONS REGEXP '(통풍시트|열선시트|가죽시트)'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC;