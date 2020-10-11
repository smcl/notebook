import os, sys
from IPython.terminal.ipapp import launch_new_instance
from IPython.lib import passwd
import warnings

# set the password you want to use
notebook_password = "test"

sys.argv.append("notebook")
sys.argv.append("--IPKernelApp.pylab='inline'")
sys.argv.append("--NotebookApp.ip='*'")
sys.argv.append("--NotebookApp.port=" + os.environ["ASPNETCORE_PORT"])
sys.argv.append("--NotebookApp.open_browser=False")
sys.argv.append("--NotebookApp.notebook_dir=./notebooks")
sys.argv.append("--NotebookApp.password=" + passwd(notebook_password))

launch_new_instance()