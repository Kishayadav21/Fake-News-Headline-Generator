# 1 - Import the random line
import random 

# 2 - Create Subjects
subjects = [
  "Shahrukh Khan",
  "Virat Kohli",
  "Pratyush Mishra",
  "A group of Monkeys",
  "Prime Minister Modi",
  "Auto rickshaw driver from Delhi",
  "Nirmala Sitharaman",
  "Harishchandra",
]

actions = [
  "orders",
  "launches",
  "cancels",
  "dances with",
  "eats",
  "cancel",
  "launches",
  "celebrates",
]


place_or_thing = [
  "at beach",
  "inside the water tank",
  "in Jalianvalabagh",
  "at Red fort",
  "at Mahakumbh",
  "dry fruits are healthiest food",
  "a plate of samosa",
  "in Mumbai local train",
  "during IPL match",
]

# start the generation line loop
while True:
  subject = random.choice(subjects)
  action = random.choice(actions)
  
  place = random.choice(place_or_thing) 

  headline = f"BREAKING NEWS: {subject} {action} {place}"
  print("\n" + headline)

  user_input = input("\nDO you want another headline? (yes/no)").strip().lower()
  if user_input == "no":
   break 

#print goodbye message 
print("\nThanks for using the Fake news Headline Generator. Have a fun day")