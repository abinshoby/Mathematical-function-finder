
from sympy import *
import matplotlib.pyplot as plt
def get_straight_line(x1,y1,x2,y2):
    max_y=100000
    p1,p2=Point(x1,y1),Point(x2,y2)
    slope=Segment(p1,p2).slope

    inter=Line(p1,p2).intersection(Line(Point(0,0),Point(0,max_y)))
    inter=inter[0][1]
    x=symbols('x')
    expr=slope*x+inter
    # f=lambdify(x,expr)
    f=expr
    # print(slope,inter)
    return f
def form_equation(x_pts,y_pts):
    lines=[]
    domains=[]
    for i in range(len(x_pts)-1):
        lines.append(get_straight_line(x_pts[i],y_pts[i],x_pts[i+1],y_pts[i+1]))
        domains.append((x_pts[i],x_pts[i+1]))
    x=symbols('a')
    expr=0
    divid=0
    for i in range(len(lines)):
        f=lines[i]
        dd=1
        for d in domains:
            
            if(not(d[0]==domains[i][0] and d[1]==domains[i][1])):
                for v in range(d[0],d[1]):
                    pp=x-v
                    if(lines[i]-pp!=0):
                        f=f*(x-v)
                        dd=dd*(x-v)
        divid=divid+dd
        expr=expr+f
    return (expr,divid)
def visual(origx,origy,compx,compy):
    plt.plot(origx,origy,label='Original')
    plt.plot(compx,compy,label='Computed')
    plt.xlabel('b')
    plt.ylabel('S(b)/S(0)')
    plt.legend()
    plt.show()
    #plt.savefig(name+'.png')
    plt.close()


x=[i for i in range(10)]
y=[i**2 for i in range(10)]
expr,divid=form_equation(x,y)
eq=expr/divid

eq=simplify(simplify(eq,rational=True),rational=True)
#X=symbols('x')
#print(simplify(X**2-eq,rational=True))
print(simplify(eq.subs('x',2),rational=True))

# print(limit(eq,'x',))
x=x[:len(x)-1]
y=y[:len(y)-1]
compy=[eq.subs('x',i).subs('a',i) for i in x]
visual(x,y,x,compy)
