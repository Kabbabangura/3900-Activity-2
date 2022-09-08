def display_title():        
    print("Welcome to the Grade Calculator")  
    
def get_totalPoints(): 
    valid = False
    while valid == False:    
        try: 
            total_points = int(input("Enter the total score (0-1000): "))  
            if(not(total_points >= 0 and total_points <= 1000)):  
                print("You must enter integer values >= 0 and <= 1000. Try again.") 
            else:
                valid = True
        except:
            print("You must enter integer values >= 0 and <= 1000. Try again.")
        
    return total_points         

def get_letterGrade(point):     
        if point >= 92 and point <= 100:       
            return 'A'
        elif point >= 88:   
            return 'B+'
        elif point >= 82:
            return 'B'
        elif point >= 78 :
            return 'C+'
        elif point >= 70 :
            return 'C'
        elif point >= 60:
            return 'D'
        else:
            return 'F'
    
def main():
    display_title();        
    choice = 'y'            
    while(choice == 'y'):   
        total_points = get_totalPoints()    
        average = total_points / 10     
        letter_grade = get_letterGrade(average)  
        print("You earned an average of : {}%.".format(average), end = " ")  
        print("Letter grade earned:",letter_grade)      
        choice = input("Would you like to enter another score (y/n)? ") 
    print("Thank you")
if __name__ == "__main__":
    main()