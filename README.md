# Home-Harmony-Final
## Deryn Brown - Capstone Project for Maryville University COCS498
### Application Description
Home Harmony...
### Components
#### Folders
- migrations:  Contains the sql file **step1:create_tables.sql** for creation of all tables and triggers associated with the database
- static:  Contains Javascript and CSS files
    -  images:  Contains images used by the application itself
    -  uploads:  Temporary storage for images uploaded by the user
- templates:  Contains all HTML files used by the application
#### Python Modules
- app.py:  Contains all endpoints used by the application; API for web and database
- database.py:  Contains all CRUD functions that interact with the database
- models.py:  Contains Pydantic models for retrieval, passing, and validation of data
#### Other Files
- requirements.txt:  Contains all dependencies for the application
- README.md:  Current file - contains information about and description of the applications
- .gitignore:  Used by GitHub - lists files that do not need source control
#### Database
- harmony.db:  SQLite database used by the application
##### Database Structure

| **Table** | **Primary Key** | **Foreign Key** | **Required** | **Field**          | **Type**     | **Description**                   |
|-----------|:---------------:|:---------------:|:------------:|--------------------|--------------|-----------------------------------|
| Users     |        X        |                 |       X      | user_id            | INTEGER      | Auto-generated                    |
| Users     |                 |                 |       X      | username           | TEXT         | User-supplied username            |
| Users     |                 |                 |       X      | salt               | TEXT         | Generated salt for authorization  |
| Users     |                 |                 |       X      | hash_password      | TEXT         | Hashed password                   |
| Rooms     |        X        |                 |       X      | room_id            | INTEGER      | Auto-generated                    |
| Rooms     |                 |                 |       X      | room_name          | VARCHAR(50)  | User-supplied room name           |
| Rooms     |                 |                 |              | room_desc          | VARCHAR(500  | User-supplied room desc           |
| Rooms     |                 |                 |              | room_num_walls     | INTEGER      | User-supplied number of walls     |
| Rooms     |                 |                 |              | room_wall_color1   | TEXT         | User-supplied wall color 1        |
| Rooms     |                 |                 |              | room_wall_color2   | TEXT         | User-supplied wall color 2        |
| Rooms     |                 |                 |              | room_ceiling_color | TEXT         | User-supplied ceiling color       |
| Rooms     |                 |                 |              | room_floor_color   | TEXT         | User-supplied floor color         |
| Rooms     |                 |                 |              | room_trim_color    | TEXT         | User-supplied trim color          |
| Rooms     |                 |                 |              | room_other_details | VARCHAR(500) | User- supplied other details      |
| Rooms     |                 |        X        |              | user_id            | INTEGER      | Foreign Key                       |
| Images    |        X        |                 |              | image_id           | INTEGER      | Auto-generated                    |
| Images    |                 |                 |       X      | image_name         | VARCHAR(50)  | User-supplied image name          |
| Images    |                 |                 |              | image_desc         | VARCHAR(500) | User-supplied image desc          |
| Images    |                 |                 |       X      | image_data         | BLOB         | Generated from uploaded file      |
| Images    |                 |                 |       X      | image_type         | TEXT         | Extracted from uploaded file name |
| Images    |                 |        X        |              | user_id            | INTEGER      | Foreign Key                       |
| Images    |                 |        X        |              | room_id            | INTEGER      | Foreign Key                       |
### Contact Information
    Deryn Brown

    Deryn.2017@gmail.com

## How to Run
1. Clone repository
2. Create harmony.db in top level folder
3. Run **step1.create_tables.sql** against **harmony.db** to create tables (or create database and tables in a tool such as DB Browswer for SQLite using above schema)
5. Create virtual environment `python -m venv .venv`
6. Activate virtual environment `.venv/Scripts/Activate on Windows`
7. Install dependencies `pip install fastapi[standard] PyJWT, passlib`
8. Run with command `fastapi dev app.py`
9. Navigate to `127.0.0.1:8000`
