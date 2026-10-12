import datetime
import subprocess
import os

##click(Pattern("1790283452186.png").targetOffset(685,720))
##click("1790283925188.png")
##click("1790285503582.png")



starting = datetime.datetime.now()

def os_print(string):
    global i
    temp = "echo "  + string
    os.system(temp)
def dota_upup():
    global i
    os_print("started")
    click("1789947020109.png")
    sleep(10)
    click("1789947033831.png")
    sleep(222)
    
    wait("1789947168955.png",300)

    doubleClick(Pattern("1789947168955.png").targetOffset(687,316)) #adventure

    click(Pattern("1789947168955.png").targetOffset(670,739)) #choose
    sleep(1)
    dragDrop(Pattern("1789947168955-1.png").targetOffset(878,292), Pattern("1789947168955-1.png").targetOffset(878,447))
    
    doubleClick(Pattern("1789947168955.png").targetOffset(689,320)) #chon diff 6
    #doubleClick(Pattern("1789947168955.png").targetOffset(670,400)) #chon diff 7
    click(Pattern("1789947168955.png").targetOffset(757,741)) #confirm diff
    sleep(1)
    doubleClick(Pattern("1789947168955.png").targetOffset(670,323)) #chon floor
    for i in range (10):
        click(Pattern("1789947168955.png").targetOffset(747,835)) ##chon corrupion
        
    click(Pattern("1789947168955.png").targetOffset(779,736)) #confirm floor
    sleep(3)
    free_mouse()

    
    


def free_mouse():
    if exists(Pattern("1790285503582.png").targetOffset(-785,226)):
        try:
            click(Pattern("1790285503582.png").targetOffset(-785,226))
        except:
            pass
    if exists("1789946285227.png"):
        try:
            click(Pattern("1789946285227.png").targetOffset(553,-56))
        except:
            pass
    if exists("1790035648946.png"):
        try:
            click("1790035648946.png")
        except:
            pass
def check_lvl():
    if exists("1789947459959.png"):
        try:
            doubleClick("1789947459959.png")
        except:
            pass
        
def changing_hero():
    if exists("1789947505899.png"):
        os.system('echo detected icon')
        try:
            click("1789947505899.png")
        except:
            pass
    try:
        click(Pattern("1789947545940.png").targetOffset(837,-472))
    except:
        pass
        
        os.system('echo chosing hero')
        sleep(3)
    
def game_running():
    sleep(5)
    global starting
    try:
        free_mouse()
    except:
        pass
    check_lvl()
    ##true- start clicking
    changing_hero()
    os.system('echo start a new circle')
    if exists("1789947616177.png"):
        os.system('echo detected purchasable item')
        try:

            click("1789947616177.png")
        except:
            pass
        try:
            free_mouse()
        except:
            pass
        if exists("1789947651449.png"):
            try:
                click("1789947651449.png")
            except:
                pass
        if exists("1790169210783.png"):
            try:
                click("1790169210783.png")
            except:
                pass
    current = datetime.datetime.now()
    time_diffrence = current - starting 
    if (time_diffrence.total_seconds() > 1820):
        os_print("game bat dau luc " + str(starting) + " end luc " + str(current))
        return False ##game end
    else: 
        return True
os.system('cls')


def post_game():
    try:
        
        click(Pattern("1790596091734.png").targetOffset(39,46))
    except:
        pass
    click(Pattern("1789946449509.png").targetOffset(13,4))
    free_mouse()
    click(Pattern("1789946449509.png").targetOffset(13,4))
    free_mouse()
    click(Pattern("1789946449509.png").targetOffset(13,4))
    post_game_begin = datetime.datetime.now()
    while not exists ("1789946805178.png"):
        post_game_current = datetime.datetime.now()
        post_game_time_diffrence = post_game_current - post_game_begin
        if (post_game_time_diffrence.total_seconds() > 120):
            break
        try:
            click(Pattern("1789946501518.png").similar(0.50))
            free_mouse()
        except:
            pass
    if exists(Pattern("1789946805178.png").targetOffset(-476,244)):
        click(Pattern("1789946805178.png").targetOffset(-476,244))
        click(Pattern("1789946805178.png").targetOffset(435,566))
        sleep(120)

    click(Pattern("1789946449509.png").targetOffset(13,4))
    free_mouse()
    click(Pattern("1789946449509.png").targetOffset(13,4))
    free_mouse()
    click(Pattern("1789946449509.png").targetOffset(13,4))
    post_game_begin = datetime.datetime.now()
    while not exists ("1789946805178.png"):
        post_game_current = datetime.datetime.now()
        post_game_time_diffrence = post_game_current - post_game_begin
        if (post_game_time_diffrence.total_seconds() > 120):
            break
        try:
            click(Pattern("1789946501518.png").similar(0.50))
            free_mouse()
        except:
            pass
    if exists(Pattern("1789946805178.png").targetOffset(-476,244)):
        click(Pattern("1789946805178.png").targetOffset(-504,434))
        click(Pattern("1789946805178.png").targetOffset(435,566))
        sleep(60)
        free_mouse()
    #click chon do
    click(Pattern("1789949316429.png").targetOffset(1555,-676))
    click(Pattern("1789949316429.png").targetOffset(1614,-668))
    click(Pattern("1789949316429.png").targetOffset(1678,-673))
    click(Pattern("1789949316429.png").targetOffset(1741,-677))
    free_mouse()
    
    if exists("1790359259637.png"):
        click("1790359259637.png") #confirm
    free_mouse()
    try:
        
        click(Pattern("1790596091734.png").targetOffset(39,46))
    except:
        pass
    
    ###smelt
    click(Pattern("1789949316429.png").targetOffset(99,-924))#click equipment
    sleep(1)
    click(Pattern("1789949448893.png").targetOffset(8,-234)) #click disassemble
    click(Pattern("1789949448893.png").targetOffset(402,401)) #click disassemble
    click(Pattern("1789949448893.png").targetOffset(488,399)) #click select all
    click(Pattern("1789949448893.png").targetOffset(331,406)) #click accept
    click(Pattern("1789949448893.png").targetOffset(-107,-466)) #click exit
    sleep(1)   
    #leave
    if exists(Pattern("1790361973644.png").targetOffset(-79,60)):
        click(Pattern("1790361973644.png").targetOffset(-79,60)) #click exit
    sleep(5)
    click(Pattern("1789946952235.png").targetOffset(1120,933))
    sleep(30)
    wait("1789947004839.png",60)

i = 1   
while True:
    if i > 0:
        dota_upup()
    else:
        i = i +1
    starting = datetime.datetime.now()
    os_print(str(starting))
    while game_running():
        pass
    try:
        free_mouse()
    except:
        pass
    post_game()