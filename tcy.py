# Importing necessary packages
import spacy
nlp = spacy.load("en_core_web_md")

# Loading all the text file
text = open("text.txt").read()
org_text = nlp(text)
ans1 = open("ans1.txt").read()
ans1_text = nlp(ans1)
ans2 = open("ans2.txt").read()
ans2_text = nlp(ans2)
ans3 = open("ans3.txt").read()
ans3_text = nlp(ans3)

# Printing the text from all the files
print("The original text is:", org_text)
print()

print("The ideal answer1 is:", ans1_text)
print()

print("The ideal answer2 is:", ans2_text)
print()

print("The ideal answer3 is:", ans3_text)
print()

# Comparing the similarity of the original text file and answer file.
print("The percentage similarity to original text is:",
      round((org_text.similarity(ans1_text))*100, 2), "%")
print()

print("The percentage similarity to original text is:",
      round((org_text.similarity(ans2_text))*100, 2), "%")
print()

print("The percentage similarity to original text is:",
      round((org_text.similarity(ans3_text))*100, 2), "%")
