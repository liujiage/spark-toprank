# spark-toprank
Spark Lab uses Python Spark RDD to run Spark job on Spark standalone, the task to calculate the top rank of review goods,  the goods data are downloaded from AWS. 
<pre>
1.Lab environment 
1 laptop
OP: window 11 Pro
Memory (RAM): 16GB
Processor: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, 2419 Mhz, 4 Core(s), 8 Logical Processor(s)
Software: 
spark-3.4.1-bin-hadoop3.tgz
winutils-master.zip (the latest version, Hadoop running on window need it) 
openjdk version 64-bit "17.0.6" 2023-01-17 LTS
python 3.11 version
Spark standalone 
Setting Environment variables:
JAVA_HOME= C:\Study\tools\jdk-17.0.6+10
HADOOP_HOME= C:\Study\tools\hadoop
SPARK_HOME= C:\Study\tools\spark
PYSPARK_PYTHON= C:\Python311\python.exe
PYSPARK_DRIVER_PYTHON= C:\Python311\python.exe
#add java,Hadoop,spark lib folders into path.
Start Master Node on Spark Standalone:
spark-class org.apache.spark.deploy.master.Master
Start a Worker Node and register it in Master Node:
spark-class org.apache.spark.deploy.worker.Worker spark://IP:7077
2.Implementation
Step 1 
Read Patio_Lawn_and_Garden.json  as RDD 1, and through by Spark RDD SDK (map, reduceByKey,SortBy,Take) to process data. ReduceByKey can help group data by key, the key is product id(asin) and review time. Can use this key to find product total reviews in one day, and then using SortBy can sort top 15 records, finally use Map to handle top 15 records, and use product id(asin) as the key.  
Step 2
Read Patio_Lawn_and_Garden.json as RDD 2, and using Map SDK to take data we need it. the key is product id(asin) , and the value is the brand name of the product. 
Step 3 
Joining RDD 1 and RDD 2 and write the result to local.
More detail can see source code in Appendix B. 
</pre>
![image](https://github.com/liujiage/spark-toprank/assets/183577/8747a803-1ea1-4ad4-a0d4-a664ba8b8f62)
<pre>
Note: Below photo is a hight level design, that is not include (reduceByKey, SortBy, and Map implement detail).   
</pre>
<pre>
3.Testing and Result
Spark-submit --master spark://172.20.10.5:7077 --driver-memory 8g --executor-memory 8g --py-files app.zip app.py Patio_Lawn_and_Garden.json meta_Patio_Lawn_and_Garden.json ./output/
Note: app.zip how to package it can reference Appendix A
</pre>
![image](https://github.com/liujiage/spark-toprank/assets/183577/b011c530-613f-4c64-8905-3c4993479091)
<pre>
Submit a python job to Spark standalone, as you can see above running the job on Spark, we can using http://localhost:8080 to watch Spark running status.  The job was successful finished and spend 3.8 minutes only. 
Result: in  ./output/part-0000 
('B00LLZ496O', 107, '08 7, 2017', 4.672897196261682, 'Skydrop')
('B01H57HKN0', 68, '07 26, 2016', 4.926470588235294, 'Sago Brothers')
('B01GE77QT0', 61, '12 7, 2017', 4.80327868852459, 'ThermoPro')
('B00FKGY2XU', 60, '10 13, 2013', 4.983333333333333, 'MyNativity')
('B01H57HKN0', 57, '07 15, 2016', 4.859649122807017, 'Sago Brothers')
('B00LLZ496O', 54, '08 23, 2017', 4.62962962962963, 'Skydrop')
('B00WJ3GFQE', 54, '03 31, 2017', 5.0, 'Flamen')
('B001N8CCQS', 52, '08 3, 2017', 5.0, 'DNR Tech.')
('B001N8CCQS', 52, '08 27, 2011', 5.0, 'DNR Tech.')
('B001N8CCQS', 52, '04 21, 2016', 5.0, 'DNR Tech.')
('B001N8CCQS', 52, '08 15, 2016', 5.0, 'DNR Tech.')
('B001N8CCQS', 52, '09 19, 2016', 4.0, 'DNR Tech.')
('B001N8CCQS', 52, '12 11, 2017', 1.0, 'DNR Tech.')
('B001N8CCQS', 52, '09 1, 2013', 5.0, 'DNR Tech.')
('B001N8CCQS', 52, '12 26, 2016', 5.0, 'DNR Tech.')
Backend running can see Appendix C
4.Reference
https://saturncloud.io/blog/how-to-setup-apache-spark-on-windows-10-a-stepbystep-guide/
https://bobbyhadz.com/blog/python-was-not-found-run-without-arguments-to-install
https://stackoverflow.com/questions/48260412/environment-variables-pyspark-python-and-pyspark-driver-python
https://www.tutorialkart.com/apache-spark/spark-read-json-file-to-rdd/#gsc.tab=0
https://sparkbyexamples.com/pyspark-tutorial/
https://sparkbyexamples.com/python/python-lambda-function/
https://sparkbyexamples.com/spark/show-top-n-rows-in-spark-pyspark/
*https://aamargajbhiye.medium.com/apache-spark-setup-a-multi-node-standalone-cluster-on-windows-63d413296971
Appendix A
How to package python project for Spark as a job  
python -m venv pyspark_venv #create a venv for python project 
./pyspark_venv/Scripts/activate #activate venv only for window (Mac source ./pyspark_venv/bin/activate)
pip freeze > requirements.txt #collecting all dependencies. Make sure your source code inside. 
python -m pip install --upgrade pip
pip install -r requirements.txt #install all dependencies into this project’s venv for packaging them. 
Package the project all source code and all dependencies to a zip file as a Spark job source file. 
Appendix B 
For Source Code see app.py
Appendix C
Running on backend 
</pre>
![image](https://github.com/liujiage/spark-toprank/assets/183577/3d220032-ed96-41fb-be54-97a3043dc8ad)

<pre>
Datasets:
Use the Patio Lawn and Garden review file (Patio_Lawn_and_Garden.json) and
metadata (meta_Patio_Lawn_and_Garden.json) from the Amazon product dataset
(https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/).
Download both files from the “Per-category files” section.
</pre>


