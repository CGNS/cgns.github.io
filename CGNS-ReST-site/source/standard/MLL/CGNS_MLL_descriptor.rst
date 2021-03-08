.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLDescriptors:
   
Descriptors
-----------

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Descriptive Text`_
   * - ``cg_descriptor_write`` 
     - Write descriptive text
   * - ``cg_ndescriptors``
     - Get number of descriptors in file
   * - ``cg_descriptor_size`` 
     - Get size of descriptor data
   * - ``cg_descriptor_read``
     - Read descriptive text
   
       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Ordinal Value`_
   * - ``cg_ordinal_write`` 
     - Write ordinal value
   * - ``cg_ordinal_read`` 
     - Read ordinal value


Descriptive Text
^^^^^^^^^^^^^^^^
Node: Descriptor_t (SIDS, File Mapping)

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                    | Modes   |
   +================================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_descriptor_write` (:in:`char *name`, :in:`char *text`);                                             | `- w m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_ndescriptors` (:out:`int *ndescriptors`);                                                           | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_descriptor_read` (:in:`int D`, :out:`char *name`, :out:`char **text`);                              | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
.. table::
   :widths: 110 15
   
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                           | Modes   |
   +==============================================================================================================================+=========+
   | call ``cg_descriptor_write_f`` (:in:`name`, :in:`text`, :out:`ier`)                                                          | `- w m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_ndescriptors_f`` (:out:`ndescriptors`, :out:`ier`)                                                                 | `r - m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_descriptor_size_f`` (:in:`D`, :out:`size`, :out:`ier`)                                                             | `r - m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_descriptor_read_f`` (:in:`D`, :out:`name`, :out:`text`, :out:`ier`)                                                | `r - m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:ndescriptors:  Number of Descriptor_t nodes under the current node.
:D:             Descriptor index number, where 1 ≤ D ≤ ndescriptors.
:name:          Name of the Descriptor_t node.
:text:          Description held in the Descriptor_t node.
:size:          Size of the descriptor data (Fortran interface only) - integer.
:ier:           Error status. 

Note that with cg_descriptor_read the memory for the descriptor character string, text, will be allocated by the Mid-Level Library. The application code is responsible for releasing this memory when it is no longer needed by calling cg_free(text).

Ordinal Value
^^^^^^^^^^^^^
Node: Ordinal_t (SIDS, File Mapping) 

.. table::
   :widths: 110 15
   
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                  | Modes   |
   +==============================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_ordinal_write` (:in:`int Ordinal`);                                                               | `- w m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_ordinal_read` (:out:`int *Ordinal`);                                                              | `r - m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+
.. table::
   :widths: 110 15
   
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                           | Modes   |
   +==============================================================================================================================+=========+
   | call ``cg_ordinal_write_f`` (:in:`Ordinal`, :out:`ier`)                                                                      | `- w m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_ordinal_read_f`` (:out:`Ordinal`, :out:`ier`)                                                                      | `r - m` |
   +------------------------------------------------------------------------------------------------------------------------------+---------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:Ordinal:   Any integer value.
:ier:       Error status.

.. last line
