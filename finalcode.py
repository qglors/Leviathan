#set window dimensions
WIDTH = 1000
HEIGHT = 650

#import module to randomize beetle movements
import random

#initialize global variables

#timers
timer = 0
book_shine_timer = 0
start_shine = 0
page_shine_timer = 0
page_shine_start = 0
page_flip_timer = 0
fade_timer = 0
buffer = 0
island_bg_timer = 0
start_text = 0
flash_in_island = 0
number = 0
mouse_move_timer = 0
explore_bg_timer = 0
chest_timer = 0
portal_timer = 0
portal_numbers = 0
close_ground_timer = 0
beetle_timer = 0
fantasy_bg_timer = 0
snake_timer = 0

#starters to tell other parts when to start/stop
page_flip_start = "NO"
start = "NO"
magic_book_move = "NO"
big_book_draw = "NO"
menutolib_fade = "NO"
draw_island = "NO"
draw_text_box = "NO"
poll = "NO"
draw_key = "NO"
go_beetles = "NO"
draw_text_box2 = "NO"
cornerbook_move = "NO"
after_beetles = "NO"
draw_fantasy = "NO"
last_scene = "NO"
theend = "NO"

#add actors

#background actor
bg = Actor("ocean1")

#actors for the starting menu text
start_play = Actor("play")
#coordinates
start_play.x = 505
start_play.y = 380

start_quit = Actor("quit")
#coordinates
start_quit.x = 505
start_quit.y = 482

#actors for library scene
magic_book = Actor("magicbook")
#coordinates
magic_book.x = 488
magic_book.y = 213

table = Actor("table")
#coordinates
table.x = 501
table.y = 472

big_book = Actor("book1")
#coordinates
big_book.x = 498
big_book.y = 433

page = Actor("page")
#coordinates
page.x = 616
page.y = 408

book_shadow = Actor("book_shadow")
#coordinates
book_shadow.x = 506
book_shadow.y = 539

#actors for shine (player hints)
book_shine = Actor("book_shine1")
#coordinates
book_shine.x = 484
book_shine.y = 205

page_shine = Actor("page_shine1")
#coordinates
page_shine.x = 553
page_shine.y = 345

#transitional actor (between library and island scenes)
flash = Actor("flash1")

#text boxs for narration/characters talking, etc.
text_box = Actor("bubble")
#coordinates
text_box.x = 500
text_box.y = 569

#button for player interaction
buttons = Actor("button1")
buttons.x = 876
buttons.y = 613

#another button for second option
buttons_two = Actor("button4")
buttons_two.x = 727
buttons_two.y = 613

#interactive character (welcomeguy)
welcomeguy = Actor("welcomeguy")
welcomeguy.x = 189
welcomeguy.y = 419

#exploring scene actors
hole = Actor("hole")
hole.x = 338
hole.y = 558

pole = Actor("pole")
pole.x = 319
pole.y = 687

#exploring ground actors
groundmiddle = Actor("groundmiddle")
groundmiddle.x = 415
groundmiddle.y = 563

groundleft = Actor("groundleft")
groundleft.x = 5
groundleft.y = 582

groundright = Actor("groundright")
groundright.x = 1001
groundright.y = 581

groundup = Actor("groundup")
groundup.x = 162
groundup.y = 249

#mouse (main character)
mousey = Actor("mouseright1")
mousey.x = 36
mousey.y = 467

#borders (stop other actors from falling through)
border_left = Actor("borderleft")
border_left.x = 184
border_left.y = 585

border_right = Actor("borderright")
border_right.x = 634
border_right.y = 589

border_midleft = Actor("bordermidleft")
border_midleft.x = 282
border_midleft.y = 571

border_midright = Actor("bordermidright")
border_midright.x = 547
border_midright.y = 568

border_upup = Actor("borderupup")
border_upup.x = 159
border_upup.y = 235

border_updown = Actor("borderupdown")
border_updown.x = 163
border_updown.y = 269

border_upright = Actor("borderupright")
border_upright.x = 260
border_upright.y = 250

border_upleft = Actor("borderupleft")
border_upleft.x = 66
border_upleft.y = 249

#visual instructions (at the top right corner)
keyarrowright = Actor("keyarrowright")
keyarrowright.x = 950
keyarrowright.y = 102

keyarrowleft = Actor("keyarrowleft")
keyarrowleft.x = 838
keyarrowleft.y = 102

keyarrowup = Actor("keyarrowup1")
keyarrowup.x = 894
keyarrowup.y = 46

keyspace = Actor("keyspace")
keyspace.x = 736
keyspace.y = 101

#interactive exploring scene actors
chest = Actor("chest1")
chest.x = 107
chest.y = 187

key = Actor("key")

portal = Actor("portal1")
portal.x = 950
portal.y = 439

#enemies
beetle1 = Actor("beetle1")
beetle1.x = 1100
beetle1.y = 488

beetle2 = Actor("beetle2")
beetle2.x = 1100
beetle2.y = 488

beetle3 = Actor("beetle3")
beetle3.x = 1100
beetle3.y = 488

beetle4 = Actor("beetle4")
beetle4.x = 1100
beetle4.y = 488

beetle5 = Actor("beetle5")
beetle5.x = 1100
beetle5.y = 488

beetle6 = Actor("beetle6")
beetle6.x = 1100
beetle6.y = 488

#character
paperbag = Actor("paperbag")
paperbag.x = 108
paperbag.y = 438

#interactive backpack item
cornerbook = Actor("cornerbook")
cornerbook.x = 55
cornerbook.y = 52

