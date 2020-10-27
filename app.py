print("Title of program: Helpful Bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day, for now just laze around and eat :D")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling and look at the brighter side of life!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think, remember that there are other people who you can talk to")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("Please don't. Close your eyes and count to ten. You might feel better. Tell a friend or family member if you do not and explain the situation.")
      counter += 1
    if each_word == "disgusted":
      feelings_list.append("disgusted")
      encouragement_list.append("Do not think about the trigger item/event. Think about other things and look at things you like to bleach your brain.")
      counter += 1
    if each_word == "scared":
      feelings_list.append("scared")
      encouragement_list.append("Don't think about what you are scared of. Think about other things or do things you love.")
      counter += 1
    if each_word == "lonely":
      feelings_list.append("lonely")
      encouragement_list.append("You have me. It is ok. Everything is alright. If you need help, you can contact my creator at his profile and tell him your problems on the repository called PROBLEMS FROM HELPFUL BOT USERS.")
      counter += 1
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("Me too! I'm so happy for you! Have fun!")
      counter += 1
    if each_word == "nervous":
      feelings_list.append("nervous")
      encouragement_list.append("Relax. There will be a good outcome!")
      counter += 1
    if each_word == "self-conscious":
      feelings_list.append("self-conscious")
      encouragement_list.append("you are amazing in your own way, do not let what other people think of you pull you down")
      counter += 1      
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("you should call your family or friends, tell them how much they mean to you")
      counter += 1     
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("see a doctor. Talk to your family or freinds, even if your friends are imaginary. Just try to think of the stuff that makes you happy")
      counter += 1  
    if each_word == "lazy":
      feelings_list.append("lazy")
      counter += 1
      encouragement_list.append("Sleep.")
    if each_word == "irritated":
      feelings_list.append("irritated")
      encouragement_list.append("talk about it to the person you are having problems with, don't jump to conclusions")
      counter += 1 
    if each_word == "stressed":
      feelings_list.append("stessed")
      encouragement_list.append("Don't worry too much. Talk to your parents or friends if you need help")
      counter += 1 
    if each_word == "hurt":
      feelings_list.append("hurt")
      encouragement_list.append("I can't imagine what you're going through. I'll be there for you")
      counter += 1    
    if each_word == "pleased":
      feelings_list.append("pleased")
      encouragement_list.append("Good job! Continue to stay positive :D")
      counter += 1 
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()

