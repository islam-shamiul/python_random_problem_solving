def count_substring(string, sub_string):
    temp_str = ""
    count = 0
    for i in range(0,(len(string) - len(sub_string))+1) :
        for n in range (0,len(sub_string)):
            temp_str += string[i+n] 
        
        if temp_str == sub_string:
            count +=1
            temp_str = ""
        else: 
            temp_str = ""
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)