import subprocess
test=subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
output = test.communicate()[0]
print(output.decode()+'\n')
