# Sqoop Sample Workflows: 

## Import single table
    sqoop import \
    -m1 \
    jdbc:mysql://vm:port/db_name \
    	--username= \
    	 --password= \
    	 --table customers \
    	--hive-import \
    	--warehouse-dir=/user/hive/warehouse 

## Import all tables

    sqoop import-all-tables \
        -m 1 \
        --connect jdbc:mysql://vm:port/db_name  \
        --username= \
        --password=\
        --compression-codec=snappy \
        --as-parquetfile \
        --warehouse-dir=/user/hive/warehouse \
        --hive-import
