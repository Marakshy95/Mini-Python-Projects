#local Scope

def drink_health_pot():
    potion_power = 5
    print(potion_power)

# drink_health_pot()
# print(potion_power)


#global Scope

player_health = 10

def drink_potion():
    potion_power = 2
    print(player_health)

drink_potion()



# =============================



player_health = 10
def game():
    def drink_potion():
        potion_power = 2      # < This one has local scope to the drink potion function.
        print(player_health)

    
    # drink_potion()  < can only call it in here

# drink_potion()   < Cant call drink potion anymore because its outside the function




#BLOCKS DONT HAVE LOCAL SCOPE. ONLY INSIDE FUNCTIONS THEY DO



enemies = "Zombie"


def change_enemy():
    enemies = "skeleton"    # < its like creating a whole new variable 
    print(enemies)          # will print skeleton

print(enemies)             # will print zombie


# to access zombie enemies
# this is a bad habit tho! 

enemies = 1


def change_enemy():
    global enemies        #<<< telling the pc that there is a global variable that we want to use inside the function.. puts the variable into the function.. optherwise wew ont be able to modify anything global
    enemies += 1
    print(enemies)         

print(enemies)             

# its wrong to do that. better avoid it


#HERE IS ANOTHER WAY is to use return
enemies

def increase_enemies():
    return enemies + 1



