def string_name(words):
	return len(words)
	
	
def name(text):
    if len(text) < 2:
        return ""
        
    return text[0]+text[1] + text[-2]+ text[-1]
    
    
def String_length(text):     
    if (text) [-3:] == "ing":
        return text + "ly"
    
    if len(text) >= 3:
        return text + "ing"
    
    if len(text) <= 2:
        return text
        
        
def list_of_words(words):
    longest = max(words, key=len)
    return longest, len(longest)

def odd_index(word):
    result = ""
    for character in range(len(word)):
        if character % 2 == 1:
            result += word[character]
    return result
    
def string_of_words(text):
    for word in text:
        if len(word) % 2 == 1:
    return word


def minimum_numbers(number):
    smallest = number[0]
    for numbers in number:
        if numbers < smallest:
            smallest = numbers
            
    return smallest
            
            
def maximum_numbers(number):
    largest = number[6]
    for numbers in number:
        if numbers > largest:
            largest = numbers
            
    return largest
   
   
def repeat_string(text, number):
    if type(number) == int:
        return text * number
    return text
    
def square_list(numbers):
    return [number ** 2 for number in numbers]

def sum_of_square(numbers):
    total = 0
    for the_numbers in numbers:
        total += (the_numbers * the_numbers)
    return total

   

