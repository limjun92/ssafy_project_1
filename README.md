# 2020.01.13) 회의록1
  6주 동안의 주차 계획을 간략하게 짜기
  업무 분담 세분화
  와이어 프레임 화면구성 짜기
  아이디어 구체화
  어떤 것을 공부하면 좋을지
  ai를 적용한 웹페이지를 만들자

# 2020.01.14) 회의록2
  목업툴을 이용해 페이지 그리기
  역할 분배
  스프린트, 지라 시스템 활용하여 계획 세우기 

# 2020.01.15) 회의록3
  DB 완성하기 : 기본 틀을 짜고 시행착오를 겪으면서 수정하자!
  GIT 게임 하기(x)
  5시30분 : 깃 올리기

# 2020.01.16) 회의록4
  발표자료 다시 정리하기(목업) - 2
  GIT 게임 하기 - 1
  GIT 파서 연습 - 2
  3명 : API - 네이버 지도 - 2
  2명 : FRONT FREE, 회원관리, 메인페이지 - 2
  중간중간 사진 찍기
  형준님의 그림 PPT앞에 넣기

# 2020.01.17) 회의록5
  스크럼 : 어제 각자 결과 발표

  지도 api
  장점
  단점
  네이버
  국내 지리 요건을 잘 반영함

  위치 정보 전달이 안됨(위도, 경도도 나오지 않음)
  검색 결과 최대 5개 한계
  서비스 2020.6.1 종료
  검색 결과 오류가 많음
  서버가 안돌아가는 경우 발생
  구글 클라우드 플랫폼으로 넘어가서 사용하기 위해 카드 등록 필요
  장소 검색 비용이 1건당 1원

  구글
  개발이 쉬움
  검색 결과 정확도가 높음

  라이브러리가 영어
  국내 지리 조건을 잘 반영하고 있는지 의문

  카카오
  다음 맵에서 넘어와서 국내 지리 조건 시스템 구축이 잘 됨
  개발자 도구 잘 되어있음


  아직 없음



  결론: 카카오 

  API 역할 분담 - 예은, 창현, 준형
  메인페이지 - 경석
  로그인 기능 - 서영

  1. API 회의
  시행착오를 겪어보자
  현재위치에서 주변카페 검색
  현재위치도 파라미터로 남기기 
  스타벅스 => 지도에 찍히기
  필터(그 카페를 제외한 결과 나오기) - 핀 사라지게


  2. 발표 feed back
  카페가 좋아 추천 받아 -> 사람 몰림 -> 자리가 없음 -> 어떻게 확인할것인가???
  내가 가고싶은 카페인데 알리고 싶을까? 사람들이 많아지는데...
  사람들이 리뷰를 달고 싶을까>(리뷰 다는게 사용자에게 무슨 이득??)
  카페 크롤링을 어떻게 할 것인가? (초기 비용 필요)
  회원가입할 때 회원과 사장 정보를 어떻게 구별할것인가?
  사장이 정보를 입력하는데 사장이 폐업하면 장소 정보를 어떻게 수정할것인가? 
  리액트 넘 어려워ㅜㅜㅜㅜ



# 2020.01.20) 회의록6
  api를 front에 받아 올지 back에 받아 올지 회의하기
  front end 담당자 필요, vue 노하우 정리하는 git을 만들자
  스프린트 새로 짜기
  공용 깃헙
  역할 나누기


  회원가입
  Front화면 구성하기
  Back REST
  DB TABLE



  로그인
  Front화면 구성하기
  Back 짜기

  메뉴
  Front화면 구성하기

  Map
  Front화면 구성하기



  상세페이지
  Front화면 구성하기
  백엔드 구현

  DB
  DB결정
  TABLE 구현

  API

  장소 검색 백엔드 구현
  코드리뷰
  현재 내 위치 기반으로 맵 표시
  검색 후 장소 리스트 보여주고 링크 연결하기, 맵에도 표시






# 2020.01.21) 회의록7
  지라에 구체적으로 작성하기
  이번주 목표 정하기
  본인이 맡은 부분 구현하기
  예은 - 로그인&회원가입 기능, 서영이 부분에 붙어서 도와주기
  경석 - 상세페이지 구현(상세페이지를 분리해서 개발할 예정)
  서영 - JWT토큰 저장하는거, 로그인&회원가입
  준형 - Map API 필터(오전안에 끝낼 예정)
  창현 - MAP marge



# 2020.01.22) 회의록8
  깃 프로젝트 통합 작업 - 잊지 말자 1/22 GIT 사태(주동자 : 양예은)
  프젝 2주차 3일째 - 본인이 맡은 부분 구현
  경석 - 프론트 마무리 하고 백엔드 부분 넘어갈 예정
  준형 - 지도 이동했을 때 동적으로 핀 찍어주기
  서영 - 	vuetify 이용해서 로그인 화면 만들기
  예은 - 로그인 및 회원가입 시 validation 작업
  창현 - vue.js 이용해서 map화면 만들기


