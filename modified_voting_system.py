# Voting System with Enhanced String Manipulation

# first we will take input of what nominee what we want to keep
nominee1 = input("Enter the name of the 1st nominee: ").strip()  # Remove leading/trailing spaces
nominee2 = input("Enter the name of the 2nd nominee: ").strip()  # Remove leading/trailing spaces

# initially vote count for both must be 0
nm1_votes = 0
nm2_votes = 0

voter_id = list(range(1, 11))  # Simplified voter ID generation
no_of_voter = len(voter_id)

while True:
    if voter_id == []: #to check when voter list is completed
        print("Voting session is over !!!")
        if nm1_votes> nm2_votes:
            percent = (nm1_votes/no_of_voter)*100 #to calculate the percentage
            print(nominee1,"has won the election with",percent,"% of votes")
            break # to get rid of infinite loop
        elif nm2_votes> nm1_votes:
            percent = (nm2_votes/no_of_voter)*100 #to calculate the percentage
            print(nominee2,"has won the election with",percent,"% of votes")
            break # to get rid of infinite loop
        else:
            print("Both have equal number of votes !!! Government will decide who will rule")
            break
        

    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter) # we will remove so that agin same voter can't vote
        print("-------------------------------------")
        print("To give vote to", nominee1,"Press 1  ")
        print("To give vote to", nominee2,"Press 2  ")
        print("-------------------------------------")
        vote = int(input("Enter you precious vote : "))
        if vote == 1:
            nm1_votes +=1
            print(nominee1,"Thank you to give your important vote to them !!")
        elif vote == 2:
            nm2_votes +=1
            print(nominee2,"Thank you to give your important vote to them !!")
        elif vote > 2:
            print("Check your pressed key !!")
        else:
            print("You are not a voter OR You have already voted")


