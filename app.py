import json
import sys
# Import SparkSession
from pyspark import SparkContext, SparkConf

'''
Student Name: Liu Jiage
Assignments: Lab 1
Submit Date: 01/09/2023
'''

'''
Spark RDD 1 Mapping Patio_Lawn_and_Garden 
'''
def rdd1_map_func(j):
    data = json.loads(j)
    tuple_data = (data['asin'] + ":" + data['reviewTime'], (1, data['overall'], data['reviewTime'], data['asin']))
    return tuple_data

'''
Spark RDD 2 Mapping meta_Patio_Lawn_and_Garden
'''
def rdd2_map_func(j):
    data = json.loads(j)
    tuple_data = (data['asin'], data['brand'])
    return tuple_data

'''
Submit this python spark job to Spark standalone
Spark-submit --master spark://172.20.10.5:7077 --driver-memory 8g 
             --executor-memory 8g --py-files app.zip app.py 
             Patio_Lawn_and_Garden.json meta_Patio_Lawn_and_Garden.json 
             ./output/
'''
if __name__ == "__main__":
    # 1.Config Spark Context
    conf = SparkConf()
    conf.set("spark.speculation", "false")
    spark = SparkContext(conf=conf)
    # 2.Read file from application parameter one, Patio_Lawn_and_Garden.json
    rdd1_json_file = spark.textFile(sys.argv[1])
    '''
    3.Handle data for RDS 1(
       3.1 map data value for (reduce and sort data)
       3.2 reduce by key(key = product id + review time)
       3.3 sort data by num of reviews, and pack top 15 records 
       3.4 map data value for (join RDD 2 and print the final result)
    '''
    rdd1_result = spark.parallelize(
        rdd1_json_file.map(rdd1_map_func).
        reduceByKey(lambda i, j: (i[0] + j[0], i[1] + j[1], i[2], i[3]), 10). \
        sortBy(lambda i: i[1][0], False, 10).take(15), 10). \
        map(lambda i: (i[1][3], (i[1][0], i[1][2], i[1][1] / i[1][0])))
    # 4.Read file from application parameter two, meta_Patio_Lawn_and_Garden.json
    rdd2_json_file = spark.textFile(sys.argv[2])
    # 5.Handle data for RDD 2 (mapping RDD2 data)
    rdd2_result = rdd2_json_file.map(rdd2_map_func)
    '''
    6. Joining RDD 1 and RDD 2 
    Mapping Spark RDD data to <product ID > <num of reviews> <review time> <avg ratings> <product brand name> 
    '''
    result = rdd1_result.join(rdd2_result). \
        map(lambda i: (i[0], i[1][0][0], i[1][0][1], i[1][0][2], i[1][1])). \
        sortBy(lambda i: i[1], False, 10)
    # 7.Merge all partitions data together, generate only one result
    result.coalesce(1).saveAsTextFile(sys.argv[3])
    spark.stop()
