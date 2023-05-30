import heapq
from queue import Queue
from queue import PriorityQueue
from tkinter import*
from PIL import Image, ImageTk
windows = Tk()
windows.configure(bg='black')
windows.title('Romania Map')
windows.minsize(900, 600)

myImg = Image.open(r'C:\Users\SLIM 7\Downloads\R.jpg')
resizedImg = myImg.resize((500, 500))
img = ImageTk.PhotoImage(resizedImg)
imgLabel = Label(image=img)
imgLabel.pack()
label1 = Label(text='WELCOME TO ROMANIA', font=("Helvetica", 20))
label1.pack(pady=20)
label1.configure(bg='black', fg='white')
label2 = Label(text='Enter Your Current City', font=("Helvetica", 12))
label2.pack(pady=10)
label2.configure(bg='black', fg='white')
current = Entry()
current.pack()
label3 = Label(text='Enter Your Destination', font=("Helvetica", 12))
label3.pack(pady=10)
label3.configure(bg='black', fg='white')
target = Entry()
target.pack()
# Romania map graph representation
romaniaMap = { 
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
  'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
    }

graph = {
'Arad': [('Sibiu', 140),
         ('Zerind', 75),
         ('Timisoara', 118)],
    'Zerind': [('Arad', 75),
               ('Oradea', 71)],
    'Oradea': [('Zerind', 71),
               ('Sibiu', 151)],
    'Sibiu': [('Arad', 140),
              ('Oradea', 151),
              ('Fagaras', 99),
              ('Rimnicu Vilcea', 80)], 
    'Timisoara': [('Arad', 118),
                  ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111),
              ('Mehadia', 70)],  
    'Mehadia': [('Lugoj', 70), 
                ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75),
                ('Craiova', 120)], 
    'Craiova': [('Drobeta', 120),
                ('Rimnicu Vilcea', 146),
                ('Pitesti', 138)], 
    'Rimnicu Vilcea': [('Sibiu', 80),
                       ('Craiova', 146),
                       ('Pitesti', 97)], 
    'Fagaras': [('Sibiu', 99),
                ('Bucharest', 211)], 
    'Pitesti': [('Rimnicu Vilcea', 97),
                ('Craiova', 138), 
                ('Bucharest', 101)], 
    'Bucharest': [('Fagaras', 211),
                  ('Pitesti', 101),
                  ('Giurgiu', 90),
                  ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)], 
    'Urziceni': [('Bucharest', 85),
                 ('Vaslui', 142), 
                 ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98),
                ('Eforie', 86)], 
    'Eforie': [('Hirsova', 86)],  
    'Vaslui': [('Iasi', 92), 
               ('Urziceni', 142)], 
    'Iasi': [('Vaslui', 92),
             ('Neamt', 87)],  
    'Neamt': [('Iasi', 87)]}

un_weighted_graph = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],  
    'Zerind': ['Arad', 'Oradea'], 
    'Oradea': ['Zerind', 'Sibiu'], 
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],  
    'Mehadia': ['Lugoj', 'Drobeta'],  
    'Drobeta': ['Mehadia', 'Craiova', ],   
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],  
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],  
    'Fagaras': ['Sibiu', 'Bucharest'], 
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],  
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],  
    'Giurgiu': ['Bucharest'], 
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'], 
    'Hirsova': ['Urziceni', 'Eforie'],    
    'Eforie': ['Hirsova'],    
    'Vaslui': ['Iasi', 'Urziceni'],  
    'Iasi': ['Vaslui', 'Neamt'],    
    'Neamt': ['Iasi']}

def BFS(graph, start, goal):    visited = set()    visited.add(start)    queue = []    # to store parent of every node    path = []    parents = {}    queue.append(start)    while queue: # Creating loop to visit each node        # remove first element
        node = queue.pop(0)        neighbours = graph.get(node)        for neighbour in neighbours:            if neighbour == goal:                parents[neighbour] = node                path.append(neighbour)                while parents.get(neighbour):                    # append parent                    path.append(parents[neighbour])                    # get to the next child in the shortest path                    neighbour = parents[neighbour]                path.reverse()                print(path)                return path
            if neighbour not in visited:                visited.add(neighbour)                # add neighbour to end                queue.append(neighbour)                parents[neighbour] = node