#fantasy scene ground
fantasy_ground = Actor("fantasy_ground")
fantasy_ground.x = 492
fantasy_ground.y = 501

#fantasy scene ground border
fantasy_borderleft = Actor("fanborderleft")
fantasy_borderleft.x = 154
fantasy_borderleft.y = 592

fantasy_borderright = Actor("fanborderright")
fantasy_borderright.x = 846
fantasy_borderright.y = 593

fantasy_door = Actor("fantasydoor")
fantasy_door.x = 300
fantasy_door.y = 414

#final scene actors
fade = Actor("fade1")

end = Actor("end")

def draw():
    #get global variables
    global start_shine, big_book_draw, fade_timer, flip_timer, draw_island, number, draw_key, after_beetles, theend
    #draw starting menu
    #clear screen
    screen.clear()
    #draw night ocean background
    bg.draw()
    #draw play and quit buttons
    start_play.draw()
    start_quit.draw()

    #draw library scene when player clicks start
    if start == "YES":
        #clear screen
        screen.clear()
        #redraw ocean night background to get rid of the menu buttons
        bg.draw()
        #after the fade (starttolibfade), draw the book
        if fade_timer >= 10:
            #draw book
            magic_book.draw()

    #start the shine animation over the book after the shine timer
    if start_shine >= 20:
        book_shine.draw()

    #draw big book
    if big_book_draw == "YES":
        #clear screen
        screen.clear()
        #redraw background
        bg.draw()
        #draw table
        table.draw()
        #draw the book's shadow
        book_shadow.draw()
        #draw the book
        big_book.draw()
        #draw the flash (animation won't play until page flips)
        flash.draw()

    #shine the page (player hint)
    if page_shine_start >= 30:
        page_shine.draw()

    #when the book flash is done, transition to the island scene
    if draw_island == "YES":
        #clear screen
        screen.clear()
        #draw background
        bg.draw()
        #draw flash
        flash.draw()
        #start roleplay portion
        if draw_text_box == "YES":
            #draw text box, button, and text using function
            dialogue_exchanges()

        #numbers are a specific part of the story (indexes from the list of roleplay dialogues)
        if number > 1 and number < 7:
            #draw character
            welcomeguy.draw()
        if number > 7 and number < 15:
            #draw character
            welcomeguy.draw()
        if number == 3 or number == 13:
            #draw second option button
            buttons_two.draw()

        #numbers are a specific part of the story (indexes from the list of roleplay dialogues)
        if number >= 13:
            #draw book (received from welcomeguy character)
            cornerbook.draw()
        if number >= 16:
            #clear screen
            screen.clear()
            #draw background
            bg.draw()
            #add cornerbook
            cornerbook.draw()
            #draw ground and borders using function
            border_and_ground_draw()
            #draw visual instructions using function
            visual_instructions()
            #add interactive actors
            chest.draw()
            mousey.draw()

            #if character touches chest, draw key
            if draw_key == "YES":
                #draw key
                key.draw()

                #key stays on top of mouse
                key.x = mousey.x
                key.y = mousey.y - 56

                #more interactive characters appear
                portal.draw()
                draw_beetles()

                #story continues
                if draw_text_box2 == "YES":
                    #draw text box, button, and text using function
                    dialogue_exchanges()
                    #add story character
                    paperbag.draw()

                    #when dialogue exchange ends
                    if number >= 20:
                        #clear screen
                        screen.clear()
                        #draw background
                        bg.draw()
                        #add corner book
                        cornerbook.draw()
                        #draw ground and borders using a function
                        border_and_ground_draw()
                        #draw visual instructions using a function
                        visual_instructions()
                        #draw interactive characters
                        chest.draw()
                        portal.draw()
                        mousey.draw()
                        #draw key
                        key.draw()
                        #make key stay on top of mouse's head
                        key.x = mousey.x
                        key.y = mousey.y - 56
                        #draw 6 beetles using a function
                        draw_beetles()

                        #after all beetles have been defeated, story continues
                        if after_beetles == "YES":
                            #draw text box, button, and text using function
                            dialogue_exchanges()
                            #add character
                            paperbag.draw()

        #when dialogue exchange ends
        if number >= 22:
            #clear screen
            screen.clear()
            #draw background
            bg.draw()
            #draw the book in the corner
            cornerbook.draw()
            #draw ground and borders using a function
            border_and_ground_draw()
            #draw visual instructions using a function
            visual_instructions()
            #draw more interactive actors
            chest.draw()
            portal.draw()
            mousey.draw()
            #draw key
            key.draw()
            #key stays on top of mouse's head
            key.x = mousey.x
            key.y = mousey.y - 56

            #when player goes into the portal
            if draw_fantasy == "YES":
                #clear screen
                screen.clear()
                #draw background
                bg.draw()
                #draw visual intructions
                keyarrowleft.draw()
                keyarrowright.draw()
                #drawground and borders (fantasy land)
                fantasy_ground.draw()
                fantasy_borderright.draw()
                fantasy_borderleft.draw()
                #draw door
                fantasy_door.draw()
                #draw mouse
                mousey.draw()
                #draw key
                key.draw()

                #when the player enters the door, the last scene will play
                if last_scene == "YES":
                    #clear screen
                    screen.clear()
                    #draw background
                    bg.draw()
                    #draw mouse
                    mousey.draw()
                    fade.draw()

                    #when the snake scene is over, the last actor will be drawn
                    if theend == "YES":
                        screen.clear()
                        end.draw()


