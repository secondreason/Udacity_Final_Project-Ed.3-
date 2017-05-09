# Udacity_Final_Project-Ed.3-

Description

This is a the Tournamnet Project, i've created  as a Final Project of The relational
databases course.It shows how is working Swiss tournament system. The main idea of this system is 
that each competitor (team or individual) does not play every other.Competitors meet one-to-one in 
each round and are paired using a set of rules designed to ensure that each competitor plays opponents 
with a similar running score, but not the same opponent more than once.The winner is the competitor 
with the highest aggregate points earned in all rounds

In the tournament.py file, there are functions necessary to run the tournament such as :
1)connect() - Connect to PostgreSQL database.

2)commit_st(func) - special function created to make coding simple.

3)deleteMatches(cursor) - delete all the match records.

4)deletePlayers(cursor)- remove all player records.

5)countPlayers(cursor) - returns a number of players currently registered.

6)registerPlayer(cursor, name) - Adds a player to the tournament database.

7)playerStandings(cursor) - Returns a list of the players and their win records, sorted by wins.

8)reportMatch(cursor, winner, loser) -Records the outcome of a single match between two players.

9)swissPairings() - Returns a list of pairs of players for the next round of a match.

In the tournament.sql file there are tables, schemas and some views already defined.

File tournament_test.py was made to check if our database and tournament.py file really works.

How to Run:

For running this porject first, you should have Vagrant and VirtualBox.
If you dont, please install it.

1.Clone [repository this with all files] (https://github.com/secondreason/Udacity_Final_Project-Ed.3-).

2.From your terminal, navigate to repository you just cloned.

3.Enter the vagrant directory using `cd vagrant`.

4.Start virtual machine by typing `vagrant up`.

5.Once the virtual machine has finishing booting up, log in to the machine using `vagrant ssh`.

6.When you are in the vm go to ../../vagrant/.

7.Before running tests you should create database using

⋅⋅*`CREATE DATABASE tournament` Create database.
⋅⋅* `\C tournament` Connect to database tournament.
⋅⋅*`\I tournament.sql` Creating all tables and views from file.

5.To run test type python tournament_test.py.

Have fun.
