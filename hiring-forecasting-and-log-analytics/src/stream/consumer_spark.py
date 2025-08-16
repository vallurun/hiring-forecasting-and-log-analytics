from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col, count
from src.common.config import STREAM_DIR

spark = SparkSession.builder.appName("log_consumer").getOrCreate()

# Use file-based streaming as a local stand-in for Kinesis
stream = (spark.readStream
          .format("json")
          .schema("ts STRING, candidate_id STRING, event STRING, req_id STRING")
          .option("maxFilesPerTrigger", 1)
          .load(STREAM_DIR))

agg = (stream
       .withColumn("ts", col("ts").cast("timestamp"))
       .groupBy(window(col("ts"), "1 minute"), col("event"))
       .agg(count("*").alias("cnt")))

query = (agg.writeStream
         .format("console")
         .outputMode("complete")
         .start())

query.awaitTermination()
