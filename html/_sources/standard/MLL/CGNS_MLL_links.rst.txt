.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLLinks:
   
Links
-----


.. list-table::
   :widths: 2 8

   * - ``cg_link_write`` 
     - Create a link at the current location
   * - ``cg_is_link``
     - Test if a node is a link
   * - ``cg_link_read`` 
     - Get path information for a link at the current location

Link functions 
^^^^^^^^^^^^^^

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | C Functions                                                                                                                    | Modes |
   +================================================================================================================================+=======+
   | :out:`ier` = :sig-name:`cg_link_write` (:in:`char *nodename`, :in:`char *filename`, :in:`char *name_in_file`);                 |\- w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_is_link` (:out:`int *path_length`);                                                                 | r - m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_link_read` (:out:`char **filename`, :out:`char **link_path`);                                       | r - m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | Fortran interfaces                                                                                                             | Modes |
   +================================================================================================================================+=======+
   | call ``cg_link_write_f`` (:in:`filename`, :in:`mode`, :out:`fn`, :out:`ier`)                                                   |\- w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_is_link_f`` (:out:`path_length`, :out:`ier`)                                                                         | r - m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_link_read_f`` (:out:`filename`, :out:`link_path`, :out:`ier`)                                                        | r - m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:nodename:	   	Name of the link node to create, e.g., :code:`GridCoordinates`.
:filename:		Name of the linked file, or empty string if the link is within the same file.
:name_in_file:		Path name of the node which the link points to. This can be a simple or a compound name, e.g., :code:`Base/Zone 1/GridCoordinates`.
:path_length:		Length of the path name of the linked node. The value 0 is returned if the node is not a link.
:link_path:		Path name of the node which the link points to.
:ier:		Error status. 

Use :code:`cg_goto(_f)` to position to a location in the file prior to calling these routines.

When using :code:`cg_link_write`, the node being linked to does not have to exist when the link is created. However, when the link is used, an error will occur if the linked-to node does not exist.

Only nodes that support child nodes will support links.

It is assumed that the CGNS version for the file containing the link, as determined by the :code:`CGNSLibraryVersion_t` node, is also applicable to :code:`filename`, the file containing the linked node.

Memory is allocated by the library for the return values of the C function :code:`cg_link_read`. This memory should be freed by the user when no longer needed by calling :code:`cg_free(filename)` and :code:`cg_free(link_path)`. 
 
.. last line