def update():
    #get global variables
    global timer, magic_book_move, page_flip_start, number, chest_timer, draw_key

    #timer for animating the night ocean background
    timer += 0.15
    if timer > 10:
        timer = 0

    #animate the night ocean background
    if bg.image == "ocean1" or bg.image == "ocean2":
        #animate starting background
        if timer > -1 and timer < 6:
            bg.image = "ocean1"
        else:
            bg.image = "ocean2"

    #run begin function when player clicks start
    begin(start)

    #run shinypage function (page will shine when the big book can be drawn)
    shinypage(big_book_draw)

    #run flippage function (page will flip when player clicks)
    flippage(page_flip_start)

    #run flashtoisland function to transition from the page flash to the island scene
    flashtoisland()

    #run island_animate function to animate the background of the island scene
    island_animate()

    #text function for the role playing text at the bottom
    text()

    #change button options during dialogue exchanges
    play_buttons(number)

    #function to let user move the mouse/main character
    mousey_move(number)

    #slides the pole back into place if player doesn't do it correctly
    pole_slip()

    #allows the mouse to climb up the pole
    mouse_up_pole()

    #animates the exploration scene background
    explore_animate()

    #animates the chest opening
    open_chest()

    #animates the portal spinning
    portal_spin(draw_key)

    #animates the ground closing before the beetles appear(or when the player finds the key)
    close_ground()

    #releases the beetles(also lets them move)
    beetles()

    #changes scenes when player goes into the portal
    in_portal()

    #sets ground/wall boundaries in the fantasy scene
    fantasy_boundaries()

    #animates the fantasy scene background
    fantasy_background()

    #final scene
    final()

def on_mouse_move(pos, buttons):
    #get global variables
    global magic_book_move

    #add arrows for when player hovers over the menu options
    if start_play.collidepoint(pos):
        start_play.image = "play_hovered"
        #coordinates
        start_play.x = 469
        start_play.y = 380
    else:
        start_play.image = "play"
        #coordinates
        start_play.x = 505
        start_play.y = 380

    #add arrows for when player hovers over the menu options
    if start_quit.collidepoint(pos):
        start_quit.image = "quit_hovered"
        #coordinates
        start_quit.x = 466
        start_quit.y = 482
    else:
        start_quit.image = "quit"
        #coordinates
        start_quit.x = 505
        start_quit.y = 482

    #move little book with player's cursor
    if magic_book_move == "YES":
        #removes the shine when player clicks the book
        book_shine.image = "emptybrotha"
        #coordinates
        book_shine.x = 403
        book_shine.y = 213
        #book coordinates = cursor/mouse coordinates
        magic_book.x = pos[0]
        magic_book.y = pos[1]

    #when player's cursor hovers over the book, a box appears telling the player what the book is
    if cornerbook.collidepoint(pos):
        cornerbook.image = "explan"
        #coordinates
        cornerbook.x = 100
        cornerbook.y = 52

    else:
        cornerbook.image = "cornerbook"
        #coordinates
        cornerbook.x = 55
        cornerbook.y = 52

    #makes the corner book follow the player's cursor when the player's allowed to click it
    if cornerbook_move == "YES":
        #coordinates/cursor coordinates
        cornerbook.x = pos[0]
        cornerbook.y = pos[1]

def on_mouse_down(pos, button):
    #get global variables
    global start, magic_book_move, big_book_draw, page_flip_start, buffer, number, poll, cornerbook_move

    #make menu options work
    if bg.image == "ocean1" or bg.image == "ocean2":
        #if player clicks quit, program quits
        if start_quit.collidepoint(pos):
            #quit
            quit()

        #if player clicks start, the game begins
        if start_play.collidepoint(pos):
            #draw starting scene (library scene)
            start = "YES"

    #if player clicks on the little book or the shine on it, the book moves with their cursor
    if book_shine.collidepoint(pos) or magic_book.collidepoint(pos):
        #removes the shine when player clicks the book
        book_shine.image = "emptybrotha"
        #coordinates
        book_shine.x = 403
        book_shine.y = 213
        #book move with cursor
        magic_book_move = "YES"

        #if player clicks in the centre area, the big book appears
        if table.collidepoint(pos):
            #big book appears
            big_book_draw = "YES"

            #when player clicks the page
            if big_book.collidepoint(pos) or page_shine.collidepoint(pos):
                #add buffer so player doesn't flip page when they click the book down
                if buffer <= 10:
                    buffer += 5
                #buffer stops and page can be clicked
                if buffer >= 9:
                    #start page flip animation
                    page_flip_start = "YES"

        #if it's time for the island scene
        if draw_island == "YES":
            #if first dialogue exchange is over
            if number < 16:
                #if player clicks button, index goes up, and the text changes to next dialogue in the list
                if buttons.collidepoint(pos):
                    number += 1

                #same as above, but for times when there are two response options
                if number == 3 or number == 13:
                    #if player clicks button, index skips a response
                    if buttons_two.collidepoint(pos):
                        number += 2

            #second dialogue exchange
            elif draw_text_box2 == "YES":
                if number < 20:
                    #if player clicks button, index goes up, and the text changes to next dialogue in the list
                    if buttons.collidepoint(pos):
                        number += 1

                    #same as above, but for times when there are two response options
                    if number == 3 or number == 13:
                        #if player clicks button, index skips a response
                        if buttons_two.collidepoint(pos):
                            number += 2

                if after_beetles == "YES":
                    if number < 22:
                        #if player clicks button, index goes up, and the text changes to next dialogue in the list
                        if buttons.collidepoint(pos):
                            number += 1

                        #same as above, but for times when there are two response options
                        if number == 3 or number == 13:
                            #if player clicks button, index skips a response
                            if buttons_two.collidepoint(pos):
                                number += 2

    #if player clicks the pole (exploration scene)
    if pole.collidepoint(pos):

        #allows the pole sliding function to start
        poll = "YES"

        #if pole isn't in place yet, pole goes up when player clicks
        if pole.y > 413:
           pole.y -= 50

        #if the pole is in place, keep it in place
        if pole.y == 413:
            pole.y = 413

        #if the pole is almost in place, add to visual instructions (an up key option)
        if pole.y <= 430:
            keyarrowup.image = "keyarrowup2"

        #if pole's not there yet, visual instructions stay the same
        if pole.y > 430:
            keyarrowup.image = "keyarrowup1"

    #if beetles are moving
    if go_beetles == "YES":
        #if player clicks the corner book
        if cornerbook.collidepoint(pos):
            #cornerbook is the image without the explanation
            cornerbook.image = "cornerbook"
            #allows the corner book to move with player's cursor in the on_mouse_move function)
            cornerbook_move = "YES"

