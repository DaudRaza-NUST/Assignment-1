free_food = 0
while free_food == 0:
    end = input("Are you at the location of the Free Food? Type Y/N ")
    if end == "Y" or end == "y":
        print("Congrats! you have arrived!")
        break
    elif end =="N" or end =="n":
        move_right = input("Is the right path clear? Type Y/N ")
        if move_right == "Y" or move_right =="y":
            print("Move towards the right")
            end
            if end == "Y" or end == "y":
                print("Congrats! you have arrived!")
                break
        elif move_right =="N" or move_right =="n":
            move_forward = input("Is the Front path clear? Type Y/N ")
            if move_forward== "Y" or move_forward=="y":
                print("Move forward")
                end
                if end == "Y" or end == "y":
                    print("Congrats! you have arrived!")
                    break
            elif move_forward =="N" or move_forward =="n":
                move_left = input("Is the left path clear? Type Y/N ")
                if move_left== "Y" or move_left=="y":
                    print("Move towards the left")
                    end
                    if end == "Y" or end == "y":
                        print("Congrats! you have arrived!")
                        break
                elif move_left =="N" or move_left =="n":
                     print("All paths are blocked, move back!")

                             