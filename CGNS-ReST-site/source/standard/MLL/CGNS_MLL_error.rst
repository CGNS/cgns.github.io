.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLErrors:
   
Error Handling
--------------

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | C Functions                                                                                                                    | Modes |
   +================================================================================================================================+=======+
   | :out:`const char* error_message` = :sig-name:`cg_get_error` ();                                                                | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | void :sig-name:`cg_error_exit` ();                                                                                             | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | void :sig-name:`cg_error_print` ();                                                                                            | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+


.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | Fortran interfaces                                                                                                             | Modes |
   +================================================================================================================================+=======+
   | call ``cg_get_error_f`` (:out:`error_message`)                                                                                 | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_error_exit_f`` ()                                                                                                    | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_error_print_f`` ()                                                                                                   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+


If an error occurs during the execution of a CGNS library function, signified by a non-zero value of the error status variable ier, an error message may be retrieved using the function cg_get_error. The function cg_error_exit may then be used to print the error message and stop the execution of the program. Alternatively, cg_error_print may be used to print the error message and continue execution of the program.

In C, you may define a function to be called automatically in the case of a warning or error using the cg_configure routine. The function is of the form :code:`void err_func(int is_error, char *errmsg)`, and will be called whenever an error or warning occurs. The first argument, is_error, will be 0 for warning messages, 1 for error messages, and −1 if the program is going to terminate (i.e., a call to cg_error_exit). The second argument is the error or warning message.



.. last line
