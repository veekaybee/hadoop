#List of useful Hadoop commands across all components

 **Put a file into Hadoop:**

		hadoop fs -put foo.txt foo.txt

**Get root directory listing**
	
		hadoop fs -ls /

**hadoop fs -ls lists location of 
	/user/user/**

**Put file into local**

	hadoop fs -get /user/cloudera/file.txt file.txt

**Create a directory**

	hadoop fs -mkdir filename

**Remove folder and contents**

	hadoop fs -rm -r folder
	
**Look at file contents**

	hadoop fs -cat /user/cloudera/songs.csv
	
	hadoop fs -tail /path/to/file
	
	hadoop fs -cat /path/to/file | head
	
	
**make path in Hadoop**

	hadoop fs -mkdir -p hip1/input
	

**create test files in Hadoop**

	echo "cat sat mat" | hadoop fs -put - hip1/input/1.txt
	
#Hadoop Locations

**XML config files**

	/usr/lib/hadoop/etc/hadoop

=======
**$HADOOP_HOME** 
Deprecated command


#Spark

**Spark Location in Cloudera VM:**

	/usr/lib/spark
	
**Starting Spark**

	bin/pyspark
	
	
	spark-shell --master yarn-client


#Sqoop

**Importing from MySQL instance**

	sqoop import-all-tables 
	-m 1 
	--connect jdbc:mysql://quickstart:3306/retail_db --username=retail_dba 
	--password=cloudera 
	--compression-codec=snappy 
	--as-parquetfile 
	--warehouse-dir=/user/hive/warehouse 
	--hive-import

 