def DFS(graph, start, goal):    visited = set()    visited.add(start)    stack = [start]    # to store parent of every node    path = []    parents = {}    while stack: # Creating loop to visit each node        # remove first element        node = stack.pop()        neighbours = graph.get(node)        for neighbour in neighbours:            if neighbour == goal:                parents[neighbour] = node                path.append(neighbour)                while parents.get(neighbour):                    # append parent                    path.append(parents[neighbour])                    # get to the next child in the shortest path                    neighbour = parents[neighbour]                path.reverse()                print(path)                return path
            if neighbour not in visited:                visited.add(neighbour)                # add neighbour to end                stack.append(neighbour)                parents[neighbour] = node
def path_cost(path):    total_cost=0    for (node,cost) in path:        total_cost+=cost    last_node=path[-1][0]    return total_cost,last_node
def UCS(graph,start,goal):    visited=[]    queue=[[(start,0)]]    while queue:        queue.sort(key=path_cost)        path=queue.pop(0)        #print(path) #if you want to see steps        node=path[-1][0]        if node not in visited:            visited.append(node)            if node == goal:                return path            else:                adjacent_nodes=graph.get(node,[])                for(node2,cost) in adjacent_nodes:                    new_path=path.copy()                    new_path.append((node2,cost))                    queue.append(new_path)def path_f_cost(path):    g_cost=0    for (node,cost) in path:        g_cost+=cost    last_node=path[-1][0]    h_cost=H_table[last_node]    f_cost=h_cost+g_cost    return f_cost,last_node
def path_Astar(path):    g_cost=0    for (node,cost) in path:        g_cost+=cost    last_node=path[-1][0]    h_cost=H_table[last_node]    f_cost=h_cost+g_cost    return f_cost,last_node
def A_star(graph,start,goal):    visited=[]    queue=[[(start,0)]]    while queue:        queue.sort(key=path_f_cost)        path=queue.pop(0)        #print(path) #if you want to see steps        node=path[-1][0]        if node not in visited:            visited.append(node)            if node == goal:                return path            else:                adjacent_nodes=graph.get(node,[])                for(node2,cost) in adjacent_nodes:                    new_path=path.copy()                    new_path.append((node2,cost))                    queue.append(new_path)                def path_h_cost(path):       gcoast=0    for (node,cost) in path:        gcoast+=cost    lastnode=path[-1][0]    h_coast=H_table[lastnode]    return h_coast,lastnode

def greedy(graph,start,goal):    visited=[]    queue=[[(start,0)]]    while queue:        queue.sort(key=path_h_cost)                path=queue.pop(0)             node=path[-1][0]                     if node not in visited:            visited.append(node)            if node == goal:                return path            else:                adjacent_nodes=graph.get(node,[])                for(node2,cost) in adjacent_nodes:                    new_path=path.copy()                    new_path.append((node2,cost))                    queue.append(new_path)


def greedy_button_on_click():    start = current.get()    end = target.get()    path = str(greedy(graph, start, end))    result = Label(text = "= "+path).pack()
def bfs_button_on_click():    start = current.get()    end = target.get()    path = str(BFS(un_weighted_graph, start, end))    result = Label(text = "= "+path).pack()
def dfs_button_on_click():    start = current.get()    end = target.get()    path = str(DFS(un_weighted_graph, start, end))    result = Label(text = "= "+path).pack()
def ucs_button_on_click():    start = current.get()    end = target.get()    path = str(UCS(graph, start, end))    result = Label(text = "= "+path).pack()            def a_star_button_on_click():    start = current.get()    end = target.get()    path = str(A_star(graph, start, end))    result = Label(text = "= "+path).pack()
    
bfs_button = Button(windows, text="BFS", command=bfs_button_on_click)bfs_button.pack()
dfs_button = Button(windows, text="DFS", command=dfs_button_on_click)dfs_button.pack()
ucs_button = Button(windows, text="UCS", command=ucs_button_on_click)ucs_button.pack()
a_star_button = Button(windows, text="A*", command=a_star_button_on_click)a_star_button.pack()
greedy_button = Button(windows, text="Greedy", command=greedy_button_on_click)greedy_button.pack()
windows.mainloop()