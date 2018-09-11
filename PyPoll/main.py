import csv
import os

count = 0
winner_votes = 0
votes = [0,0,0,0]
candidates = []
path = 'election_data.csv'

with open(path, 'r', newline='', encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        count = count + 1
        if row[2] not in candidates:
            candidates.append(row[2])

        candidate_index = candidates.index(row[2])
        votes[candidate_index] += 1

    for i in votes:
        cand1 = votes[0]
        cand2 = votes[1]
        cand3 = votes[2]
        cand4 = votes[3]

    file = open('Output.txt', 'w')
    file.write('Total Votes: ' + str(count) + "\n")
    print(f'Total Votes: {count}')
    for i in range(len(candidates)):
        print(str(candidates[i] + ' %' + '{0:.2f}'.format((votes[i]/count) *100) + ' ' + str(votes[i])))
        if votes[i] > winner_votes:
            winner_votes = votes[i]
            winner = candidates[i]
        file.write(str(candidates[i] + ' %' + '{0:.2f}'.format((votes[i]/count) *100) + ' ' + str(votes[i]) + '\n'))
    print(f'Winner: {winner}')
    file.write('Winner: ' + str(winner))
