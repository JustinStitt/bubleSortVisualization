import pygame
import sys
import random
import time
import datetime
pygame.init()

size = (750,750)
window = pygame.display.set_mode(size)
window_fill_color = pygame.Color(240,240,239)
pygame.display.set_caption('Bubble Sort Visualization | Justin Stitt')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial',30)


#LIST TO BUBBLE SORT
#nums = [4,8,2,1,9,6,10,3,5,7]
#nums = [7,6,15,11,2,9,10,8,5,3]

nums = []
##LIST OF VISUAL SLOTS
slots = []
old_time = time.time()
done = False
first_run = True
last_pos = [0,0]
spacing = 20
offset = 10

class Slot():
    def __init__(self,pos,index,value,color = 0):
        self.color = color
        self.draw_color = pygame.Color(0,0,0)
        self.determine_color()
        self.index = index
        self.value = value
        self.pos = pos #[x,y]
        self.pos[1] -= (offset*self.value)# accounting for offset in height in accordance to its value

        self.w = 10
        self.h = 50 + (offset*self.value)#making the height smaller the smaller its value is
    def determine_color(self):
        if self.color == 1:
            pass
            #self.draw_color = pygame.Color(255,0,0)
    def update(self):
        spacing = 20 / (1 + (len(nums)/125))
        self.value = nums[self.index]
        self.pos[0] = 5 + self.index * spacing
        self.h = 50 + (offset*self.value)
        self.pos[1] = (size[1]) - (offset*self.value)
        pass

    def render(self):
        pygame.draw.rect(window,self.draw_color,pygame.Rect(self.pos[0],self.pos[1],self.w,self.h))
        #bubble_sort(nums)
        #print("I am in render my index is: {}, and my position is: {}, and my value is: {}, and my height is: {}".format(self.index,self.pos,self.value,self.h))

def generate_nums(list_to_gen,length,low,high):
    if (high - low) < length:
        raise ValueError('There must be enough possible unique random integers in range (low,high), Try lowering length')
        return

    for x in range(length):
        rand = random.randint(low,high)
        if rand not in list_to_gen:
            list_to_gen.append(rand)
    print(list_to_gen)
    return list_to_gen

nums = generate_nums(nums,90,2,100)


def bubble_sort(nums,last_x = 0,last_y = 0):
    global slots
    global old_time
    last_position = [0,0]
    #print(nums)



    if last_y == len(nums) - 2 - last_x:
        last_y = 0
        last_x += 1

    for x in range(last_x,len(nums),1):

        for y in range(last_y,len(nums) - 1,1):
            last_y = y

            if nums[y] > nums[y+1]:
                temp = nums[y]
                nums[y] = nums[y+1]
                nums[y+1] = temp


                last_position = [last_x,last_y]
                return(last_position)
            else:
                token = 0
                for z in range(last_y,len(nums)-1,1):
                    if nums[z] < nums[z+1]:
                        token += 1
                if token == (len(nums) - 1) - last_y:
                    last_y = 0
                    last_position = [last_x,last_y]

                    return(last_position)


                #print(last_position)
                #break
            #flabreak





def check_if_done(slots):
    global spacing
    token = 0
    for x in range(len(slots) - 1):
        if slots[x].value <= slots[x+1].value:
            token += 1
            #print(token)
    if token == len(slots) - 1:
        print("Sim Complete")
        pygame.quit()
        sys.exit()
def create_slots(n):
    global slots
    global nums
    for x in range(n):
        value = nums[x]
        slots.append(Slot( [15 + x * spacing,size[1]/1.3] ,x,value))
        #print('created a slot at: {}, with pos[0] of: {}, and pos[1] of: {}'.format(x,slots[x].pos[0],slots[x].pos[1]))

create_slots(len(nums))



def update():
    global slots
    global nums
    global done
    global old_time
    global first_run
    global last_pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting...')
            pygame.time.wait(5)
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                slots[0].pos[0] += 25

    if first_run == True:
        #print('ran : {}'.format(first_run))
        last_pos = bubble_sort(nums)
        #print(last_pos)
        first_run = False
        old_time = time.time()
    elif time.time() - old_time > 0:
        old_time = time.time()
        print(last_pos)
        last_pos = bubble_sort(nums,last_pos[0],last_pos[1])
        slots[last_pos[1]+1].draw_color = pygame.Color(175,67,81)
    elif time.time() - old_time > 0.075:
        slots[last_pos[1]+1].draw_color = pygame.Color(0,0,0)




    check_if_done(slots)



    #Slot updating

    for x in range(len(slots)):
        slots[x].update()



def render():
    global slots
    #Slot rendering
    for x in range(len(slots)):
        slots[x].render()





while True:
    window.fill(window_fill_color)

    update()
    render()

    pygame.display.flip()
    clock.tick(9999)
