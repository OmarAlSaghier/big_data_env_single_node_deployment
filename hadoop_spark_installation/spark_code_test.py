from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Trial app") \
    .config("spark.executor.memory", '4g') \
    .config('spark.executor.cores', '1') \
    .config('spark.cores.max', '1') \
    .config("spark.driver.memory",'4g') \
    .getOrCreate()


ordersDF = spark.read.csv("/Users/oalsaghier/Desktop/orders.csv", \
    header=True, \
    schema='''
        order_id INT, 
        order_date STRING, 
        order_customer_id INT, 
        order_status STRING'''
    )

ordersDF.show(10)

ordersDF.write. \
    mode('overwrite'). \
    option('compression', 'none'). \
    format('json'). \
    save('/Users/oalsaghier/Desktop/orders.json')
