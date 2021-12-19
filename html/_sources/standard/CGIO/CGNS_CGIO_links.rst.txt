.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIOLinks:
   
Link Management Routines
========================

cgio_is_link
------------
:C Signature:
  .. c:function:: int cgio_is_link(int cgio_num, double id, int *link_len)

:Fortran Signature:
  .. f:subroutine:: cgio_is_link_f(cgio_num, id, link_len, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Identifier for the open database file.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`link_len`
      - OUT: Total length of the link information (:code:`file_len + name_len`).

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Determines if the node indentified by :code:`id` in the database given by :code:`cgio_num` is a link or not. The function returns 0 if successfull, else an error code. If this node is a link, then the total length of the linked-to file and node information is returned in :code:`link_len`. If the node is not a link, :code:`link_len` will be 0. 


cgio_link_size
--------------
:C Signature:
  .. c:function:: int cgio_link_size(int cgio_num, double id, int *file_len, int *name_len)

:Fortran Signature:
  .. f:subroutine:: cgio_link_size_f(cgio_num, id, file_len, name_len, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Identifier for the open database file.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`file_len`
      - OUT: Length of the name of the linked-to file. This will be 0 if this is an internal link.
    * - :code:`name_len`
      - OUT: Length of the pathname of the linked-to node.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the size of the linked-to file name in file_len and the node pathname length in name_len for the node identified by id in the database given by cgio_num. The function returns 0 for success, else an error code. If this is an internal link (link to a node in the same database), then file_len will be returned as 0. 
 

cgio_create_link
----------------
:C Signature:
  .. c:function:: int cgio_create_link(int cgio_num, double pid, const char *name, const char *filename, const char *name_in_file, double *id)

:Fortran Signature:
  .. f:subroutine:: cgio_create_link_f(cgio_num, pid, name, filename, name_in_file, id, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Identifier for the open database file.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`name`
      - IN: Name of the link node.
    * - :code:`filename`
      - IN: Name of the linked-to file. If creating an internal link, then this should be NULL or an empty string. When reading an internal link, this will be returned as an empty string.
    * - :code:`name_in_file`
      - IN: Pathname of the linked-to node.
    * - :code:`id`
      - OUT: Node identifier.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Creates a link node as a child of the parent node identified by pid in the database given by cgio_num. The name of the node is given by name, the name of the linked-to file by filename, and the pathname to the linked-to node by name_in_file. If this is an internal link (link to a node in the same database), then filename should be defined as NULL or an empty string. The function returns 0 and the indentifier of the new node in id on success, otherwise an error code is returned.


cgio_get_link
-------------

:C Signature:
  .. c:function:: int cgio_get_link(int cgio_num, double id, char *filename, char *name_in_file)

:Fortran Signature:
  .. f:subroutine:: cgio_get_link_f(cgio_num, id, filename, name_in_file, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Identifier for the open database file.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`filename`
      - OUT: Name of the linked-to file. If creating an internal link, then this should be NULL or an empty string. When reading an internal link, this will be returned as an empty string.    
    * - :code:`name_in_file`
      - OUT: Pathname of the linked-to node.
    
:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the link information for the node identified by id in the database given by cgio_num. If successfull, the function returns 0 and the linked-to file name in filename and the node pathname in name_in_file. These strings are '0'-terminated, and thus should be dimensioned at least (file_len + 1) and (name_len + 1), respectively If this is an internal link (link to a node in the same database), then filename will be an empty string. The maximum length for a file name is given by CGIO_MAX_FILE_LENGTH (1024) and for a link pathname by CGIO_MAX_LINK_LENGTH (4096).



.. last line
