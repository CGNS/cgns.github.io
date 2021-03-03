.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIOStructure:

Data Structure Management Routines
==================================

cgio_create_node
----------------
:C Signature:
  .. c:function:: int cgio_create_node(int cgio_num, double pid, const char *name, double *id)

:Fortran Signature:
  .. f:subroutine:: cgio_create_node_f(cgio_num, double pid, name, id, ier)
  
:Parameters:
  .. list-table::
    :widths: 25 75

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`name`
      - IN: Node name (max length 32).
    * - :code:`id`
      - OUT: Node identifier.

:Returns:      :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Creates a new empty node in the database given by :code:`cgio_num` as a child of the node identified by :code:`pid`. The name of the new node is given by :code:`name`, and must not already exist as a child of the parent node. The node will contain no label, dimensions, or data. Use the :ref:`Node Management Routines <StandardCGIONodeManagement>` to change the properties of the node, and the :ref:`Data I/O Routines <StandardCGIODataIO>` to add data. Returns 0 and the identifier of the new node in :code:`id` on success, else an error code.


cgio_new_node
-------------
:C Signature:
  .. c:function:: int cgio_new_node(int cgio_num, double pid, const char *name, const char *label, const char *data_type, int ndims, const cgsize_t *dims, const void *data, double *id)

:Fortran Signature:
  .. f:subroutine:: cgio_new_node_f(cgio_num, pid, name, label, data_type, ndims, dims, data, id, ier)
  
:Parameters:
  .. list-table::
    :widths: 25 75

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`name`
      - IN: Node name (max length 32).
    * - :code:`label`
      - IN: Node label (max length 32).
    * - :code:`data_type`
      - | IN: Type of data contained in the node. Options are:
        |   **MT** - empty
        |   **C1** - character data
        |   **I4** - 32-bit integer
        |   **I8** - 64-bit integer
        |   **U4** - unsigned 32-bit integer
        |   **U8** - unsigned 64-bit integer
        |   **R4** - 32-bit real
        |   **R8** - 64-bit real
        |   **X4** - 64-bit complex 
        |   **X8** - 128-bit complex
        |   **B1** - byte data

    * - :code:`ndims`
      - IN: Number of dimensions for the data (max 12).
    * - :code:`dims`
      - IN: Data dimension values (:code:`ndims` values).
    * - :code:`data`
      - IN: Data array to be stored with the node.
    * - :code:`id`
      - OUT: Node identifier.


:Returns:   :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Creates a new node in the database given by :code:`cgio_num` as a child of the node identified by :code:`pid`. The name of the new node is given by :code:`name`, and must not already exist as a child of the parent node. The node label is given by :code:`label`, the type of data by :code:`data_type`, the dimensions of the data by :code:`ndims` and :code:`dims`, and the data to write to the node by :code:`data`. This is equivalent to calling the routines:
  
  .. parsed-literal::
  
    :c:func:`cgio_create_node`
    :c:func:`cgio_set_label`
    :c:func:`cgio_set_dimensions`
    :c:func:`cgio_write_all_data`

  Returns 0 and the identifier of the new node in :code:`id` on success, else an error code. 


cgio_delete_node
----------------
:C Signature:
  .. c:function:: int cgio_delete_node(int cgio_num, double pid, double id)

:Fortran Signature:
  .. f:subroutine:: cgio_delete_node_f(cgio_num, pid, id, ier)

:Parameters:
  .. list-table::
    :widths: 25 75

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`id`
      - IN: Node identifier.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Deletes the node identified by :code:`id` below the parent node identified by :code:`pid` in the database given by :code:`cgio_num`. All children of the deleted node will also be deleted unless a link is encountered. The link node will be deleted but nothing below it. Returns 0 on success, else an error code.



cgio_move_node
--------------
:C Signature:
  .. c:function:: int cgio_move_node(int cgio_num, double pid, double id, double new_pid)

:Fortran Signature:
  .. f:subroutine:: cgio_move_node_f(cgio_num, pid, id, new_pid, ier)
  
:Parameters:
  .. list-table::
    :widths: 25 75

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`new_pid`
      - IN: New parent node identifier under which the node is to be moved.

