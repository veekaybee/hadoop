package name

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object CountIPs {
   def main(args: Array[String]) {
     if (args.length < 1) {
       System.err.println("Usage: CountIPs <file>")
       System.exit(1)
     }
    //Parse log files from HDFS to get IP, count of IPs
	var logs = sc.textFile("/logdata/access_log_20160329-153657.log")
	var iplines = logs.map(lines => (lines.split(' ')(0),1)).reduceByKey((a, b) => a + b)

	//print out to console
	for (pair <- iplines.take(10)) {
   printf("IP: %s, Count: %s\n",pair._1,pair._2)
}



	sc.stop
	}
  }	
