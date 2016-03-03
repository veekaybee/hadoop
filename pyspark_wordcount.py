

"""
Simple Spark stand-alone app with pyspark on Cloudera quickstart vm
To run through CLI: ./bin/spark-submit SimpleApp.py
Uses Gutenberg Alice in Wonderland Text UTF-8 
http://www.gutenberg.org/cache/epub/11/pg11.txt
Set log4j.rootCatetory=WARN, console in log4j.properties to WARN or you're going to have a bad time
"""

from pyspark import SparkContext 

#exclude some basic stopwords
def notStopword(wordCounts): 
	if wordCounts[0] in ["a","the","and"]:
		pass
	else:
     		return wordCounts

#Build SparkContext and FlatMap/Reduce words split by whitespace, exclude punctuation
sc= SparkContext()
alice = sc.textFile("hdfs://quickstart.cloudera:8020/user/cloudera/alice/alice.txt")
wordCounts = alice.map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower()).flatMap(lambda x: x.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b) 
filteredWords = wordCounts.filter(notStopword)
filteredWordsTop = filteredWords.takeOrdered(100, key=lambda x: -x[1])


#output to CLI
for (word, count) in filteredWordsTop:
	print("%s: %i" % (word, count))