# 2020.01.23) 회의록9
  프젝 2주차 4일째(2주차 마지막날, 4시 마감)
  준형 - 맵 필터, 장소 목록 기능 합치기
  서영 - 로그인(반응형 웹), 회원가입 화면 완성
  예은 - 데이터베이스 설계 및 장고 구현
  경석 - 이미지 선택, 업로드, 삭제 구현
  창현 - vue.js 이용해서 kakao map api 붙이기


# 2020.01.28) 회의록10
  이경석 - MERGE, DJANGO - DETAIL, 사장님 등록 페이지
  준형 - MAP API 기능 VUE에다가 합치기, 기능 추가하기
  창현 - MAP API 기능 VUE에다가 합치기, 기능 추가하기, MODAL붙이기
  이번주 : 목업처럼 클릭하면 넘어가게끔 만들자
  서영 - 상세페이지 구현(좋아요)
  예은 - DB마무리, BACK기능 구현, DJANGO README추가


# 2020.01.29) 회의록11
  경석 - 이미지관리보관, axios통신
  준형 - map api 기능 vue에 옮기기, 필터기능 옮기기(+보완) => API완성
  창현 - MODAL를 이용해서 페이지 구성방식 생각하고 구현하기(다른페이지참고), 데이터 전송
  서영 -  좋아요 기능, 경석님과 대화후 작업
  예은 - 댓글 crud, 마이페이지

# 2020.01.30) 회의록12
  경석 - image upload
  준형 - map 충돌난 부분 해결
  창현 - modal keyword button, map과 keyword 로직
  서영 - 좋아요 기능구현
  예은 - 댓글 front구현

  회의 - 회의 내용 10시까지 올리기
  DB 내용 같이 보면서 수정하기(이름바꾸기)
  맵 로직? 맵에 보여지는 우선순위? 
  예를 들어) 1) ‘분위기가 좋은’, ‘의자가 편한’ 을 선택하고 검색 누르면 어떻게 맵에 보여지는지와 그 안의 로직
  2) 로그인 했을 때 사용자 추천 맵을 줄지?
  3) 맵 화면 기능은 뭐뭐 보여주는지? (기존 맵이랑 비교)
  현재 역할 배분을 기능별로 나눠서 불편함은 없는지(프론트,백엔드 둘다 하는데에 있어 어려움)
  vue 폴더로 세분화 - ok

  콘센트 개수에 따른 그림 
  아메리카노 가격
  좌석당 콘센트 비율
  흡연실
  DB안에서 

  Map 건의할거
  ‘스타벅스’ 검색하면 내 위치로 찾지만 주변 가까운게 없어서 화면에 안보임

# 2020.01.31) 회의록13
  경석 - foreignkey, manytomany post방식 수정
  준형 - 리스트와 필터를 연동시켜서 만들기
  창현 - map keyword search 오류 해결, 검색 정확도 높이기
  서영 - 좋아요 버튼 수정(POST 요청 해결)
  예은 - foreignkey, manytomany post방식 수정

# 2020.02.03) 회의록14
  경석 - 디테일 리스트 뿌려주기 확인 웹 페이지에서 뭐할지 나누기
  준형 - api 합치기 
  창현 - 웹 화면을 모바일 화면 으로 디자인
  서영 - 좋아요 오류 수정, 리스트 & 디테일 템플릿
  예은 -  댓글 crud 웹적용,디테일 리스트 뿌려주기

# 2020.02.04) 회의록15
  경석 - 반응형 웹 구성하기, 필터창 만들기
  준형 - db데이터 map페이지로 가져오기
  창현 - 부모자식간 데이터 통신, 사용자 설문작업 
  서영 - 건물등록 프론트 꾸미기
  예은 -  사람들 리뷰 폼 만들고 리뷰 분석 , 댓글 오류 

 
# 2020.02.05) 회의록16
  경석 - 오버레이 치환
  준형 - 마커 or 커스텀 오버레이 db연동
  창현 - 더미데이터 워드 클라우드, 사용자쪽에서 나는 에러 파악
  서영 - 건물등록 폼 만들기, 핀 디자인
  예은 - 워드 클라우딩과 더미데이터 

# 2020.02.06) 회의록17
  경석 - 마커 오버레이 수정 엑시오스 통신
  준형 - 사용자 리뷰와 나의 선호도를 비교하여 맵에 입력해주기
  창현 - 자연어 처리, 로그인 vuex
  서영 - 디테일페이지 디자인, 마커 구상
  예은 - 자연어 처리, 댓글분석 알고리즘 로직 구현

# 2020.02.07) 회의록18
  경석 - 커스텀 오버레이에서 데이터 받아서 상세페이지 
  준형 - 마커 오류 수정
  창현 - 서버 구축하고 더미데이터 입력
  서영 - 디테일페이지 꾸미기
  예은 - 댓글 카운트  디비에 입력


