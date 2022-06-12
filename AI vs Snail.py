import arcade
import os
import copy





rows = 10
cols = 10
Width =65
height = 65
margin = 2
screen_Width = (Width +margin )*cols +margin 
screen_height = (Width + margin) * rows + margin 


sprite_scaling1 = .14
sprite_scaling2 =  .12

print(screen_Width,screen_height)
screen_title = "Welcome to The Snail Game"



class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.width =None
        self.height = None

        self.width, self.height = self.window.get_size()
        self.window.set_viewport(0, self.width, 0, self.height)
        print(self.width,self.height)

    # def on_show(self):
        # arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def on_draw(self):
        arcade.start_render()
        texture = arcade.load_texture("background.jpg")
        scale = 0.73
        arcade.draw_scaled_texture_rectangle(self.width /2, self.height/2, texture,scale, 0)
        # self.update_board()
        
       
        # arcade.draw_text("Menu Screen ", self.width/2, self.height/2,arcade.color.BLACK, font_size =50, anchor_x="center")
        # arcade.draw_text("Press F to Full Screen", self.width/2, self.height/2-60,arcade.color.BLACK, font_size =25, anchor_x="center")

        arcade.draw_text("CLICK FOR INSTRUCTIONS PAGE", self.width/1.5, self.height/6,arcade.color.WHITE, font_size =30, anchor_x="center")
    
    def on_mouse_press(self, x, y, button, modifiers):
        instructions_view = InstructionsView()
        self.window.show_view(instructions_view)

    def on_key_press(self, key, modifiers):


        """Called whenever a key is pressed. """
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.window.set_fullscreen(not self.window.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.window.get_size()
            self.window.set_viewport(0, width, 0, height)

        # if key == arcade.key.S:
        #     # User hits s. Flip between full and not full screen.
        #     self.window.set_fullscreen(not self.window.fullscreen)

        #     # Instead of a one-to-one mapping, stretch/squash window to match the
        #     # constants. This does NOT respect aspect ratio. You'd need to
        #     # do a bit of math for that.
        #     self.window.set_viewport(0, screen_Width, 0, screen_height)
    
class InstructionsView(arcade.View):
    def __init__(self):
        super().__init__()

        self.width, self.height = self.window.get_size()
        self.window.set_viewport(0, self.width, 0, self.height)
        

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

class InstructionsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.width, self.height = self.window.get_size()
        self.window.set_viewport(0, self.width, 0, self.height)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_text("Instructions Screen", self.width/2, self.height/1.1,
                         arcade.color.GRAY, font_size=35, anchor_x="center")  
                
        arcade.draw_text("1: First turn will be of Player1.", self.width/6, self.height/1.2,
                         arcade.color.GRAY, font_size=25, anchor_x="center")

        arcade.draw_text("2: Use left click of mouse to move sprite.", self.width/4.4, self.height/1.3,
                         arcade.color.GRAY, font_size=25, anchor_x="center")
        
        arcade.draw_text("3: Can only click on boxes adjacent to sprite.", self.width/4, self.height/1.4,
                         arcade.color.GRAY, font_size=25, anchor_x="center")

        arcade.draw_text("4: Clicking on wrong box, opponent splash or sprite will considered as foul.", self.width/2.4, self.height/1.53,
                         arcade.color.GRAY, font_size=25, anchor_x="center")

        arcade.draw_text("5: On foul turn will be lost.", self.width/6.75, self.height/1.65,
                         arcade.color.GRAY, font_size=25, anchor_x="center")         

        arcade.draw_text("6: That player will be the winner who got maximum splashes.", self.width/2.95, self.height/1.78,
                         arcade.color.GRAY, font_size=25, anchor_x="center")  
        
        arcade.draw_text("Click to Play :", self.width/2, self.height/2-75,
                         arcade.color.ORANGE_PEEL, font_size=20, anchor_x="center") 

            
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.window.set_fullscreen(not self.window.fullscreen)
            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.window.get_size()
            self.window.set_viewport(0, width, 0, height)




class GameView(arcade.View):
    def __init__( self):
        # window = arcade.window(fullscreen=True)
        super().__init__()


        self.width, self.height = self.window.get_size()
        self.window.set_viewport(0, self.width, 0, self.height)
        
        self.bot_pos = (9,9)
        self.player_pos = (0,0)
        
        self.splash_p = 0
        self.splash_ai = 0
        
              
        self.temp1 = ((margin + Width) * 9 +margin +Width // 2,(margin + height) * 9 +margin +height // 2)
        self.temp2 = ((margin + Width) * 0 +margin +Width // 2,(margin + height) * 0 +margin +height // 2)

        self.sprite1 = arcade.Sprite("new.png", sprite_scaling1)
        self.sprite2 = arcade.Sprite("angrysnail.png.png",sprite_scaling2)
        
        self.sprite1.center_x = 50
        self.sprite1.center_y = 50
        
        self.sprite2.center_x = 50
        self.sprite2.center_y = 50
        self.count = 3
        
        
        self.window.score1 = 0
        self.window.score2 = 0
        
        self.grid_size = rows * cols

        self.grid = []
        self.turn = 1
        self.a = True



    def on_key_press(self, key, modifiers):
        

        """Called whenever a key is pressed. """
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.window.set_fullscreen(not self.window.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.window.get_size()
            self.window.set_viewport(0, width, 0, height)

    def initialize_board(self):
    
        for row in range(rows):
            self.grid.append([])
            for column in  range(cols):
                self.grid[row].append(0)
        self.grid[0][0],self.grid[9][9] = 1,2
    def update_board(self):
        for row in range (rows):
            for column in range(cols):
                x = (margin + Width) * column +margin +Width // 2  
                y = (margin + height) * row +margin +height // 2
                if self.grid[row][column] == 2: 
                    # texture = arcade.load_texture(":resources:C:/Users/Manzar Computers/OneDrive/Desktop/Artificial Intelligence/AI in action/Snail Game Project/Snail1.png")
                    # scale = .040
                    # arcade.draw_scaled_texture_rectangle(x,y, texture,scale, 0)
                    self.sprite1.center_x = x
                    self.sprite1.center_y = y
                    self.sprite1.draw()
                
                elif self.grid[row][column] == 1: 
                    # texture = arcade.load_texture(":resources:C:/Users/Manzar Computers/OneDrive/Desktop/Artificial Intelligence/AI in action/Snail Game Project/1.png")
                    # scale = .025
                    # arcade.draw_scaled_texture_rectangle(x,y, texture,scale, 0)s
                    self.sprite2.center_x = x
                    self.sprite2.center_y = y
                    self.sprite2.draw()
               
                arcade.draw_rectangle_outline(x, y, Width, height,arcade.color.WHITE,2)
                # arcade.draw_text("Player 1",800, 650,arcade.color.WHITE,font_size=30)
                # arcade.draw_text("Player 2",1100, 650,arcade.color.WHITE,font_size=30)

                arcade.draw_text(str(self.window.score1),850, 550,arcade.color.WHITE,font_size=30)
                arcade.draw_text(str(self.window.score2),1150, 550,arcade.color.WHITE,font_size=30)



                if self.grid[row][column] ==  20:
                    a1 = (margin + Width) * column +margin +Width // 2
                    b1 = (margin + height) * row +margin +height // 2
                    texture = arcade.load_texture("redsplash2.png")
                    scale = .16
                    arcade.draw_scaled_texture_rectangle(a1,b1, texture,scale, 0)
                elif self.grid[row][column] == 10:
                    a1 = (margin + Width) * column +margin +Width // 2
                    b1 = (margin + height) * row +margin +height // 2
                    texture = arcade.load_texture("splash2.png")
                    scale = .16
                    arcade.draw_scaled_texture_rectangle(a1,b1, texture,scale, 0)

        
    # for i in self.grid:
    #         print(i)
    

    def update_grid(self, player,x,y):
        # print(self.grid_size)
        
        if player ==1:
            
            
            column = int(x // (Width + margin))
            row = int(y //(height + margin))
          

            prow = int( self.temp2[1] //(Width + margin))
            pcolumn = int(self.temp2[0] // (Width + margin)) 

            legal = self.isLegalMove(row,column,prow,pcolumn)
            if legal == True:
                if self.grid[row][column] == 0:
                    self.splash_p = 0
                    
                    self.window.score1 += 1
                    self.grid_size -= 1
              
                    self.grid[row][column] = 1
                    self.grid[prow][pcolumn] = 10
                    self.player_pos = (row,column)   
                    self.temp2= (x,y)
                    self.turn =0
                elif self.grid[row][column] == 10:
                    self.splash_p +=1
                    
                    # self.slipping(player,row,column,prow,pcolumn)
                    # temp = None

                    
                        # print("looop")
                        # print(row,column)
                        
                    if row == prow -1:
                        while prow !=0 and self.grid[row][column] == 10 and self.grid[row][column] != 2 and self.grid[row][column] != 20 and self.grid[row][column] !=0:
                            # self.on_draw()
                            
                            # print(temp,"1")
                            # print("looooooooooooooooooooooooooooop")
                            self.grid[row][column] = 1
                            self.grid[prow][pcolumn] = 10
                            self.temp2 = ((margin + Width) * column +margin +Width // 2,(margin + Width) * row +margin +Width // 2)
                            # print(self.temp1)
                            # self.player_pos = (row,column)
                            prow,pcolumn = row, column
                            # self.on_draw()
                            
                            # if temp == 0:
                            #     self.window.score1 +=1
                            #     self.grid_size -= 1
                                
                            row = row - 1

                    elif row == prow + 1:
                        while prow !=9 and self.grid[row][column] == 10 and self.grid[row][column] != 2 and self.grid[row][column] != 20 and self.grid[row][column] !=0:
                            # self.on_draw()
                        
                            
                            # print(temp,"2")
                            # print("looooooooooooooooooooooooooooop")
                            self.grid[row][column] = 1
                            self.grid[prow][pcolumn] = 10
                            self.temp2 = ((margin + Width) * column +margin +Width // 2,(margin + Width) * row +margin +Width // 2)
                            # print(self.temp1)
                            prow,pcolumn = row, column
                            
                            # if temp == 0:
                            #     self.window.score1 +=1
                            #     self.grid_size -= 1
                            
                            row = row + 1
                        
                        # print(self.grid[trow][tcolumn],"asa")
                        # print(self.grid)
                    elif column == pcolumn -1:
                        while pcolumn !=0  and self.grid[row][column] == 10 and self.grid[row][column] != 2 and self.grid[row][column] != 20 and self.grid[row][column] !=0:
                            
                            
                            # print(temp,"3")
                            # print("looooooooooooooooooooooooooooop")
                            self.grid[row][column] = 1
                            self.grid[prow][pcolumn] = 10
                            self.temp2 = ((margin + Width) * column +margin +Width // 2,(margin + Width) * row +margin +Width // 2)
                            # print(self.temp1)
                            prow,pcolumn = row, column
                            
                            # if temp == 0:
                            #     self.window.score1 +=1
                            #     self.grid_size -= 1
                            
                            column = column - 1

                    elif column == pcolumn +1:
                        # print("asadad",column,pcolumn)
                        while pcolumn !=9  and self.grid[row][column] == 10 and self.grid[row][column] != 2 and self.grid[row][column] != 20 and self.grid[row][column] !=0:
                        
                            # print(temp,"4")
                            # print("looooooooooooooooooooooooooooop")
                            self.grid[row][column] = 1
                            self.grid[prow][pcolumn] = 10
                            self.temp2 = ((margin + Width) * column +margin +Width // 2,(margin + Width) * row +margin +Width // 2)
                            # print(self.temp1)
                            prow,pcolumn = row, column

                            # if temp == 0:
                                #     self.window.score1 +=1
                                #     self.grid_size -= 1

                                
                            column = column + 1
                    self.player_pos = (row,column)
                    self.turn = 0        
                else:   
                    self.turn = 0
            else:
                self.turn = 0
            
        if self.turn ==0:
            self.ai_turn()
                
        
        if self.grid_size == 2 or self.window.score1 ==50 or self.window.score2==50 or self.splash_p ==5 or self.splash_ai ==5:
            # print(self.grid_size,"Inner")
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)
    


    
     
            
    def isLegalMove(self,row,column,trow,tcolumn):
        # print("In LegAL")
        
        # print(row,column,trow,tcolumn)
                
        if row < rows and column < cols and (row == trow -1 or column ==tcolumn -1 or row == trow +1 or column ==tcolumn +1) and (row == trow  or column ==tcolumn):
            if self.grid[row][column] == 0:
               
                return True
            elif self.grid[row][column] == 10:
                # print("vvvvv")
                # print(self.turn)
                return True
            elif  self.grid[row][column] == 20:
                # print("cccccc")
                return True
        else:
            # print("bnbnbnbn")
            return False 

    def on_draw(self):
        

        if self.a== True:
            self.initialize_board()
            self.a = False
        else:
        # print(self.grid)
            # arcade.start_render()
            # texture = arcade.load_texture(back)
            # scale = 0.73
            # arcade.draw_scaled_texture_rectangle(self.width /2, self.height/2, texture,scale, 0)
            # # if self.turn ==0:
            #     self.ai_turn()
            arcade.start_render()
            texture = arcade.load_texture("Back22.jpg")
            scale = 0.73
            arcade.draw_scaled_texture_rectangle(self.width /2, self.height/2, texture,scale, 0)
            texture = arcade.load_texture("new.png")
            scale = .4
            arcade.draw_scaled_texture_rectangle(1190,130, texture,scale, 0)
       
            texture = arcade.load_texture("angrysnail.png.png")
            scale = .27
            arcade.draw_scaled_texture_rectangle(850, 400, texture,scale, 0)

            texture = arcade.load_texture("red.png")
            scale = .6
            arcade.draw_scaled_texture_rectangle(1000, 250, texture,scale, 0)
            
            texture = arcade.load_texture("redtext1.png")
            scale = 1.3
            arcade.draw_scaled_texture_rectangle(850, 650, texture,scale, 0)
            
            texture = arcade.load_texture("redtext2.png")
            scale = 1.3
            arcade.draw_scaled_texture_rectangle(1150, 650, texture,scale, 0)
            self.update_board()
            
           

        
    def on_mouse_press(self, x, y, button, modifiers):
        if self.turn == 1:  
            player = self.turn
            self.update_grid(player,x,y)
        
        
    ''' 
             AI  FUNCTIONS 
             
    '''
    
    def ai_turn(self):
        player = self.turn
        bot_loc = self.bot_pos
        if self.count > 0:
           row,column = bot_loc[0],bot_loc[1]
           if self.count ==3:
                self.bot_pos = (row-1,column)
                self.count -=1
                return self.update_AI_grid(player, row-1, column)
           elif self.count ==2:
                self.bot_pos = (row,column-1)
                self.count -=1
                return self.update_AI_grid(player, row, column-1)
           else:
                self.bot_pos = (row-1,column)
                self.count -=1
                return self.update_AI_grid(player, row-1, column)
               
       
        ai_move = self.findBestMove(self.grid)
        row,column = ai_move[0],ai_move[1]
        # print("AI_MOVE", ai_move)
        self.bot_pos = (row,column)
        updated_grid = self.update_AI_grid(player, row, column)
        
        return updated_grid
    
    
    
    
    
    def gen_childboards(self,grid,location):
        row= location[0]
        col = location[1]
        p_row,p_col = row,col
        index_lst= []
        child_boards = []
        print(row,col,row-1, col-1)
        if col+1 < len(grid): 
            print(row,col+1,len(grid))
            if grid[row][col+1] == 0:
                index_lst.append((row,col+1))
            # grid[row][col] = 20
        if col -1 >=  0 :
            if grid[row][col-1] == 0 :        
                index_lst.append((row,col-1))
            # grid[row][col] = 20
        if row + 1 < len(grid):
            if grid[row+1][col] == 0:
                index_lst.append((row+1,col))
            # grid[row][col] = 20
        if row -1 >= 0 :
            if grid[row-1][col] == 0: 
                index_lst.append((row-1,col))
            # grid[row][col] = 20
            
            
        for i in range(len(index_lst)):
            index = index_lst[i]
            row,col = index[0],index[1]
            # print(row)
            # print(index)
            c = copy.deepcopy(grid)
            c[row][col] = 2
            c[p_row][p_col] = 20
            child_boards.append(c)
        return child_boards    

    def heuristic(self,board,row,col):
        winningChances = 0
        #  First Condition
        for i in board:
            for j in i:
                if j ==20:
                    winningChances +=1
        
        #2nd
        
        #below
        if row + 1 < len(board) and  board[row + 1][col] ==0:
            winningChances +=1
        #above
        if row -1 >= 0 and board[row-1][col] ==0:
            winningChances +=1
        #left
        if col -1 >= 0 and board[row][col-1] == 0:
            winningChances +=1
        #right 
        if col +1 < len(board) and board[row][col +1] == 0:
            winningChances +=1
        
        #3rd Condition
        rangeMin = (len(board)//2)-3
        rangeMax = (len(board)//2) +3
        
        for i in range(rangeMin,rangeMax):
            for j in range(rangeMin,rangeMax):
                if board[i][j] == 2 :
                    winningChances +=10
        
        
        #A* Search 
        
        
        
        # winningChances = 
        
        
                    
        return winningChances
        
    def legalMoves(self,board,loc):
        moves = []
        # loc = 0
        # for row in range(len(board)):
        #     for col in range(len(board)):
        #         if board[row][col] ==2:
        #             loc = (i,j)
        
        row,col = loc[0],loc[1]
        # print(len(board))
        if row+1 < 10 :
            # print(row +1,"below")
            if board[row+1][col] == 0:
                move = (row +1,col)
                # print("below")
            # print(move)
                moves.append(move)
        if row-1 >= 0:
            if board[row -1][col] == 0:
                # print("above")
                move = (row-1,col)
                moves.append(move)
        if col + 1 < 10: 
            if board[row][col +1] == 0:
                # print("right")
                move = (row,col +1)
                moves.append(move)
        if col -1  >=0:
            if board[row][col -1] == 0:
                # print("left")
                move = (row,col-1)
                moves.append(move)
        return moves
            
            
        
        
    def minmax(self,board,depth,targetDepth,isMax,bot_loc,p_loc,alpha,beta):
        row,col = bot_loc[0],bot_loc[1]
        if depth == targetDepth:
            score = self.heuristic(board, row, col)
            # print("score",score)
            return score

        
        if isMax:
            best = -99999999999999
            allowed = self.legalMoves(board,bot_loc)
            # slipping = self.ai_slip(board)
            if len(allowed)!= 0:
                for i in allowed:
                    # print("bot allowed",allowed)
                    new_row,newcol = i[0],i[1]
                    board[new_row][newcol] = 2
                    prev_row,prev_col = row,col
                    board[prev_row][prev_col] =20
                    bot_loc = (new_row,newcol)
                    # print("before")
                    # for i in board:
                    #     print(i)
                    best = max(best,self.minmax(board, depth +1, targetDepth, False, bot_loc,p_loc,alpha,beta))
                    alpha = max(best,alpha)
                    #undo move 
                    # print("after")
                    board[new_row][newcol] = 0
                    board[prev_row][prev_col] =2
                    for i in board:
                        print(i)
                    bot_loc = (prev_row,prev_col)
                    if beta<=alpha:
                        break
                        
                    
            else:
                score = self.heuristic(board, row, col)
                return score
                
            return best
        else: 
            best = 99999999999999
            allowed = self.legalMoves(board,p_loc)
            print(allowed)
            if len(allowed)!= 0:
                for i in allowed:
                    # print(" human allowed",allowed)
                    new_row,newcol = i[0],i[1]
                    board[new_row][newcol] = 1
                    prev_row,prev_col = p_loc[0],p_loc[1]
                    board[prev_row][prev_col] =10
                    p_loc = (new_row,newcol)
                    # print("before")
                    # for i in board:
                    #     print(i)
                    best = min(best,self.minmax(board, depth +1, targetDepth, True, bot_loc,p_loc,alpha,beta))
                    beta = min(beta,best)
                    #undo move 
                    # print("after ")
                    board[new_row][newcol] = 0
                    board[prev_row][prev_col] =1
                    # for i in board:
                    #     print(i)
                    p_loc = (prev_row,prev_col)
                    
                    if beta<=alpha:
                        break
            else:
                score = self.heuristic(board, row, col)
                return score
                    
            return best
        
         







    def findBestMove(self,board):
        location = self.bot_pos
        row,col = location[0],location[1]
        
        bestVal =-10000
        # Val = -1000
        # Move = (-1,-1)
        # bot_location = (3,2)
        p_loc = self.player_pos
        
        moves= self.gen_childboards(self.grid, location)
        if len(moves) != 0:
        # count = 0
        # temp = ()
        # g= []
            for board in moves:
                g = board
                if (row+1)< len(board) and board[row+1][col] == 2:
                    bot_loc= (row+1,col)
                elif (row-1)>=0 and board[row -1][col] == 2:
                    bot_loc = (row -1,col)
                elif col+1 < len(board) and board[row][col +1] ==2  :
                    bot_loc = (row,col +1)
                elif col-1>=0 and board[row][col-1] ==2:
                    bot_loc = (row,col-1)
                
                moveVal = self.minmax(board,0,6,False, bot_loc,p_loc,-999999999,999999999999)
                # print(moveVal)
                
                if  moveVal > bestVal:
                    
                    bestVal = moveVal
                    bot_move = bot_loc
            for i in moves:
                for j in i:
                    print(j)
            print("\n")
            return bot_move
        else:
            bot_move = self.ai_slipping(board,self.bot_pos)
            # print(bot_move,"Slipping Bot move")
            return  bot_move
                    
        
            # print("\n\n\n")
            
        # print(
        
                

    
    
    def update_AI_grid(self, player,row,column):
        # print(self.grid_size)
        if player == 0:
            x = (margin + Width) * column +margin +Width // 2  
            y = (margin + height) * row +margin +height // 2
            prow = int( self.temp1[1] //(height + margin))
            pcolumn = int(self.temp1[0] // (Width + margin))
            # print("out of the grid")
        
        
            # print("In the Grid")
            if self.grid[row][column] == 0:
                self.splash_ai = 0
                
                self.window.score2 += 1
                self.grid_size -= 1 
                self.grid[row][column] = 2
                self.grid[prow][pcolumn] = 20 

                self.temp1= (x,y)
                # print("TEMP!",self.temp1)
                self.turn = 1
            elif self.grid[row][column] ==20: 
                self.splash_ai +=1
                self.grid[row][column] = 2
                self.grid[prow][pcolumn] = 20 

                self.temp1= (x,y)
                # print("TEMP!",self.temp1)
                self.turn = 1
                    
            #   

    def ai_slipping(self,board,bot_pos):
        row,column = bot_pos[0],bot_pos[1]
        slimed = []
        slime = 0
        above,below,left,right = 0,0,0,0 
        above_count = 0
        below_count = 0
        right_count = 0
        left_count = 0
        # print(row,column,"Player")
        
        # Above 
        if row +1 < len(board):
            if board[row +1][column] == 20:
                
                while row +1  < len(board):
                    # print("In above")
                    slime +=1
                    prow,pcolumn = row,column
                    row = row+1
                    # print(row +1)
                    if row <len(board):
                        above = (row,column)
                        if (board[row ][column] == 1 or board[row ][column] ==10):
                            above = (prow,pcolumn)
                            # print("Oppenent Break")
                            break
                    # print(row+1,column)
                        if  board[row][column]  == 0:
                            above = (prow,pcolumn)
                            
                    
                
                            zero_row,zero_column = above[0],above[1]
                            
                            while  int(zero_row +1) !=10 and board[zero_row +1][zero_column]  != 20 and board[zero_row +1][zero_column]  != 10 and board[zero_row +1][zero_column] != 1:
                                above_count +=1
                                zero_row = zero_row +1
                            # print("above", above,above_count)
                            break
                       
                            
                   
        slimed.append(slime)
        slime = 0
        #Below
        row,column = bot_pos[0],bot_pos[1]
        if  row -1 >= 0:
            if board[row -1][column]  ==20:
            
                while row -1 >= 0 :
                    # print("In below")
                    slime +=1
                    prow,pcolumn = row,column
                    row = row-1 
                    if row >= 0:
                        below = (row,column)
                        
                        
                        if  row >= 0 and (board[row ][column]  == 1 or board[row ][column]  == 10):
                            below = (prow,pcolumn)
                            # print("oppenet break below")
                            break
                        if  board[row][column]  == 0:
                            below = (prow,pcolumn)
                            
                    
                
                            zero_row,zero_column = below[0],below[1]
                            
                            while  zero_row -1 >= 0   and board[zero_row -1][zero_column]  != 20 and board[zero_row -1][zero_column] != 10 and board[zero_row + 1][zero_column]  != 1:
                                below_count +=1
                                zero_row = zero_row -1
                            # print("below",below,below_count)
                            break
                        
                        # print(below)
        #right
        
        slimed.append(slime)
        slime = 0
        row,column = bot_pos[0],bot_pos[1]
        if  column +1 < len(board):
            if board[row ][column +1]  == 20:
                while int(column +1) < len(board) :
                    # print("in right")
                    prow,pcolumn = row,column
                    slime +=1
                    column = column+1
                    if column < len(board):
                        right = (row,column)
                        # print("asasasaaaaaaaaaaaaaaaaa")
                        if   board[row ][column]  == 1 or board[row ][column ] ==10:
                            # print("oppnent reak right")
                            right = (prow,pcolumn)
                            break
                        if  board[row][column]  == 0:
                            # print("zero of right")
                            right = (prow,pcolumn)
                            
                    
                            zero_row,zero_column = right[0],right[1]
                            
                            while  zero_column +1  < len(board) and board[zero_row][zero_column +1]  != 20 and board[zero_row ][zero_column+1]  != 10 and board[zero_row ][zero_column + 1]  != 1:
                                right_count +=1
                                zero_column = zero_column +1
                            # print("right", right,right_count)
                            break
        slimed.append(slime)
        slime = 0          
        #left
        row,column = bot_pos[0],bot_pos[1]
        
        if  int(column -1) >= 0: 
            if board[row ][column -1]  ==20:
            
                while int(column -1) >= 0:
                    slime +=1
                    # print("In left")
                    prow,pcolumn = row,column
                    left = (row,column)
                    column = column - 1
                    if column >= 0:
                        left = (row,column)
                    if int(column ) >=0    and board[row ][column ] == 1 or board[row ][column ]  == 10:
                        left = (prow,pcolumn)
                        break
                    if  board[row ][column] ==0:
                        left = (prow,pcolumn)
                        
                    
                        zero_row,zero_column = left[0],left[1]
                        
                        while  int(zero_column -1) >=0  and board[zero_row ][zero_column -1] != 20 and board[zero_row ][zero_column -1]!= 10 and board[zero_row ][zero_column -1] != 1:
                            left_count +=1
                            zero_row = zero_row -1
                        # print("left",left,left_count)
                        break
                   
        slimed.append(slime)
        # print(above_count,below_count,left_count,right_count, "Count of Zeros")
        alist = (above,below,left,right)
        max_zeros = max(above_count,below_count,left_count,right_count)
        if max_zeros != 0:
            if max_zeros == above_count:
                self.turn =1 
                return above
            elif max_zeros == below_count:
                self.turn =1 
                return below
            elif max_zeros == left_count:
                self.turn =1 
                return left
            elif max_zeros == right_count:
                self.turn =1 
                return right
        else:
            max_slime = max(slimed)
            max_slime = slimed.index(max_slime)
            if max_slime == 0:
                return above
            elif max_slime == 1:
                return below
            elif max_slime == 2:
                return right
            elif max_slime ==3:
                return left
        
                    
            
        
        
        
        
    # def __init__(self):
    #     self.width = None
    #     self.height = None
    #     self.width,self.height = self.get_size(self)
    
class GameOverView(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.width, self.height = self.window.get_size()
        self.window.set_viewport(0, self.width, 0, self.height)
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.window.set_fullscreen(not self.window.fullscreen)
            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.window.get_size()
            self.window.set_viewport(0, width, 0, height)
    
    
    
    def on_draw(self):
        arcade.start_render()
        texture = arcade.load_texture("over1.jpg")
        scale = 0.35
        arcade.draw_scaled_texture_rectangle(self.width /2, self.height/2, texture,scale, 0)
        if self.window.score1 == self.window.score2:     
            arcade.draw_text("ooppps! Match Draw.", self.width/2, self.height/10,
                            arcade.color.GRAY, font_size=25, anchor_x="center")
        elif self.window.score1 >self.window.score2 : 
            texture = arcade.load_texture("win1.png")
            scale = 2.5
            arcade.draw_scaled_texture_rectangle(self.width/2, self.height/10, texture,scale, 0)   
        else:
            texture = arcade.load_texture("win2.png")
            scale = 2.5
            arcade.draw_scaled_texture_rectangle(self.width/2, self.height/10, texture,scale, 0)
            
        
        
            


def main():
    window = arcade.Window(screen_Width, screen_height, screen_title,fullscreen=True)
    window.score1 = 0
    window.score2 = 0
    menu_view = MenuView()
    window.show_view(menu_view)

    arcade.run()


if __name__ == "__main__":
    main()
