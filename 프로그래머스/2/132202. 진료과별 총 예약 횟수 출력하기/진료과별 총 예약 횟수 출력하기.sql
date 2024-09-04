-- 코드를 입력하세요/ 2022년 5월에 예약한 환자 수 / 진료과코드 별로 조회
#                  /컬럼명은 '진료과 코드', '5월예약건수'
#                 /예약한 환자 수를 기준으로 오름차순 정렬 / 환자 수가 같다면 진료과 코드 오름차순 정렬
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = '2022' AND MONTH(APNT_YMD) = '05'
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO) ASC, MCDP_CD ASC
