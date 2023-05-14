# import openai
#
# my_key = "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"
# openai.api_key = my_key
#
# prompt = input("Enter your question: ")
# model = "ada"
#
# response = openai.Completion.create(
#     engine=model,
#     prompt=prompt,
#     max_tokens=100,
#     n=1,
#     stop=None,
#     temperature=0.7
# )
#
# answer = response.choices[0].text.strip()
# print(answer)
#
#
# class Myclass :
#
#      __name__ = "dfg"
#
#
#
#
#
#
# n = Myclass()
# print(n.__name__)
# n.__name__ = "sdfghjk"
# print(n.__name__)


# class MyClass:
#     def __init__(self):
#         self.public_field = "I'm public!"
#         self._private_field = "I'm private!"
#         self.__mangled_field = "I'm mangled!"
#
# my_object = MyClass()
# print(my_object.public_field)  # Output: "I'm public!"
# print(my_object._private_field)  # Output: "I'm private!"
# # print(my_object.__mangled_field)  # Raises an AttributeError
# print(my_object._MyClass__mangled_field)  # Output: "I'm mang


# import random
#
# def hangman():
#     words = ['python', 'hangman', 'game', 'openai', 'coding']
#     chosen_word = random.choice(words)
#     guessed_letters = []
#     attempts = 6
#
#     while attempts > 0:
#         hidden_word = ''
#         for letter in chosen_word:
#             if letter in guessed_letters:
#                 hidden_word += letter
#             else:
#                 hidden_word += '_ '
#
#         print(f"\nWord: {hidden_word}")
#         print(f"Attempts left: {attempts}")
#
#         if hidden_word == chosen_word:
#             print("\nCongratulations! You've guessed the word correctly!")
#             break
#
#         guess = input("Enter a letter: ").lower()
#
#         if guess in guessed_letters:
#             print("You've already guessed that letter. Try again.")
#         elif guess in chosen_word:
#             print("Correct guess!")
#             guessed_letters.append(guess)
#         else:
#             print("Incorrect guess!")
#             attempts -= 1
#             guessed_letters.append(guess)
#
#     if attempts == 0:
#         print("\nGame over! You've run out of attempts.")
#         print(f"The word was: {chosen_word}")
#
# hangman()










def is_palindrome(word):
    if word = word[::-1]:


# Test the function
word = "level"
is_palindrome = is_palindrome(word)
print("Is the word a palindrome?", is_palindrome)
















