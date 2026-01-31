# TASK--3-CODTECH-MIGRATE-DATA-BETWEEN-TWO-DATABASES-E.G.-FROM-MYSQL-TO-POSTGRESQL-

Company: CODTECH IT SOLUTIONS

Name: Shaik Saniya Sulthan

Intern ID: CTIS3401

Domain: SQL

Duration: 4 Weeks

Mentor: Neela Santosh

*Project Description – Task 3: Database Migration Using Python and SQLite*

The primary objective of this internship task was to perform a database migration, which involves transferring data from one database (source) to another database (target) while maintaining data integrity. Database migration is an essential task in the field of software development and data management, as it ensures that applications or systems continue to function smoothly when data is moved between different environments or technologies. In this project, Python programming language, along with its built-in sqlite3 module, was used to create, migrate, and verify the data between two SQLite databases.

The project was divided into three main stages: creating the source database, migrating data to the target database, and verifying the data integrity after migration. Each stage was carefully planned and executed to ensure the success of the migration process.

Stage 1: Creating the Source Database
The first step involved creating a source SQLite database named source.db. This database served as the original repository of data that needed to be migrated. Within the source database, a table called users was created, consisting of two fields: id and name. The id field was of integer type and served as the unique identifier for each user, while the name field stored text values representing user names. Sample data was then inserted into the table to simulate real-world database content. This stage allowed for a working database setup that could be used to test the migration process and verify that data could be successfully copied to another database.

Stage 2: Migrating Data to the Target Database
After creating the source database, the next step was to migrate the data to a new target database named target.db. A Python script was developed to perform this task efficiently. The script established a connection to both the source and target databases using the sqlite3 module. It then created a table in the target database that matched the structure of the source table. All records from the users table in the source database were fetched and inserted into the corresponding table in the target database. This automated approach ensured that the migration was accurate, efficient, and repeatable. By using Python scripts for migration, the process became less prone to manual errors, faster, and easier to document.

Stage 3: Verifying Data Integrity
Ensuring data integrity was a critical part of this project. After migration, a separate Python script was created to verify that the data in the target database matched the source database exactly. The script compared the number of records in both databases, confirming that no rows were lost or altered during the migration process. This step is vital in real-world scenarios, as data loss or corruption during migration can have significant consequences for businesses or applications that rely on accurate data. The verification confirmed that the migration process was successful and that the data integrity was preserved.

Technologies and Tools Used
The project was implemented using Python 3, which provides the built-in sqlite3 module for interacting with SQLite databases. SQLite was chosen because it is lightweight, file-based, and does not require server setup, making it ideal for small-scale migration projects and learning exercises. The project was developed and tested on the Windows operating system, using the Command Prompt to run the Python scripts.

Outcome and Conclusion

The project was completed successfully, with the source database created, data migrated to the target database, and verification confirming that all data was accurately transferred. This task not only demonstrated practical skills in Python scripting and SQLite database management but also emphasized the importance of data integrity during migration. The project provides a foundation for handling more complex database migrations in future real-world scenarios, including migrations between different database systems like MySQL, PostgreSQL, or SQL Server.

Overall, this task enhanced understanding of database operations, scripting for automation, and the systematic approach required for accurate and reliable data migration. The project meets the requirements of CODTECH Task-3 and can be considered a successful demonstration of database migration skills.

*OUTPUT*:

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/a65b7476-d3c9-4f7c-bc19-19c5f3417c62" />
