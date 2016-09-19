Tournament Results
=======================================================

Udacity's Full Stack Web Developer Nanodegree Program Project

## Overview

This project is connected to the Intro to Relational Databases course of Udacity's Full Stack Web Developer Nanodegree. This project includes a database schema (SQL table definitions) that stores data of players, matches; and a Python module for adding players, reporting matches, ranking players, and pairing registered players. 

This project will run a simple Swiss system tournament: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

## Requirements
In order to run this project, you must have Python and PostgreSQL installed and configured, as well as the psql command line interface (CLI).

### Download Python: https://www.python.org/
### Use Vagrant Virtual Machine to install and configure PostgreSQL:
The Vagrant VM has PostgreSQL installed and configured, as well as the psql command line interface (CLI), so that you don't have to install or configure them on your local machine. (Provided by Udacity at https://github.com/udacity/fullstack-nanodegree-vm)
To use the Vagrant virtual machine, navigate to the full-stack-nanodegree-vm/tournament directory in the terminal, then use the command vagrant up (powers on the virtual machine) followed by vagrant ssh (logs into the virtual machine).  
Remember, once you have executed the vagrant ssh command, you will want to cd /vagrant to change directory to the synced folders in order to work on your project, once your cd /vagrant, if you type ls on the command line, you'll see your tournament folder.
The Vagrant VM provided in the fullstack repo already has PostgreSQL server installed, as well as the psql command line interface (CLI), so you'll need to have your VM on and be logged into it to run your database configuration file (tournament.sql), and test your Python file with tournament_test.py.

## Installation

### 1. Setting up database

After downloading this code to your machine, type the following command in your terminal from the project directory in order to set up the database schema:

```
psql
\i tournament.sql
```

### 2. Run unit tests

The project provides set of tests to make sure everything is working properly. In order to run the tests:

```
python tournament_test.py
```
Expected results on command line interface:

```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
[(70, 'Bruno Walton', 0L, 0L), (71, "Boots O'Neal", 0L, 0L), (72, 'Cathy Burton', 0L, 0L), (73, 'Diane Grant', 0L, 0L)]
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

## References
1. Udacity's Tournament Results Project Getting Started Guide:
	https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
2. PostgreSQL 9.3.14 Documentation:
	https://www.postgresql.org/docs/9.3/static/
3. http://stackoverflow.com/questions/31484776 cant-display-matches-won-matches-played-and-matches-drawed-by-each-player
4. http://stackoverflow.com/questions/37248659/psycopg2-psql-select-statement-returning-0l-instead-of-0
5. http://stackoverflow.com/questions/888731/two-sql-count-queries
