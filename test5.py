from jetlag import Universal, pp, mk_input, pcmd, RemoteJobWatcher
from knownsystems import *

from time import sleep
import os
import html

# Test creation of shelob configuration using Agave
uv = Universal()
uv.init(
  backend = backend_agave,
  notify = 'sbrandt@cct.lsu.edu',
  **shelob
)

j1 = RemoteJobWatcher(uv, uv.hello_world_job('fork'))
print("Job was submitted")
j1.stop()
j1.wait()
assert j1.status() == "STOPPED"

print("Test passed")
exit(0)