#function for drawing borders and the ground in the exploration scene
#ground for visual effects
#borders to stop actors from going through the ground
#for convenience
def border_and_ground_draw():
    border_right.draw()
    groundright.draw()
    border_left.draw()
    groundleft.draw()
    hole.draw()
    pole.draw()
    groundmiddle.draw()
    border_midleft.draw()
    border_midright.draw()
    groundup.draw()
    border_upup.draw()
    border_updown.draw()
    border_upleft.draw()
    border_upright.draw()

#function for visual instructions (in the exploration scene)
#just a visual aid
#for convenience
def visual_instructions():
    keyarrowleft.draw()
    keyarrowright.draw()
    keyarrowup.draw()
    keyspace.draw()

#function to draw the beetle actors
def draw_beetles():
    beetle1.draw()
    beetle2.draw()
    beetle3.draw()
    beetle4.draw()
    beetle5.draw()
    beetle6.draw()

#function to keep the story going when it's time for a dialogue exchange
#for convenience
def dialogue_exchanges():
    #draw text box
    text_box.draw()
    #add text (from a list of texts)
    screen.draw.text(roleplay(number), (79, 542), color="black", fontname="minecraft", fontsize=30)
    #add interactive(clickable) buttons
    buttons.draw()

#function to make pole slide back into place when it's not at the right y value (not high enough)
def pole_slip():
    #get global variables
    global poll

    if poll == "YES":
        #if it's not at the right y value
        if pole.y != 413:
            #if it's too high
            if pole.y < 687:
                #go down
                pole.y += 1
            #if it's too low (somehow)
            else:
                #go up
                pole.y -= 1

#fade from the menu (night ocean) to the library scene
def starttolibfade():
    #get global variables
    global fade_timer

    #increase the timer
    if fade_timer <= 10:
        fade_timer += 0.3

    #change bg image frame by frame for a fade
    if fade_timer > 0 and fade_timer < 2:
        bg.image = "starttolibfade1"
    if fade_timer > 2 and fade_timer < 4:
        bg.image = "starttolibfade2"
    if fade_timer > 4 and fade_timer < 6:
        bg.image = "starttolibfade3"
    if fade_timer > 6 and fade_timer < 8:
        bg.image = "starttolibfade4"
    if fade_timer > 8 and fade_timer < 10:
        bg.image = "starttolibfade5"
    #fade ends and library scene is there
    if fade_timer >= 10:
        bg.image = "library"

#when player clicks start, game begins
def begin(start):
    #get global variables
    global start_shine, book_shine_timer
    #if player clicked start, game starts
    if start == "YES":

        #play starttolibfade function (menu fades to library)
        starttolibfade()

        #timer so the animated shine on the book doesn't start immediately (buffer)
        if start_shine < 21:
            start_shine += 0.5

        #start the animated shine on the book
        if start_shine >= 20:
            #as long as the book is on the shelf (player has not moved it), the animated shine runs
            if magic_book_move == "NO":
                book_shine_timer += 0.4
                if book_shine_timer > 70:
                    book_shine_timer = 0
                if book_shine_timer > 0 and book_shine_timer < 2:
                    book_shine.image = "book_shine1"
                    #coordinates
                    book_shine.x = 484
                    book_shine.y = 205
                if book_shine_timer > 2 and book_shine_timer < 4:
                    book_shine.image = "book_shine2"
                    #coordinates
                    book_shine.x = 488
                    book_shine.y = 213
                if book_shine_timer > 4 and book_shine_timer < 6:
                    book_shine.image = "book_shine3"
                    #coordinates
                    book_shine.x = 488
                    book_shine.y = 213
                if book_shine_timer > 6 and book_shine_timer < 8:
                    book_shine.image = "book_shine4"
                    #coordinates
                    book_shine.x = 491
                    book_shine.y = 220
                if book_shine_timer > 8:
                    #empty (except one pixel) so the animated shine doesn't constantly repeat
                    book_shine.image = "emptybrotha"
                    #coordinates
                    book_shine.x = 403
                    book_shine.y = 213

