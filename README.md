# Election_Analysis
##**Project Overview**

*A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local election for a congressional seat.*
  1. Calculate the total number of votes cast.
  2. Get a complete list of cnadidates who received votes. 
  3. Calculate the total number of votes received by each candidate
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on the popular vote. 
  6. Determine which county had the highest voter turnout 
  7. Determine the voter turnout for each county and what percentage of votes cast that county represents

##**Resources**

  -Data Source: election_results.csv
  
  -Software: Python 3.7.10, Visual Studio Code version 1.62
  
##**Summary** 

*The Analysis of the election shows that:*

  - There were 369,711 total votes cast in the election
  
  - There were three candidates in the election that received votes.
  
  - In this election Charles Casper Stockham received 85,213 votes, which totalled 23% of the votes cast. 
  
  - Diana DeGette received 272,892 votes and 73.8% of the votes cast in the election.
  
  - Raymon Anthony Doane received 11,606 votes in the election, and 3.1% of the votes cast.
  
  - Based on the popular vote numbers in the election Diana DeGette won the election with 73.8% of votes cast at a total of 272,892         votes received. 
 
 - In this election the county voter turnouts were as follows: Jefferson County 38,855 votes (10.5% of votes cast), Denver County 306,055 votes (82.8% of votes cast). and Arapahoe County 24,801 votes (6.7% of votes cast).
 
 -Based on these election numbers the county with the largest voter turnout was Denver county with 306,055 votes.
 
 ##**Recommendation to Election Committee**
 
  This software's framework is very simple to adapt to more elections in the future. By simply changing the file path to load (line #9 in the code) we can use this code framework to read and analyze additional election results, so long as the file we are analyzing is in CSV format. 
  
Additionally if the election committee was inclined to find out which candidates performed best in each county we could do so by setting our code to iterate through each county and popluate every instance in which a candidate's name appears on the vote count.   



