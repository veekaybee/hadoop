<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [CCA -175 Tasks](#cca--175-tasks)
  - [Sqoop:](#sqoop)
    - [Basic Sqoop import with changing delimiter and file format](#basic-sqoop-import-with-changing-delimiter-and-file-format)
    - [changing Delimiters](#changing-delimiters)
    - [Append in incremental mode](#append-in-incremental-mode)
  - [Exporting data from Sqoop](#exporting-data-from-sqoop)
  - [Load data in and out of HDFS filesystem](#load-data-in-and-out-of-hdfs-filesystem)
  - [Flume](#flume)
  - [Spark](#spark)
    - [Spark-shell](#spark-shell)
      - [Load data from HDFS into Spark shell](#load-data-from-hdfs-into-spark-shell)
      - [Load data from HDFS into Spark shell](#load-data-from-hdfs-into-spark-shell-1)
    - [Export to HDFS or Local Filesystem](#export-to-hdfs-or-local-filesystem)
    - [Joining two datasets in Spark](#joining-two-datasets-in-spark)
    - [Average, Sum, Count in Spark](#average-sum-count-in-spark)
      - [Sum of](#sum-of)
      - [Average in Python](#average-in-python)
    - [Sort by Descending/Ascending](#sort-by-descendingascending)
  - [Avro](#avro)
    - [Creating a Partitioned Hive Table](#creating-a-partitioned-hive-table)
    - [Creating a Hive Table from an Avro File](#creating-a-hive-table-from-an-avro-file)
    - [Generating Avro Schema:](#generating-avro-schema)
    - [Evolving Avro Schema by Changing JSON Files](#evolving-avro-schema-by-changing-json-files)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# CCA -175 Tasks

List of tasks based on [CCA-175 exam page](http://www.cloudera.com/training/certification/cca-spark.html). Heavily biased towards documentation and the Cloudera practice VM. 


## Sqoop: 

[Sqoop Documentation](https://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html#_syntax)

### Basic Sqoop import with changing delimiter and file format 

	sqoop import 
	- m 1 \ #(parallelism/number of mappers)
	--connect jdbc:mysql://localhost/database \ 
	--username user \
	--password password \
	--table mysqltable \
	--as-avrofile \  #import as avrofile with schema
	--hive-dir /hive/warehouse/whatever \ 
	--target-dir /loudacre/webpage \  #straight to hdfs instead
	--fields-terminated-by "\t"
	--where "id > 400 \ select * from the table
	--query 'SELECT a.*, b.* FROM a JOIN b on (a.id == b.id) 	WHERE $CONDITIONS'\ #use instead of where clause and table statements

### changing Delimiters

 	--fields-terminated-by , 
 	--escaped-by \\ 
 	--enclosed-by '\"'

### Append in incremental mode

	sqoop import 
	--connect \
	- m 1 \ #(parallelism/number of mappers)
	--connect jdbc:mysql://localhost/database \ 
	--username user \
	--password password \
	--table mysqltable \
	--incremental append \
	--check-column columntoappend \
	--last-value last value to append


## Exporting data from Sqoop

	sqoop export 
	--connect jdbc:mysql://localhost/database \ 
	--username user \
	--password password \
	--table mysqltable \
	--export-dir /results/tabletoexport
	--input-lines-terminated-by "\n"

## Load data in and out of HDFS filesystem

[HDFS Command Documentation](https://hadoop.apache.org/docs/r1.2.1/file_system_shell.html)


`hdfs dfs` # filesystem commands

`hdfs dfs -ls` # examine filesystem directory (assumes user home folder)

`hdfs dfs -ls /` #examine top-level of file-system

`hdfs dfs -mkdir /directory` # creates new directory at top level

`hdfs dfs -rm -r /directory/folder` #recursively removes contents of folder (-skipTrash is an option..NOT recommended)

`hdfs dfs -put localfile /hdfsfolder` -puts a local file into an HDFS folder

`hdfs dfs -get /hdfsfolder localfile ` -HDFS file to local folder

`hdfs dfs -chmod /folder` #change file persmissions (see `man chmod` for available options)

`hdfs dfs -cat /dir/file.txt` #see file contents

`hdfs dfs -cat /dir/file.txt | tail -n 10` #see last ten lines of file

CopyFromLocal and CopyToLocal work if you're in the same local directory the file is located. 

## Flume

[Flume Manual](https://flume.apache.org/)


Basic Flume config file includes sources--> channels --> sinks for each agent. 
These are instructions given to MapReduce in Java about locations for each of these. Each part of the flume agent has different specifciations and options. 

	#### example.conf: A single-node Flume configuration

	#### Name the components on this agent
	a1.sources = r1
	a1.sinks = k1
	a1.channels = c1

	#### Describe/configure the source
	a1.sources.r1.type = netcat
	a1.sources.r1.bind = localhost
	a1.sources.r1.port = 44444

	#### Describe the sink
	a1.sinks.k1.type = logger

	#### Use a channel which buffers events in memory
	a1.channels.c1.type = memory
	a1.channels.c1.capacity = 1000
	a1.channels.c1.transactionCapacity = 10000

	#### Bind the source and sink to the channel
	a1.sources.r1.channels = c1
	a1.sinks.k1.channel = c1


This uses netcat and localhost instead of a spooldir. For more examples of flume conf files of different types, try a [GitHub search](https://github.com/search?utf8=%E2%9C%93&q=.type+%3D+spooldir&type=Code&ref=searchresults). 


## Spark


### Spark-shell

#### Load data from HDFS into Spark shell

Python:

Each file creates a partition. 

pyspark
file = sc.textFile("/hdfs/dir/files* ")

wholeTextFiles creates pairRDD with first value being the path
file = sc.wholeTextFiles("/hdfs/dir/files*")

Spark allows for the import of different kinds of data through RDDs. Mainly, people use it to access either HDFS directories or local files. the textFile method is prety flexible in both Python and Scala. It can read directories, textfiles, or groups of directories. It creates one partition in the assigned RDD for each file it reads in. 

#### Load data from HDFS into Spark shell

Python:

	pyspark
	file = sc.textFile("/hdfs/dir/files* ")
	file.getNumPartitions()
	
Other file types: 

	pyspark
	file = sc.textFile("/hdfs/dir/part-00000 ")
	file.getNumPartitions()
	
	pyspark
	file = sc.textFile("/hdfs/dir/myfile.txt ")
	file.getNumPartitions()


The vanilla install of Spark will default to reading files from your local directory; if you have Hadoop configured, you have to specify that the file is local. 
	
	pyspark
	file = sc.textFile("localdirectory://file ")
	file.getNumPartitions()
	
And:

sc.textFile("/my/dir1,/my/paths/part-00[0-5]*,/another/dir,/a/specific/file")
	
Scala

	spark-shell
	val file = sc.textFile("/hdfs/dir/files* ")
	file.getNumPartitions()

All of these are great for data that is delimited by lines. For XML, and data delimited by |, or other characters, you can also read in with a method called wholeTextFiles that creates pairRDD with first value being the path and the second being all of the contents of the file. 

	file = sc.wholeTextFiles("/hdfs/dir/files*")


Here's the difference: 	

	In [1]: logs = sc.textFile("/logdata/access_log_20160329-153657.log")
	In [2]: logs.first()
	Out[2]: u'244.157.45.12 - - [10/Oct/2013:00:04:23 ] "GET /wheelsets HTTP/1.0" 200 4677 "http://bleater.com" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36"'
	In [5]: logs.getNumPartitions()
	Out[5]: 1



	In [6]: logs = sc.wholeTextFiles("/logdata/access_log_20160329-153657.log")

	In [7]: logs.first()
	Out[7]: 
	(u'hdfs://localhost:8020/logdata/access_log_20160329-153657.log',u'244.157.45.12 - - [10/Oct/2013:00:04:23 ] "GET /wheelsets 	HTTP/1.0" 200 4677 "http://bleater.com" "Mozilla/5.0 	(Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 	(KHTML, like Gecko) Chrome/36.0.1944.0 Safari/	537.36"\n123.221.14.56 - -
 	In [8]: logs.getNumPartitions()
	Out[8]: 1

To work with the second one, you'll need to flatten it: 

	In [11]: values = logs.map(lambda (fname,data): data)
	
	In [12]: values.first()
	Out[12]: u'244.157.45.12 - - [10/Oct/2013:00:04:23 ] "GET /wheelsets HTTP/1.0" 200 4677 "http://bleater.com" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36"\n123.221.1


### Export to HDFS or Local Filesystem

	values.saveAsTextFile("/weblogs/mapspark.txt")
	
###  Joining two datasets in Spark

	dataset1.join(dataset2) # need to have the same key	
	
### Average, Sum, Count in Spark 

#### Sum in Scala: 

**Simple arrays: **
 val data = Array(1, 2, 3, 4, 5)
 data.reduce((k,v) => k+v)

**Tuples: **

More about [Scala Tuples](http://www.tutorialspoint.com/scala/scala_tuples.htm). 

	val data = sc.parallelize(Array((1,2),(2,4),(1,3),(3,5)))

#### Sum (MapReduce in Scala)

	data.map(line => line.split(' ')).map(item => (item(0), 1)).reduceByKey((v1,v2)=> v1+v2).take(5)
	val data = sc.textFile("logs/access_log_20160329-153657.log")


####Average in Scala

	val data = sc.parallelize(Seq(("A", 2), ("A", 4), ("B", 2), ("Z", 0), ("B", 10)))
	val counts = data.map(tuple => (tuple._1,1)).reduceByKey((v1,v2) => (v1+v2))
	val sum = data.reduceByKey((v1,v2)=>(v1+v2))

#### Average in Python
	data = sc.parallelize( [(0, 2.), (0, 4.), (1, 0.), (1, 10.), (1, 20.)] )
	counts = data.map(lambda (k,v): (k,1)).reduceByKey(lambda v1,v2: v1+v2)
	sums = data.reduceByKey(lambda v1,v2: v1+v2)
	sums.join(counts).map(lambda (k,v): (k,(v[0]/v[1]))).collect()
	val total = counts.join(sum).map(t  => (t._1,t._2._2/t._2._1)).collect()


### Sort by Descending/Ascending

sums.join(counts).map(lambda (k,v): (k,(v[0]/v[1]))).sortByKey(ascending=False).collect()


## Avro 

### Creating a Partitioned Hive Table

CREATE EXTERNAL TABLE schema.webpage
   (page_id SMALLINT,
	name STRING,
    assoc_files STRING)
   PARTITIONED BY (areacode STRING)
   ROW FORMAT DELIMITED
   FIELDS TERMINATED BY '\t'
   LOCATION '/hdfsdir'

### Creating a Hive Table from an Avro File

CREATE EXTERNAL TABLE schema.webpage
STORED AS AVROTBLPROPERTIES 
LOCATION '/loudacre/webpage'
(TBLPROPERTIES ('avro.schema.url'=
'hdfs:/dir/sqoop_import_accounts.avsc');


### Generating Avro Schema:


1) Import a file via Sqoop as Avro: 

	sqoop import \
 	 --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  	--username=retail_dba \
  	--password=cloudera \
  	--table departments \
 	 --as-avrodatafile \
 	 --target-dir=/user/cloudera/departments
 	 
2) Export that file to a local directory or work with it in HDFS

`hdfs dfs -get /user/hive/warehouse/retail_stage.db/departments .`


3) **avro-tools getschema filename**


	avro-tools getschema part-m-00000.avro 
	log4j:WARN No appenders could be found for logger 	(org.apache.hadoop.metrics2.lib.MutableMetricsFactory).
	log4j:WARN Please initialize the log4j system properly.
	log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
	{
 	 "type" : "record",
 	 "name" : "departments",
 	 "doc" : "Sqoop import of departments",
 	 "fields" : [ {
    "name" : "department_id",
    "type" : [ "null", "int" ],
    "default" : null,
    "columnName" : "department_id",
    "sqlType" : "4"
 	 }, {
   	 "name" : "department_name",
    	"type" : [ "null", "string" ],
    	"default" : null,
   	 "columnName" : "department_name",
    	"sqlType" : "12"
  	} ],
  	"tableName" : "departments"
	}


### Evolving Avro Schema by Changing JSON Files

CREATE EXTERNAL TABLE orders
STORED AS AVRO
LOCATION 'hdfs:///user/hive/warehouse/retail_stage.db/orders'
tblproperties('avro.schema.url'='hdfs:///user/cloudera/retail_stage/orders.avsc')


Go into the .avsc file, make changes and add a column: 


	{
 	 "type" : "record",
 	 "name" : "departments",
 	 "doc" : "Sqoop import of departments",
 	 "fields" : [ {
    "name" : "department_id",
    "type" : [ "null", "int" ],
    "default" : null,
    "columnName" : "department_id",
    "sqlType" : "4"
 	 }, {
    "name" : "department_manager_name",
    "type" : [ "int"],
    "default" : null,
    "columnName" : "department_id",
    "sqlType" : "4"
 	 },{
   	 "name" : "department_name",
    	"type" : [ "null", "string" ],
    	"default" : null,
   	 "columnName" : "department_name",
    	"sqlType" : "12"
  	} ],
  	"tableName" : "departments"
	}

2) Put the file hdfs dfs -put -f file.avsc /hdfs/location
3) Cat the file to validate
	



