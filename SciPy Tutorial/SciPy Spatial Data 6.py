# SciPy Spatial Data

# Working with Spatial Data
    # Spatial data refers to data that is represented in a geometric space.
    # E.g. points on a coordinate system.
    # We deal with spatial data problems on many tasks.
    # E.g. finding if a point is inside a boundary or not.
    # SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.

# Triangulation
   # A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.
   # A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.
   # One method to generate these triangulations through points is the Delaunay() Triangulation.

# Example
   # Create a triangulation from following points:

