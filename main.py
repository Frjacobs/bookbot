def main():

    with open('books/frankenstein.txt') as f:
        print("--- Begin report of books/frankenstein.txt ---")
        file_contents = f.read()
        total_count = get_word_count(file_contents)
        print(f"{total_count} words found in the document\n") # print the output contents
        total_characters = get_characters(file_contents)
        print(total_characters)

def get_word_count(words): 
    # takes the words from the text file and counts them
    word_list = words.split()     
    return len(word_list)


def get_characters(characters): 
    # takes the characters from the text file and counts them
    total_characters = {}

    for c in characters:
        c = c.lower()
        if c in total_characters:
            total_characters[c] += 1
        else:
            total_characters[c] = 1 #initialize the value for the dictionary
    
    # Filter and sort the dictionary by values (character counts) in descending order
    sorted_characters = sorted(
        {k: v for k, v in total_characters.items() if k.isalpha()}.items(), 
        key=lambda item: item[1], 
        reverse=True )


    for s, count in sorted_characters:
            print(f"The '{s}' character was found {count} times")
    return ("--- End Report ---")  
    


if __name__ == "__main__":
    main()
    
