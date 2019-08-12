STEP3  :     데이터 준비
             - pandas(데이터처리, 분석), numpy(수학, 과학용) 등을 사용
             - 데이터의 품질을 향상시킨다. 여기에 주안점
        3-1 데이터 정제 : 결측치, 이상치 처리
        3-2 데이터 통합 : 여러 군데서 가져온 데이터를 조합, 데이터 구성
        3-3 데이터 변환 : 데이터를 모델(4~5단계)에서 적합하게 사용되도록 변경 처리
        
1. pandas
- numpy를 기반으로 R에 대응하기 위해서 파이썬 진영에서 만든 데이터 분석용 라이브러리
- 데이터 전처리(정제, 통합, 변환) -> 시각화 -> 통찰!!

2. 환경구성
- 가상환경 analysis
- requirements.txt
  => 데이터 수집 시 사용한 내용 + @
- 절차
  1) CondaNavigatior에서 가상환경 analysis 생성
     1-1) 가상환경 analysis 기반 주피터 설치
  2) analysis 가상환경에서 open terminal 구동
  3) requirements.txt 작성
  4) requirements.txt 파일이 존재하는 곳까지 현재 디렉토리 이동
  5) (DataCrawling)$ conda install --file requirements.txt
  6) conda에 없는 캐피지는 제거 후 따로 설치
     $ pip install pymysql
     $ pip install folium==0.10.0

3. 목표
   - 데이터 준비 과정의 이해
   - pandas 사용
   - 시각화 처리(step4)도 병행
   - pandas, matplotlib, seaborn, foilum 등 주로 사용

4. 주제
 4-1. 서울시 구별 CCTV 분석, 구별 인구대비 분석, 
      - 연구목표 설정: 인구대비 CCTV 현황 분석 도출(약식)
      - 데이터 확보(수집)
        a) 공공데이터나 공개된 데이터를 확보할 수 있는지 검토
          1) 서울시 구별 CCTV 현황
             
             - 데이터 수집 출처 및 방법 : 
               서울열린데이터광장 -> cctv 검색 -> 서울시 자치구 연도별 cctv 현황 선택 -> 바로가기 -> 서울시 자치구 년도별 CCTV 설치 현황(2011년 이전
                _2018년)다운로드
             
             - 저작권 확인 필수 : 
               제공기관 서울특벽시
               저작궈자 자치구
               저작권자표시(BY)  이용허락조건
               이용이나 변경 및 2차적 저작물의 작성을 포함한 자유이용을 허락합니다.
             
             - 파일 위치 : 
               서울시 자치구 년도별 CCTV 설치 현황(2011년 이전_2018년)을  C:\Users\User\Desktop\py_projects\analysis\pandas\data 에 저장.
               편의상 파일명을 영문(seoul_cctv_state)으로 변경
       
           2) 서울시 인구 통계
              
             - 서울열린데이터광장
             
             - 저작권
               이용허락조건 저작권자표시(BY)  저작권자표시(BY)
               이용이나 변경 및 2차적 저작물의 작성을 포함한 자유이용을 허락합니다.
             
             -              
             
             - 주민등록인구 검색 > 서울시 주민등록인구(구별)통계 > 조회: 한국어, 소수점(0), 2011~2018년 > csv 다운로드
               > report.txt=> report.csv 변경 > ~./pandas/data/report.csv 위치
 
 4-2. 5대 강력 범죄 분석, CCTV, 인구대비 연관성 및 분석
      - 범죄분석을 통한 서울시 시각화 도출
      - 4-1 자료를 확장하여 분석진행




