# gothic-site
A CRUD API about Gothic game.

I've created a REST API based on Flask web framework. Application is based on MVC (Model-View-Controller) pattern and also incorporates SQLAlchemy ORM with an Alembic database migration tool. It exposes /weapons, /armors, /npc endpoints which support GET, PATCH, POST, DELETE http methods to process CRUD requests (for example: adding a sword, updating an armor or deletion of an NPC). It can operate on data stored in SQL-based database of choice with database model created in SQLAlchemy ORM or JSON files.
