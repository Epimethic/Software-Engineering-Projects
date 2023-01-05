# Example 1
import spacy
print("-" * 30 + "Example 1" + "-" * 30)
nlp = spacy.load('en_core_web_md') # change the en_core_web_md to en_core_web_sm to view how the information is different
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Example 2
print("-" * 30 + "Example 2" + "-" * 30)
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Example 3
print("-" * 30 + "Example 3" + "-" * 30)
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# I have noticed that having monkey and cat together are similar with over .5 rating
# Monkey and banana also have similarities with a score higher than .4
# With en_core_web_sm instead of en_core_web_md, the similarity increases for every output.