#function to animate the shine on the big book page
def shinypage(big_book_draw):
    #get global variables
    global page_shine_start, page_shine_timer

    #if the book has been drawn, the animated shine on the page can start
    if big_book_draw == "YES":
        #timer so the shine doesn't start right away (buffer)
        if page_shine_start <= 30:
            page_shine_start += 0.5

        #start the animated shine on the page
        if page_shine_start >= 30:
            page_shine_timer += 0.4

            #reset timer so the animated shine replays
            if page_shine_timer > 80:
                page_shine_timer = 0

            #animated shine on the big book page
            if page_shine_timer > 0 and page_shine_timer < 2:
                page_shine.image = "page_shine1"
                #coordinates
                page_shine.x = 553
                page_shine.y = 345
            if page_shine_timer > 2 and page_shine_timer < 4:
                page_shine.image = "page_shine2"
                #coordinates
                page_shine.x = 593
                page_shine.y = 408
            if page_shine_timer > 4 and page_shine_timer < 6:
                page_shine.image = "page_shine3"
                #coordinates
                page_shine.x = 603
                page_shine.y = 426
            if page_shine_timer > 6 and page_shine_timer < 8:
                page_shine.image = "page_shine4"
                #coordinates
                page_shine.x = 681
                page_shine.y = 479
            #empty (except one pixel) so the animated shine doesn't constantly repeat
            if page_shine_timer > 8:
                page_shine.image = "emptybrotha"

#animated the flipping page
def flippage(page_flip_start):
    #get global variables
    global page_flip_timer

    #initialize local variables
    number_list = [0]*18
    numbers = 0
    list_counter = 0
    big_book_images = ["book"]*18
    flash_images = ["flash"]*18

    #for loop
    #get a list of 1-18
    for i in range(len(number_list)):
        numbers += 1
        number_list[i] = numbers

    #reset to zero to reuse
    numbers = 0

    #rename items in the image lists (to use as the image name file)
    while list_counter < 18:
        #rename each item in list to the names of my image files
        big_book_images[numbers] = 'book' + str(number_list[numbers])
        #rename each item in list to the names of my image files
        flash_images[numbers] = 'flash' + str(number_list[numbers])
        #add one
        numbers += 1
        #add one
        list_counter += 1

    #reset to zero to reuse
    numbers = 0

    #animate
    #when player clicks page, page flips
    if page_flip_start == "YES":
        for x in range(17):
            #timer to slow the flipping down
            page_flip_timer += 0.02
            #when timer goes up 5 times, index can rise once (slowing the flipping down)
            if page_flip_timer > number_list[numbers]:
                numbers += 1

        for x in range(len(big_book_images)):
            #image changes
            big_book.image = big_book_images[numbers]
            flash.image = flash_images[numbers]


#animate from the flash (of the book opening) to the island scene
def flashtoisland():
    #get global variables
    global draw_island, flash_in_island, number

    #when page flip flash is done, transition to island scene
    if page_flip_timer >= 17:
        #change background image to island scene
        bg.image = "nightisland1"
        #signal draw function to redraw everything
        draw_island = "YES"

    #start timer so images can change frame by frame
        if flash_in_island <= 18:
            flash_in_island += 0.2

        #change images frame by frame (18 images) to animate the page flip and white flash
        if flash_in_island > 17:
            flash.image = "flash1"
        elif flash_in_island > 16:
            flash.image = "flash2"
        elif flash_in_island > 15:
            flash.image = "flash3"
        elif flash_in_island > 14:
            flash.image = "flash4"
        elif flash_in_island > 13:
            flash.image = "flash5"
        elif flash_in_island > 12:
            flash.image = "flash6"
        elif flash_in_island > 11:
            flash.image = "flash7"
        elif flash_in_island > 10:
            flash.image = "flash8"
        elif flash_in_island > 9:
            flash.image = "flash9"
        elif flash_in_island > 8:
            flash.image = "flash10"
        elif flash_in_island > 7:
            flash.image = "flash11"
        elif flash_in_island > 6:
            flash.image = "flash12"
        elif flash_in_island > 5:
            flash.image = "flash13"
        elif flash_in_island > 4:
            flash.image = "flash14"
        elif flash_in_island > 3:
            flash.image = "flash15"
        elif flash_in_island > 2:
            flash.image = "flash16"
        elif flash_in_island > 1:
            flash.image = "flash17"
        elif flash_in_island > 0:
            flash.image = "flash18"

#animate island background (in the nighttime island scene)
def island_animate():
    #get global variables
    global draw_island, island_bg_timer

    #when island has been draw (specifically the background cause it's going to animate it)
    if draw_island == "YES":

        #timer to slow animation down
        island_bg_timer += 0.2
        #reset timer when it gets too high
        if island_bg_timer > 10:
            island_bg_timer = 0

        #flip between two island backgrounds
        if island_bg_timer >= 0 and island_bg_timer <= 5:
            bg.image = "nightisland1"

        if island_bg_timer > 5 and island_bg_timer < 10:
            bg.image = "nightisland2"

#timers/buffers to stop text from appearing right away
def text():
    #get global variables
    global start_text, draw_text_box, draw_island, draw_text_box2

    #when island has been drawn (right before first dialogue exchange)
    if draw_island == "YES":
        #wait for buffer
        if start_text < 50:
            start_text += 1

        #when buffer ends, text can appear
        elif start_text >= 50:
            draw_text_box = "YES"

    #when key has been found (right before second dialogue exchange)
    if draw_key == "YES":

        #wait for buffer (using the same timer)
        if start_text < 100:
            start_text += 1

        #when buffer ends, text can appear
        elif start_text >= 100:
            draw_text_box2 = "YES"

