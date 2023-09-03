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

</pre>

