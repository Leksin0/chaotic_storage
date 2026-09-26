def make(route):
    global flights, routes
    way = False
    for j in range(len(flights)):
        if (route[-1] == flights[j][0]) and (flights[j][1] not in route) and (route[1] + flights[j][3] < 2880) and \
            (flights[j][2] - route[1] >= 90 or flights[j][2] - route[1] + 1440 >= 90):
            cr = route[::]
            cr.append(flights[j][1])
            transit = flights[j][2] - cr[1]
            if transit < 90:
                transit += 1440
            cr[1] += flights[j][3]      # route[start, curtime, points ...]
            cr[1] += transit            # flight[dep, arr, deptime, durat]
            way = True
            make(cr)
    if not way:
        routes.append(route)
    return
def convtom(hm):
    a = list(map(int, hm.split(':')))
    return a[0] * 60 + a[1]
def convtoh(m):
    return str(m//60) + ':' + str(m%60)
flights = []
routes = []
for q in range(int(input())):
    flights.append(input().split('|'))
    flights[q][2] = convtom(flights[q][2])
    flights[q][3] = convtom(flights[q][3])
fasrt = 99999999
rtind = 0
impos = True
for pl in flights:
    if pl[0] == 'Moscow':
        impos = False
        make([pl[2], 0, 'Moscow'])
if impos:
    print(0)
    exit(0)
for i in range(len(routes)):
    if routes[i][-1] == "Malokribirsk" and routes[i][1] - routes[i][0] < fasrt:
        fasrt = routes[i][1] - routes[i][0]
        rtind = i
print('|'.join(routes[rtind][2::]))
print(convtoh(fasrt))
