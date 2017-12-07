import numpy as np

pre_amble = ""
tex_src = ""
tex_body = ""

pre_amble = pre_amble + "% Now generating" + "\n"
pre_amble = pre_amble +  "\documentclass{article}" + "\n"
pre_amble = pre_amble +  "\usepackage{tikz}" + "\n"
pre_amble = pre_amble +  "\usetikzlibrary{shapes, arrows, decorations.pathmorphing}" + "\n"
pre_amble = pre_amble + "\\begin{document}" + "\n"
pre_amble = pre_amble + "\\begin{tikzpicture}[ >=stealth', pos = .8, photon/.style={decorate, decoration = {snake, post length = 1mm}}]" + "\n"
pre_amble = pre_amble + "\\draw [step = 1cm, gray, very thin] (-7, -7) grid (7,7);" + "\n"

def draw_circle(x,y,r, unit = "cm"):
    
    latex_command = "\\draw (" + str(x) +"," + str(y) + ") circle [radius = " + str(r) + unit + "];"  + "\n"

    return latex_command

def draw_circle_with_arrow(x, y, r, arrow_l, angle):

    tmp_latex_command = draw_circle(x,y,r)

    x_b_arrow = x + r*np.cos(angle) 
    y_b_arrow = y + r*np.sin(angle) 

    x_e_arrow = x_b_arrow + arrow_l*np.cos(angle)
    y_e_arrow = y_b_arrow + arrow_l*np.sin(angle)

    
    latex_arrow_command = "\\draw [->, thick] (" + str(x_b_arrow) + "," + str(y_b_arrow) + ") -- (" + str(x_e_arrow) + "," + str(y_e_arrow) + ");\n" 

    return tmp_latex_command + latex_arrow_command

def draw_arrow(x1, y1, arrow_l, angle):

    x_e_arrow = x1 + arrow_l*np.cos(angle)
    y_e_arrow = y1 + arrow_l*np.sin(angle)
    
    latex_arrow_command = "\\draw [->, thick] (" + str(x1) + "," + str(y1) + ") -- (" + str(x_e_arrow) + "," + str(y_e_arrow) + ");\n" 

    return latex_arrow_command



#tex_body = tex_body + draw_circle(2,2,0.1)
#tex_body = tex_body + draw_circle_with_arrow(0,0,0.1,1,90)
tex_body = tex_body + draw_circle(0,0,0.5)
tex_body = tex_body + draw_circle(-4,0,0.5)
tex_body = tex_body + draw_circle_with_arrow(-6,0,0.1,0.5,0)

#tex_body = tex_body + draw_circle(-2,3,0.5)
tex_body = tex_body + draw_circle_with_arrow(-1.5,4.2,0.1,0.5,np.pi/4)
tex_body = tex_body + draw_circle_with_arrow(-2,3,0.5,0.3,-np.pi/4)
#tex_body = tex_body + "\draw[->, photon] (0,0) -- node[above left] {$SV$} (60:2);"
#tex_body = tex_body + draw_arrow(0,1,5,np.pi/4)

tex_body = tex_body + draw_circle_with_arrow(-2,-3,0.5,0.3,-np.pi/4)
tex_body = tex_body + draw_circle_with_arrow(-3,-2,0.1,0.5,np.pi/1.5)

tex_body = tex_body + "\draw[->, photon] (-2,-1) -- node[above] {$\gamma$} (60:2);"

post_amble = "\\end{tikzpicture}" + "\n"
post_amble = post_amble + "\\end{document}"

f = open("output_tex.tex", "w")
f.write(pre_amble + tex_body + post_amble)
f.close()
