Purpose is to provide a framework for giving analyst or any application end-user understandable and natural way of presenting the multidimensional data. One of the main features is the logical model, which serves as abstraction over physical data to provide end-user layer.

Features:

* OLAP and aggregated browsing (default backend is for relational databse - ROLAP)
* multidimensional analysis
* logical view of analysed data - how analysts look at data, how they think of data, not not how the data are physically implemented in the data stores
* hierarchical dimensions (attributes that have hierarchical dependencies, such as category-subcategory or country-region)
* localizable metadata and data
* SQL query generator for multidimensional aggregation queries
* OLAP server – HTTP server based on Flask Blueprint, can be easily integrated into your application.

# OLAP数据粘合剂

data_cubes


pip freeze requirements.txt
