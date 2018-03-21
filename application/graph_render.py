import graphviz as gv
import string

position_map_reverse = {a: b for a, b in
                zip([(i, j) for i in range(0, 3) for j in range(0, 5)], [s for s in string.ascii_uppercase[0:24]])}

def render(s):
    g1=gv.Graph(format='svg')
    current_node=s.start_node
    g1.node(str(id(current_node)), label="Start")
    open_list=[]
    c=True
    while(c):
        for n in current_node.children:
            open_list.append(n)
            g1.node(str(id(n)),label=str(n.h))
            g1.edge(str(id(current_node)), str(id(n)),label=position_map_reverse[n.past_moves[len(n.past_moves)-1]])
        if len(open_list)!=0:
            current_node=open_list[len(open_list)-1]
            open_list.pop()
        else:
            c=False



    g1.render('graphs/ss.gv')


