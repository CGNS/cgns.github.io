.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIONodeManagement:
   
Node Management Routines
========================

cgio_get_node_id
----------------
:C Signature:
  .. c:function:: int cgio_get_node_id(int cgio_num, double pid, const char *pathname, double *id)

:Fortran Signature:
  .. f:subroutine:: cgio_get_node_id_f(cgio_num, pid, pathname, id, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`pathname`
      - IN: Absolute or relative path name for a node.
    * - :code:`id`
      - OUT: Node identifier.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the node identifier for the node specified by :code:`pathname` in the database given by :code:`cgio_num`.
  if :code:`pathname` starts with :code:`'/'`, then it is taken as an absolute path and is located based on the root id of the database,
  otherwise it is taken to be a relative path from the parent node identifed by :code:`pid`.
  The function returns 0 and the node identifier in :code:`id` on success, else an error code.

cgio_get_name
-------------

:C Signature:
  .. c:function:: int cgio_get_name(int cgio_num, double id, char *name)

:Fortran Signature:
  .. f:subroutine:: cgio_get_name_f(cgio_num, id, name, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`name`
      - OUT: Node name (max length 32).

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the name of the node identified by :code:`id` in the database given by :code:`cgio_num`.
  The name is returned in :code:`name`, and has a maximum length of :code:`CGIO_MAX_NAME_LENGTH` (32).
  In C, name should be dimensioned at least 33 to allow for the terminating :code:`'0'`.
  The function returns 0 for success, else an error code.

cgio_set_name
-------------
:C Signature:
  .. c:function:: int cgio_set_name(int cgio_num, double pid, double id, const char *name)

:Fortran Signature:
  .. f:subroutine:: cgio_set_name_f(cgio_num, pid, id, name, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`pid`
      - IN: Parent node identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`name`
      - IN: Node name (max length 32).

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Sets (renames) the node identied by :code:`id` in the database given by :code:`cgio_num` to :code:`name`.
  The parent node identifier is given by :code:`pid`. There must not already exist a child node of :code:`pid` with that name. The function return 0 on success, else an error code.

cgio_get_label
--------------

:C Signature:
  .. c:function:: int cgio_get_label(int cgio_num, double id, char *label)

:Fortran Signature:
  .. f:subroutine:: cgio_get_label_f(cgio_num, id, label, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`label`
      - OUT: Node label (max length 32).

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the label of the node identified by id in the database given by cgio_num. The label is returned in label, and has a maximum length of CGIO_MAX_LABEL_LENGTH (32). In C, label should be dimensioned at least 33 to allow for the terminating '0'. The function returns 0 for success, else an error code. 


cgio_set_label
--------------
:C Signature:
  .. c:function:: int cgio_set_label(int cgio_num, double id, const char *label)

:Fortran Signature:
  .. f:subroutine:: cgio_set_label_f(cgio_num, id, label, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`label`
      - IN: Node label (max length 32).

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Sets the label of the node identied by :code:`id` in the database given by :code:`cgio_num` to label.
  The function return 0 on success, else an error code. 

cgio_get_data_type
------------------
:C Signature:
  .. c:function:: int cgio_get_data_type(int cgio_num, double id, char *data_type)

:Fortran Signature:
  .. f:subroutine:: cgio_get_data_type_f(cgio_num, id, data_type, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`data_type`
      - OUT: Type of data contained in the node. One of "MT", "I4", "I8", "U4", "U8", "R4", "R8, "C1", or "B1".

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the data type of the data associated with the node identified by :code:`id` in the database given by :code:`cgio_num`.
  The data type is returned in :code:`data_type`, and has a maximum length of :code:`CGIO_MAX_DATATYPE_LENGTH` (2).
  In C, data_type should be dimensioned at least 3 to allow for the terminating :code:`'0'`.
  The function returns 0 for success, else an error code.

cgio_get_dimensions
-------------------
:C Signature:
  .. c:function:: int cgio_get_dimensions(int cgio_num, double id, int *ndims, cgsize_t *dims)

:Fortran Signature:
  .. f:subroutine:: cgio_get_dimensions_f(cgio_num, id, ndims, dims, ier)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`ndims`
      - OUT: Number of dimensions for the data (max 12).
    * - :code:`dims`
      - OUT: Data dimension values (ndims values).

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the dimensions of the data associated with the node identified by :code:`id` in the database given by :code:`cgio_num`.
  The number of dimensions is returned in :code:`ndims` and the dimension values in :code:`dims`.
  Since the maximum number of dimensions is :code:`CGIO_MAX_DIMENSIONS` (12), :code:`dims` should be dimensioned 12, unless the actual number of dimensions is already known.
  The function returns 0 for success, else an error code.

cgio_set_dimensions
-------------------
:C Signature:
  .. c:function:: int cgio_set_dimensions(int cgio_num, double id, const char *data_type, int ndims, const cgsize_t *dims)

:Fortran Signature:
  .. f:subroutine:: cgio_set_dimensions_f(cgio_num, id, data_type, ndims, dims, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - IN: Node identifier.
    * - :code:`data_type`
      - IN: Type of data contained in the node. One of "MT", "I4", "I8", "U4", "U8", "R4", "R8, "C1", or "B1".
    * - :code:`ndims`
      - IN: Number of dimensions for the data (max 12).
    * - :code:`dims`
      - IN: Data dimension values (ndims values).

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Sets the data type and dimensions for data associated with the node identified by :code:`id` in the database given by :code:`cgio_num`.
  The data type (:code:`data_type`) as one of:

  .. table::
    :widths: 15 85

    ===== =======================================================
    "MT"  An empty node containing no data
    "I4"  32-bit integer (int or integer*4)
    "I8"  64-bit integer (cglong_t or integer*8)
    "U4"  32-bit unsigned integer (unsigned int or integer*4)
    "U8"  64-bit unsigned integer (cgulong_t or integer*8)
    "R4"  32-bit real (float or real*4)
    "R8"  64-bit real (double or real*8)
    "X4"  64-bit complex (complex or complex*8)
    "X8"  128-bit complex (complex double or complex*16)
    "C1"  character (char or character)
    "B1"  unsigned bytes (unsigned char or character*1)
    ===== =======================================================

  The number of dimensions is given by :code:`ndims` (maximum is 12), and the dimension values by :code:`dims`. Note that any existing data for the node will be destroyed. To add the data to the node, use one of the :ref:`data writing routines <StandardCGIODataIO>`.
  The function returns 0 for success, else an error code.


.. last line