:Returns:     :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Moves the node indentified by :code:`id` below the parent node identified by :code:`pid` to below the new parent node identified by :code:`new_pid` in the database given by :code:`cgio_num`. A node by the same name as that that for id must not already exist under :code:`new_pid`. A node may only be moved if it and the parent nodes all reside in the same physical database. Returns 0 on success, else an error code. 


cgio_number_children
--------------------
:C Signature:
  .. c:function:: int cgio_number_children(int cgio_num, double id, int *num_child)

:Fortran Signature:
  .. f:subroutine:: cgio_number_children_f(cgio_num, id, num_child, ier)
  
:Parameters:
  .. list-table::
    :widths: 25 75

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`num_child`
      - OUT: Number of children of the specified node.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the number of children of the node identified by :code:`id` in the database given by :code:`cgio_num`, Returns 0 and the number of children in :code:`num_child` on success, else an error code. 


cgio_children_names
-------------------
:C Signature:
  .. c:function:: int cgio_children_names(int cgio_num, double id, int start, int max_ret, int name_len, int *num_ret, char *child_names)

:Fortran Signature:
  .. f:subroutine:: cgio_children_names_f(cgio_num, id, start, max_ret, name_len, num_ret, child_names, ier)
 
:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`start`
      - IN: Starting index for returned child names or ids (1 <= :code:`start` <= :code:`num_child`).
    * - :code:`max_ret`
      - IN: Maximum child names or ids to be returned (1 <= :code:`max_ret` <= :code:`num_child-start+1`).
    * - :code:`name_len`
      - IN: Length reserved for each returned child name.
    * - :code:`num_ret`
      - OUT: Number of returned values of child names or identifiers.
    * - :code:`child_names`
      - OUT: Child node names (:code:`num_ret` values). This array should be dimensioned at least (:code:`name_len * max_ret`).


:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the names of the children of the node identified by :code:`id` in the database given by :code:`cgio_num`.
  The starting index for the array of names is given by :code:`start`,
  and the maximum number of names to return by :code:`max_ret`.
  Both :code:`start` and :code:`max_ret` should be between 1 and :code:`num_child`, inclusively.
  The size reserved for each name in :code:`child_names` is given by :code:`name_len`.
  The array :code:`child_names` should be dimensioned at least (:code:`name_len * max_ret`).
  Since node names are limited to a length of :code:`CGIO_MAX_NAME_LENGHT` (32), :code:`name_len` should be at least 32 to ensure the returned names are not truncated.
  In C, an additional byte should be added to :code:`name_len` allow for the terminating :code:`'0'` for each name. If successfull, the function returns 0; the actual number of returned names is given by :code:`num_ret`, and the array of names in :code:`child_names`. In C, the names are '0'-terminated within each name field. In Fortran, any unused space is padded with blanks (space character).


cgio_children_ids
-----------------
:C Signature:
  .. c:function:: int cgio_children_ids(int cgio_num, double id, int start, int max_ret, int *num_ret, char *child_ids)

:Fortran Signature:
  .. f:subroutine:: cgio_children_ids_f(cgio_num, id, start, max_ret, num_ret, child_ids, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`start`
      - IN: Starting index for returned child names or ids (1 <= :code:`start` <= :code:`num_child`).
    * - :code:`max_ret`
      - IN: Maximum child names or ids to be returned (1 <= :code:`max_ret` <= :code:`num_child-start+1`).
    * - :code:`num_ret`
      - OUT: Number of returned values of child names or identifiers.
    * - :code:`child_ids`
      - OUT: Child node identifiers (:code:`num_ret` values). This array should be dimensioned at least (:code:`max_ret`).

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the node identifiers of the children of the node identified by :code:`id` in the database given by :code:`cgio_num`.
  The starting index for the array of ids is given by :code:`start`, and the maximum ids to return by :code:`max_ret`.
  Both :code:`start` and :code:`max_ret` should be between 1 and :code:`num_child`, inclusively.
  The array :code:`child_ids` should be dimensioned at least (:code:`max_ret`).
  If successfull, the function returns 0; the actual number of returned ids is given by :code:`num_ret`, and the array of identifiers in :code:`child_ids`.


.. last line