#list for dialogue blurbs
#when player clicks button, index goes up, and a different blurb appears
def roleplay(number):
    #all of the dialogue blurbs in the entire game
    responses = ["...What's this?", "...Where am I?", "Welcome, newcomer! Welcome to Leviathan Island!",
    "How did you get here?", "...", "Ho ho! Well, it's good you're here!", "Let me show you around!",
    "This is Leviathan!", "Our lord and saviour created this island!",
    "Yup! He created the sun, the clouds, and the sea.", "And with his last bit of energy, he turned himself\ninto this island here.",
    "To pay homage, we have named this island after him.\nWelcome to Leviathan Island!", "Yup!",
    "Here's the Will of Leviathan. It's a little scripture\nof our origin and life.", "Haha! Well, I'll leave you to explore the island!",
    "Shh. Say no more. Go explore.", "Psst.", "Waaatch ouuut...", "The beeeetles are coooming...", "The beeetles...",
    "Phew, thanks. On our island, we don't get along with\nthe other animals.", "Yeah. Be careful.", "Leviathan...?"]

    #return the dialogue to the draw function
    return responses[number]

#change buttons (for different options)
def play_buttons(number):
    #get global variables
    global go_beetles

    #change buttons depending on which blurb is currently there
    #number is the index of the dialogue list
    if number == 2:
        buttons.image = "button2"

    elif number == 3:
        buttons.image = "button3"

    elif number == 6:
        buttons.image = "button5"

    elif number == 8:
        buttons.image = "button6"

    elif number == 11:
        buttons.image = "button7"
        buttons.x = 807
        buttons.y = 613

    elif number == 13:
        buttons_two.image = "button9"
        buttons.image = "button8"

    elif number == 18:
        buttons.image = "button11"

    elif number == 20:
        go_beetles = "YES"
        buttons.image = "button12"

    elif number == 22:
        buttons.image = "button13"

    #button says "next" unless specified otherwise
    else:
        buttons.image = "button1"
        #coordinates
        buttons.x = 876
        buttons.y = 613

    #change background when first dialogue exchange is over
    if number == 16:
        bg.image = "norm1"
        buttons.image = "button10"

#allow the mouse/main character to move
def mousey_move(number):
    #get global variables
    global mouse_move_timer, chest_timer, draw_key
    #when first dialogue exchange has finished
    if number >= 16:
        #mouse moves left when the player clicks the left arrow on the keyboard
        if keyboard.left:
            #same key on the visual instructions presses down
            keyarrowleft.image = "keyarrowleft_down"
            #coordinates of visual instructions
            keyarrowleft.x = 838
            keyarrowleft.y = 109
            #mouse moves left
            mousey.x -= 5
            #timer for movement animation
            mouse_move_timer += 0.5
            #reset when timer gets too high
            if mouse_move_timer > 4:
                mouse_move_timer = 1
            #flip between two mouse images
            if mouse_move_timer >= 1 and mouse_move_timer <= 2:
                mousey.image = "mouseleft2"
            if mouse_move_timer >= 3 and mouse_move_timer <= 4:
                mousey.image = "mouseleft1"

        #mouse moves right when the player clicks the right arrow on the keyboard
        elif keyboard.right:
            #same key on the visual instructions presses down
            keyarrowright.image = "keyarrowright_down"
            #coordinates of visual instructions
            keyarrowright.x = 950
            keyarrowright.y = 109
            #mouse moves right
            mousey.x += 5
            #timer for movement animation
            mouse_move_timer += 0.5
            #reset when timer gets too high
            if mouse_move_timer > 4:
                mouse_move_timer = 1
            #flip between two mouse images
            if mouse_move_timer >= 1 and mouse_move_timer <= 2:
                mousey.image = "mouseright2"
            if mouse_move_timer >= 3 and mouse_move_timer <= 4:
                mousey.image = "mouseright1"

        if draw_fantasy == "NO":
            #stop mouse from falling through the ground (pushes mouse up by 5 when it's standing on the ground)
            if mousey.colliderect(groundright):
                mousey.y -= 5
            if mousey.colliderect(groundleft):
                mousey.y -= 5
            if mousey.colliderect(groundmiddle):
                mousey.y -= 5

            #left and right ground borders for when mouse falls between the ground
            #so mouse can't go into the ground
            if mousey.colliderect(border_left):
                mousey.x += 5
            if mousey.colliderect(border_right):
                mousey.x -= 5
            if mousey.colliderect(border_midleft):
                mousey.x -= 5
            if mousey.colliderect(border_midright):
                mousey.x += 5

            #borders for the platform in the air (exploration scene/the one with the chest)
            if mousey.colliderect(border_upleft):
                mousey.x -= 5
            if mousey.colliderect(border_upright):
                mousey.x += 5
            if mousey.colliderect(border_upup):
                mousey.y -= 5
            if mousey.colliderect(border_updown):
                mousey.y += 5

        #gravity (mouse is always falling down, so ground needs to push mouse back up by 5)
        mousey.y += 5

    #if mouse falls too far down, reset the scene and put the mouse back into starting position
    if mousey.y > 1000:
        #reset chest
        chest.image = "chest1"
        chest_timer = 0
        #mouse coordinatea
        mousey.x = 36
        mousey.y = 467
        #remove key
        draw_key = "NO"
        #put pole back
        pole.x = 319
        pole.y = 687
        #reset visual instructions
        keyarrowup.image = "keyarrowup1"

    #stop mouse from going beyond the set window dimensions
    if mousey.x <= 25:
        mousey.x = 26
    if mousey.x >= 975:
        mousey.x = 974

