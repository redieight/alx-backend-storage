0x01. NoSQL
=

NoSQL databases do not rely on these structures and use more flexible data models. NoSQL can mean “not SQL” or “not only SQL.” As RDBMS have increasingly failed to meet the performance, scalability, and flexibility needs that next-generation, data-intensive applications require, NoSQL databases have been adopted by mainstream enterprises. NoSQL is particularly useful for storing unstructured data, which is growing far more rapidly than structured data and does not fit the relational schemas of RDBMS.

TYPES OF NOSQL DATABASES
=

* <h2>Key-value data stores</h2>

 Key-value NoSQL databases emphasize simplicity and are very useful in accelerating an application to support high-speed read and write processing of non-transactional data. Stored values can be any type of binary object (text, video, JSON document, etc.) and are accessed via a key.

* <h2>Document stores</h2>

Document databases typically store self-describing JSON, XML, and BSON documents. They are similar to key-value stores, but in this case, a value is a single document that stores all data related to a specific key.

* <h2>Wide-column stores</h2>

Wide-column NoSQL databases store data in tables with rows and columns similar to RDBMS, but names and formats of columns can vary from row to row across the table. Wide-column databases group columns of related data together.

* <h2>Graph stores</h2>

A graph database uses graph structures to store, map, and query relationships. They provide index-free adjacency, so that adjacent elements are linked together without using an index.


Managing NoSQL Databases With MongoDB
=

MongoDB is a document-oriented database classified as NoSQL. It’s become popular throughout the industry in recent years and integrates extremely well with Python. Unlike traditional SQL RDBMSs, MongoDB uses collections of documents instead of tables of rows to organize and store data.

MongoDB stores data in schemaless and flexible JSON-like documents. Here, schemaless means that you can have documents with a different set of fields in the same collection, without the need for satisfying a rigid table schema.

