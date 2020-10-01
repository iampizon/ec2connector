# ec2connector

매번 맥 터미널로 aws ec2 에 붙을때… 콘솔을 열고 퍼블릭 주소를 카피해서, 터미널을 열고, pem 파일이 있는 디렉토리로 이동해서, 

“ssh -I key.pem -h ec2-user@복사한아이피” 를 타이핑하고 접속 하곤 했죠…

이게 넘나 귀찮아서 sdk 로 online 인 인스턴스들 주소를 받아와서 뿌려주고 선택하면 접속되는 파이썬 스크립트를 하나 만들었습니다.
 
이런 모양으로 동작합니다. 
<pre><code>
>> ec2connector % ecc                          
--[ ap-northeast-2 ( 16 ) ]---------------------------------------------------------------------------------------
  1|#Noname                  |i-1116c8f1bff824d9f  |t2.micro      |13.124.111.111  |ap-northeast-2a |mykey.pem
  2|BenchmarkWebserver       |i-111398d94649608b4  |c5n.2xlarge   |54.180.111.111  |ap-northeast-2a |mykey.pem
  3|BenchmarkWebserver_ori   |i-1112f7940b649f455  |c5n.2xlarge   |15.165.5.111    |ap-northeast-2b |mykey.pem
  4|DBTEST-linux1-mysql57    |i-1117926821a97dd4c  |r5.large      |15.111.41.106   |ap-northeast-2d |mykey.pem
  5|IoT_Bot                  |i-11102d81be381047f  |c5n.2xlarge   |54.111.111.88   |ap-northeast-2b |mykey.pem
  6|IoT_Bot_Test2            |i-1112b3ae288c528bd  |c5n.2xlarge   |54.111.80.0     |ap-northeast-2c |mykey.pem
  7|IoT_Bot_Test3            |i-1114d2bbe80eaaa65  |c5n.2xlarge   |54.111.89.111   |ap-northeast-2c |mykey.pem
  8|IoT_Bot_Test4            |i-11131022da6b5d33e  |t2.xlarge     |13.111.111.48   |ap-northeast-2a |mykey.pem
  9|Iotchat-env              |i-111591f4184cc217f  |t2.micro      |15.111.216.111  |ap-northeast-2a |N/A
 10|TEST-BOT-azC-SYSBENCH    |i-111b8a6223835e98d  |c5n.2xlarge   |54.111.30.111   |ap-northeast-2c |mykey2.pem
 11|TestClients              |i-1118cb93436a88f99  |c5n.xlarge    |15.111.221.2    |ap-northeast-2c |mykey2.pem
 12|WebServer2               |i-111be5a612dcba8aa  |c5.xlarge     |15.111.44.95    |ap-northeast-2d |mykey2.pem
 13|Webserver-azC-SYSBENCH   |i-1113b4692387427df  |c5n.2xlarge   |52.79.111.111   |ap-northeast-2c |mykey.pem
 14|internal redis_connector |i-111bffb269013fa32  |t2.micro      |52.79.111.111   |ap-northeast-2c |mykey.pem
 15|publish test             |i-111423a13ac71ab24  |t2.micro      |N/A             |ap-northeast-2a |mykey.pem
 16|test web                 |i-1115ea8b498071ef6  |t2.xlarge     |13.111.11.1     |ap-northeast-2c |mykey.pem
 ?> 2
running... ssh -i /Users/My/Documents/ec2connector/mykey.pem ec2-user@54.111.111.230
</code></pre>
아래 방법대로 사용하시면 됩니다

1. 로컬에 aws cli 가 설치되있어야 합니다. 
- aws configure 로 access key id / secret key / region 을 설정해주기 위함인데(이 정보로 접속합니다), 직접 ~/aws/config, credentials 를 수정해도 됩니다.
- 맥용cli : https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/install-cliv2-mac.html
 
2. Python 3 로 만들었습니다, python 과 python 용 aws sdk 인 boto3 도 설치가 되있어야 합니다.
- 파이썬 : https://www.python.org/downloads/
- Boto3 : https://aws.amazon.com/ko/sdk-for-python/   (pip install boto3 하면 됩니다)
 
3. ec2connector.py 을 다운로드 받으시고, 파일을 열어서 , 다음 라인에 pem 키파일이 있는 위치를 설정해줍니다.
<pre><code>
#########CONFIG############################
key_path = "/Users/Your/Documents"
########################################### 
</pre></code>

4. python ec2connector.py 로 실행시켜주면 끝입니다!! 원하는 인스턴스 번호를 누르면 쑝 접속됩니다. 넘나 편하지용

5. 더 편하게 쓰기 위해서, 저는 ec2connector.sh 파일을 만들어서, python ec2connector.py 실행하도록 써주고,
- ln -s /usr/local/bin/ecc /Users/Your/Documents/ec2connector.sh
- 이렇게 /usr/local/bin 에 링크를 만들어서, 아무데서나 ecc 를 치면 작동하도록 해두었습니다!!
- 터미널에서 ecc 치고, 번호 고르면 땡!!! 입니다…

6. 실행 인자로 리전을 선택하는 기능을 추가했습니다(2020/10/1)
- ecc ap-northeast-2 처럼 리전을 파라미터로 넘기면 해당 리전의 인스턴스 정보를 가져옵니다.
