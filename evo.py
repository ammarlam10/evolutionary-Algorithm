# Created By: Muhammad Ammar Ahmed 09389
# Running this program will output 12 graphs, 1st 6 will contain avg_avg fitness and avg_best fitness of Function 1
# and last 6 will produce for function 2.
# ------------------------------------------
# The values printed on the console are average average fitness of 40 generations and average best fitness of
# of 40 generations
# ------------------------------------------
# I have used the following nested structure to store values: A dictionary containing a list of 3 elements against every
# key. The elements of the list are [x,y,fitness] for each chromosome
# -----------------------------------------

from random import randint
import matplotlib.pyplot as plt
# import csv
import random

def initialPopulation(size,f):
    # initializes population as per
    list={}
    if(f==1):
        for a in range(0,size,1):
            list[a]=[float(randint(-5,5)),float(randint(-5,5))]

    else:
        for a in range(0,size,1):
            list[a]=[float(randint(-2,2)),float(randint(-1,3))]
    return list

def computeFitness(pop,f):
    if(f==1):
        for k in pop:
            if(len(pop[k])==2):
                pop[k].append((pop[k][0]**2)+ (pop[k][1]**2))
                # pop[k].append((100*((pop[k][0]**2)-(pop[k][1]))**2) + (1-(pop[k][0])**2))
            else:
                pop[k][2]= (pop[k][0]**2)+ (pop[k][1]**2)

    else:
        for k in pop:
                if(len(pop[k])==2):
                    # pop[k].append((pop[k][0]**2)+ (pop[k][1])**2)
                    pop[k].append((100*((pop[k][0]**2)-(pop[k][1]))**2) + (1-(pop[k][0])**2))
                else:
                    # pop[k][2]= (pop[k][0]*pop[k][0])+ (pop[k][1])*(pop[k][1])
                    pop[k][2]= (100*((pop[k][0]**2)-(pop[k][1]))**2) + (1-(pop[k][0])**2)
    return pop


def offspring(pop,xu,yu,xl,yl):
    iter = len(pop)
    i=0
    while i<iter:
        # pri/nt i
        prob=randint(0,10)  # print i
        if(prob>=9):
            if(pop[i][0]<xu)and(pop[i][0]>xl):
                # print "mutate x"
                temp=pop[i][0]
                pop[i]=[pop[i+1][0]+random.uniform(-.25, .25),pop[i][1],pop[i][2]]
                pop[i+1]=[temp,pop[i+1][1],pop[i+1][2]]
                # print pop[i]
            else:
                temp=pop[i][0]
                pop[i]=[pop[i+1][0],pop[i][1],pop[i][2]]
                pop[i+1]=[temp,pop[i+1][1],pop[i+1][2]]

        elif(prob>=7):
            if(pop[i][1]<yu)and(pop[i][1]>yl):
                # print "mutate y"
                temp=pop[i][0]
                pop[i]=[pop[i+1][0],pop[i][1],pop[i][2]]
                pop[i+1]=[temp,pop[i+1][1]+random.uniform(-.25, .25),pop[i+1][2]]
                # print pop[i]
        else:
            temp=pop[i][0]
            pop[i]=[pop[i+1][0],pop[i][1],pop[i][2]]
            pop[i+1]=[temp,pop[i+1][1],pop[i+1][2]]

        i+=2
    # print pop
    return pop



def rbs(pop, num):
    # print pop
    for i in range(len(pop)):
        for j in range(len(pop)-1-i):
                if pop[j][2] > pop[j+1][2]:
                        pop[j], pop[j+1] = pop[j+1], pop[j]
    total=0
    # print pop
    for i in pop:
        total+=i+1
    # print total
    rel_rank = [(f+1)/float(total) for f in pop]
    probs = [sum(rel_rank[:i+1]) for i in range(len(rel_rank))]
    # print rel_rank
    # print probs
    new_pop={}
    for n in range(num):
        r=random.random()
        for p in pop:
            if(r<=probs[p]):
                new_pop.update({n:pop[p]})
                break


    return new_pop




def roulette_select(pop, num):
    total=0
    for i in pop:
        total+=pop[i][2]
    rel_fitness = [pop[f][2]/float(total) for f in pop]
    probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    new_pop = {}
    for n in range(num):
        r=random.random()
        for p in pop:
            if(r<=probs[p]):
                new_pop.update({n:pop[p]})
                break
    return new_pop

def binarytour(pop,num):
    new_pop={}
    count=0
    for i in range(num):
        r1=randint(0,len(pop)-1)
        r2=randint(0,len(pop)-1)
        if(pop[r1][2]>=pop[r2][2]):
            new_pop.update({(i):pop[r1]})
        else:
            new_pop.update({(i):pop[r2]})

    # print new_pop
    return new_pop

def truncation(pop,percent,size):
    for i in range(len(pop)):
        for j in range(10-1-i):
                if pop[j][2] < pop[j+1][2]:
                        pop[j], pop[j+1] = pop[j+1], pop[j]
    prop=percent*len(pop)/100 # 10*20/100
    # print prop
    repeat=size/prop
    # print repeat
    new_pop={}
    k=0
    for i in range(repeat):
        for j in range(prop):
            new_pop[k]=pop[j]
            k+=1
    # print new_pop
    return new_pop

