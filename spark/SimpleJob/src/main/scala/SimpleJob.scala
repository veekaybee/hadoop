import org.apache.spark._
import org.apache.spark.SparkContext._

object SimpleApp {
	def main(args: Array[String]) {
	val conf = new SparkConf().setAppName("wordCount") // create SparkContext in Scala  
	val sc = new SparkContext(conf)
	val alice = sc.textFile("hdfs://quickstart.cloudera:8020/user/cloudera/alice/alice.txt") // Simple WordCount   
	val filtered = alice.map(x => x.replace(',',' ').replace('.',' ').replace('-',' ')).flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)
	val counted = filtered.collect().foreach(println)
	}
}