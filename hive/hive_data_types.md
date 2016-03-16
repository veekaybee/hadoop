# Hive Commands

### Create table with multiple complex data structures 

Given this header format: 

	Name|Location1,Location2...Location5|Sex­,Age|Father_Name:Number_of_Child

create a table DDL: 

	CREATE TABLE FamilyHead (
	Name INT,
	locations, ARRAY<string>
	Sex_Age, STRUCT<sex:string, age:int>,
	fathername_NuofChild MAP<string,int>
	unixtime STRING)
	ROW FORMAT DELIMITED
	FIELDS TERMINATED BY '|'
	COLLECTION ITEMS TERMINATED BY ','
	MAP KEYS TERMINATED BY ;
	

[For more on complex Hive types](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types) 


	**arrays:** ARRAY<data_type> (Note: negative values and non-constant expressions are allowed as of Hive 0.14.)

	**maps:** MAP<primitive_type, data_type> (Note: negative values and non-constant expressions are allowed as of Hive 0.14.)

	**structs:** STRUCT<col_name : data_type [COMMENT col_comment], ...>

	**union: **UNIONTYPE<data_type, data_type, ...> (Note: Only available starting with Hive 0.7.0.)