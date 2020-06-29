# Qdoc을 소개합니다.
현재 한국 의료시스템의 단점을 개선하고자 환자-의사 소통증진 챗봇 서비스를 기획했다. 목적은 환자가 내원하기 전, 진료에 필요한 사전 정보를 제공하고 의사는 이를 통해 더 정밀한 진료를 해내는 데 있다. 환자는 어플의 챗봇을 이용해 과거 병력, 증상, 기간, 복용 약물, 환부 사진 등의 정보를 제공하고 의사는 이를 받아 사전에 환자를 파악할 수 있다. 또한 환자는 네비게이션을 통해 병원에 쉽게 찾아갈 수 있으며 진료가 끝난 후 약물 복용시간 알라미를 이용해 지속적인 관리를 받을 수 있다.

##  구성 요소

 1. flutter
 2. Rasa
 3. flask_python
 4. etc. (crawling file)

### flutter
- 의학 상식 사전 : 
Dart를 이용하여 Flutter내 Crawling 작업으로 단어 및 설명 수집
snackbar 형식으로 각각의 설명 보여준다.

- 약물 복용 알람 :
복용하는 약의 이름, 용량, 종류, 복용시간을 입력받아 Database에 저장
매일 복용 시간이 되면 어플이 꺼져있어도 자동으로 Notification을 이용해 복용할 약과 용량을 진동과 함께 알려준다.

- 오시는 길:
flutter의 Webview package 를 이용하여 google map service 를 출력한다. 현재 위치에서병원까지의 대중교통 경로를 알려준다.
### Rasa
- 챗봇 : 
웹 UI를 제공하는 Rasa X 를 이용한다.
python을 이용하여 story, actions, NLU(intent) 구현한다.
웹 서버를 이용하여 Rasa X 내에 이미지 전송 기능 구현한다.

- 충치 검진 : 
데이터 전처리 를 이용한 Labeling 작업한다.
YOLO model training을 이용하여 충치 검진 한다.

### flask_python
- 이미지 전송 :
Rasa X 내서의 이미지 전송을 위해 웹서버로 이미지 전송 기능을 구현한다.

### etc.(crawling file)
- 코로나 확진자 경로를 위해 selenium 라이브러리를 이용하여 Crawling, 및 txt 파일로 작성한다.

## 실행 방법
 이미지 전송 및 수신을 위해 flask_template.py, flask_upload.py 를 python flask_template.py, python flask_upload.py 명령어로 각각 실행 시켜 준다.

 Rasa의 actions를 실행하기 위해 rasa run actions 명령어를 입력해준다. 그 후 작업이 완료 되면 rasa X 를 입력하여 rasa X 서버를 가동시켜 준다.

 가동이 완료되면 Flutter을 이용하여 만든 어플을 실행시키고 '챗봇 상담연결' 버튼을 누르면 rasa X guest session 으로 접속이 되고, 챗봇을 이용할 수 있게 된다.

 Flutter 어플리케이션 기능들은 어플을 실행 시키고 각각의 버튼을 누르는 방식으로 이용 할 수 있다
 
 '의학 용어 사전'은 실시간으로 추가되는 사전 내용을 위해 버튼을 누르면 Crawling 을 하여 용어들을 목록으로 출력하게 해주고, 용어들을 누르면 snackbar 형태로 용어 설명을 볼 수 있게 하였다. 그리고 검색 기능을 추가하여 원하는 단어를 검색하여 결과를 누르면 설명이 나오게끔 개발 되었다.

 '알람 예약하기' 기능은 병원에서 복용약을 처방받은 환자나 만성질환자의 경우 주기적인 약복용 관리를 위해 개발 하게 되었다.
먼저 오른쪽 하단에 + 모양 버튼을 누른 뒤 약물의 이름, 용량, 종류를 고르고 시간을 입력 해 줍니다. 그러면 그 시간이 되면 백그라운드에서도 자동으로 notification 기능을 이용해 진동과 함께 알림이 울리는 것을 확인 할 수 있다.

'오시는 길' 기능은 버튼을 누르면 원하는 병원이 목적지로 설정되어 있는 것을 확인 할 수 있고, 출발지에 '내 위치' 버튼을 클릭하여 병원까지의 대중교통 정보 및 경로를 알려 주는 것을 확인 할 수 있다.

# 역할 분담
- [Flutter]
Controller : 성현규
UI: 박세리

- [Rasa]
NLU : 이진수
Core : 류연준
Story : 류연준
Action : 이진수

- [ YOLO ]
Labeling : 박세리
Training : 이진수 성현규 류연준

- [ Flask ]
Upload : 성현규
template : 박세리
