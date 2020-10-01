# ec2connector

매번 맥 터미널로 aws ec2 에 붙을때… 콘솔을 열고 퍼블릭 주소를 카피해서, 터미널을 열고, pem 파일이 있는 디렉토리로 이동해서, “ssh -I key.pem -h ec2-user@복사한아이피” 를 타이핑하고 접속 하곤 했죠…
이게 넘나 귀찮아서 sdk 로 online 인 인스턴스들 주소를 받아와서 뿌려주고 선택하면 접속되는 파이썬 스크립트를 하나 만들었습니다.
 
이런 모양으로 동작합니다. 좋죵?
<pre><code>
(base) pizon@Documents % ecc
---------------------------------------------------------------------------------------------------------
  1|#Noname (i-1196c8f1bff824d9f)                     |t2.micro       |13.111.226.180   |pizon.pem
  2|BenchmarkWebserver (i-11398d94649608b4)           |c5n.2xlarge    |54.111.154.230   |pizon.pem
  3|BenchmarkWebserver_ori (i-1162f7940b649f455)      |c5n.2xlarge    |15.111.5.142     |pizon.pem
  4|DBTEST-linux1-mysql57 (i-1147926821a97dd4c)       |r5.large       |15.111.1.106     |pizon.pem
  5|IoT_Bot (i-11a02d81be381047f)                     |c5n.2xlarge    |54.111.1.88      |pizon.pem
  6|IoT_Bot_Test2 (i-112b3ae288c528bd)                |c5n.2xlarge    |54.111.80.0      |pizon.pem
  7|IoT_Bot_Test3 (i-1194d2bbe80eaaa65)               |c5n.2xlarge    |54.222.89.194    |pizon.pem
  8|IoT_Bot_Test4 (i-11431022da6b5d33e)               |t2.xlarge      |13.333.224.48    |pizon.pem
  9|Iotchat-env (i-11f591f4184cc217f)                 |t2.micro       |15.444.216.159   |N/A
 10|TEST-BOT-azC-SYSBENCH (i-11fb8a6223835e98d)       |c5n.2xlarge    |54.555.1.180     |pizon.pem
 11|TestClients (i-1118cb93436a88f99)                 |c5n.xlarge     |15.666.1.2       |pizon.pem
 12|WebServer2 (i-11dbe5a612dcba8aa)                  |c5.xlarge      |15.111.22.915    |pizon.pem
 13|Webserver-azC-SYSBENCH (i-1193b4692387427df)      |c5n.2xlarge    |52.111.22.116    |pizon.pem
 14|internal redis_connector (i-110bffb269013fa32)    |t2.micro       |52.111.22.127    |pizon.pem
 15|publish test (i-111423a13ac71ab24)                |t2.micro       |N/A              |pizon.pem
 16|test web (i-1145ea8b498071ef6)                    |t2.xlarge      |13.111.22.41     |pizon.pem
 ?> 
select number to connect, press x to exit.
 ?> 5
running... ssh -i /Users/pizon/Documents/pizon.pem ec2-user@54.111.111.88
</code></pre>
아래 방법대로 사용하시면 됩니다

1. 로컬에 aws cli 가 설치되있어야 합니다.
aws configure 로 access key id / secret key / region 을 설정해주기 위함인데(이 정보로 접속합니다), 직접 ~/aws/config, credentials 를 수정해도 됩니다.
맥용cli : https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/install-cliv2-mac.html
 
2. Python 3 로 만들었습니다, python 과 python 용 aws sdk 인 boto3 도 설치가 되있어야 합니다.
파이썬 : https://www.python.org/downloads/
Boto3 : https://aws.amazon.com/ko/sdk-for-python/   (pip install boto3 하면 됩니다)
 
3. ec2connector.py 을 다운로드 받으시고, 파일을 열어서 , 다음 라인에 pem 키파일이 있는 위치를 설정해줍니다.
<pre><code>
#########CONFIG############################
key_path = "/Users/Your/Documents"
########################################### 
</pre></code>

4. python ec2connector.py 로 실행시켜주면 끝입니다!! 원하는 인스턴스 번호를 누르면 쑝 접속됩니다. 넘나 편하지용

5. 더 편하게 쓰기 위해서, 저는 ec2connector.sh 파일을 만들어서, python ec2connector.py 실행하도록 써주고,
ln -s /usr/local/bin/ecc /Users/Your/Documents/ec2connector.sh
이렇게 /usr/local/bin 에 링크를 만들어서, 아무데서나 ecc 를 치면 작동하도록 해두었습니다!!
터미널에서 ecc 치고, 번호 고르면 땡!!! 입니다…