def combine(pop,ofs):
    new={}
    # print ofs
    # print pop

    for i in range(len(ofs)):
        new[i]=ofs[i]
    j=0
    for i in range(len(ofs),len(pop)+len(ofs)):
        # print j
        # print pop[j]
        new[i]=pop[j]
        j+=1
    return new

def average(pop):
    fitness = [pop[f][2] for f in pop]
    return sum(fitness)/len(fitness)
def best(pop):
    fitness = [pop[f][2] for f in pop]
    return max(fitness)
# def avg_plot(plot):
#     plot[][]
#


# STEP 1

def rbs_trunc(run,xu,yu,xl,yl,f):
    p=initialPopulation(10,f)
    p=computeFitness(p,f)
    t_plot=[]
    for i in range(10):
          plot={}
          p=initialPopulation(10,f)
          p=computeFitness(p,f)
          for i in range(run):
                select = rbs(p,10)
                select=computeFitness(select,f)
                ofs=offspring(select,xu,yu,xl,yl)
                ofs=computeFitness(ofs,f)
                # print ofs

                # ofs=computeFitness(ofs)
                total=combine(ofs,p)
                p=truncation(total,20,10)
                plot[i]=[average(p),best(p)]
                if(i==39):
                    print "------------------------"
                    print plot
                    print "-------------------------"

          t_plot.append(plot)
    # print t_plot
    avg_plot=[]
    best_plot=[]


    for i in range(len(t_plot[0])):
        atemp=[]
        btemp=[]
        for j in range(len(t_plot)):
            atemp.append(t_plot[j][i][0])
            btemp.append(t_plot[j][i][1])
        avg_plot.append(sum(atemp)/len(atemp))
        best_plot.append(sum(btemp)/len(atemp))

    print "average average fitness"
    print avg_plot
    print "average best fitness"
    print best_plot
    line_up, = plt.plot(best_plot, label='Best')
    line_down, = plt.plot(avg_plot, label='Average')
    plt.legend([line_up, line_down], ['Best', 'Average'])
    plt.title("RBS with Truncation")
    plt.show()    # plt.show()

def fps_trunc(run,xu,yu,xl,yl,f):
    p=initialPopulation(10,f)
    p=computeFitness(p,f)
    t_plot=[]
    for i in range(10):
          plot={}
          p=initialPopulation(10,f)
          p=computeFitness(p,f)
          for i in range(run):
                select = roulette_select(p,10)
                select=computeFitness(select,f)
                ofs=offspring(select,xu,yu,xl,yl)
                ofs=computeFitness(ofs,f)
                total=combine(ofs,p)
                p=truncation(total,20,10)
                plot[i]=[average(p),best(p)]
          t_plot.append(plot)
    # print t_plot
    avg_plot=[]
    best_plot=[]
    for i in range(len(t_plot[0])):
        atemp=[]
        btemp=[]
        for j in range(len(t_plot)):
            atemp.append(t_plot[j][i][0])
            btemp.append(t_plot[j][i][1])
        avg_plot.append(sum(atemp)/len(atemp))
        best_plot.append(sum(btemp)/len(atemp))
    print "average average fitness"
    print avg_plot
    print "average best fitness"
    print best_plot
    line_up, = plt.plot(best_plot, label='Best')
    line_down, = plt.plot(avg_plot, label='Average')
    plt.legend([line_up, line_down], ['Best', 'Average'])
    # plt.show()
    plt.title("FPS with Truncation")
    plt.show()

def bin_trunc(run,xu,yu,xl,yl,f):
    p=initialPopulation(10,f)
    p=computeFitness(p,f)
    t_plot=[]
    for i in range(run):
          plot={}
          p=initialPopulation(10,f)
          p=computeFitness(p,f)
          for i in range(40):
                select = binarytour(p,10)
                select=computeFitness(select,f)
                ofs=offspring(select,xu,yu,xl,yl)
                ofs=computeFitness(ofs,f)
                total=combine(ofs,p)
                p=truncation(total,20,10)
                plot[i]=[average(p),best(p)]
          t_plot.append(plot)
    # print t_plot
    avg_plot=[]
    best_plot=[]
    for i in range(len(t_plot[0])):
        atemp=[]
        btemp=[]
        for j in range(len(t_plot)):
            atemp.append(t_plot[j][i][0])
            btemp.append(t_plot[j][i][1])
        avg_plot.append(sum(atemp)/len(atemp))
        best_plot.append(sum(btemp)/len(atemp))
    print "average average fitness"
    print avg_plot
    print "average best fitness"
    print best_plot
    line_up, = plt.plot(best_plot, label='Best')
    line_down, = plt.plot(avg_plot, label='Average')
    plt.legend([line_up, line_down], ['Best', 'Average'])
    # plt.show()
    plt.title("Binary Tournament with Truncation")
    plt.show()

