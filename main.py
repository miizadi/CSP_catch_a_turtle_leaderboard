# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random 
import leaderboard as lb

leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name: ")

spo = ["red", "blue","salmon","pink", "goldenrod", "ivory","dark orange"]
sh = ["turtle", "arrow", "circle", "square", "triangle",]
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
spot_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game configuration----
spot_size = random.randint(2,5)
spot_color = random.choice(spo)
spot_shape = random.choice(sh)
score = 0
timelime = 30
#-----initialize turtle-----
spot = trtl.Turtle()
spot.speed(0)
spot.penup()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def countdown():
  global timer, timer_up
  spot.clear()
  if timer <= 0:
    spot.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    print("Your final score is", score)
    spot.hideturtle()
  else:
    spot.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    spot.getscreen().ontimer(countdown, spot_interval) 
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
def spot_clicked(x,y):
  global spot_color, spot_shape, score, spot_size
  rendomx = random.randint(-200,200)
  rendomy = random.randint(-200,200)
  spot.setposition(rendomx,rendomy)
  spot_size = random.randint(2,5)
  spot_color = random.choice(spo)
  spot_shape = random.choice(sh)
  spot.shapesize(spot_size)
  spot.shape(spot_shape)
  spot.fillcolor(spot_color)
  score = score + 1

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, spot_interval)
wn.mainloop()