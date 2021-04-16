from models.player import * 


player_1 = Player("Kieran", "Rock")
player_2 = Player("Aidan", "Scissors")
player_3 = Player("Nick", "Paper")

players = [player_1, player_2]

def get_preferred_option(player_1, player_2):
    if player_1.gesture == "Rock" and player_2.gesture == "Scissors":
        return player_1
        
    if player_1.gesture == "Scissors" and player_2.gesture == "Paper":
        return player_1
        
    if player_1.gesture == "Paper" and player_2.gesture == "Rock":
        return player_1
    
    if player_1.gesture == player_2.gesture:
        return "draw"
        
    return player_2


def get_this_working(gesture_1, gesture_2):
    gesture_1 = player_1
    gesture_2 = player_2
    if player_1.gesture == "Rock" and player_2.gesture == "Scissors":
        return player_1
        
    if player_1.gesture == "Scissors" and player_2.gesture == "Paper":
        return player_1
        
    if player_1.gesture == "Paper" and player_2.gesture == "Rock":
        return player_1
    
    if player_1.gesture == player_2.gesture:
        return "draw"
        
    return player_2

def this_works(gesture_1, gesture_2):
    if gesture_1 == "Rock" and gesture_2 == "Scissors":
        return gesture_1
        
    if gesture_1 == "Scissors" and gesture_2 == "Paper":
        return gesture_1
        
    if gesture_1 == "Paper" and gesture_2 == "Rock":
        return gesture_1
    
    if gesture_1 == gesture_2:
        return "draw"
        
    return gesture_2




       

       


