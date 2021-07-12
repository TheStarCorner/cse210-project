import arcade

class Score():
    def __init__(self):
        self.score_tank1_count = 10
        self.score_tank2_count = 10
        self.change_x = 0
        self.change_y = 0


    def add_score_tank1(self):
        self.score_tank1_count += 1

    def subtract_score_tank1(self):
        self.score_tank1_count -= 1    

    def add_score_tank2(self): 
        self.score_tank2_count += 1  

    def subtract_score_tank2(self):
        self.score_tank2_count -= 1  

    def draw(self):
        start_x = 25
        start_y = 558
        arcade.draw_text("SCORE BLUE TANK: " + str(self.score_tank1_count), start_x, start_y, arcade.color.WHITE, 15, font_name='GARA') 
        start_x1 = 572
        start_y1 = 558
        arcade.draw_text("SCORE RED TANK: " + str(self.score_tank2_count), start_x1, start_y1, arcade.color.WHITE, 15, font_name='GARA')    