#when player presses down a key
def on_key_down(key):
    #if player presses space and mouse is on the ground (no double jumping)
    if key == keys.SPACE and mousey.colliderect(groundleft):
        #mouse jumps
        mousey.y -= 100
        #key on the visual instructions presses down too
        keyspace.image = "keyspace_down"
        #visual instruction coordinates
        keyspace.x = 736
        keyspace.y  = 110
    elif key == keys.SPACE and mousey.colliderect(groundmiddle):
        #mouse jumps
        mousey.y -= 100
        #key on the visual instructions presses down too
        keyspace.image = "keyspace_down"
        #visual instruction coordinates
        keyspace.x = 736
        keyspace.y  = 110
    elif key == keys.SPACE and mousey.colliderect(groundright):
        #mouse jumps
        mousey.y -= 100
        #key on the visual instructions presses down too
        keyspace.image = "keyspace_down"
        #visual instruction coordinates
        keyspace.x = 736
        keyspace.y  = 110
    elif key == keys.SPACE and mousey.colliderect(groundup):
        #mouse jumps
        mousey.y -= 100
        #key on the visual instructions presses down too
        keyspace.image = "keyspace_down"
        #visual instruction coordinates
        keyspace.x = 736
        keyspace.y  = 110

#when player releases a key
def on_key_up(key):
    #when the key is no longer being pressed, visual instructions go back to normal
    if key == keys.SPACE:
        keyspace.image = "keyspace"
        #reset coordinates
        keyspace.x = 736
        keyspace.y = 101

    #when the key is no longer being pressed, visual instructions go back to normal
    if key == keys.RIGHT:
        keyarrowright.image = "keyarrowright"
        #reset coordinates
        keyarrowright.x = 950
        keyarrowright.y = 102

    #when the key is no longer being pressed, visual instructions go back to normal
    if key == keys.LEFT:
        keyarrowleft.image = "keyarrowleft"
        #reset coordinates
        keyarrowleft.x = 838
        keyarrowleft.y = 102

    #up arrow key appears on the visual instuctions when the pole is almost in position
    if pole.y <= 430:
        #when the key is no longer being pressed, visual instructions go back to normal
        if key == keys.UP:
            keyarrowup.image = "keyarrowup2"
            #reset coordinates
            keyarrowup.x = 894
            keyarrowup.y = 46

#allows the mouse to climb up the pole
def mouse_up_pole():
    #if mouse is touching the pole
    if mousey.colliderect(pole):
        #if player pressed up arrow key
        if keyboard.up:
            #make sure mouse doesn't go up in the next scene
            if draw_fantasy == "NO":
                #and if pole is in position
                if pole.y <= 430:
                    #key on visual instructions presses down too
                    keyarrowup.image = "keyarrowup_down"
                    #visual instructions coordinates
                    keyarrowup.x = 894
                    keyarrowup.y = 52
                    #mouse goes up
                    mousey.y -= 10

#animate the exploration scene background
def explore_animate():
    #get global variables
    global number, explore_bg_timer

    #after first dialogue exchange
    if number >= 16:

        #timer for animation
        explore_bg_timer += 0.2
        #reset timer when it gets too high
        if explore_bg_timer > 10:
            explore_bg_timer = 0

        #swap between two backgrounds
        if explore_bg_timer >= 0 and explore_bg_timer <= 5:
            bg.image = "norm1"

        if explore_bg_timer > 5 and explore_bg_timer < 10:
            bg.image = "norm2"

#animate the chest opening
def open_chest():
    #get global variables
    global chest_timer, draw_key

    #if mouse touches chest
    if mousey.colliderect(chest):
        #key appears (or is drawn)
        draw_key = "YES"
        #timer for animating chest
        chest_timer += 0.3
        #reset timer when it gets too high
        if chest_timer > 50:
            chest_timer = 0

        #play four images
        if chest_timer > 0 and chest_timer < 1:
            chest.image = "chest1"
        if chest_timer > 1 and chest_timer < 2:
            chest.image = "chest2"
        if chest_timer > 2 and chest_timer < 3:
            chest.image = "chest3"
        if chest_timer > 3:
            chest.image = "chest4"

#animate the portal spinning
def portal_spin(draw_key):
    #get global variables
    global portal_timer, portal_numbers

    #initialize local variable
    counter = 0

    #if key has appeared(or if the key has been drawn)(or if the player has touched the chest)
    if draw_key == "YES":
        #initialize images list
        portal_images = [0]*9

        #rename each item in list to the names of my image files
        for x in range(len(portal_images)):
            #index goes up
            counter += 1
            portal_images[x] = "portal" + str(counter)

        #timer (to slow animation down)
        portal_timer += 0.2
        #when timer goes up 5 times, reset
        if portal_timer > 1:
            portal_timer = 0

        #index goes up when timer is up
        if portal_timer >= 1:
            portal_numbers += 1

        #index resets (to avoid going out of range)
        if portal_numbers >= 9:
            portal_numbers = 0

        #change image files
        portal.image = portal_images[portal_numbers]

#when key is found (and when beetles come out), close the gaps in the ground
def close_ground():
    #get global variables
    global close_ground_timer, draw_key

    #if key has been found
    if draw_key == "YES":
        #stop moving the ground when the timer is up
        if close_ground_timer < 20:
            close_ground_timer += 0.2

            #move the ground into the middle
            groundleft.x += 1
            groundright.x -= 1

