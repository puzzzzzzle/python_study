from math import isclose, sqrt


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def int_2d(self):
        return [int(self.x), int(self.y)]


class Edge:
    def __init__(self):
        self.p1 = 0
        self.p2 = 0


class Triangle:
    def __init__(self):
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0


def circumCircle(xp, yp, x1, y1, x2, y2, x3, y3, circle):
    """
    Return ture if pos is inside the circumCircle made up of the triangle
    the circumCircle center pos and the radius ard also returned

    """

    if isclose(y1, y2) and isclose(y2, y3):
        return False

    if isclose(y2, y1):
        m2 = - (x3 - x2) / (y3 - y2)
        mx2 = (x2 + x3) / 2.0
        my2 = (y2 + y3) / 2.0
        xc = (x2 + x1) / 2.0
        yc = m2 * (xc - mx2) + my2
    elif isclose(y3, y2):
        m1 = - (x2 - x1) / (y2 - y1)
        mx1 = (x1 + x2) / 2.0
        my1 = (y1 + y2) / 2.0
        xc = (x3 + x2) / 2.0
        yc = m1 * (xc - mx1) + my1
    else:
        m1 = - (x2 - x1) / (y2 - y1)
        m2 = - (x3 - x2) / (y3 - y2)
        mx1 = (x1 + x2) / 2.0
        mx2 = (x2 + x3) / 2.0
        my1 = (y1 + y2) / 2.0
        my2 = (y2 + y3) / 2.0
        xc = (m1 * mx1 - m2 * mx2 + my2 - my1) / (m1 - m2)
        yc = m1 * (xc - mx1) + my1

    dx = x2 - xc
    dy = y2 - yc
    rsqr = dx * dx + dy * dy
    r = sqrt(rsqr)

    dx = xp - xc
    dy = yp - yc
    drsqr = dx * dx + dy * dy

    circle[0:3] = [xc, yc, r]
    return drsqr <= rsqr
    pass


def triangulate(points):
    """
    Triangulation subroutine
    Takes as input NV vertices in array points
    Returned is a list of ntri triangular
    """
    nv = len(points) - 3
    assert nv > 0
    nedge = 0
    emax = 200
    trimax = 4 * nv
    complete = [False for x in range(trimax)]
    edges = [Edge() for x in range(emax)]
    v = [Triangle() for x in range(3 * nv)]
    # sort pxyz

    # Find the maximum and minimum vertex bounds.
    # This is to allow calculation of the bounding triangle
    xmin = points[0].x
    ymin = points[0].y
    xmax = xmin
    ymax = ymin
    for i in range(1, nv):
        if points[i].x < xmin:
            xmin = points[i].x
        if points[i].x > xmax:
            xmax = points[i].x
        if points[i].y < ymin:
            ymin = points[i].y
        if points[i].y > ymax:
            ymax = points[i].y

    dx = xmax - xmin
    dy = ymax - ymin
    dmax = max(dx, dy)
    xmid = (xmax + xmin) / 2.0
    ymid = (ymax + ymin) / 2.0

    """
      Set up the supertriangle
      This is a triangle which encompasses all the sample points.
      The supertriangle coordinates are added to the end of the
      vertex list. The supertriangle is the first triangle in
      the triangle list.
    """
    points[nv + 0].x = xmid - 20 * dmax
    points[nv + 0].y = ymid - dmax
    points[nv + 0].z = 0.0
    points[nv + 1].x = xmid
    points[nv + 1].y = ymid + 20 * dmax
    points[nv + 1].z = 0.0
    points[nv + 2].x = xmid + 20 * dmax
    points[nv + 2].y = ymid - dmax
    points[nv + 2].z = 0.0
    v[0].p1 = nv
    v[0].p2 = nv + 1
    v[0].p3 = nv + 2
    complete[0] = False
    ntri = 1

    # Include each point one at a time into the existing mesh
    for i in range(nv):
        xp = points[i].x
        yp = points[i].y
        nedge = 0
        """
         Set up the edge buffer.
         If the point (xp,yp) lies inside the circumcircle then the
         three edges of that triangle are added to the edge buffer
         and that triangle is removed.
         """
        circle = [0, 0, 0]
        j = 0
        while j < ntri:
            if complete[j]:
                j += 1
                continue
            x1 = points[v[j].p1].x
            y1 = points[v[j].p1].y
            x2 = points[v[j].p2].x
            y2 = points[v[j].p2].y
            x3 = points[v[j].p3].x
            y3 = points[v[j].p3].y
            inside = circumCircle(xp, yp, x1, y1, x2, y2, x3, y3, circle)
            xc = circle[0]
            yc = circle[1]
            r = circle[2]
            if xc + r < xp:
                complete[j] = True
            if inside:
                if nedge + 3 >= emax:
                    emax += 100
                    for ie in range(100):
                        edges.append(Edge())
                edges[nedge + 0].p1 = v[j].p1
                edges[nedge + 0].p2 = v[j].p2
                edges[nedge + 1].p1 = v[j].p2
                edges[nedge + 1].p2 = v[j].p3
                edges[nedge + 2].p1 = v[j].p3
                edges[nedge + 2].p2 = v[j].p1
                nedge += 3
                v[j] = v[ntri - 1]
                complete[j] = complete[ntri - 1]
                ntri -= 1
                j -= 1
            j += 1
        """
         Tag multiple edges
         Note: if all triangles are specified anticlockwise then all
               interior edges are opposite pointing in direction.
        """
        for j in range(nedge - 1):
            for k in range(j + 1, nedge):
                if (edges[j].p1 == edges[k].p2) and (edges[j].p2 == edges[k].p1):
                    edges[j].p1 = -1
                    edges[j].p2 = -1
                    edges[k].p1 = -1
                    edges[k].p2 = -1
                # Shouldn't need the following, see note above 
                if (edges[j].p1 == edges[k].p1) and (edges[j].p2 == edges[k].p2):
                    edges[j].p1 = -1
                    edges[j].p2 = -1
                    edges[k].p1 = -1
                    edges[k].p2 = -1
        """
         Form new triangles for the current point
         Skipping over any tagged edges.
         All edges are arranged in clockwise order.
        """
        for j in range(nedge):
            if edges[j].p1 < 0 or edges[j].p2 < 0:
                continue
            if ntri >= trimax:
                raise Exception("ntri >= trimax")
            v[ntri].p1 = edges[j].p1
            v[ntri].p2 = edges[j].p2
            v[ntri].p3 = i
            complete[ntri] = False
            ntri += 1
    """
    Remove triangles with supertriangle vertices
    These are triangles which have a vertex number greater than nv
    """
    for i in range(ntri):
        if v[i].p1 >= nv or v[i].p2 >= nv or v[i].p3 >= nv:
            v[i] = v[ntri - 1]
            ntri -= 1
            i -= 1
    return v[0:ntri]
    pass
