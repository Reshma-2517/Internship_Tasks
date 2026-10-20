# Problem 2: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
rooms = list(map(int, input().split()))

# every family room number appears k times, the captain's room appears once.
# sum(set) * k counts the captain's room k times, so the extra (k - 1) copies
# are exactly the difference from the real total.
unique_rooms = set(rooms)
captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

print(captain_room)
