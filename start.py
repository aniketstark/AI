import os
from core.input_module import take_input
from core.process_module import process
from core.output_module import output
os.system("clear")
while(True):
	i = take_input()
	o = process(i)
	output(o)
