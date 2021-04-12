Improvements for Multiblock Unstructured

This CPEX is not completely defined yet.  The issue and some proposals are highlighted in
the file CGNS-MultiBlockUnstructured.pdf; supporting example CGNS files are also available:
  bump_3df_unstr_native_pw.cgns
  bump_3df_unstr.cgns
  bump_3df_hybrid.cgns  

---------------------

Here are some Q&As that occurred after the original posting:

Q1: Regarding the unstructured-to-unstructured connectivity data, you indicated
that the parent cell numbers on the "other" side of the connection should be
written to the ParentElements array, but the example file you sent shows
zeroes for those values in the dom-14 boundary element structure. We're
assuming this was an oversight - can you update your example file to show what
should be there? If they're supposed to be zeroes, then we're not sure how
this data is useful.

A1: For the sake of consistency and generality, I agree that the ParentElement
data for interior "Elements_t" nodes (like dom-14) should contain element ids
from the blocks on both sides of the interface.  I've updated the example file
(bump_3df_006x002x001_unstr.cgns) to reflect this.  We don't actually use this
interior ParentElement data to construct interior faces for our cell-centered
code since, once we've merged the connectivities, we can get the cell ids on
both sides of the interface.  However, I have needed and used two-sided
interior interfaces for finite element codes in the past, so having this data
on hand can only be helpful and doesn't hurt anything.



Q2: In your uns-to-uns example where you switched to point-to-point mappings,
you've specified Abutting interfaces, but Pointwise will always use
Abutting1to1 until we support more general (e.g., overset) block interfaces.
Is that sufficient, or is there some reason you need Abutting interfaces?

A2: I see now this is a little confusing but there's a reason.  We use a
"GridConnectivity_t" node (the general interface) but give it a
GridConnectivityType of Abutting1to1 – this is legal but confusing because why
aren't we using "GridConnectivity1to1_t" if we essentially have a 1to1
connection?  The reason is in the SIDS definition.  A GridConnectivity1to1_t
only allows you to specify a PointRange and PointRangeDonor – which is only
applicable to structured grids and no good if what you actually want to
specify is a PointList and PointListDonor of unstructured (i.e. not in any
specific order) node ids.  So, we went with the more general
GridConnectivity_t which allows for a PointList and PointListDonor.  The
answer here could either be to have the CGNS folks modify CGNS to allow for
optional PointList and PointListDonors in a GridConnectivity1to1_t or for
Pointwise to use the GridConnectivity_t with the understanding that there's
only support for 1to1 interfaces.


Q3: Regarding the hybrid connectivity examples, we're not sure why you'd want
to use cell-centered mappings for structured-to-unstructured, and a
user-defined cell-centered mapping from uns-to-str, when you're proposing to
use point-to-point mappings for the general uns-to-uns case. That is, wouldn't
it would be more consistent to write both sides (str-to-uns and uns-to-str) of
the hybrid connection using point-to-point (Vertex, PointList,
PointListDonor)?

A3: There's two things to discuss here:
1) First, your question at hand.  I can't claim to have this perfectly thought
out, but this is how I see it: 

For the unstr-to-unstr case, needing a Vertex-to-Vertex mapping as a means to
merge connectivities between unstructured blocks is a must – I think we all
agree on that.  However, between an unstructured and structured block, where
the interface is necessarily distinct, it depends on the application code and
how it needs the data.  We're working with a cell-centered code, so we want to
know CellCenters, hence we define the GridLocation as CellCenter and give our
PointRange, PointList, etc in terms of cell ids.  It's very convenient for a
cell-centered code to have the data served up this way.  If we were a
node-centered code, we'd want what you are suggesting which is Vertex ids.
However, I don't see the Vertex-to-Vertex mapping for these hybrid interfaces
as being the general case (consistent yes, but not convenient) since it means
we need a way to figure out what cell is on the unstructured side based on
vertex ids – which is not an easy task.  It seems like the best thing would be
to have Pointwise support outputting either CellCenter or Vertex information
for hybrid interfaces.  

str-to-str GridConnectivity: node-to-node mapping specified by Transform,
PointRange, and PointRangeDonor
uns-to-uns GridConnectivity: node-to-node mapping specified by PointList and
PointListDonor
str-to-uns GridConnectivity: cell-to-cell or node-to-node (user declared)
mapping specified by PointRange (str side) and PointListDonor (uns side)
uns-to-str GridConnectivity: cell-to-cell or node-to-node (user declared)
mapping specified by PointList and PointListPosition (uns side) and
PointRangeDonor (str side)

2) The reason for the user defined "PointListPosition" and "PointRangeDonor"
for the uns-to-str GridConnectivity in the example file is the SIDS definition
doesn't allow for this information.  On the unstructured side, a cell-id and a
face of that cell must be specified and that needs to map to a structured
block cell id range.  This obviously assumes that one has bought off on the
idea that the hybrid interface is specified with cell-ids (and not vertex ids
as you've mentioned).




Q4: When mapping str/uns block faces through the hybrid interface, what do you
expect ParentElements and ParentElementsPosition will contain for the cell
number and face position on the "other" (structured) side of the interface?
The hybrid example file you sent has zeroes, and we're not sure if these
should be structured cell indices (which doesn't fit in the array) or
something else.

A4: I think it's fair to just leave the ParentElements and
ParentElementsPosition for the structured side as zeros.  This interface is
completely defined in the GridConnectivity and the "Elements_t" node for the
hybrid interface is just "bonus" information.  We currently do not use it for
anything since the uns-to-str GridConnectivity give us everything we need.  I
suppose it would be possible to fill those zeros with assumed cell ids and
face positions from the structured side, but that may be misleading.

