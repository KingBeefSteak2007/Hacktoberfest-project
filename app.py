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
      encouragement_list.append("tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
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
      feelings_list.append("scarted")
      encouragement_list.append("Don't think about what you are scared of. Think about other things or do things you love.")
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

