# w4111-proj-WorldCup-DB -- Team 25: Jiahao Lai, Tangwen Zhu
##  PostgreSQ account
jl6274
## URL of web application
http://35.185.84.232:8111/
## Features in Part 1 proposal that we implemented
1. User can navigate to **Teams** tab and input the country name to look up the national team match records and team makeup. In addition, we also added information regarding the coach.
2. User can naviagte to **Players** tab, under which we have implemented several features:<br>
* Player look-up -- user can type in the full name or part of the name of a player to check information such as DOB, Club, Height, etc. 
In addition, all match records and related events of this player will also be shown. <br> However, please notice that player names that contain accent in different languages 
such as Spanish and French will render garbled letters (Mojibake)--eg. "Kylian Mbappé" will be shown as "Kylian Mbapp√©". The player's jersey number data is not completely 
accurate due to outdated datasource. Lastly, "match records and related events" section doesn't include player assist reading due to lack of data.
* Player data insertion -- user can insert new player data to the database. For now, user can specify 
**Name of new player you want to add**, **Postion**, **Club**, **Height** and **Weight**. <br>
Please notice that When adding a player, the player's team attribute is not set because we have a constraint on the size of the team when designing the database.
* Player VS feature -- user can type in two players' names (we encourage using full name for 
more accurate searching) to compare their basic information as well as performance throughout the entire Worldcup 
2022, which consists of **Player Name**, **Position**，**National Team**, **Club Team**, **Goals**, **Own Goals**,
**Disallowed Goals**, **Penalty**, **Missed Penalty**, **Yellow Card** and **Red Card**.
## Features not in Part 1 proposal that we implemented
1. User can navigate to **Referees** tab to check referees who participated in Worldcup 2022.
2. User can navigate to **Scoreboard** tab to check score/ranking information of the group stage seperated from group A to group 
H, though we did not show the knockout stage information.

## Features in Part 1 proposal that we didn't implement
1.Match data insertion.
2.Detailed comparison of players' specific skills such like tackling, dribbing, etc.

## Two of the web pages that require the most interesting database operations
1. **Players** tab: this web page features 8 input text, all serving their unique SELECT and INSERT query. For example, input under the section titled 
**Players Performance Comparison** are passed in as parameter for SQL search for a specified pattern, which accompanied by SELECT() and COUNT() function altoghter enable
player performance data retrieval and summary.
2. **Teams** tab：
