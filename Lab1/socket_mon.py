# pylint: disable=C0103

from collections import Counter
import psutil

connections = psutil.net_connections(kind="tcp")

valid_connections = []

for connection in connections:
    if connection.pid != None and str(connection.laddr) != "::" and str(connection.raddr) != "()":
        valid_connections.append(connection)
    else:
        pass

pid_count = Counter(item[-1] for item in valid_connections)
sorted_connection = sorted(valid_connections, key=lambda x: pid_count[x[-1]], reverse=True)

print """
"pid","laddr","raddr","status"
""",

for connection in sorted_connection:
    laddr = "{}@{}".format(connection.laddr[0], connection.laddr[1])
    raddr = "{}@{}".format(connection.raddr[0], connection.raddr[1])
    print "\"{}\",\"{}\",\"{}\",\"{}\"".format(connection.pid, laddr, raddr, connection.status)
