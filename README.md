# spark-toprank
Spark Lab uses Python to run Spark job on Spark standalone, the task to calculate the top rank of review goods,  the goods data are downloaded from AWS. 
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
Note: Below photo is a hight level design, that is not include (reduceByKey, SortBy, and Map implement detail). 

</pre>
![image](https://github.com/liujiage/spark-toprank/assets/183577/8747a803-1ea1-4ad4-a0d4-a664ba8b8f62)

