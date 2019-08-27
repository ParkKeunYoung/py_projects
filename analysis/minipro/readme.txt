< miniproject 과정 > 
   - Aanconda nevigator 가동
   - Environments > create > minipro 생성
   - 프로젝트에 필요한 패키지 설치
     (DataCrawling)$ pip install -r requirements.txt
     or
     (DataCrawling)$ conda install --file requirements.txt
   -  ERROR: Could not find a version that satisfies the requirement pymysql==0.9.8 (에러남)
      > conda update -n base conda > conda install tensorflow > conda install --file requirements.txt

   - ※ 2006년 7월부터 출국카드작성 폐지로 행선지별 집계 불가 > 주요국의 관광부 / 관광공사에서 집계 발표하는 한국인 입국 (우리 입장에서는 출국) 통계를 수집한 자료 

   - 자료 분석 할 수 있는것
     자료1. 월별,년도별 입국자( 수, 목적 )
              1) 년도별 - 주 별(아시아주,중동,미주,구주,대양주,아프리카주) 인구비교, 목적 비교 
		     - 주 별로 비교해보니 아시아주 입국자가 월등히 많았다. 아시아주에서 오는 관광자들의 목적을 비교.
              2) 년도별 - 각 나라 관광 인구비교, 탑 5 목적비교
              3) 월별
              
              
     1) 외래객 입국 목적별,국적별 분석 (나라마다 어느 월에 제일 많이 오는지, 나라마다 입국목적 1순위)
     2) 출국자(성별,연령별), 어느 나라에 얼마나 갔는지 통계
     3) 관광수입,지출,수지 파악
     * 시각적인 부분 plt이용가능

   - 2004년부터 