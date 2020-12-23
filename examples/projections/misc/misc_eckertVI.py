"""
Eckert VI
=========

The Eckert VI projections, presented by the German cartographer
Max Eckert-Greiffendorff in 1906, is a pseudo-cylindrical equal-area projection.
Central meridian and all parallels are straight lines; other meridians are equally
spaced sinusoids. The scale is true along latitude 49°16’.

``Ks[central meridian]/width``: Give the optional central meridian (default is the
center of the region) and the map width.
"""
import pygmt

fig = pygmt.Figure()
# Use region "d" to specify global region (-180/180/-90/90)
fig.coast(region="d", projection="Ks12c", land="ivory", water="bisque4", frame="afg")
fig.show()