#beetle battle
#after key has been found
def beetles():
    #get global variables
    global beetle_timer, go_beetles, number, chest_timer, draw_text_box2, draw_key, close_ground_timer, after_beetles, cornerbook_move

    #initialize local variable and beetle list
    beetle_list = [0]*6
    numero = 0

    #rename items in the list to my image files
    for x in range(len(beetle_list)):
        numero += 1
        beetle_list[x] = "beetle" + str(numero)

    #when beetles get the signal to start moving
    if go_beetles == "YES":

        #slow beetle movements down using a timer
        beetle_timer += 0.5
        #when timer goes too high, timer resets
        if beetle_timer > 11:
            beetle_timer = 0

        #beetles move/appear randomly (on the ground though, so only x coordinate)
        if beetle_timer%2 == 0:
            beetle1.x = random.randint(560,1000)
            beetle2.x = random.randint(560,1000)
            beetle3.x = random.randint(560,1000)
            beetle4.x = random.randint(560,1000)
            beetle5.x = random.randint(560,1000)
            beetle6.x = random.randint(560,1000)

        #if the mouse touches any of the beetles, everything in the exploration resets
        if mousey.colliderect(beetle1) or mousey.colliderect(beetle2) or mousey.colliderect(beetle3) or mousey.colliderect(beetle4) or mousey.colliderect(beetle5) or mousey.colliderect(beetle6):
            #chest closes
            chest.image = "chest1"
            chest_timer = 0
            #mouse gets put into starting position
            #coordinates
            mousey.x = 36
            mousey.y = 467
            #key disappears
            draw_key = "NO"
            #pole goes back into place
            pole.x = 319
            pole.y = 687
            #visual instructions are reset
            keyarrowup.image = "keyarrowup1"
            #dialogue goes back to before the second dialogue exchange
            number = 16
            draw_text_box2 = "NO"
            #capitalize
            draw_text_box2.upper()
            #ground goes back to where it was originally (before it closed)
            groundleft.x = 5
            groundright.x = 1001
            close_ground_timer = 0

            #beetles are reset
            beetle_timer = 0
            go_beetles = "NO"
            beetle1.x = 1100
            beetle2.x = 1100
            beetle3.x = 1100
            beetle4.x = 1100
            beetle5.x = 1100
            beetle6.x = 1100

        #if the book touches any of the beetkes, they disappear
        if cornerbook.colliderect(beetle1):
            beetle1.y = 1100

        if cornerbook.colliderect(beetle2):
            beetle2.y = 1100

        if cornerbook.colliderect(beetle3):
            beetle3.y = 1100

        if cornerbook.colliderect(beetle4):
            beetle4.y = 1100

        if cornerbook.colliderect(beetle5):
            beetle5.y = 1100

        if cornerbook.colliderect(beetle6):
            beetle6.y = 1100

        #when all beetles are defeated
        if beetle6.y == 1100 and beetle5.y == 1100 and beetle4.y == 1100 and beetle3.y == 1100 and beetle2.y == 1100 and beetle1.y == 1100:
            #the book goes back into the corner
            cornerbook.x = 55
            cornerbook.y = 52
            #the beetles can't move
            go_beetles = "NO"
            cornerbook_move = "NO"
            #the aftermath dialogue exchange begins
            after_beetles = "YES"

#changes scenes when player goes into the portal
def in_portal():
    #get global variables
    global number, draw_fantasy

    #after the third dialogue exchange
    if number >= 22:
        if draw_fantasy == "NO":
            if mousey.colliderect(portal):
                mousey.y -= 20
                draw_fantasy = "YES"

#set boundaries for the fantasy scene
def fantasy_boundaries():
    if draw_fantasy == "YES":
        bg.image = "fantasy1"

        if mousey.colliderect(fantasy_ground):
            mousey.y -= 5

        if mousey.colliderect(fantasy_borderleft):
            mousey.x -=5

        if mousey.colliderect(fantasy_borderright):
            mousey.x += 5
            mousey.y -= 5

#animate fantasy scene background
def fantasy_background():
    #get global variables
    global number, fantasy_bg_timer, last_scene

    #after second dialogue exchange
    if draw_fantasy == "YES":

        #timer for animation
        fantasy_bg_timer += 0.2
        #reset timer when it gets too high
        if fantasy_bg_timer > 10:
            fantasy_bg_timer = 0

        #swap between two backgrounds
        if fantasy_bg_timer >= 0 and fantasy_bg_timer <= 5:
            bg.image = "fantasy1"

        if fantasy_bg_timer > 5 and fantasy_bg_timer < 10:
            bg.image = "fantasy2"

        if mousey.colliderect(fantasy_door):
            last_scene = "YES"

#final scene function (after the fantasy door scene)
def final():
    #get global variables
    global last_scene, snake_timer, theend

    #when player enters the door
    if last_scene == "YES":

        #initialize lists
        snake_images = [0]*18
        fade_images = [0]*18
        number_list = [0]*18
        #initialize local variables
        numero = 0
        counter = 0

        #fixed mouse coordinates (player can't move)
        mousey.x = 149
        mousey.y = 271

        #rename items in list so they match the names of the image files
        for x in range(18):
            numero += 1
            #rename
            snake_images[x] = "snake" + str(numero)
            fade_images[x] = "fade" + str(numero)

        #reset for reuse
        numero = 0

        #get a list of numbers 1-18
        for i in range(len(number_list)):
            numero += 1
            number_list[i] = numero

        #reset for reuse
        numero = 0

        #animate
        #when player clicks page, page flips
        for x in range(17):
            #timer to slow the flipping down
            snake_timer += 0.1
            #when timer goes up 5 times, index can rise once (slowing the flipping down)
            if snake_timer > number_list[numero]:
                numero += 1

        #animate the snake and the fade overtop of the snake
        for x in range(len(snake_images)):
            #image changes
            bg.image = snake_images[numero]
            fade.image = fade_images[numero]

            #when the fade is over, the last image is drawn
            if fade.image == "fade18":
                theend = "YES"








