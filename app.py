import os
from subprocess import Popen
 
command = ["mercury", "run", f"0.0.0.0:{os.environ.get('PORT', 7860)}"] 
worker = Popen(command) 
worker.wait()