# 2020.02.10) 회의록19
  경석- 에러 inner html element만들어서 create , appned child 에러 고치기, 더미 데이터 넣어서 확인하고, 키워드 분석 뿌리기
  준형- DB 정리 
  창현- map 화면 로그인 컴포넌트, 필터 버튼 엘리먼트를 모바일 화면에서 보이고 동작하게 연결
  서영- bootsrap 템플릿 적용하기 

# 2020.02.11) 회의록20
  경석- 자바스크립트 그림 선택 이팩트 소스 찾기, 컴포넌트 구성 
  준형- 맵 이동할 때 추천 사라지는 에러 고치기, DB에 등록 된 내용 다 맵에 표시, 필터 적용
  창현- checkbox UI, 맵과 검색 컴포넌트(부모, 자식)연결, 장소id, 위도, 경도 받아오기, DB데이터 전송, 저장까지 완성하기,
  예은-  회원가입할 때 사장님은 설문조사 안뜨게, place 없는 곳에 comment 만들 때 place 추가 되게, 댓글 로그인 한 사람만, 좋아요할 때 새창 생기게, 그래프로 차트 보여주기
  서영- 디테일  페이지 구성 완성하기, 맵에 넣을 핀 기능별로 완성하기

# 2020.02.12) 회의록21
  경석- 상세페이지 디자인 합치기 
  창현- 맵 UI 호갱노노 참고해서 꾸미기
  준형- 마커 번경(이미지)
  예은- 그래프 차트 보여주기, 리뷰 생성시 장소 생성
  서영- 마커 간단하게 바꾸기, 상세정보 페이지 안뜨는 오류 해결하기

  플래티콘?

# 2020.02.13) 회의록22
  경석- 디테일 페이지에서 가게 정보를 보여주기, 댓글, 마이페이지랑 사장님 등록페이지 템플릿 어떻게 할지 고민, 배포를 해야되는데,, 고민을 해봐야할듯!
  창현- 도서관 스터디카페 분류 모델 등록하기
  준형- 도서관, 스터디카페 모델, 사소한 오류 해결
  예은- 카카오라이브러리 분류 디테일페이지에 바로 나오게, 등록페이지에서 db에 있는지 확인하고 update 있으면 create, 리뷰분석 차트 그래프 바꾸기
  서영- 서치바 고치기, 디테일 페이지 세부적인 디자인 수정

# 2020.02.14) 회의록23
  경석- 통합, 내용 채우기, 추후에 꾸미기
  창현- 마이페이지 좋아요 누른 카페 보여주기
  준형- 오류, 맵에 못한 기능(필터), 프론트 꾸미기 도와주기
  예은- 도서관, 스터디카페 등록 폼 만들기
  서영- 폼 꾸미기, 디테일 페이지 이미지 보여주기,

  웹서비스 설명 (서치 바 아래에 달기)

# 2020.02.17) 회의록24
  창현 - 오류수정, 디버깅
  경석 - 주말에 한거 합치기, db넣을 실데이터 스크립트 만들기, 디테일페이지 수정, aws올리기 & 테스트
  서영 -  front 디자인 수정 - map, detail, regist, login, signup
  준형 - 주말에 한거 합치기, css
  예은 - 오류수정, msql insert 문 스크립트


# 2020.02.18) 회의록25
  준형 - 검색 기능 수정, PPT, 동영상, 디자인 변경, 교통뷰 스크롤
  창현 - 카카오 장소 INFO 다른 방법으로 구해오는거 찾아보기, DETAIL에러 SUBMIT 잘됐는지 표시하는 기능, SUBMIT 클릭 확실히, MAP 댓글 보이게 
  삼잉 - DETAIL PAGE, LOGIN, SIGNUP
  경석 - 컨텐츠 바꾸기(+ TEST),
  예은 - 서영DETAIL 오류확인, FRONT 수정, 시나리오 
  모두 - 에러잡기 

  UCC
  시간 : 2분 - 대화, 3분 - 기술 소개
  주인공 : 준형,창현,서영,경석
  시나리오, 촬영 : 예은

  대화(2분)
  준형이는 노트북을 챙기고 있다.

  창현 - 준형쿤 프로젝트 안하고 지금 어디가! !!!!
  준형 - 나 카페가서 알고리즘 풀려고
  창현 - 어디카페? 
  준형 - 응?...어디가지? 그냥 노트북 사용할 수 있는 곳
  경석 - 응안돼
  준형 - 경석님 너무해요.

  서영이 NCS책을 챙기며
  서영 - 저도 같이가요. NCS해야겠어요.
  경석 - 응안돼
  준형 - 서영님 어디로갈까요??
  서영 - 전 책으로 공부해야해서 밝고 조용한곳이 좋아요.
  준형 - 서영님 저는 어디로 가야할지 모르겠어요 ㅠㅠ
  창현 - 스터디 맵을 사용해봐! 카페, 도서관, 스터디카페 해결(빡빡빡빡)



스터디맵 설명(3분)


