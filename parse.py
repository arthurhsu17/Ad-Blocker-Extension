file_input = open("domainsblockraw.txt", "r")
file_output= open("blockedsites.js","w")

line = file_input.readline()
file_output.write("var blocked_sites = [\n")

initial = True
while(line):
    if("127.0.0.1 " not in line): 
        if not initial:
            file_output.write(",\n")
        initial= False
        line = (line.lstrip("127.0.0.1 ")).rstrip("]\n")
        new_line = "*://*." + line + "/*"
        file_output.write("\""+ new_line + "\"")
    line = file_input.readline()

file_output.write("]")
file_output.close()
file_input.close()