def fps_bin(run,xu,yu,xl,yl,f):
    p=initialPopulation(10,f)
    p=computeFitness(p,f)
    t_plot=[]
    for i in range(10):
          plot={}
          p=initialPopulation(10,f)
          p=computeFitness(p,f)
          for i in range(run):
                select = roulette_select(p,10)
                select=computeFitness(select,f)
                ofs=offspring(select,xu,yu,xl,yl)
                ofs=computeFitness(ofs,f)
                total=combine(ofs,p)
                p=binarytour(total,10)
                plot[i]=[average(p),best(p)]
          t_plot.append(plot)
    # print t_plot
    avg_plot=[]
    best_plot=[]
    for i in range(len(t_plot[0])):
        atemp=[]
        btemp=[]
        for j in range(len(t_plot)):
            atemp.append(t_plot[j][i][0])
            btemp.append(t_plot[j][i][1])
        avg_plot.append(sum(atemp)/len(atemp))
        best_plot.append(sum(btemp)/len(atemp))
    print "average average fitness"
    print avg_plot
    print "average best fitness"
    print best_plot
    line_up, = plt.plot(best_plot, label='Best')
    line_down, = plt.plot(avg_plot, label='Average')
    plt.legend([line_up, line_down], ['Best', 'Average'])
    # plt.show()
    plt.title("FPS with Binary Tournament")
    plt.show()

def rbs_bin(run,xu,yu,xl,yl,f):
    p=initialPopulation(10,f)
    p=computeFitness(p,f)
    t_plot=[]
    for i in range(run):
          plot={}
          p=initialPopulation(10,f)
          p=computeFitness(p,f)
          for i in range(40):
                select = rbs(p,10)
                select=computeFitness(select,f)
                ofs=offspring(select,xu,yu,xl,yl)
                ofs=computeFitness(ofs,f)
                total=combine(ofs,p)
                p=binarytour(total,10)
                plot[i]=[average(p),best(p)]
          t_plot.append(plot)
    # print t_plot
    avg_plot=[]
    best_plot=[]
    for i in range(len(t_plot[0])):
        atemp=[]
        btemp=[]
        for j in range(len(t_plot)):
            atemp.append(t_plot[j][i][0])
            btemp.append(t_plot[j][i][1])
        avg_plot.append(sum(atemp)/len(atemp))
        best_plot.append(sum(btemp)/len(atemp))
    print "average average fitness"
    print avg_plot
    print "average bset fitness"
    print best_plot
    line_up, = plt.plot(best_plot, label='Best')
    line_down, = plt.plot(avg_plot, label='Average')
    plt.legend([line_up, line_down], ['Best', 'Average'])
    # plt.show()
    plt.title("RBS with Binary Tournament")
    plt.show()

def bin_bin(run,xu,yu,xl,yl,f):
    # p=initialPopulation(10)
    # p=computeFitness(p)
    t_plot=[]
    for i in range(10):
          plot={}
          p=initialPopulation(10,f)
          p=computeFitness(p,f)
          for i in range(run):
                select = binarytour(p,10)
                select=computeFitness(select,f)
                ofs=offspring(select,xu,yu,xl,yl)
                ofs=computeFitness(ofs,f)
                total=combine(ofs,p)
                p=binarytour(total,10)
                plot[i]=[average(p),best(p)]
          t_plot.append(plot)
    # print t_plot
    avg_plot=[]
    best_plot=[]
    for i in range(len(t_plot[0])):
        atemp=[]
        btemp=[]
        for j in range(len(t_plot)):
            atemp.append(t_plot[j][i][0])
            btemp.append(t_plot[j][i][1])
        avg_plot.append(sum(atemp)/len(atemp))
        best_plot.append(sum(btemp)/len(atemp))
    print "average average fitness"
    print avg_plot
    print "average best fitness"
    print best_plot
    line_up, = plt.plot(best_plot, label='Best')
    line_down, = plt.plot(avg_plot, label='Average')
    plt.legend([line_up, line_down], ['Best', 'Average'])
    plt.title("Binary Tournament with Binary Tournament")
    plt.show()




                                             # 1st FUNCTION


rbs_trunc(40,5,5,-5,-5,1) # arguments are (total runs, x upperboud, y upperbound,x lower bound, y lower bound, function)
fps_trunc(40,5,5,-5,-5,1)
bin_trunc(40,5,5,-5,-5,1)
fps_bin(40,5,5,-5,-5,1)
rbs_bin(400,5,5,-5,-5,1)
bin_bin(40,5,5,-5,-5,1)

                                             # 2nd FUNCTION


rbs_trunc(40,2,3,-2,-1,2) # arguments are (total runs, x upperboud, y upperbound,x lower bound, y lower bound, function)
fps_trunc(40,2,3,-2,-1,2)
bin_trunc(40,2,3,-2,-1,2)
fps_bin(40,2,3,-2,-1,2)
rbs_bin(40,2,3,-2,-1,2)
bin_bin(40,2,3,-2,-1,2)
