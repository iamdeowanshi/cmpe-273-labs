# pylint: disable=C0103

import operator
from collections import Counter
from collections import defaultdict
import psutil

connections = psutil.net_connections(kind="tcp")
connection_dict = defaultdict(int)

valid_connections = []

for connection in connections:
    if str(connection.laddr) != "::" and str(connection.raddr) != "()":
        valid_connections.append(connection)
    else:
        pass

freq = Counter(item[-1] for item in valid_connections)
valid_connections = sorted(valid_connections, key=lambda x: freq[x[-1]], reverse=True)

print """
"pid","laddr","raddr","status"
""",

for connection in valid_connections:
    laddr = "{}@{}".format(connection.laddr[0], connection.laddr[1])
    raddr = "{}@{}".format(connection.raddr[0], connection.raddr[1])
    print "\"{}\",\"{}\",\"{}\",\"{}\"".format(connection.pid, laddr, raddr, connection.status)
