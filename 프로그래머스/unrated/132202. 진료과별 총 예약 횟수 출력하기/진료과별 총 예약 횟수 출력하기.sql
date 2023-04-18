# SELECT
#     MCDP_CD AS 진료과코드,
#     COUNT(PT_NO) AS 5월예약건수
#     # APNT_NO,
#     # PT_NO,
#     # APNT_CNCL_YN,
#     # APNT_CNCL_YMD
# FROM APPOINTMENT
# WHERE EXTRACT(YEAR FROM APNT_YMD) = 2022
# AND EXTRACT(MONTH FROM APNT_YMD) = 5
# AND APNT_CNCL_YN = 'N'
# GROUP BY 진료과코드
# ORDER BY 5월예약건수 ASC, 진료과코드 DESC;

SELECT MCDP_CD as "진료과코드", count(APNT_NO) as "5월예약건수"
from APPOINTMENT
where MONTH(APNT_YMD) = 05
group by MCDP_CD
order by count(APNT_NO) ASC, MCDP_CD ASC