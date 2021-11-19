#The data re want to retrieve
#assign a variable for the file to load and path
import csv
import os
#assign a variable to load a file from a path
file_to_load= os.path.join("resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize total_votes and set to zero
total_votes= 0
#initialize candidate options
candidate_options= []
#inititalize votes for each candidate
candidate_votes= {}
#winning candidate and winning count tracker
winning_candidate= ""
winning_count= 0
winning_percentage= 0




# Open the election results and read the file.
with open(file_to_load) as election_data:

    #read the file object with the reader function
    file_reader= csv.reader(election_data)
   
    #print each row in the CSV reader
    headers= next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #total number of votes cast
        total_votes+=1

        #complete list of candidates who received votes
        candidate_name= row[2]

        #if cndidate is not on list
        if candidate_name not in candidate_options:
            #add the candidate name toi the lsit
            candidate_options.append(candidate_name)

            #track candidates vote count
            candidate_votes[candidate_name]= 0
        #add a vote to candidate's count
        candidate_votes[candidate_name]+=1

    #percentage of votes won by each candidate
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrrieve the vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes 
        vote_percentage= float(votes) / float(total_votes) *100
        #print out candidate percentage and candidate name
        print(f"{candidate_name} received {vote_percentage: .2f} % of the total vote.")
        #determine the winning vote count and candidate
         #to do: print out winning candidate, vote count and percentage to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count= winning_percentage and votes= voting_percentage
            winning_count= votes
            winning_percentage= vote_percentage
            #set winning_candidate equal to candidates name
            winning_candidate= candidate_name
        winning_candidate_summary = (
            f"----\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----\n")
        print(winning_candidate_summary)
        
   


