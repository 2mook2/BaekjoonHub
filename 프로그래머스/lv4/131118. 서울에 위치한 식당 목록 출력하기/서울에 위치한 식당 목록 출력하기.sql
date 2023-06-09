# SELECT
#     A.REST_ID,
#     A.REST_NAME,
#     A.FOOD_TYPE,
#     A.FAVORITES,
#     A.ADDRESS,
#     (
#         SELECT ROUND(AVG(B.REVIEW_SCORE), 2)
#         FROM REST_REVIEW B
#         WHERE A.REST_ID = B.REST_ID
#             AND B.REVIEW_SCORE IS NOT NULL
#     ) AS SCORE
# FROM
#     REST_INFO A
# WHERE
#     A.ADDRESS LIKE '서울%'
# ORDER BY
#     SCORE DESC,
#     FAVORITES DESC;


SELECT
    A.REST_ID,
    A.REST_NAME,
    A.FOOD_TYPE,
    A.FAVORITES,
    A.ADDRESS,
    (
        SELECT ROUND(AVG(B.REVIEW_SCORE), 2)
        FROM REST_REVIEW B
        WHERE A.REST_ID = B.REST_ID
    ) AS SCORE
FROM
    REST_INFO A
WHERE
    A.ADDRESS LIKE '서울%'
    AND EXISTS (
        SELECT 1
        FROM REST_REVIEW C
        WHERE A.REST_ID = C.REST_ID
            AND C.REVIEW_SCORE IS NOT NULL
    )
ORDER BY
    SCORE DESC,
    FAVORITES DESC;
